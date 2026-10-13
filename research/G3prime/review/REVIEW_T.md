# REVIEW_T: Rule R second reading of PROOF.md §6–§7 (Theorem T, G3′*), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files.
- **Scratch check.** `lemR.py` computed Lemma R's F on the true smooth f for three thinnings (every 2nd, random 50%,
  random 30%) with ε = 0.4. All bounds hold with wide margins:
  - near-pair min F is 0.26–0.76, against the bound ≈ 0.03–0.05;
  - near-pair max F(b−a)/(εa) is 0.94, against the bound 5;
  - far-pair F ∈ [0.82, 0.98], against the bound 1.4.

| Result | Verdict | Required fixes (applied) |
|---|---|---|
| Lemma R | ACCEPT WITH FIXES | state a_ε ≥ 2/ε |
| Lemma K | ACCEPT WITH FIXES | needs both halves of (Hw); vacuous when t₀ ≥ 1 |
| Theorem T, upper | ACCEPT WITH FIXES | near sum over m < εa; cross-factor argument (distinct Mn − a); factor 2 for squares; n log λ = o(n²) |
| Theorem T, lower | ACCEPT WITH FIXES | head near count Σ_{a∈S}, ≤ n·min(n, εMn); small i < a_ε for L_E; factor 2 |
| Remark T′ | ACCEPT WITH FIXES | write out the proof; ε ≍ 2η^{1/3}; ω(η) is δ-free only because C_θ is |
| G3′*-U | ACCEPT WITH FIXES | cross pairs carry ρ(k(a), k(Mn)); (Hw) with U = C log(j+2)L(Cj); Lemma K needs the upper half |
| G3′*-L | **REJECT as written** | order-of-limits gap: a δ(η)-dependent near loss against ε ≍ η^{1/3}. Repair: split near pairs into near-long (δ-free) and near-short (b − a ≤ C log a; loss log(1/δ); ≤ n log(M₂n) head pairs + (t₀(M₂)n)² deep pairs via Lemma K at a second scale M₂); limits n → ∞, M₂ → ∞, M₁, η → 0. Also: state the lower-Z2 far-pair factor; write out the F ≥ cθ′δ computation; Lemma K needs (Hw) upper; step 4 needs only "≥" |
| §6 claims | ACCEPT WITH FIXES | correct the table entries (random 50%; every-2nd has non-convergent density; near-duplicates only to n = 4000, not "1/n"); the Rule N caveat; reword necessity and "not provable" claims as heuristic; "suggest", not "show" |
| Literature (N_d ≥ 0.4075N) | ACCEPT | add the liminf-convention note |

**Overall.** ACCEPT WITH FIXES for everything except G3′*-L, which needs re-review after the two-scale repair.

(Condensed from the reviewer's full report, as relayed in the session.)
