"""SPEC §3.6: aggregate spec_stats_seeds.out (GUE-like vs Poisson node statistics, seeds 7, 11, 13, 17, 19)."""
import re, numpy as np, os
d = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(d, 'spec_stats_seeds.out')).read()
data = {'gue': [], 'poisson': []}
for b in re.split(r'\n(?=(?:gue|poisson) seed)', txt):
    m = re.match(r'(gue|poisson) seed (\d+)', b.strip())
    if m: data[m.group(1)].append([float(r) for r in re.findall(r'\[\s*\d+,\s*\d+\)\s+([\d.e+-]+)', b)])
wins = ['[50,100)', '[100,200)', '[200,400)', '[400,800)', '[800,1600)']; mid = np.array([75, 150, 300, 600, 1200])
print(f"seeds: gue {len(data['gue'])}, poisson {len(data['poisson'])}")
print(f"{'window':>11} {'GUE mean':>9} {'sd':>6} {'Poi mean':>9} {'sd':>6} {'ratio':>6}")
for k in data: data[k] = np.array(data[k])
for i, w in enumerate(wins):
    g, p = data['gue'][:, i], data['poisson'][:, i]
    print(f"{w:>11} {g.mean():9.2f} {g.std(ddof=1):6.2f} {p.mean():9.2f} {p.std(ddof=1):6.2f} {p.mean()/g.mean():6.2f}")
for k in data:
    print(f"growth exponent of mean RMS n(y - y_lat), {k}: {np.polyfit(np.log(mid), np.log(data[k].mean(0)), 1)[0]:.3f}")
