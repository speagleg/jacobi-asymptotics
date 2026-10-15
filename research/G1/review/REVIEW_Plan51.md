# REVIEW_Plan51: Rule R review of Plan 51 (Route II for 0 < p < 1; Lemma CT)

Reviewer: independent second reader (Rule R), 2026-10-14. Branch `plan-51-r2plt1`, commit d7289d8 (`git diff master...HEAD`,
merge base e5fb7a5). Targets: `research/G1/RH/route2/ROUTE2_plt1.md`; `research/G1/PROOF.md` §3.20, the §0 row
"RII_{<1} / CT / B_{p<1}" and the §4 cross-reference; `research/G1/LOG.md` Plan 51 entry; `research/G1/RH/CITATIONS.md`
"(DLMF-5.11, Plan 51)"; `checks/check_r2p_{coeff,lw1}.py/.out`. Bases: ROUTE2.md (Plan 48, REVIEWED) and REVIEW_Plan48.md
(including UR′(b′)); RH_plt1b.md (REVIEWED). Comparison: Plan 52 (ROUTE2_alpha.md, Theorem SH/SH-r, REVIEWED and **already
merged to master** as 9495e14; the path `/mnt/c/Users/gspea/source/repos/ja-plan52` named in the brief does not exist, so I read
Plan 52 from master in `jacobi-asymptotics`).

**Overall verdict: ACCEPT WITH FIXES.** No mathematical error affects any stated theorem. The fixes are a merge and naming
conflict with Plan 52 (F1), a mislocated diagnosis of the RH_plt1b sign slip (F2), and small text corrections (F3–F6).

## Verdicts

| Claim | Verdict | Recommended label |
|---|---|---|
| §1 Lemma S_w (strip \|Im u\| ≤ π/2; π/p not needed) | ACCEPT | PROVED (bookkeeping on RH_plt1b §2) |
| (H_an^{<1}); RedA in every strip; exp √log(t + e) example | ACCEPT | as stated |
| §2 change table; seams (Ψ₁ does not enter F; no seam jump with W̃ := D_w) | ACCEPT | PROVED (bookkeeping) |
| §3.2 Lemma X0 | ACCEPT WITH FIX (F3: the \|z\| ≥ 1 bound is (1 + log\|z\|)², not (1 + log\|z\|); not used) | PROVED-mod-cite (DLMF 5.5.1, 5.11.1 + §5.11(ii)) |
| Sign convention / RH_plt1b slip | slip REAL, but the diagnosis puts it in the wrong line (F2) | text fix only |
| §3.3 LW1′_{<1} | ACCEPT (F4, F5 cosmetic) | PROVED (given X0, RH_plt1b, ROUTE2 §3.3) |
| §4.1 UR′_{<1} incl. (b′) | ACCEPT | PROVED-mod-cite |
| §4.2 (Q in L²), C′_{<1}, D′_{<1} | ACCEPT | PROVED-mod-cite |
| **Theorem RII_{<1}** | ACCEPT | PROVED-mod-cite; REVIEWED after fixes |
| **Lemma CT** (i) identity, (ii) limits, (iii) rate | ACCEPT (every step re-derived; rate claim correct; F1 naming) | PROVED (self-contained; classical identity, novelty not claimed) |
| **Corollary RII⁺_{<1}** | ACCEPT (F6 remark on the choice of s₀) | PROVED-mod-cite |
| **Corollary B_{p<1}** | ACCEPT | PROVED-mod-cite |
| Remark CT-px | mathematically correct, but **duplicates** Plan 52's Corollary B_all (REVIEWED, on master) (F1) | make it a cross-reference: "second proof of Plan 52's B_all via the Cholesky form" |
| GAP-rate, GAP-p1 | ACCEPT | GAP |
| §6 numerics | ACCEPT (re-run reproduces every printed number; F7 scope) | NUMERICAL (p = ½, one Ψ, atom + continuum-tail model) |

## Checks done

1. **Lemma S_w (strip), item by item against RH_plt1b §1–§2.**
   - |Im u| = |arg z|/p, so S_in = {|arg z| < πp/2} is exactly |Im u| < π/2, whatever p < 1 is.
   - The band lens in U(0, δ) is the region between the band and the lips at ±θ_L. Outside U(0, δ), the lens and Σ^△ heights are
     < δ tan θ_s/2 ≤ (Re z) tan θ_s/2, so arg < arctan(½ tan θ_s) < θ_s. The top segment has arg ≈ δ/N^p, with Re u ∈ [−c₀, 0]:
     that is why (H_an^{<1}) also needs "bounded for Re u ≤ 0".
   - The (Y4)_x lens sector is φ₀ ≤ θ_L (RH_plt1b needs only φ₀ < πp). The hard-edge true jump on the lips needs w₀ at arg ±θ_L.
     The comparison jump needs only D_w, which is built from w on [0, b].
   - Ω_∞ and S_out ∩ U(0, δ) carry no weight: V = C_∞QF^{σ₃} there, and F is weight-free.
   - So every evaluation point lies in |arg z| ≤ θ_w < θ_s, and |Im u| < π/2 holds strictly.
   - **Why not π/p:** π/p was the p > 1 bookkeeping (arg z up to π). For p < 1 the seam construction confines w to S_in, and
     RH_plt1b's glued W̃ (which did enter S_out) is replaced by D_w.
   - The hard-edge disk, lips, Bessel rays and band are all covered.
   - **KMVV angle freedom.** The quote ("any angle in (0, π)") is in CITATIONS via RH_plt1b, and π − θ_L ∈ (0, π). On
     |arg ζ| < π − θ_L, |arg 2ζ^{1/2}| < π/2, so the principal-branch I_α/K_α asymptotics apply. The thin sectors are the Hankel
     sectors.
   - The lip decay is Re ζ^{1/2} = |ζ|^{1/2}cos((π − θ_L)/2) = |ζ|^{1/2}sin(θ_L/2) ✓.
2. **Example L₁(u) = √log(e^u + e).** The singularities are at e^u + e ∈ (−∞, 1], i.e. e^u real and negative, i.e. Im u ≡ π
   (mod 2π). So L₁ is analytic on |Im u| < π, and (H_an^{<1}) holds (L₁′ = e^u/(2(e^u + e)√log(e^u + e)) → 0 uniformly). The π
   strip fails at p = 1, and the π/p strip fails for p ≤ 1 ✓. RedA(ii) holds for every σ₀ (ROUTE2 §1). The constants are
   e^{π²/8} ≈ 3.43 and e^{2π²} ≈ 3.7·10⁸ ✓.
3. **Seams.** F = D·B_in·K·e^X on S_in and F = B_out·K·e^X on S_out. F is continuous across Γ±, and L± and X use only
   μ(t), e^{∓2πit}, B_in and B_out, none of which involve Ψ₁ ✓. D_w is analytic off [0, b], so Q̃ has no seam jump. The seam
   enters only through h_N ∋ e^{−2X} ✓.
4. **Lemma X0.**
   - (i), |ζ| ≤ 1: |μ(t)| ≤ sec²(π/4)·(1/12)/|t| = 1/(6|t|) at |ph t| = π/2 (DLMF §5.11(ii) with n = 1, re-fetched; see
     Rule C below). This gives ≤ |ζ|^{1/p}/(6N) ≤ |ζ|. The e^{−2π|t|} term is super-small, and the B_in and B_out terms are O(|ζ|).
   - (i), |ζ| ≥ 1: re-derived. This uses 5.5.1 for |t| < 1, the concavity bound 1 − e^{−y} ≥ (1 − e^{−2π})y/(2π), and
     |1 − w| ≥ sin θ_s on the ray.
   - (ii): X − X(0) = (z/2πi)Σ±∫L/(ζ(ζ − z)) ✓. The kernel bound |ζ − z| ≥ (κ/3)(|ζ| + |z|) holds in both cases (|ζ| ≥ 2|z|,
     and |ζ| < 2|z|) ✓.
   - Both |z| ≤ 1 integrals ✓.
   - The lip at +θ_L has distance |z|sin(θ_s − θ_L) to Γ₊ and ≥ |z|·min(1, sin(θ_s + θ_L)) to Γ₋, so κ = sin(πp/4) works ✓.
   - Error found in the |z| ≥ 1 clause: F3.
5. **Sign convention.** RH_px §1 defines D̃ = exp(−μ) with μ **Binet's function**. RH_plt1b repeats "D̃ = exp(−μ(t))" in its §1
   first bullet, and its t → 0 expansion "−μ = ½log 2π + ½Log t + …" is correct for Binet's μ (μ_B = LogΓ − (t − ½)Log t + t −
   ½log 2π ≈ −½Log t − ½log 2π as t → 0). Only RH_plt1b's **displayed definition** μ(t) := ½log 2π + (t − ½)Log t − t − LogΓ(t)
   has the wrong sign (it is −μ_B). The L± formula, the proof and the check (which computes +μ_displayed = −μ_B) are mutually
   consistent. I also re-did the real-part bookkeeping at ∞; it vanishes only with log D̃ ≈ ½log 2π + ½Log t. See F2.
6. **LW1′_{<1}.**
   - The h_N part: |log h(x) − log h(z)| ≤ C(x^{1/2} + |z|^{1/2}) (through h(0)). The integral is C|z|^{1/2}∫(x^{1/2} + |z|^{1/2})
     x^{−1/2}(x + |z|)^{−1}dx = O(|z|^{1/2}log(2b/|z|)) ✓.
   - |μ(t)| ≤ C/|t| on |arg t| ≤ π/4 (sec²(π/8)) ✓.
   - The q_N part: Re u ≥ T_N along arc + segment, |Im u| ≤ π/4 ✓. F5 is a constant slip.
   - The final sup ✓.
7. **UR′_{<1}(b′).**
   - Re-read REVIEW_Plan48 F1 and ROUTE2 §4.1(b′). The geometric inputs are: the factorization Q̃ = G(−z)^{ασ₃/2}Θ (it needs
     only N²f/(−z) analytic and positive near 0); Θ constant per sector; the core bound |T_a| ≤ C‖h‖d^{−1/2}, which uses only
     |a| < ½ and rays; and ∬d^{−1/2}dA = O(ε^{3/2}) for finitely many arcs at distinct angles.
   - At 0 the star is {band, two lips at ±θ_L}. No arc lies on (−δ, 0) and no seam is a contour, because V, Q and Q̃ have no seam
     jump (check 3). So (b′) transfers verbatim, with constants depending on θ_L only ✓.
   - (c) Carleson, (d) KMVV (6.28) on the π − θ_L sectors, and (e) Airy are as in ROUTE2 ✓.
8. **D′_{<1}.** For |ζ| ≥ 2: ∫(|z|^{1/2}log + ε₁)|z|^{−1/2}e^{−cN|z|^{1/2}} = O(N^{−2}log N + ε₁/N) ✓. For |ζ| ≤ 2: O(ε′_N/N) ✓.
   Extraction as ROUTE2 §4.4 ✓.
9. **Lemma CT, line by line.**
   - (o) Cholesky and nesting ✓. Positivity uses supp σ ∩ (0, ∞) infinite ✓.
   - (i) a_j = l_j² + m_{j−1}², b_j = l_jm_j; (LᵀL)_{jj} = l_j² + m_j², (LᵀL)_{j+1,j} = l_{j+1}m_j ✓. Associativity: every product
     is lower-triangular × lower-triangular or bidiagonal, so all sums are finite ✓. ∫RRᵀx dσ = LᵀL^{−ᵀ} = (L^{−1}L)ᵀ = I ✓.
     Uniqueness of orthonormal polynomials with positive leading coefficient ✓.
   - (ii) r_j = A_j − B_j/r_{j−1} ✓. T_j(r) − r ≤ [−(1 − r)² + δ(1 + r)]/r ✓. The "below" step: the decrement is ≤ −3ε²/4 ≤ −ε²/2 ✓.
     The "above" step: ε²/(1 + ε) − 2δ ≥ (2/3 − 1/4)ε² > ε²/4 ✓. Invariance of (1 − ε, 1 + 2ε) ✓.
   - (iii) Every inequality was re-derived:
     - η_j ≤ |A − 2| + 2|B − 1| (r ≥ ½) ✓;
     - negative side g/(1 − g) ≥ g + g² ✓;
     - positive side e/(1 + e) ≤ e − e²/2 on [0, 1] ✓;
     - the invariant band 2Kj^{−1/2} for j ≥ 16/K² ✓ (they bound by −K²/(4j), weaker than the true −K²/j but valid);
     - entry via 1/(e − e²/4) ≥ 1/e + ¼ ✓.
   - **Rate claim.** Only e_j² (in (r + 1/r)/2 = 1 + e²/(2(1 + e))) and the increments r_{j+1}/r_j = 1 + O(1/j) enter the output.
     So O(1/j) in ⇒ ã/(2b̃) − 1, b̃/b − 1 = O(1/j) out ✓. Then B̃_j − 1 = O(1/j) follows from b̃/b and B, so CT iterates ✓.
     **CT does not claim r_j − 1 = O(1/j).** It proves O(j^{−1/2}), and that is sharp for the recursion: with η_j = 0.5/j,
     e_j√j → 0.7071 (reviewer run, j = 10³ … 10⁶). This is exactly the Plan 52 review's observation (G_n − c = O(√r_n), sharp;
     only increments matter), and CT handles it correctly.
   - **Equivalence with Plan 52.** Plan 52's chain-sequence variables are g_j = l_j², h_j = m_{j−1}², β_j = g_{j−1}h_j = b_{j−1}².
     So r_j² = g_j/h_{j+1}, and CT(ii)/(iii) is Plan 52's CS/CS-r in ratio form. CT needs only ratio hypotheses (A_j → 2,
     B_j → 1), with no n^p normalization: slightly more general, same content.
   - Identity, independent check (reviewer, mpmath 60 digits, 40 random atoms in (0, 1) plus an atom at 0, n = 20): LᵀL vs
     J(xσ) agree to 10⁻⁶⁰.
   - xσ_{s,Ψ} = σ_{s+p,Ψ} ✓.
   - s₀: m = ⌈(s − 1)/p⌉ − 1 gives s₀ − 1 = p((s − 1)/p − m) ∈ (0, p] ✓. For s ≥ 1 + 2p, m ≥ 1 ✓.
10. **Corollary B_{p<1}.** RedA(i)–(iii) are stated in ROUTE2 §1 for every p > 0 and s > 1 (REVIEWED). (H_an^{<1}) holds for
    RedA's entire L₁ ✓. The rate is O(1/n + ρ(⌈n/M₀⌉)) ✓.
11. **Rule C.** dlmf.nist.gov/5.11 and /5.5 were re-fetched on 2026-10-14. The 5.11.1 sector condition "|ph z| ≤ π − δ", the
    §5.11(ii) sentence "terminated at k = n − 1 (k ≥ 0) … If z is complex, then the remainder terms are bounded in magnitude by
    sec^{2n}(½ ph z) for (5.11.1), and sec^{2n+1}(½ ph z) for (5.11.2), times the first neglected terms", and 5.5.1 "Γ(z+1) = zΓ(z)"
    (no condition in §5.5(i)) all match the CITATIONS quotes verbatim ✓.
12. **Numerics re-run** (from `jacobi-asymptotics`, `.venv/bin/python ../ja-plan51/.../check_r2p_lw1.py` and `check_r2p_coeff.py`).
    See the log at the end.

## Findings

**F1 (MEDIUM: merge and naming conflict with Plan 52; no math change). Location: ROUTE2_plt1 label table, §5.1 title "Lemma CT",
§5.3 Remark CT-px, §7; PROOF.md §0 row "RII_{<1} / CT / B_{p<1}", §3.20 "Remark CT-px", §4 cross-reference; LOG.md.**
Plan 52 (REVIEWED, merged to master 9495e14) already has the following:
- a **"Lemma CT"** (ROUTE2_alpha §2.2: the LU/Christoffel transfer α̃_n = g_n + h_{n+1}, β̃_n = g_nh_n);
- Theorems SH and SH-r (the law and its regular rate pass from σ to xσ);
- **Corollary B_all** (p > 1, every s > 1; O(1/n) under (H_an)), the PROOF §0 row "SH / B_all", and §3.21 ("GAP-α closed for
  the law").

As a result:
1. After merge, PROOF.md has two different statements named "Lemma CT".
2. Remark CT-px is a second proof of B_all, labelled here as a new closure of GAP-α ("Rule R pending").
3. The §4 cross-reference line and the §0 G1-R line will collide with Plan 52's edits of the same lines.

Fix:
- Rebase onto master, and rename Plan 51's lemma (e.g. "Lemma CT-Ch (Cholesky form)").
- State the equivalence: g_j = l_j², h_j = m_{j−1}², r_j² = g_j/h_{j+1}. CT-Ch(ii)/(iii) is Plan 52's CS/CS-r in ratio form, with
  ratio-only hypotheses.
- Turn Remark CT-px into a cross-reference ("independent second proof of Corollary B_all, §3.21").
- Corollaries RII⁺_{<1} and B_{p<1} may cite either CT-Ch(iii) or SH-r; both are valid.
- Merge the §4 line with Plan 52's.

**F2 (LOW: the RH_plt1b sign slip is real but mislocated). Location: ROUTE2_plt1 §3.2 "Sign convention"; LOG.md Plan 51 last
bullet; PROOF.md §3.20 "(Sign note …)"; docstring of check_r2p_lw1.py.**
- RH_plt1b is consistent with **Binet's** μ (RH_px §1: "D̃ = … = exp(−μ(t)), where μ is Binet's function") in three places:
  (a) "D̃ = exp(−μ(t))"; (c) L± = −μ − …; (d) the t → 0 expansion "−μ = ½log 2π + ½Log t + …".
- Only (b), the displayed definition μ(t) := ½log 2π + (t − ½)Log t − t − LogΓ(t), has the opposite sign. It is −μ_Binet.
- So the slip is the sign of that one displayed definition, not "−μ should be +μ".
- ROUTE2_plt1 then defines its own μ := log D̃ = −μ_Binet. That collides with RH_px's μ.

Fix:
- Reword the note: "RH_plt1b §1's displayed definition of μ has the wrong sign; with Binet's μ (RH_px), L± = −μ − … is correct
  as written".
- In ROUTE2_plt1, use μ for Binet's function and write L± = −μ(t) − …, or rename the local quantity (e.g. λ(t) := log D̃).
- Adjust the LOG/PROOF note and the script docstring.
- No statement changes; only |μ| enters.

**F3 (LOW: Lemma X0(ii) large-|z| clause). Location: ROUTE2_plt1 §3.2, (ii) last clause, and the last line of the proof.**
- For |z| ≥ 1, ∫_1^∞(1 + log ρ)ρ^{−1}(ρ + |z|)^{−1}dρ ≥ |z|^{−1}·(log|z| + ½log²|z|)/2. So the proof as written gives
  C(1 + log|z|)²/|z|, not C(1 + log|z|)/|z|, and the clause should read |X(z) − X(0)| ≤ C(1 + log|z|)² (or needs a better
  argument).
- It is used only as "bounded N-uniformly on [η₀, b]" in LW1′_{<1}, which holds either way.
- Fix: replace the exponent, or restrict the clause to η₀ ≤ |z| ≤ R with C = C(R).

**F4 (LOW: typo). Location: ROUTE2_plt1 §3.1, line "D/D̃ − 1 = O(exp(−2π sin(θ_L/p)|t|)) = O(exp(−√2πN|z|^{−2}))".**
|t| = N|z|^{−1/p}, so the exponent is −√2πN|z|^{−1/p}. |z|^{−2} is the p = ½ case only. Fix the exponent.

**F5 (LOW: constant). Location: ROUTE2_plt1 §3.3, q_N bullet, "|log q_N(x) − log q_N(z)| ≤ ε₁,N(π/4 + |log(x/|z|)|)/p".**
The arc in u has length θ_L/p = π/4 already, so the bound is ε₁,N(π/4 + |log(x/|z|)|/p). Only the constant changes; the
scale-invariant integral is still finite. Fix the formula.

**F6 (LOW: Rule A (e) inaccurate; optional strengthening). Location: ROUTE2_plt1 §7 Rule A (e); §5.2 proof of RII⁺_{<1}.**
- "CT avoids the endpoint by choosing s₀ ∈ (1, 1 + p]" is only half true. α_x(s₀) = (s₀ − 1 − p)/p ∈ (−1, 0], so it avoids
  α_x → +1 but comes arbitrarily close to −1 when s − 1 is slightly above a multiple of p.
- This is harmless, since RII_{<1} covers all |α_x| < 1 for each fixed s.
- But the choice s₀ ∈ (1 + p/2, 1 + 3p/2] (possible for every s > 1 + p/2) keeps |α_x| ≤ ½. Then RII⁺_{<1} for s > 1 + p/2 needs
  only the |α_x| ≤ ½ part of UR′ (plus Lemma W′ at α_x = 0), as Plan 52 F2 noted for p > 1.
- Fix: correct the sentence, and optionally add the remark.

**F7 (INFO: numerics scope). Location: ROUTE2_plt1 §6; PROOF.md §3.20 NUMERICAL paragraph.**
- (a) The coefficient numerics are for the model measure "atoms k ≤ K plus a Gauss–Legendre continuum tail to 10⁴⁸". K-doubling
  tests the atom/tail seam, not the tail quadrature parameters (ratio 1.02, 8 nodes, T_END). There is one p (½) and one Ψ.
  Labels: NUMERICAL ✓, but say "model measure", as Plan 45 does.
- (b) In `check_r2p_lw1.out` [2b] the sup is attained at the largest radius |z| = 0.5, so the printed Q_N does not by itself
  probe the |z| → 0 claim of X0.
  - The reviewer's run on the same code at |z| = 10⁻⁸, 10⁻⁶, 10⁻⁴, 10⁻² (band and lip θ_L) gives ratios 0.0247, 0.0323, 0.0469,
    0.0851 at N = 10², and 0.0257, 0.0337, 0.0489, 0.0887 at N = 10⁶. These are N-flat and decreasing as |z| → 0.
  - This is consistent with X0, and in fact with the sharper |X − X(0)| = O(|z|).
  - Optional: print the small-|z| sup separately.

**F8 (INFO: labels in the summary row).** The PROOF §0 row says "a_n/b_n → 2, b_{n−1}/b_n → 1 transfer". The output that gives
the *same constant* c(p), b̃_n/b_n → 1, is stated in ROUTE2_plt1 but not in the row. Optional: add "and b̃_n/b_n → 1".

## Items checked and found correct (no action)

- Lemma S_w's list is complete for RH_plt1b's contour. The (Y4)_x sector needs only φ₀ ≤ θ_L < πp.
- "Why not π/p": no evaluation in S_out (check 1).
- The no-seam-jump claim for Q, Q̃.
- The KMVV angle freedom, and the Bessel sectors at π − θ_L.
- UR′_{<1}(b′): a star of three C² arcs at 0, ±θ_L, with N-independent constants.
- (Q in L²) with D_{h_N} bounded at 0, for fixed N.
- D′_{<1} integrals; extraction.
- Lemma CT (o)–(iii) and the iteration.
- s₀ existence.
- RedA's applicability for p < 1.
- The DLMF quotes.
- The statement "no claim on the 1/n coefficient" (GAP-rate) is kept, as in Plan 48 F3.

## Recommended labels after fixes

| Item | Label |
|---|---|
| Lemma S_w, change table, seams | PROVED (bookkeeping) |
| Lemma X0 (with F3) | PROVED-mod-cite (DLMF 5.5.1, 5.11.1 + §5.11(ii)) |
| LW1′_{<1} | PROVED (given X0, RH_plt1b, ROUTE2 §3.3) |
| UR′_{<1} (incl. (b′)), C′_{<1}, D′_{<1} | PROVED-mod-cite |
| Theorem RII_{<1} | PROVED-mod-cite; Rule R ACCEPT WITH FIXES — REVIEWED after fixes |
| Lemma CT (renamed per F1) | PROVED (self-contained; classical identity; equivalent to Plan 52 CS/CS-r) |
| Corollaries RII⁺_{<1}, B_{p<1} | PROVED-mod-cite; REVIEWED after fixes |
| Remark CT-px | cross-reference: second proof of Plan 52's Corollary B_all (no new label) |
| GAP-rate, p = 1 | GAP |
| §6 numerics | NUMERICAL (p = ½, Ψ = exp √log(k + e), model measure) |

## Numerics re-run log (reviewer, 2026-10-14)

- `check_r2p_lw1.py`: identical to the committed `.out`.
  - [1] ratios 1.647, 1.972, 2.19, 2.389, 2.508.
  - [2a] X(0) = −1.242, −1.933, −3.314, −4.695.
  - [2b] Q_N = 0.2297, 0.2406, 0.2417.
  - Extra small-|z| probe (F7(b)) as above.
- `check_r2p_coeff.py` (full run, 108 s): identical to the committed `.out` in every line except the timing stamp.
  - [1] nB and E for s = 1.5, 1.75, 2, 2.5 at K = 10⁵ and 2·10⁵; K-doubling 9.7e−8.
  - [2] CT identity 8.3e−17 / 8.0e−17 and 8.7e−17 / 8.2e−17; n(r_n − 1) = 0.49 … 0.55 and 1.70 … 1.78; Laguerre 7.1e−15 … 1.4e−14.
  - [3] quad vs long double 5.1e−14.
  - [4] no-tail −1.81 … −105.9.
  - The doc's tilt ratio (nB(w) − nB(v))/θ_n = 0.1030/0.2262 = 0.455 → 0.0857/0.1837 = 0.467 (s = 2) ✓.
- Independent: the Cholesky identity on a random 41-atom measure (with an atom at 0) holds to 10⁻⁶⁰ (mpmath). The recursion e_j =
  e_{j−1}/(1 + e_{j−1}) + 0.5/j gives e_j√j → 0.7071, so O(j^{−1/2}) is sharp for CT(iii)'s r_j − 1. The output rate is
  unaffected.
