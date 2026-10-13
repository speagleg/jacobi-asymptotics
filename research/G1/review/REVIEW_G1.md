# REVIEW_G1: Rule R second reading of research/G1 (Plan 9), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files.
- **Re-runs.** check_tauberian, check_tailsum and check_regularity reproduce byte-identically.
- **Sources.** Both arXiv PDFs were read; the quotes were verified.
- **Scratch:**
  - `a2.py`: brute-force Heine identity;
  - `alt.py`: a counterexample to A4's density claim;
  - `trunc.py`: K-dependence;
  - an envelope run for the parity weights.

| Result | Verdict | Required fixes (applied) |
|---|---|---|
| H_all ⇔ G = o(n²) | ACCEPT | — |
| Lemma K | ACCEPT | — |
| G1-T | ACCEPT WITH FIXES | retract "(T4) fails numerically" (T4 is δn-scale); (T3) means only the slow-oscillation part; δ small |
| G1-L | ACCEPT WITH FIXES | index slips; the second inequality was false as written (corrected); not "unconditional" |
| A1 | ACCEPT | minor: state a_j ≥ 0 and min b/max b → 1 |
| A2 | ACCEPT WITH FIXES | index Σ_{j>n}; define V(S) for general atoms; derive Heine's formula |
| A3 | ACCEPT | relabel PROVED (citation-free) |
| A4 | ACCEPT WITH FIXES | **density claim withdrawn** (counterexample a = 2b(1 + 0.3(−1)^j)); state block-Cesàro and window-average results; label CONDITIONAL on (CL) |
| §4 stop report | ACCEPT WITH FIXES | label the energy-method remarks heuristic; add BKMM analyticity and saturation quotes; WLXZ squared variable; GAP legend |
| Numerics | ACCEPT WITH FIXES | p = 2, 3 also truncation-limited at large n (true exponent −1); parity fits replaced by an envelope; ω-shrinking supported by the envelope; transcription 1.2360 |

**Overall: ACCEPT WITH FIXES.** G1-T, Lemma K, A1 and A3 are sound. The GAP conclusion of §4 stands.

(Condensed from the reviewer's full report, as relayed in the session.)
