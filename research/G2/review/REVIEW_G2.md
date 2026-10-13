# REVIEW_G2: Rule R second reading of research/G2 (Plan 8), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files.
- **Sources.** Downloaded and checked: arXiv:1105.3088v2, 1510.01901v3 and 0901.1883 (Monien).
- **Re-runs.** All three checks reproduce byte-identically.
- **Scratch checks:**
  - `r1.py`: J(p) − (2/p)I(p) ≈ 1e−17; E[log min] = −3/2; B0 by direct quadrature; the closed form
    dμ*/dσ = I_{min(1,x/4c)}(1/p+½, ½).
  - `a1.py`: A1 excess within bounds on degenerate S.
  - `al.py`: the quantile configuration of μ* tracks κ_p within O(log n/n).

| Result | Verdict | Required fixes (applied) |
|---|---|---|
| B0 | ACCEPT | minor: L² convergence; continuity at β |
| B* | ACCEPT WITH FIXES | mutual-energy finiteness (cite (P) §1 after (1.13)); E_p < ∞; absolute Fubini bounds; note the unread [7] behind Lemma 2.1 |
| A1 | ACCEPT | minor: one-sided harmonic sum wording |
| A2 / scaling | ACCEPT | — |
| A-U | ACCEPT | minor: write φ_M out; N = 0 edge |
| A-L | ACCEPT WITH FIXES | step 1 formula I(ν) = m_U⁻²I(μ_U) + p log m_U and "≥ κ_p − η"; **step 3 written out** (it was not proved as written); restate as ≥ κ_p, citation-free; dominated convergence justified |
| H_all | ACCEPT WITH FIXES | f′ < 0 line; the error is o(n²), a weakening for item 11's exact cases |
| HZ | ACCEPT WITH FIXES | **prior art: Monien 0901.1883 §3** (p = 1 equilibrium, heuristic), recorded with quotes and the novelty wording narrowed; real a > 0 |
| Numerics | ACCEPT WITH FIXES | p = 0.5 density 0.9862 is quadrature error; U* check circular (Rule X); Frank–Wolfe gap unsupported, now marked superseded; check_hz comment |
| Framing | ACCEPT WITH FIXES | explain the PROVED-mod-cite label; Rule A entries per lemma in LOG.md |

**Overall: ACCEPT WITH FIXES.** No mathematical error breaks Theorem H_all or Corollary HZ.

(Condensed from the reviewer's full report, as relayed in the session.)

## Re-check (commit f3ee265): A-L steps 1–4 and the B* optimality paragraph

**ACCEPT.** Every inequality was re-derived. All first-pass fixes are present. Three cosmetic items were applied:
- r_{j+1} → u_j ≤ (j+1)/(d_U n) in 3(c);
- the i = 1 diagonal uses log(1/min) ≤ log(1/u) + log(1/v);
- the HZ status row now reads a > 0.
