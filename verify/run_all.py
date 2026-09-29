"""verify/ 안의 모든 문항 파일을 실행해 공통 검사 + 문항별 검사를 돌리고,
통과 여부와 상관없이 problems/<id>.md, variants/<id>-k.json 을 갱신한다.
사용: python3 verify/run_all.py [문항ID ...]
"""
import importlib.util, json, pathlib, sys, traceback
from lib import Ctx, val, same

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
SKIP = {"lib.py", "run_all.py"}


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def is_nat(v):
    v = val(v)
    return not isinstance(v, str) and v.is_integer and 0 < v < 1000


def common_checks(c, O, V):
    ck = c.check
    ck("원문 정답 재계산", "orig" in c.answers and same(c.answers["orig"], O["answer"]))
    kinds = [v["variant_type"] for v in V]
    ck("변형 2개", len(V) == 2)
    ck("분기 유발형 최소 1개", "분기 유발형" in kinds)
    ck("변형끼리 근거 다름", len({v["basis"] for v in V}) == len(V))
    ck("변형끼리 정답 다름", not same(V[0]["answer"], V[1]["answer"]))
    for k, v in enumerate(V, 1):
        p = f"{k}번 변형: "
        ck(p + "정답 재계산", k in c.answers and same(c.answers[k], v["answer"]))
        ck(p + "해설 3~6줄", 3 <= len(v["explanation"]) <= 6)
        ck(p + "자연스러움 기록", len(v["changed"]) >= 1 and (len(v["changed"]) < 2 or v.get("naturalness")))
        if v["type"] == "객관식":
            ch = v["choices"]
            ck(p + "선지 5개", len(ch) == 5)
            ck(p + "정답이 선지에 정확히 1번", sum(same(s, v["answer"]) for s in ch) == 1)
        else:
            ck(p + "주관식 정답 1~999 자연수", is_nat(v["answer"]))
        if v["variant_type"] == "분기 유발형":
            ck(p + "함정 답 기록", v.get("trap_answer") is not None and v.get("trap_path"))
        if v.get("trap_answer") is not None:
            ck(p + "함정 경로 실행값 == 기록", k in c.traps and same(c.traps[k], v["trap_answer"]))
            ck(p + "함정 답 ≠ 정답", not same(v["trap_answer"], v["answer"]))
            if v["type"] == "객관식":
                ck(p + "함정 답이 선지에 있음", any(same(s, v["trap_answer"]) for s in v["choices"]))


def md(O):
    L = [f"# {O['id']} (PDF {O['page']}쪽 = 교재 {O['page'] - 2}쪽, {O['num']}번)", "",
         f"출처: {O['source']} · {O['type']}", "", "## 원문", O["stem"]]
    for b in O.get("box", []):
        L.append(f"- {b}")
    for b in O.get("bogi", []):
        L.append(f"- {b}")
    if O.get("choices"):
        L.append("선지: " + " / ".join(f"{'①②③④⑤'[i]} {s}" for i, s in enumerate(O["choices"])))
    L += ["", f"## p.{O['page']} {O['num']}번. 답 {O['answer']}",
          f"- 일반해: {O['general']}", f"- 특수 풀이: {O['special']}",
          f"- 더 일반적인 관점: {O.get('perspective') or '없음'}", "",
          "## 3-A 조건 역추적", "| 요소 | 이 조건이 잘라낸 경우 | 지우거나 바꾸면 생기는 일 |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in O["table"]]
    L += ["", "## 3-B 임계값 스윕"] + [f"- {s}" for s in O["sweep"]] + [""]
    return "\n".join(L)


def run(path):
    mod = load(path)
    O, V = mod.ORIG, mod.VARS
    c = Ctx()
    try:
        mod.verify(c)
    except Exception:
        c.check("verify() 실행 오류\n" + traceback.format_exc(limit=3), False)
    common_checks(c, O, V)
    (ROOT / "problems").mkdir(exist_ok=True)
    (ROOT / "variants").mkdir(exist_ok=True)
    (ROOT / f"problems/{O['id']}.md").write_text(md(O))
    for k, v in enumerate(V, 1):
        d = dict(v, id=f"{O['id']}-{k}", origin=O["id"], source=O["source"] + " 변형",
                 chapter=O["chapter"])
        (ROOT / f"variants/{O['id']}-{k}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return O["id"], c.results


def main(ids):
    files = sorted(p for p in HERE.glob("*.py") if p.name not in SKIP)
    if ids:
        files = [p for p in files if p.stem in ids]
    bad = 0
    for f in files:
        qid, res = run(f)
        fails = [n for n, ok in res if not ok]
        print(f"{'PASS' if not fails else 'FAIL'}  {qid}  ({len(res) - len(fails)}/{len(res)})")
        for n in fails:
            print("      ✗", n)
        bad += bool(fails)
    print(f"== {len(files) - bad}/{len(files)} PASS ==")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
