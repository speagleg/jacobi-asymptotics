# Rule R review A: JZC_TODA (Theorem T, T_H) and JZC_SHIFT (Theorem SH)

Reviewer: independent second reader (Rule R), reviewer **A**, 2026-10-23. Branch plan-e2-d2.

- **Targets** (both NOT REVIEWED before this report):
  - research/G1/RH/spectral/JZC_TODA.md, sha256 05aa649f…f246f7 (in commit 7c18fcd);
  - research/G1/RH/spectral/JZC_SHIFT.md, sha256 ea8923f4…ed646 (in commit af22e48).
- **Read for this review:**
  - AGENTS.md and VERIFICATION_POLICY.md;
  - papers/paper2: sec_front.tex (Definition A, main theorem), sec_5.tex (standing assumptions, Lemma interp, Lemma
    invariance, (eq:t)–(eq:W), Lemma bandweight, Lemma gfunction, (O1)–(O5), (eq:W0), Lemma weightdomain, Remark angles,
    Lemma pottersector), sec_6.tex (Proposition frame, items F1–F8, headers only), sec_7.tex (introduction, the Conway–Deift remark);
  - E3.md §§3–5 (Lemma E3.4, Lemma E3.5, Prop E3.6) and its table;
  - RH_plt1b.md (all of it: seam scalar, hard edge, glued W̃);
  - JZC_M3a_H.md §1 (Theorem H setting and (i)), and the headers and weight-related lines of JZC_M3a_H_G12, _G3, _G23plt1,
    _Ha, _Hc;
  - toda_engine.py vs w2_engine.py (diff), and the check scripts named below.
- **Not done:** I did not re-read E_pgt1, E_plt1, RH_px or G1u line by line. For those rows of the transfer table I checked
  only that the weight enters as the author says (§2.2).
- I edited nothing except this file. All re-runs were done in an isolated copy of the checks tree (scratchpad `rr/`), with
  **empty** engine caches except where stated. Scripts and outputs are in
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewTODA_A/ and
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/rrout/.
- No claim about RH is made or implied here. The "zeta times" enter only as the numbers ζ(−jp), ζ(−jp, 1 + δ) in the
  band-factor parameters.

## Overall verdicts

| Item | Verdict |
|---|---|
| **Theorem T** (JZC_TODA) | **ACCEPT WITH FIXES**. After T1–T5: PROVED-mod-cite + REVIEWED. The one non-elementary step, Lemma T.A, holds. Its transfer table is correct for the lattice. Independently, ball-arithmetic computations on the actual tilted lattice agree with Theorem T (i) at first and second order in τ and at finite τ = ±3, ±10 (§3.3). |
| **Theorem T_H** (JZC_TODA) | **ACCEPT WITH FIXES**. The Hurwitz half of Lemma T.A is stated only as "the same bounded-factor argument". Fix T2 supplies the row list. It is not a gap in substance: the tilt is a function of x, so in the z-plane it is the entire factor e^{P_τ(z/n^p)} for any node set. Numerical support at δ = −1/2 is in §3.3 (D). After T2: PROVED-mod-cite + REVIEWED. |
| **Theorem SH** (JZC_SHIFT) | **ACCEPT WITH FIXES**. Lemmas LB, D, R, H and the proof are correct; I re-derived each one. On β′ = ν with integer exponents: PROVED-mod-cite (Theorem T) + REVIEWED. Fractional, symbolic and pole exponents (Cor SH.2): same label, but the identification of the continued layers with JZC_W2's pole layers inherits JZC_W2 Prop 2.1, which is NOT REVIEWED (fix S3). On β′ ≠ ν, the hypothesis (T_H) is now supplied by JZC_TODA's Theorem T_H with Cor T.3, so Cor SH.3 is PROVED-mod-cite once JZC_SHIFT is updated (fix S1). |

No counterexample was found. No stop condition of AGENTS.md is triggered.

## 1. Re-runs (Rule R: "re-run the checks")

Python: the session venv, `-B`. The tree was copied to scratchpad `rr/` with `tmp/toda/` and `tmp/shift/` **empty**, so
every engine below was run fresh, except `shift_existing`, which reads the JZC_W2 caches `tmp/w2/` (copied; these are
JZC_W2's exact outputs, as in the original run). The diffs are against the stored `.out` files.

| script | fresh engine? | result | diff vs stored `.out` |
|---|---|---|---|
| toda_measures.py | (no engine) | ALL 736 IDENTITIES HOLD; ALL 864 CONTROLS FAIL | **byte-identical** |
| toda_layers.py (L1–L3 at SHI = 16, Q1–Q4 at SHI = 30) | yes, all 7 configurations | see §1.1 | see §1.1 |
| shift_toda.py | — | ALL 40 CHECKS PASSED (31 identities, 9 controls) | identical except timing lines and the trailing "EXIT 0" (added by the author's runner) |
| shift_existing.py | tmp/w2 caches (JZC_W2) | ALL 60 CHECKS PASSED (40 / 20) | identical except "EXIT 0" |
| shift_dressing.py | uses eng_R1 if present | first run without eng_R1: 17 checks; the (E4) R1 comparison is skipped (it is conditional on the file, l. 117). After the fresh R1 run: **ALL 18 CHECKS PASSED (14 / 4)** | identical except timings and "EXIT 0" |
| shift_exact.py R1 | **yes** (85 s) | ALL 10 CHECKS PASSED | identical except the "cached"/timing line; **engine JSON byte-identical** to tmp/shift/eng_R1_6bd04b9e02e1.json |
| shift_exact.py R4 | **yes** (64 s) | ALL 16 CHECKS PASSED | as R1; engine JSON byte-identical |
| shift_exact.py R5 | **yes** (6 s) | ALL 19 CHECKS PASSED | as R1; engine JSON byte-identical |
| shift_exact.py R6 | **yes** (14 s) | ALL 24 CHECKS PASSED | as R1; engine JSON byte-identical |

So four of the seven registered runs (R1, R4, R5, R6; the task asked for at least two) were reproduced from scratch, with
byte-identical exact outputs. R2, R3 and R7 were not re-run.

### 1.1 toda_layers (fresh engines; SHI)
I re-ran all seven configurations from empty caches (698 s in total; L3 alone took 437 s at SHI = 16). Result:
**ALL 75 IDENTITIES HOLD; ALL 91 CONTROLS FAIL**, including X1 (b-part string-identical to w2_engine), X2 (α-layers vs
m4_rh4) and X3. The only diff from the stored toda_layers.out is the seven added "engine N s" lines, which a fresh run
prints. All eight engine JSONs (L1, L2, L3, Q1, Q1_w2, Q2, Q3, Q4) are **byte-identical** to tmp/toda/.

The SHI = 16 setting for L1–L3 is safe for two reasons. (a) The engine asserts that every principal part is determined
(`toda_engine.py` l. 314: `assert e.hi >= -1, "truncation too shallow"`), so a too-shallow depth stops the run; it cannot
give a wrong answer. (b) X3 compares the symbolic L1 (SHI = 16) at (3/2, 3/10) with Q1 (SHI = 30), and the two agree. The
diff of toda_engine.py against w2_engine.py contains only the marked "toda change" blocks: R₂ and the α-extraction.

I checked the R₂ formula against Lemma T.B.1. At e = 4c: Res_{4c}(zF) = 4c·Res F + [w^{−2}]F, w = z − 4c. At 0:
Res_0(zF) = [z^{−2}]F. The extraction is 𝖺 = (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂, with n^pα_n/(2c) = 𝖺/2 at c = 1. Both are right.

### 1.2 Registration timestamps (JZC_SHIFT §4.1, Rule X)
- shift_predictions.json: internal timestamp 2026-10-23T08:32:31−06:00, file mtime 08:32:33.87. The earliest engine
  output, eng_R3, has mtime 08:35:57.50. shift_common.py has mtime 08:31:46, and its sha256 1a4c1c70… is printed in every
  output. These are consistent.
- shift_predictions2.json: timestamp 09:02:55, mtime 09:02:55.29. eng_R7 has mtime 09:12:43, consistent with a 584 s run
  started after 09:02:59. hjk_closed.json (09:02:45) precedes the registration, as it must: the prediction is computed from it.
- shift_exact.py was modified at 08:58:48, after R1–R6 had run. This is disclosed (Rule A 12). The fresh re-runs above
  use the final script and give the same verdicts.
- **Caveat (process, not mathematics).** Both registration files entered git only in af22e48, at 09:13:39, which is after
  every engine output. So the precedence rests on filesystem mtimes and the in-file timestamp alone, with no external
  anchor. The engine is deterministic: four fresh runs are byte-identical. That makes the risk small, but the note should say
  it (fix S5).
- **Inconsistency in Rule A 1.** eng_R1 and eng_R3 have mtimes 08:35:57.60 and 08:35:57.50. The quoted engine times are
  162 s and 160 s, so both runs started at ≈ 08:33:15–17. That is the "first launch (08:33)", which Rule A 1 says was
  "killed by pid after ~1 min, before either engine finished". The likely explanation is that the kill reached the detached
  shell but not its engine subprocesses, which then finished and wrote the caches. The restarted tracked jobs would then have
  found the cache. Both runs are still after the registration, and R1 is byte-identical when re-run fresh, so nothing
  changes. The log sentence is inaccurate (fix S5).

## 2. JZC_TODA

### 2.1 Lemma T.1 (Toda hierarchy for exponential tilts) — **ACCEPT**
I re-derived 1–4 from the write-up.
- 1: (L^j)_{nm}h_m = ∫x^jπ_nπ_m dμ_t, read directly from xπ = Lπ with L_{n,n+1} = 1, L_{n,n−1} = b_n². The detour via
  J = D^{−1}LD is correct as well.
- 2, 3: correct as written.
- 4: a_n = c_n − c_{n+1} from the x^n coefficient; ∂c_n = −(L^j)_{n,n−1} = −F_j(n−1).
- The finite-M boundary: π_M = Π(x − x_k) is t-free, so F_j(M−1) := 0. This is right.
- Regularity: the moments are entire in t because the support is compact, and the Cramer-rule ratios have D_n > 0.
- Nothing depends on the sign of t. The tilt only has to be positive and continuous on a compact support.

*Independent check* (`rv_toda_T1.py/.out`). Exact rationals with dual numbers, a Stieltjes procedure (the author used a
different route, moments to L-form), random 7-atom measures with atoms of **both signs**, and tilts x⁴, x⁵, x⁶ (the author
used j ≤ 3), every n including n = M − 1. **252/252 identities hold**, and 0/126 controls hold (controls: transposed F_j,
(L^{j+1})_{nn}).

### 2.2 Lemma T.A (the transfer) — **ACCEPT WITH FIXES** (T2, T3)
I checked the hypotheses of Paper 2 one by one against the sources.
- **(A_ϑ)** (sec_front.tex Def. A, quoted exactly in the note). Λ_τ(ξ) = Σ_jτ_je^{−jpξ} is entire and real on ℝ. On
  S_ϑ ∩ {Re ξ ≤ 0} ⊂ {Re ξ ≥ −c₀}, |Λ_τ| ≤ Σ|τ_j|e^{jpc₀}. Also ε_{Λ_τ}(T) ≤ pΣj|τ_j|e^{−jpT} → 0. This holds for every
  ϑ, every c₀ and **every sign and size of τ**. Remark angles: θ_w ≤ pϑ is arranged through 𝗆, so any ϑ works.
- **Standing assumptions** (sec_5.tex): p > 0, 1 < s < 1 + 2p, ℓ₁ with (A_ϑ). The tilt changes neither p nor s, and α is
  unchanged.
- **Band weight.** By (eq:w-rn), r_n(z) = ℓ₁(t(z))/ℓ₁(n) with t = nz^{−1/p}. So r_n = exp(Σ_jτ_jn^{−jp}(z^j − 1)) exactly, and
  r_n(1) = 1 matches the band-factor normalisation "log H_n(z) − log H_n(1)". By (eq:W0), W₀ = 𝗐_nz^α(4c − z)H_nr_n. By
  (O1)–(O5) and app_outer.tex (which never mentions ℓ₁ or r_n), H_n is weight-free. sec_5 says of g: "Nothing here depends on
  ℓ₁". So **H_n ↦ H_nr_n** is exactly right.
- **Sign of the shift.** r_n = const·q_{μ′}, q_μ = e^{−Σμ_kz^k}, μ′_j = −τ_jn^{−jp}. So μ^τ = μ_n − τn^{−p·}, and u = t + τ,
  ∂_u = ∂_τ = ∂_{t_j} of Lemma T.1 (tilt e^{+t_jx^j}). The signs are consistent.
- **E3.4 (i)** is stated "for real μ", and μ′ is real. The multiplicativity q_{μ₁}q_{μ₂} = q_{μ₁+μ₂} gives the combined
  gauge G_{μ_n+μ′_n}.
- **Hard edge, p > 1 and p < 1 (RH_plt1b, read in full).**
  - The seam scalar X and F = D·B_in·K·e^X / B_out·K·e^X are built from t, D, B, K only. They are weight-free, as the author
    says.
  - The glued W̃ = (C(−z)^α(4c − z))^{1/2}/G̃ becomes W̃·r_n^{1/2}. r_n^{1/2} is entire and the same on both sides of each
    seam ray, so W̃_out/W̃_in = 1 − e^{∓2πit} is unchanged and the super-small seam jump is untouched.
  - Lemma weightdomain: Ω_∞ never uses the weight, so the S_out region raises no issue.
- **Off-circle and a-priori bounds.** On |z| ≤ e^{pc₀}n^p, |log r_n| ≤ Σ|τ_j|(e^{jpc₀} + 1). This bound is τ-dependent and
  n-uniform, and (O3) and (O4) for H_nr_n follow at once: on |z| ≤ 1 the tilt adds O(|z|) ≤ O(|z|^{ν_p}). The super-small
  bounds e^{−n/C} absorb any fixed constant for n ≥ n₀(τ).
- **The specific worry: a large negative τ makes masses tiny or reorders dominance.** This does not affect the argument.
  Theorem T (i) is an n → ∞ statement at **fixed** τ. Every constant, and the threshold n₀, may depend on τ, and Lemma T.2
  needs exactly that (pointwise in u, then Baire). Positivity is preserved. No step uses monotonicity of the masses or a
  comparison between atoms: Paper 2 explicitly requires neither boundedness nor monotonicity of ℓ. The only weight-sensitive
  object near the support's top end is the saturated region, where e^{P_τ(x)} is a fixed bounded factor. The equilibrium
  measure and g do not involve the weight (sec_5: "the external field of the weight is (1/n)log w = O(log n/n) … not put into
  g"). With a tilt, (1/n)·|P_τ(z/n^p)| ≤ C(τ)/n. So the sign conditions of Lemma signs are those of the lattice. **No
  uniformity in τ is claimed or needed.** §3.3 tests this directly at τ = −10.
- **What I did not verify.** I did not check line by line that every REVIEWED lemma of E_pgt1, E_plt1, RH_px and G1u uses
  the weight only through W₀, its Szegő data and the stated bounds. The author's rows match the statements I read (E3.4, E3.5,
  E3.6 proof, RH_plt1b, Paper 2 frame). This is the same granularity as the precedent the note cites (JZC_SIGMA Lemma F (ii)).
- **Hurwitz half (σ^δ_τ).** The note states it in one paragraph: "the Hurwitz chain's own frame … with W₀ multiplied by r_n:
  the same bounded-factor argument". The argument is sound. The tilt multiplies the node mass at x by e^{P_τ(x)}, so for
  **any** node parametrisation the interpolating weight is multiplied by the entire function e^{P_τ(z/n^p)} = e^{Στ_jn^{−jp}}r_n(z).
  L Ha.2's residue weight, Lemma bandweight's W (JZC_M3a_H_Ha l. 58: "W = 𝗐_nz^α exactly") and W₀^{(β′)} = 𝗐_nz^{β′}(4c − z)H_n^δ
  (G12 l. 128) all just acquire the factor r_n. But the Hurwitz frame consists of the lemmas of Ha, G12, G3, G23plt1, Hc and
  G1u, not Paper 2's Proposition frame, so it needs its own row list. Fix T2 gives one.

*Spot check: the "missing" direct test of a tilted lattice* (§3.3) is done and passes.

### 2.3 Lemma T.B (α_n layers) — **ACCEPT**
- R_k = −(1/2πi)∫R₋(J − I)s^{k−1}ds is the 1/z^k coefficient. On clockwise circles this gives Res(sF_m). The decomposition
  Res_e(sF) = e·Res_eF + [(s − e)^{−2}]F is right.
- The far and super-small pieces carry |s| ≤ Cn^p, which is absorbed. For p < 1 this includes the seam and lip pieces of
  E3.6's proof.
- (F8): 𝖺(Q) = n^pa_n. Q₁ = P₁ + R₁, Q₂ = P₂ + R₁P₁ + R₂ (outside the discs Q = RP₀^∞). (Q₁)₁₂ = ic + O(1/n) ≠ 0, so 𝖺 is
  analytic in (R₁, R₂).
- The n⁰ term is 1, and it is μ-independent, so 𝔄_β = O(1/n) for β ≠ 0.
- Re-run: the engine reproduces 𝔄₀'s n^{−1} coefficient −p(β + 2)/2 (E_pgt1 Thm E.1).
- My LB check (§4.4) also found that the α-layers' leading coefficients are LB(β), as the hard-edge reduction α⁰ = 2b⁰
  requires. This is a non-trivial consistency check on the R₂ extraction.

### 2.4 Lemma T.2 (Baire → formal identity) — **ACCEPT WITH FIXES** (T1)
I checked the logic step by step.
- **Step 0.** J′ = J. The band parameters t_j, j > J, go into the remainder n^{−1−(J+1)p}, so J must grow with L. That is
  harmless: the identity for a smaller exponent set is the restriction u_{J₀+1} = … = 0, and the layers do not depend on J
  (§1.1).
- **Step 1.**
  - Φ_n is continuous (b_m, α_m are real-analytic in u; β̃, α̃ are polynomials).
  - sup_nΦ_n(u) < ∞ pointwise: finitely many n < n₀(u), each finite.
  - F_M is closed and ⋃F_M = ℝ^J.
  - The nested-ball proof of Baire is correct.
  - Φ_n uses indices n + i, i ∈ I = {−J − 1, …, J + 1}. Those cover every entry of (J^j)_{n−1,n−1} and F_j(n), j ≤ J.
- **Step 2.**
  - (4.2) is Lemma T.1.3 integrated, which is legitimate because b_n(σ^{[u]}) is C¹ in u.
  - On U the entries are O(n^{−p}) uniformly (U is bounded).
  - Ψ_j is homogeneous of degree j + 1, so the replacement error is O(n^{−(j+1)p−L}) and (4.3) holds.
- **Step 3.**
  - The coefficient-extraction via a fixed tensor grid in U′ × [−h₀, h₀] is correct.
  - The weight bookkeeping is right. A u^γh^m term of the left side comes from δ = γ + me_j, with weight n^{−p(1+|γ|_w+mj)}.
    In the integral, δ = γ + (m − 1)e_j, and the product of j + 1 entries adds n^{−pj}, which gives the same weight. So all
    contributions to a fixed (γ, m) carry the same power n^{−p(1+|γ|_w+mj)} times an analytic function of 1/n. Separation is
    by u-monomial, not by powers of n, so no irrationality of p is needed. This is correct, and it is where the free tilt times
    are used.
  - The truncations B (u-degree) and K (1/n) affect only coefficients with |γ| + m > B, or order > K. Polynomial products
    and S_i preserve the u-degree.
- **Error (T1).** Coefficient = n^{−p(1+|γ|_w+mj)}ψ_{γ,m}(1/n) = O(n^{−p−L}) gives ψ_{γ,m}(1/n) = O(n^{−L+p(|γ|_w+mj)}). So
  the correct exponent is **L′ := L − p(|γ|_w + mj)**, not L + p(|γ|_w + mj). The conclusion is unaffected: to get the
  n^{−k} Taylor coefficient of ψ_{γ,m}, take L > k + p(|γ|_w + mj) (and J, K, B accordingly). L is arbitrary. See the fix
  text.
- **Step 4.** The h-linear coefficient is right. Entries: b_{n+i} = cn^{−p}𝒷_i, α_{n+i} = cn^{−p}𝒶_i, (J^j) = (c/n^p)^j(𝒥^j).
  I re-derived (T-a) from T.1.4: F_j(n) = (cn^{−p})^{j+1}𝒷₁(𝒥^j)₁₀ and α_n = cn^{−p}·2â.
- The f_n = n^{−L}sin(n^{L+1}τ) remark is apt. The proof never differentiates an asymptotic expansion.

### 2.5 Theorem T (ii)–(iv), (1.1) — **ACCEPT**
- (1.1) is the chain rule for μ_j = −u_jn^{−jp} in ℛ_J ≅ ℂ[[x, s]], which I checked on monomials.
- (T1) as a sanity check. 𝒶₀ − 𝒶₋₁ = 2[1 − (1 + p/n)] + O(n^{−2}) = −2p/n + …, so 𝔇_{e₁} = −½c(𝒶₀ − 𝒶₋₁)B = cp/n + …. In
  engine units e = 2cμ this is p/2, which is E3.7's value.
- (iv): the recursion (u^{γ+e_j} coefficient = (γ_j + 1)·layer; S_i preserves the u-degree) is right.

### 2.6 Theorem T_H — **ACCEPT WITH FIXES** (T2)
Same proof with Theorem H (i). Theorem H's range is −1 < δ ≤ 0, with δ < 0 for p < 1 (JZC_M3a_H §1); T_H states this. The
total time is u = τ + t^{δ,(J)}. Lemma T.1 applies to σ^δ_τ: the support lies in [0, (1 + δ)^{−p}], and the tilt is a fixed
positive factor, even when 1 + δ is small.

### 2.7 Cor T.3 (rationality) — **ACCEPT** (minor T4)
- The set {(p, α + 2δ, α): p ∈ (0, ∞) ∖ {1}, |α| < 1, δ ∈ (−1, 0)} is open in (p, β′, ν)-space: (β′ − ν)/2 ∈ (−1, 0),
  ν ∈ (−1, 1). A rational function vanishing there is 0.
- The rationality of the layer coefficients in (p, β′, ν) uses the engine normalisation c = 1, i.e. homogeneity of the model
  under z ↦ z/c with μ_j c^j (engine units e_a = C(2j_a, j_a)c^{j_a}μ_a). (T-b) and (T-a) carry exactly c^j with u_j. Say this
  in §5.2, since c(p) itself is not rational in p (T4).

### 2.8 Prop T.4 — **ACCEPT**
- Re-run: see §1.1.
- My own arithmetic at the Bessel point (2, −½): a₂ = −1/8 + 3/8 = 1/4, and
  a₄ = 15·(180 + 360 − 156)/(5760·2·8) = 1/16.
- §7.2's form (p + 1)(3(p + 2)ν² − 1)/24 equals −(p + 1)/24 + (p + 1)(p + 2)ν²/8.

### 2.9 Labels, status lines — fix T5
- The status lines say "nothing committed", but the note is in commit 7c18fcd (and JZC_SHIFT in af22e48).
- §5.1 says Thm SH on β′ ≠ ν "becomes PROVED-mod-cite": correct, once JZC_SHIFT is updated (S1).

## 3. Independent spot checks (Rule R)

### 3.1 Lemma T.1, other degrees — `rv_toda_T1.out`: 252/252, controls 0/126 (§2.1).

### 3.2 LB against exact engine layers not used by JZC_SHIFT — `rv_lb.out`
JZC_SHIFT's LB evidence is the JZC_W2 caches (B, T, M, Q, H) and its own R1–R7. JZC_TODA's toda_engine outputs (L1–L3, Q1–Q4)
were never compared with LB. I compared every monomial of all seven configurations, for **both** the b-layers and the
α-layers (A = n^pα_n/(2c)), against LB(β) = Π(pj_a/2)^{β_a}(p + 1 + S)_{|β|−1}/(β!p^{|β|−1}) at n^{−|β|}, with zeros below.
The configurations cover:
- symbolic (p, α) with exponent pairs (1), (2, 3), (1, 2);
- symbolic (p, α, β) decoupled (β ≠ ν);
- p = 3/2, 7/3, and **p < 1**: Q2 (p = 3/5, decoupled β = 1/3 ≠ ν = −2/7) and Q4 (p = 2/5, e₁³).

Result: **96/96 hold. The control p + 2 + S holds in 0/24 cases.** The α-layers obeying LB is the prediction α⁰ = 2b⁰ of
Lemma R, at p < 1 and at β ≠ ν. The note does not state it explicitly.

### 3.3 Direct test of the tilted lattice (the test JZC_TODA §8 item 2 lists as missing) — `rv_tilted.out`, `rv_tilted_finite.out`
**Method.** The moments of the *infinite* tilted lattice are explicit: ∫x^k e^{τx^j}dσ^δ = Σ_rτ^r/r!·ζ(s + p(k + jr), 1 + δ).
With Arb (rigorous ζ) I ran Gautschi's Chebyshev algorithm over truncated power series in τ (orders 0, 1, 2), at 2048 bits.
This gives b_n and ∂_τb_n, ∂²_τb_n at τ = 0 as balls with > 120 correct bits for n ≤ 40. No truncation of the lattice and
no use of Lemma T.1 is involved. I compared them with Theorem T (i): n^pb_n(σ_τ)/c = Σ_βe^β𝔅_β(n) evaluated at
μ^τ_n = μ_n − τn^{−jp}, with the exact engine layers from tmp/toda. The prediction carries the zeta band parameters μ_n, so
the n-dependence of μ is tested ("relerr1" = (∂_τF − pred)/leading).

| case | layers | relerr1, n = 6 → 40 | decay | second order (rel. error) |
|---|---|---|---|---|
| A: p = 2, s = 3, tilt x | L1 | 5.0·10⁻³ → 3.0·10⁻⁶ | n^{−4} (KORD 4) | 0.16 → 5.4·10⁻⁴, n^{−3} as expected |
| B: p = 2, s = 3, tilt x² | L2 (2, 3) | 2.9·10⁻² → 1.9·10⁻⁵ | n^{−3.9} | — |
| C: p = 3/2, s = 59/20 (α = 3/10), tilt x, μ_n ≠ 0 (ζ(−3/2), ζ(−3)) | Q1 (1, 2) | 7.1·10⁻³ → 4.2·10⁻⁶ | n^{−4} | 0.17 → 5.9·10⁻⁴, n^{−3} |
| D: **Hurwitz** δ = −1/2, p = 2, s = 3, tilt x (M(β′ = −1, ν = 0); μ^δ from ζ(−2, ½), ζ(−4, ½)) | L3 (decoupled) | −8.2·10⁻⁵ → −5.6·10⁻⁸ (n ≤ 36) | n^{−4} | — |
| E: p = 7/3, α = −1/2, tilt x³ | Q3 (3, 2) | 6.0·10⁻² → 1.2·10⁻⁴ (n ≤ 30) | n^{−3.9} (μ₁ absent from Q3) | — |

**Finite, large tilts of both signs** (`rv_tilted_finite.py`). The setting is p = 2, s = 3, where the lattice band factor
vanishes, so Lemma T.A predicts the model at μ = −τn^{−2} alone. The moments at finite τ were computed with a rigorous tail
bound. For τ = −10, −3, +3, +10 and n ≤ 40, (n^pb_n/c − prediction)·n⁵ converges to the same τ-independent constant
(≈ −0.87, −0.91, −0.94, −0.99 at n = 40, approaching the untilted truncation coefficient). Meanwhile the tilt effect itself is
1.8·10⁻⁴ at n = 40 and 4·10⁻² at n = 6 (τ = −10). So the tilted expansion holds with the **same** layers, with only a
τ-dependent pre-asymptotic constant, as Lemma T.A states. A large negative τ, which suppresses the top atoms by e^{−10},
changes nothing.

Label of these spot checks: NUMERICAL. The b_n data are certified balls, but the comparison with a truncated asymptotic
series is not.

## 4. JZC_SHIFT

### 4.1 Lemma LB — **ACCEPT**
I re-derived the Lagrange inversion: [λ^m]H(y) = (1/m)[y^{m−1}]H′ψ^m, with H = (1 + y)^{−p} and
ψ^m = (−1/p)^mΣ(m!/β!)σ^β(1 + y)^{−S}. The binomial coefficient is binom(−p − 1 − S, m − 1) = (−1)^{m−1}(p + 1 + S)_{m−1}/(m − 1)!.
The signs collect to (−1)^{2m} = +1, which gives Σσ^β(p + 1 + S)_{m−1}/(β!p^{m−1}). The residue-invariance argument is correct.

### 4.2 Lemma D — **ACCEPT WITH FIXES** (S2, wording)
- Defect bookkeeping. Take a product of j + 1 factors with t-orders β_k and n-orders i_k. Its weight is
  n^{−p(j+1+Σ|β_k|_w)−Σi_k}. After (1 − S₋₁) and ∂_{t_j}, the new coefficient (t^{β+e_j}, β = Σβ_k) has i = Σi_k + 1. Its defect is
  Σi_k + 1 − |β| − 1 = Σ(i_k − |β_k|) ≥ 0. So (i) holds by induction.
- The defect-0 parts close: S_k is the identity on them, and (1 − S₋₁) acts as ∂_n. That gives (ii). Uniqueness holds.
- The sentence "(= 1/(β_j + 1) × the t^β coefficient of the right side, kp index j + 1 → 1)" is garbled (S2).
- The hypothesis α_n(0) = 2cn^{−p}(1 + O(1/n)), i.e. A₀ = 1, is now Lemma T.B.3 directly. §2.1 (c) still derives it from E3.7
  via (T1); either is fine.

### 4.3 Lemma R — **ACCEPT**
- H_j(2b, b) = C(2j, j)b^j and G_j(2b, b) = C(2j, j + 1)b^{j+1}: these are the coefficients of x^j and x^{j+1} in (1 + x)^{2j}.
  I re-derived the path counts (stay a, up/down b).
- Hence ∂_t(α − 2b) = 0 on α = 2b, and V_j = (j/2)C(2j, j)b^j.

### 4.4 Lemma H, Theorem SH — **ACCEPT** (labels: fix S1, S3)
- Implicit differentiation of x = n + Σt_kV_k(cx^{−p}): ∂_{t_j}x·(1 − Σt_kV_k′·∂_xb) = V_j and ∂_nx·(same) = 1. So
  ∂_{t_j}x = V_j∂_nx, and b̃ = cx^{−p} solves the Hopf equations.
- Normalisation: −(1/p)ε̂_j = (j/2)C(2j, j)c^jt_j with μ̂ = −t. This is consistent with Theorem T's u: μ_j = −u_jn^{−jp}.
- First order: (n/x)^p ≈ 1 + ε/n, ε = (pj/2)e, which is E3.7.
- §3.2 confirms all of this independently on 96 monomials.

### 4.5 Cor SH.1–SH.3 — **ACCEPT WITH FIXES** (S1, S3, S4)
- SH.1: with Theorem T now proved for all p ≠ 1, "on p > 1" can read "on p ≠ 1" (S4).
- SH.2: the rationality argument is sound. A rational function of the exponents vanishing on ℕ^r_{≥1} is 0. The
  denominators (2j − odd) never vanish at integers. The engine's j-structure is a statement about code, and it is supported
  directly by the symbolic-j runs R1, R2 and JZC_W2's H, which obey LB identically in j.
- SH.2, pole layers: identifying the continued layers at j = q_m with the pole layers rests on JZC_W2 Prop 2.1 (iii), which is
  NOT REVIEWED. The label should say so (S3).
- SH.3: (T_H) is supplied by JZC_TODA Theorem T_H + Cor T.3. Lemma D's initial data for M(β′, ν) hold: d₀ = 1, and 𝔄₀'s n⁰
  coefficient is 1 (Lemma T.B.3, for every model).

### 4.6 Prop DR, Obs DR′, §5.3 — **ACCEPT**
- Re-run reproduces all of it (shift_dressing 18/18 with R1 present).
- The labels are honest: the g_j split for j > 10 and the h(j, k) closed form are CONJECTURE, and R7 is a genuine registered
  out-of-sample test.
- The claim "a₂ derived from (T1)" is now also confirmed by direct extraction (JZC_TODA Prop T.4, re-run).

### 4.7 Rule X / registration — **ACCEPT** with the process caveats of §1.2 (S5).

## 5. Fix texts

**T1 (JZC_TODA §4.1 Step 3, error; conclusion unaffected).** Replace "With L′ := L + p(|γ|_w + mj), the Taylor coefficients of
ψ_{γ,m} of order < L′ vanish." by:
> "Since the u^γh^m-coefficient of Π_n is O(n^{−p−L}), ψ_{γ,m}(1/n) = O(n^{−L′}) with L′ := L − p(|γ|_w + mj); hence the Taylor
> coefficients of ψ_{γ,m} of order < L′ vanish. Given (γ, m) and an order k, choose L > k + p(|γ|_w + mj) (and then J, K, B as in
> Step 0); so every Taylor coefficient of every ψ_{γ,m} vanishes."

**T2 (JZC_TODA §3.1, Hurwitz rows).** Replace the paragraph "Paper 2's frame for general ℓ₁ does not cover Hurwitz nodes. …" by:
> "For σ^δ_τ the tilt multiplies the mass at the node x by e^{P_τ(x)}; for any node parametrisation, the interpolating weight
> is therefore multiplied by the entire function e^{P_τ(z/n^p)} = e^{Σ_jτ_jn^{−jp}}r_n(z), r_n as above. Row by row: (H-a)
> JZC_M3a_H_Ha L Ha.2 and P Ha.5: residues n^pτ_k^{−s}e^{P_τ(τ_k^{−p})}U_{j1}(X_k); W ↦ W·e^{P_τ(z/n^p)} (l. 58 there); the
> interpolation and uniqueness arguments do not use the form of w. (H-b) the outer scalars (G12 §1, G3 §2) are built from t, δ
> alone: unchanged. (H-b′) the a-priori bounds (G12 L2.1–P2.4; G23plt1 L2.1′–P2.6) use W₀^{(β′)} through D_W and bounds of
> Paper 2 Lemma szego (vi) type; D_{r_n} is explicit by E3 Lemma E3.4 (i) (real μ′_n), bounded above and below on the
> relevant sets uniformly in n, so the constants change by a factor depending on τ only. (H-c) Hc.2, Hc.3 (p > 1), Hc.5
> (p < 1): log H_n^δr_n − log(H_n^δr_n)(1) = −Σ_k(μ^δ_{n,k} + μ′_{n,k})(z^k − 1) + O(n^{−(K+1)p}), K ≥ J, same remainder. (H-d)
> the index transfer is a weight-free gauge. (H-e) N.6a–c for M(β′, α) at μ^δ_n + μ′_n (E3.4 (iii), the same G_μ). (G1u,
> G1u_plt1 L P3) W̃ ↦ W̃·r_n^{1/2}, entire: same jumps, bounds changed by sup_{U(0,δ)}|r_n^{±1/2}|."

**T3 (JZC_TODA §3.1, scope sentence).** After "an entire, zero-free polynomial tilt, real and positive on (0, ∞).", add:
> "All constants and the threshold n₀ in Lemma T.A depend on τ; no uniformity in τ is claimed or used (Lemma T.2 needs only
> pointwise expansions). No step uses monotonicity of the masses or comparisons between atoms, so the sign and size of τ are
> immaterial (Paper 2 Definition A requires neither boundedness nor monotonicity; the external field (1/n)log of the tilt is
> ≤ C(τ)/n on Z_n and is not put into g)."

**T4 (JZC_TODA §5.2, normalisation).** Add after the first bullet:
> "c = c(p) is not rational in p; the layers are computed at c = 1, and the model is homogeneous under z ↦ z/c with
> μ_j ↦ μ_jc^j, which is how c^j enters (T-b), (T-a). So the identities R = 0 are rational in (p, β′, ν) in these units."

**T5 (JZC_TODA, JZC_SHIFT status lines).** Replace "nothing committed" by the commit (7c18fcd; af22e48). Set the labels after
the fixes: Lemma T.A, T.B, T.2, Theorem T, T_H, Cor T.3: "+ REVIEWED (review A, REVIEW_JZC_TODA_SHIFT_A.md)". Record that §8
item 2 (direct tilted-lattice test) was done in this review (NUMERICAL), and §8 item 1 (Rule R) is done.

**S1 (JZC_SHIFT header, §2.1 (b), Cor SH.3, Rule A 9, §7 item 2).** Replace the input "JZC_M4 §8 Theorem T (… proof sketch,
NOT REVIEWED)" by "JZC_TODA Theorem T and T_H (PROVED-mod-cite + REVIEWED)". Cor SH.3: "(T_H) is JZC_TODA Theorem T_H with
Cor T.3; hence Thm SH holds for all (β, ν): PROVED-mod-cite." Remove "a transfer not written (CONDITIONAL)" in §0.

**S2 (JZC_SHIFT §2.2 proof).** Replace "(= 1/(β_j + 1) × the t^β coefficient of the right side, kp index j + 1 → 1)" by:
> "(= 1/(β_j + 1) times the t^β coefficient of the right side; the extra factor n^{−pj} of the right side is the weight of
> t_j, so the n-order index i of the new coefficient is Σi_k + 1)"

**S3 (JZC_SHIFT table row Thm SH, Cor SH.2).** Append: "the identification with JZC_W2's pole layers uses JZC_W2 Prop 2.1 (iii)
(NOT REVIEWED); the continued identities themselves hold for the engine's model at every exponent."

**S4 (JZC_SHIFT Cor SH.1).** "the identities hold on p > 1, |α| < 1" → "on p ≠ 1, |α| < 1 (JZC_TODA Theorem T)".

**S5 (JZC_SHIFT Rule A 1, §4.1).** Add:
> "The registration files were first committed in af22e48 (09:13:39), after the runs; precedence rests on the filesystem mtimes
> and the in-file timestamps. eng_R1 and eng_R3 (mtimes 08:35:57) come from the 08:33 launch: the kill stopped the detached shell
> but not the engine subprocesses. Rule R review A re-ran R1, R4, R5, R6 from empty caches: byte-identical engine outputs."

## 6. Rule A of the reviewer (attempts to break the statements)
1. *Can a tilt change the hard-edge exponent or the equilibrium?* No. e^{P_τ(x)} → 1 at x = 0, and it is O(1) on the support.
   Tested at τ = ±10 (§3.3).
2. *Does Lemma T.1 need positivity of the support?* No. My check used atoms of both signs.
3. *Is the Baire ball enough when it does not contain u = t?* Yes. Step 3 yields polynomial identities in u, i.e. formal
   identities, which hold at every u. Checked: Step 3 never evaluates at a specific u.
4. *Scaled vs unscaled time.* My second-order τ-derivatives (§3.3 A, C) are predicted with μ^τ = μ_n − τn^{−p} at each n
   separately. Combined with Lemma T.1 they confirm the unscaled-time form of (T2) on the actual lattice. The author's
   scaled-time control fails at second order in the re-run toda_layers as well.
5. *LB at p < 1 and β ≠ ν without (T_H)?* Holds on Q2 and Q4 (§3.2). This is exact data, not proof.
6. *Does T.B's α-extraction have a hidden μ-dependence at n⁰?* No. Every computed α-layer with β ≠ 0 starts at n^{−|β|} ≥ n^{−1}.
