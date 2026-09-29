"""verify/ 안의 모든 문항 스크립트 실행 + 같은 원문 변형끼리 정답 중복 검사"""
import json, pathlib, subprocess, sys
from collections import defaultdict

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
results = {}
for s in sorted(HERE.glob("*.py")):
    if s.name in ("run_all.py", "common.py") or s.name.startswith("sweep_"):
        continue
    r = subprocess.run([sys.executable, str(s)], cwd=HERE, capture_output=True, text=True)
    results[s.stem] = r.returncode == 0
    if r.returncode:
        print(r.stdout, r.stderr)

groups = defaultdict(list)
for v in ROOT.glob("variants/*.json"):
    d = json.loads(v.read_text())
    groups[d["origin"]].append(d)
for origin, items in groups.items():
    ans = [d["answer"] for d in items]
    results[f"{origin} 변형 정답 중복 없음"] = len(ans) == len(set(ans))
    results[f"{origin} 분기 유발형 최소 1개"] = any(d["variant_type"] == "분기 유발형" for d in items)
    results[f"{origin} 분기 유발형은 함정 답 있음"] = all(d["trap_answer"] is not None for d in items if d["variant_type"] == "분기 유발형")
    results[f"{origin} 변형끼리 근거 다름"] = len({d["basis"] for d in items}) == len(items)

print("== 결과 ==")
for k, ok in results.items():
    print(f"{'PASS' if ok else 'FAIL'}  {k}")
sys.exit(0 if all(results.values()) else 1)
