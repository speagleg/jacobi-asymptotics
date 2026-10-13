# REVIEW_RH1: Rule R second reading of RH_p1.md (Theorem RH₁), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus). It read WLXZ v1 §§1–7 and edited no repo files.
- **Scratch:** wlxz_id.py, tc_pipe.py, tc_tend.py.

| Item | Verdict | Fix (applied) |
|---|---|---|
| §1 identification | ACCEPT | Stirling with a sectorial bound (DLMF 5.11); record D̃ ≡ 1/H_n at α = 1 (verified to 30 digits) and that σ's weight is a pure power |
| W1 | ACCEPT WITH FIXES | F1: convention error (V^H vs N^H) — moot after dropping D_H; F2: Airy discs, build V_l/V_r from σ's own weight (no residual jumps); F3: D_H estimates loose, **dropped D_H**, since the band mismatch H_n² = 1 + O(1/n) is handled exactly as WLXZ's own H_n; F4: Rule A log for W1 |
| §3 extraction | ACCEPT WITH FIXES | F5: β_n notation, (U₁)₁₂(U₁)₂₁ = nβ_n, (N₁)₁₂(N₁)₂₁ = 1 at α = 1; F6: S₁ = O(1/n) via the L¹ bound on the long contour |
| TC coefficients | ACCEPT | — |
| Numerics | ACCEPT WITH FIXES | F7: the old 6e−12 was not an accuracy claim; the tail cut-off bias was 3e−8. Now same-pipeline comparison with an exact-TC validation (bias 3e−10 at tend 1e16) gives n²·dev = −0.0417 |
| Labels and citations | FIX | WLXZ v1 quotes added (Theorem 2.3, (4.16)–(4.17), (5.8), §6.1, (6.27)–(6.28), Remark 6.1, (6.34)–(6.37)); v1 recorded; reliance on WLXZ's uniform-up-to-k_n claim noted |

**Overall.** After fixes F1–F7 and the Rule C quotes, Theorem RH₁ can be labelled PROVED-mod-cite (WLXZ v1 §§2–6),
after a re-check.

(Condensed from the reviewer's full report, as relayed in the session.)
