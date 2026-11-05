"""Post-processing of w_test.out (added 2026-11-05 after an adversarial review): which PASS rows actually discriminate W from the
alternatives that w_test.py reports.

w_test.py passes a row when |fit - W| <= tol, tol = max(3 half-ranges, 2e-6 (1 + |W|)), and calls an alternative "excluded" when it
misses the fit by > 10 tol. A PASS is counted here as
  DISCRIMINATING      every reported alternative is excluded (> 10 tol) and tol < |W| (so W = 0 would not also pass);
  NON-DISCRIMINATING  otherwise: some alternative is within 10 tol, no alternative is reported, or tol >= |W|.
Only the committed w_test.out is read (the measure caches tmp/w_cache are not in the repository, so w_test.py cannot be re-run
here). Usage: w_test_discrimination.py [w_test.out]."""
import os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'w_test.out')
for fn in [__file__, src]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}")

ROW = re.compile(r"^\s*n\^-(?P<e>[\d.]+)\s*: fit (?P<fit>\S+) \(half-range \S+\)\s+W (?P<w>\S+)\s+diff \S+\s+tol (?P<tol>\S+)\s+"
                 r"(?P<v>PASS|FAIL)(?:\s+\| alternatives: (?P<alts>.*))?$")
key = None; rows = []
for line in open(src):
    m = re.match(r"^=== (\S+):", line)
    if m: key = m.group(1); continue
    m = ROW.match(line.rstrip('\n'))
    if not m: continue
    alts = []
    if m.group('alts'):
        for a in m.group('alts').split('; '):
            am = re.match(r"(.+): \S+ \((\d+) tol\)$", a.strip())
            assert am, a
            alts.append((am.group(1), int(am.group(2))))
    rows.append(dict(key=key, e=m.group('e'), w=float(m.group('w')), tol=float(m.group('tol')), verdict=m.group('v'), alts=alts))

npass = nfail = ndisc = 0; nondisc = []
for r in rows:
    if r['verdict'] == 'FAIL': nfail += 1; continue
    npass += 1
    why = []
    if not r['alts']: why.append("no alternative reported")
    near = [f"{n} ({t} tol)" for n, t in r['alts'] if t <= 10]
    if near: why.append("within 10 tol: " + ", ".join(near))
    if r['tol'] >= abs(r['w']): why.append(f"tol {r['tol']:.1e} >= |W| = {abs(r['w']):.1e} (W = 0 would pass)")
    if why: nondisc.append((r, why))
    else: ndisc += 1

print(f"rows: {len(rows)}  PASS: {npass}  FAIL: {nfail}")
print(f"PASS rows that discriminate W from every reported alternative: {ndisc}")
print(f"PASS rows that do NOT discriminate: {len(nondisc)}")
for r, why in nondisc:
    print(f"   {r['key']} n^-{r['e']}: " + "; ".join(why))
assert ndisc + len(nondisc) == npass
print("EXIT 0")
