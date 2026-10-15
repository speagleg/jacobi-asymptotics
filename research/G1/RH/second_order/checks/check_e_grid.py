"""Plan 65 (E_pgt1.md §8.1): compare the proved closed forms of Theorem E.1 / Corollary E.6 with the Plan 62 grid fits
(check_so_grid.out, rows p > 1).  A row passes if |fit - closed form| <= max(fit half-range, 5e-10); 5e-10 is the
rounding of the 9-decimal table."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
worst, bad = (0.0, None), 0
for line in open(os.path.join(here, "check_so_grid.out")):
    m = re.match(r"\s*([\d.]+)\s+([\d.]+)\s*\|(.*)", line)
    if not m:
        continue
    p, s = float(m.group(1)), float(m.group(2))
    if p <= 1:
        continue
    vals = re.findall(r"([+-]?\d+\.\d+) \(([\d.e+-]+)\)", m.group(3))
    a = (2 * s - 2 - p) / (2 * p)
    pred = {"d1": -(s - 1) / 2, "e1": p / 2, "e1s": -p / 2, "k0": -(s - 1) - p / 2, "k1": -(p + 2) * a}
    for (v, fh), name in zip(vals, pred):
        d = abs(float(v) - pred[name])
        tol = max(float(fh), 5e-10)
        status = "ok" if d <= tol else "FAIL"
        bad += status != "ok"
        if d > worst[0]:
            worst = (d, (p, s, name))
        print(f"p={p} s={s} {name:3s}: fit {v:>13}  proved {pred[name]:+.9f}  |diff| = {d:.1e}  tol {tol:.1e}  {status}")
print(f"largest |diff| = {worst[0]:.2e} at {worst[1]}; failures: {bad}")
