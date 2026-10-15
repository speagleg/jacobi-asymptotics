# Rule R review — Plan 48 (Route II, stage 1): RedA, Theorem RII, Corollary B_{p>1}

Reviewer: independent second reader (Rule R). Branch `plan-48-route2`, commit 56bd70c (`git diff master...HEAD`).
Targets: `research/G1/RH/route2/ROUTE2.md`; PROOF.md §3.17 and §0 row "RII / B_{p>1}"; LOG.md 2026-10-14 entry;
RH/CITATIONS.md "(DLMF-3)"; `RH/route2/checks/*`; plan doc `docs/superpowers/plans/2026-10-14-plan-48-route2.md`.
Compared against: RH/px/RH_px.md (REVIEWED), RH/zeta/RH_zeta_close.md §1 (REVIEWED), PROOF.md §3.3 (T3-conv, Sat_p⁺),
§3.14 (L0, FV⁺, B-cond), RH/CITATIONS.md (KMVV, C–D, DLMF-2), master's research/G1/CITATIONS.md.

## Verdicts

| Claim | Verdict | Recommended label |
|---|---|---|
| Lemma RedA (o)–(iii) | **ACCEPT** (numerics fix F7 only) | PROVED; REVIEWED once F7 is applied |
| Theorem RII | **ACCEPT WITH FIXES** (F1 needed for the whole range α_x ∈ (−1, 1); F3–F6) | PROVED-mod-cite after F1; REVIEWED after re-check of F1 |
| Corollary B_{p>1} | **ACCEPT WITH FIXES** (inherits F1; F3, F9) | PROVED-mod-cite after F1; REVIEWED after re-check |
| Stop condition (i) RESOLVED-mod-cite, (ii) MOOT, GAP-α, GAP-rate, tilt law CONJECTURE | ACCEPT | as stated |

Without F1, the written proof covers only |α_x| ≤ ½, i.e. 1 + p/2 ≤ s ≤ 1 + 3p/2. That range includes the numerics case
p = s = 2, α_x = −½. With F1 (sketched below; it re-uses the decomposition of UR′(d)) it covers all of 1 < s < 1 + 2p.

## Checks done

1. **RedA, re-derived.**
   - *Analyticity.* |φ(τ + iσ − y)| = φ(τ − y)e^{σ²/2}, so the imaginary direction costs only the constant e^{σ₀²/2} on a
     strip. L grows at most linearly (L0(ii)), so L₁ is entire. The worry in the brief, that the Gaussian grows in the
     imaginary direction, is harmless on bounded strips.
   - *(ii).* ∫φ^{(j)}(c − y)dy = 0 for complex c holds by the identity theorem: c ↦ ∫φ(c − y)dy is entire and equals 1 on ℝ.
   - *Local oscillation, ω(τ) ≤ 2δ_m(2e²).* Checked the index ranges. For τ ≥ 1 + log 2, k ≥ e^{τ−1} − 1 ≥ e^{τ−1}/2. Also
     m/λ ≤ (e^τ + 1)/(2e²) ≤ e^{τ−1}/2 and λm ≥ 2e^{τ+2} ≥ e^{τ+1} + 1.
   - *Chaining.* All three ranges are correct. The y < τ/2 tail is killed by ∫_{|z|>τ/2}(1 + |z|)P_jφ.
   - (ii) holds in every strip, so (H_an) with σ₀ = π/p is satisfied (indeed for any σ₀).
2. **RedA (iii), line by line against T3-conv (§3.3).** Path w(t) = vΨ₁ψ^t, f = log ψ, G = sup|log ψ| < ∞. FV/FV⁺ apply
   because ΣvΨ₁ < ∞ by Potter.
   - No centering is needed, since ψ → 1.
   - The difference is bounded by sup_tΣ|log ψ|(μ_n + μ_{n−1}). On k ≥ n/M₀ this is ≤ 2ρ(⌈n/M₀⌉), with ρ defined
     correctly as a tail supremum over all k ≥ m. This is exactly what is needed, and ρ → 0 by (i).
   - Head: Sat_p⁺ with W(t)/w_k(t) ≤ e^{2G}Σ_j j^{−s}Ψ₁(j)/(k^{−s}Ψ₁(k)) ≤ C_ηk^{s+η}. The lower Potter bound for
     Ψ₁ = Ψ/ψ follows from L0(ii) and ψ ≤ e^G. This gives the head term n^{O(1)}e^{−2(n−1)}.
   - a-part: FVa with bounded f, the cross piece |q_{n−1}q_n| ≤ ½(μ_{n−1} + μ_n), and the Sat_p⁺-only bounds
     a_n^{(t)}, b_n^{(t)} ≤ 2M₀^p(n − 1)^{−p}. The constant 6M₀^p2^p is generous and consistent with the proof's 3C_p.
   - The outline's "base-independent" claim is correctly qualified: only W/w_k sees the base.
3. **§2 table vs RH_px.** Each weight-dependent item of RH_px was checked against the table.
   - The lens and saturated transformations (w and 1/(Πw) need Ψ₁ analytic and nonvanishing: exp L₁ ✓).
   - Lemma 1.2.
   - w₀ and D_w.
   - The saturated region, Σ^△ lips and top pieces: q_N^{±1} = poly(N) by Potter, using Ψ₁(N) ≥ cN^{−η}.
   - The Airy edge (q_N analytic near b, log q_N = O(ε₁)).
   - The hard edge.
   - (Y4)_x.
   - The (h1) entries: super-small times |z|^{−η}.

   Weight-free, as claimed: μ*, g, φ, D̃, B, K, F, Lemma 3.5, N₀. One domain point is F4.
4. **Stop condition (i).** The continuation of q_N^{1/2} across (−δ, 0) jumps by a ratio
   exp(½(L₁(T − iπ/p) − L₁(T + iπ/p))) = 1 + O(ε₁), with no rate. This is the analogue of RH_ζ_close's (Λ − iπ/2)/(Λ + iπ/2).
   The diagnosis is correct.
5. **Lemma H1′.** With W̃ := D_w the weight cancels from Ẽ_N (N·D_w^{σ₃} = D_∞^{σ₃}N₀). It also cancels from P̃₀N^{−1}
   on ∂U(0, δ) and from Q̃ inside U(0, δ) and outside the discs (Q̃ = D_∞^{−σ₃}𝒵̃D_∞^{σ₃}N₀).
   - c_± = e^{∓iπα_x} is consistent with KMVV (6.45) as quoted (W̃² = e^{−βπi}w for Im z > 0).
   - It is also consistent with the explicit D_{x^α}² below.
6. **LW1′, re-derived.**
   - D_{x^α}² = (bz/Φ)^α with Φ = (z^{1/2} + (z − b)^{1/2})². Checked: Φ₊Φ₋ = b² on the band; no jump on (−∞, 0); Φ(0) = −b;
     bz/Φ → b/4. Hence D²/z^α = e^{∓iπα}(1 + O(|z|^{1/2})).
   - The q_N part: along the arc-plus-segment path, Re u ≥ T_N and |Im u| ≤ arg z/p < π/p, and the total length in u is
     (arg z + |log(x/|z|)|)/p. With |z − x| ≥ c(x + |z|) on the lips, the scale-invariant integral
     ∫(π + |log u|)u^{−1/2}(1 + u)^{−1}du is finite. The [b/2, b] piece is O(|z|^{1/2}log(2b/|z|)).
   - So ‖v − ṽ‖_∞ ≤ C(N^{−2ν}log N + ε₁,N) → 0.
7. **Local form (§3.2), re-derived.** E_±, F_± are entire, including for α < 0 (1/Γ is entire).
   - S is correct: the (1,2) and (2,2) entries were reproduced from 10.27.4.
   - det S = i/(2 sin απ), so det Ψ̂ = −2i sin απ given det Ψ = 1 (see F5 for the source).
   - α = 0: the coefficient κ = −i/(2π) is reproduced from 10.31.2 (ln(½x) = ½log ζ).
   - Bounds: |Ψ^{±1}| ≤ C|ζ|^{−|α|/2}, and Ψe₂e₁ᵀΨ^{−1} = O(|ζ|^{−|α|}) for |ζ| ≤ 3.
8. **UR′.**
   - (a): the exponent ε^{(1−|α|)/2} is correct.
   - (d): Lemma W at a = ±α/2 needs |a| < ½ ⇔ |α| < 1 ✓. The HS bounds are correct: ∬|s|^{−|α|}|z|^{−|α|} < ∞, and the
     small-ζ block is O(N^{−2}).
   - Lemma W′: the kernel −log u/(ue^{iθ_j} − e^{iθ_i}) is regular at u = 1 and integrable against u^{−1/2}, and the
     Schur/Mellin bound is fine.
   - **(b) is not α-independent: F1.**
9. **(Q ∈ L²_loc), Theorem C′, Proposition D′.**
   - Q = O(|z|^{−|α_x|/2 − η}) pointwise near 0, for fixed N. This is L² on the contour, and it puts Q in I + ∂C(L²) by the
     usual pointwise argument, for every |α_x| < 1.
   - Q̃^{±1} is pointwise O(|z|^{−|α|/2}), which is likewise fine.
   - C′: ‖C_v − C_ṽ‖ ≤ ‖C₋‖‖v − ṽ‖_∞ → 0, then C–D's Neumann series (quoted). **Sup-norm o(1) with no rate is genuinely
     sufficient here**, exactly as in C–D Thm 4.7's proof (quoted: "‖v_Σ − ṽ_Σ‖_{L^∞} → 0 … implies … → 0").
   - D′ re-derived. For |ζ| ≥ 2 the entries of μ̃e₂e₁ᵀμ̃^{−1}e^{2Nφ} are O(|z|^{∓1/2}), and
     ∫r^{−1/2}e^{−cN√r}dr = O(1/N). For |ζ| ≤ 2 the entries are O(N|ζ|^{−|α|}) and |dz| = N^{−2}|dζ|, giving O(ε′/N).
   - Correction term: ‖δμ̃e₂‖₂‖δe₁ᵀμ̃^{−1}‖₂ = O(ε′²/N).
   - **The 1/N comes from the Bessel localization** (e^{2Nφ} confines the mismatch to |z| ≲ N^{−2} up to the |z|^{−1/2}
     tail). It is independent of any rate for ε₁.
10. **Rate consistency.** Q₁ = Q̃₁ + O(ε′/N), with (Q̃₁)₁₂(Q̃₁)₂₁ = c²(1 + O(1/N)). So O(1/n) is consistent with a
    mismatch that has no rate: the mismatch contributes o(1/n). Numerically, n(b_n(w)/b_n(v) − 1) ≈ ϑ_n/2 → 0, which is
    consistent. See F3 for the wording.
11. **Corollary chain.**
    - RedA's L₁ is entire and real on ℝ, and L₁′ → 0 uniformly in |Im u| ≤ π/p. So (H_an) holds (modulo F4's domain
      remark, which RedA's entire L₁ satisfies anyway).
    - RedA(iii) transfers the law with an extra O(ρ(n/M₀)).
    - Example exp√log(t + e): its branch points are at Im u = ±π, outside the strip for p > 1 ✓.
12. **Rule C.**
    - Fetched dlmf.nist.gov/10.25 and /10.31. The quotes of 10.25.2, the §10.25(ii) branch sentence and 10.31.2 match the
      pages.
    - 10.27.4 and 1.14.38–40 are in DLMF-2 (verified in Plan 14's review, not re-fetched).
    - The KMVV (6.16)–(6.28), (6.45) and C–D Thm 4.4 / 4.7 / Prop. 4.9 quotes in RH/CITATIONS.md are those used. No new
      statement of them is used.
13. **Numerics re-run** (from the jacobi-asymptotics root, `.venv/bin/python`).
    - `check_r2_mellin`, `check_r2_lw1` and `check_r2_coeff` reproduce their `.out` files digit for digit.
    - `check_r2_redA` [1]–[2] reproduce; [3] did not finish in the review session (see the end of this file).
    - Findings F7 and F8 below.

## Findings

**F1 (HIGH: a gap in the range 1/2 < |α_x| < 1; fixable). Location: ROUTE2 §4.1, UR′, the bullet "(b), (c), (e): unchanged (they do
not involve α)".**

RH_ζ_close UR(b) proves m := C(gQ̃₊^{−1})Q̃ ∈ ∂C(L²) by the crude bound
|C(gQ̃^{−1})(z)| ≤ C‖g‖_{L²(U(z₀,η))}|z|^{−1/4}dist(z, Σ)^{−1/2} + C_η, together with |Q̃| ≤ C|z|^{−1/4}. The area integral over
ε < |z| < 2ε is then ‖g‖_η·ε, which is o(ε) only through η → 0. So it is exactly borderline at α = −½.

For general α the same bound gives:
- |C(gQ̃^{−1})| ≲ ‖g‖_η|z|^{−|α|/2}d^{−1/2};
- |m| ≲ ‖g‖_η|z|^{−|α|}d^{−1/2};
- area integral ≍ ‖g‖_η ε^{3/2−|α|};
- c_{−1} ≲ ‖g‖_η ε^{1/2−|α|}.

This blows up for |α| > ½. So (b) does involve α. As written, UR′, and hence C′, D′ and RII, are proved only for
|α_x| ≤ ½, i.e. 1 + p/2 ≤ s ≤ 1 + 3p/2.

*Fix (the reviewer checked that it works).* Estimate m through the decomposition of UR′(d) instead of the crude product.
- Core term: z^{a}∫h(s)s^{−a}(s − z)^{−1}ds with |a| = |α|/2 < ½. By Cauchy–Schwarz it is ≲ ‖h‖_η d^{−1/2} + C_η|z|^{−|a|},
  with no |z|^{−|α|}: the s-integral is ≲ |z|^{−2a}/d for a ≥ 0, and ≲ |z|^{2|a|}/d + C for a < 0.
- Ψ̂-commutator and K-terms: these have bounded kernels between |s|^{−|α|/2} and |z|^{−|α|/2} factors. For fixed N they
  are ≲ C_N‖g‖|z|^{−|α|/2}.
- The area integrals are then ‖h‖_η ε^{3/2} + C_ηε^{2−|α|/2} = o(ε) for every |α| < 1.
- The α = 0 log core is the same, with Lemma W′'s kernel.

Alternatively, use Smirnov's theorem: m ∈ E^r of each sector for some r > 0 and m± ∈ L² ⇒ m ∈ E². That needs a new
citation. Write the fix out as UR′(b′). Until then, label RII and B_{p>1} as PROVED-mod-cite only for |α_x| ≤ ½ or keep
them unlabelled.

**F2 (MEDIUM: citation label clash). Location: RH/CITATIONS.md new heading "(DLMF-3)"; LOG.md Plan 48 entry ("quoted in
RH/CITATIONS.md "DLMF-3"").**

Master's research/G1/CITATIONS.md already has "(DLMF-3) NIST DLMF §§10.25, 10.27, 10.32, 10.34, 10.40 … for Plan 46 (Lemma
QLP)". REVIEW_Plan46.md, the plan-46 doc and LOG.md line 341 refer to it. After the merge, "DLMF-3" is ambiguous; both
entries even quote 10.25.2.

*Fix:* rename the Plan 48 entry, e.g. "(DLMF-4)" or "(DLMF-R2)", and update LOG.md and ROUTE2 §3.2. Alternatively,
reference Plan 46's DLMF-3 for 10.25.2 and keep only 10.31.2 as new.

**F3 (MEDIUM: overclaim in the summaries). Location: PROOF.md §0 row "RII / B_{p>1}" ("the slowly varying factor costs
O(ε₁/n)"); §3.17 ("the slowly varying factor contributes O((ε₁(log n − C) + n^{−2ν}log n)/n)"); ROUTE2 Theorem RII "more
precisely …".**

What is proved is Q₁ − Q̃₁ = O(ε′_N/N), i.e. the true problem versus *its own* comparison problem. Q̃ still depends on Ψ₁:
through 𝒵̃ at the Airy edge (weight w₀ ∋ q_N), at order 1/N. Nothing proves that b_n(w₁) and b_n(v) (pure power) differ
by O(ε₁/n). Only O(1/n) follows: both are c(1 + O(1/n)). That statement is the tilt-law territory (GAP-rate).

*Fix:* say "the lip mismatch (the non-Fisher–Hartwig part of the hard edge) moves Q₁, Q₂ by O(ε′_N/N)". Drop "the slowly
varying factor costs O(ε₁/n)" from the §0 row.

**F4 (LOW: domain of (H_an)). Location: ROUTE2 §2 table, first row, and (H_an).**

RH_px's contour reaches the top closing segment N^p + δ′ + i(0, ±δ). There t = N(N^p + δ′)^{−1/p} < 1, so Re u < 0:
outside the closed half-strip Σ_p. "A neighbourhood of Σ_p" covers it only if the neighbourhood contains a fixed
{Re u > −c₀, |Im u| ≤ π/p}. The bound q_N^{±1} = poly(N) there needs L₁ bounded on that set.

*Fix:* state (H_an) on {Re u ≥ −c₀, |Im u| ≤ π/p} with L₁ bounded on {−c₀ ≤ Re u ≤ 0}. RedA's entire L₁ satisfies this,
since L is constant on y ≤ 0. Also say explicitly that Ω_∞ (|z| > N^p + δ′, where Re u < −c₀ is possible) never uses w.

**F5 (LOW: source for det Ψ ≡ 1). Location: ROUTE2 §3.2 ("det Ψ ≡ 1, KMVV (6.33)-type").**

KMVV (6.33), as quoted, is det E_n = 1, not det Ψ = 1. det Ψ = −2ζ^{1/2}(I_αK′_α − I′_αK_α) = 1 follows from the
Wronskian, DLMF 10.28.2 (not quoted). It is needed for det Ψ̂ = 1/det S, although only det Ψ̂ ≠ 0, i.e. Ψ̂^{−1} bounded,
is used.

*Fix:* quote 10.28.2 in the new DLMF entry, or a KMVV statement of det Ψ = 1 if there is one.

**F6 (LOW: misplaced justification). Location: ROUTE2 §4.4 proof of RII, the parenthetical "(the 1/z-coefficient of log D_w is
∫log w₀·(bounded kernel), finite and N-uniform …)".**

Outside the discs Q̃ = D_∞^{−σ₃}𝒵̃D_∞^{σ₃}N₀ contains no D_w. The 1/z coefficient d₁ of log D_w enters only in Q₁ versus
V₁ (Q = D_∞^{−σ₃}VD_w^{σ₃}), where the invariance lemma removes it. Its finiteness for each N is what is needed; uniformity
is not.

*Fix:* move and reword the remark.

**F7 (LOW: numerics, an incorrect comment). Location: check_r2_redA.py [3], comment "for k > 2e4, |log Psi − L1| < 1e−6 (see
[1])"; ROUTE2 Remark RedA-3 ([3]).**

[1] itself shows |log Ψ − L₁(log k)| ≈ 4.5e−3 at 10⁴ and 2.4e−3 at 10⁶ for √log. So [3] compares vΨ with a *hybrid*:
L₁ for k ≤ 2·10⁴ and log Ψ beyond. That is not vΨ₁.

*Fix:* evaluate L₁ for all k (vectorize over k, or interpolate L₁ on a fine τ-grid), or state honestly that [3] is a hybrid
test. RedA itself is proved, so this does not affect any label.

**F8 (LOW: numerics, convergence overstated). Location: ROUTE2 §5 ("K-converged except n = 800 (third digit)"); PROOF.md
§3.17 NUMERICAL ("−0.387 … −0.411").**

From check_r2_coeff.out:
- n = 800: nB = −0.4285 (K = 1.2·10⁵) versus −0.4111 (K = 2.4·10⁵), and E = 1.0281 versus 1.0065. These differ in the
  second digit, and K = 2.4·10⁵ is not shown to be converged.
- n = 400: −0.4033 versus −0.4008.

So the claimed match with the tilted baseline at n = 800 (−0.404 vs −0.411) is not meaningful. T and R are stable.

*Fix:* drop n = 800 from the nB/E claims, or run K = 4.8·10⁵. Reword to "converged to ~3 digits for n ≤ 200".

**F9 (LOW: consistency of the summary). Location: PROOF.md §0 row G1-R and §4 (lines "open: slowly varying Ψ with D(γ) = ∞"),
§3.14 "D(γ) = ∞: no case of QL is proved".**

These are still literally true, since QL is still unproved. But they now omit that the *law* is proved for p > 1,
1 < s < 1 + 2p by a route that bypasses QL. Theorem B-cond (§3.14) is not contradicted: B_{p>1} neither proves nor needs
QL/QL₀, and B-cond's unconditional bounds remain the only statement for p ≤ 1.

*Fix:* add one-line cross-references after Rule R. Merge note: the branch is based on d19c3ea and lacks master's §3.15–3.16.
§3.17 is the right number after the merge; keep both.

**F10 (INFO: Lemma W′ flattening). Location: ROUTE2 §4.2 "The flattening step".**

On a single C² arc, 1/(γ(ρ) − γ(r)) − 1/((ρ − r)e^{iθ}) is O(1) only when the measure factor γ′(ρ)dρ is included, i.e.
with arclength parametrisation and the error term taken as γ′(ρ)/(γ(ρ) − γ(r)) − 1/(ρ − r). Without it the difference is
O(r/|ρ − r|). For W′ this is harmless either way: the factor log(r/ρ) vanishes at ρ = r, which makes the product O(1).

*Fix:* add half a sentence. (Lemma W is inherited, REVIEWED.)

## Items checked and found correct (no action)

- Plan review-focus items: RedA oscillation and chaining; ∫φ^{(j)} = 0 for complex c; the T3-conv transfer.
- The §2 table, which misses nothing weight-dependent apart from F4. The (h1) entries are super-small × |z|^{−η}. The Σ^△
  lips near b lie outside U(b, ε), as in RH_ζ_close F10.
- The strip |Im u| < π/p suffices for the lips, lens and saturated lips, since arg z ∈ (−π, π).
- LW1′ (path, the bound |z − x| ≥ c(x + |z|), the scale-invariant integral, D_{x^α}² and c_±).
- The local form and the O(|ζ|^{−|α|}) bound.
- UR′(a), (d) and Lemma W′.
- (Q ∈ L²_loc), including the D_w-conjugation exponents.
- D′ in both ζ-ranges, including the factor N from N^{σ₃/2}.
- Stop (i) RESOLVED-mod-cite and (ii) MOOT: correct (the fixed order α_x; the drifting order is never used).
- GAP-α: the reasoning is correct. Lemma W needs α_x/2 < ½, and L²_loc fails at the Bessel scale.
- Rule A items (a)–(g): sensible. (b) Ψ = k^ρ correctly fails ε₁ → 0.
- LW1′ numerics: ratio 2.40 → 2.90, consistent with the pure-tilt limit π.
- Mellin: M₀ = π² reproduced.

## Recommended labels after fixes

- RedA: PROVED, REVIEWED (after F7).
- LW1′: PROVED.
- Local form: PROVED-mod-cite (after F5).
- Lemma W′: PROVED.
- UR′: PROVED-mod-cite after F1. Until then, valid as written only for |α_x| ≤ ½.
- Theorem RII and Corollary B_{p>1}: PROVED-mod-cite (sources as listed). REVIEWED after a re-check of F1 (and F2–F4).
- Stop (i) RESOLVED-mod-cite; (ii) MOOT; GAP-α, GAP-rate as stated; tilt law CONJECTURE; numerics NUMERICAL (p = s = 2 only).
- Novelty UNCHECKED.

## Numerics re-run log

`check_r2_mellin`, `check_r2_lw1` and `check_r2_coeff` reproduced exactly. `check_r2_redA` [1]–[2] reproduced exactly. [3] did not finish within ~45 min in the review session (it
evaluates 2·10⁴ Gaussian quadratures per example); it was not re-run to completion. Its .out values are consistent with ROUTE2
Remark RedA-3, but see F7 for what [3] actually tests.
