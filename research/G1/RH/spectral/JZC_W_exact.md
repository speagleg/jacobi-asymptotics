# JZC W exact: computer-algebra tests of branched E3.7 and of Refinement W′

Note (2026-10-22, after Rule R review A of the W chain, research/G1/review/REVIEW_JZC_W_kappa_chain_A.md): Lemma WE.1 is now an input of
JZC_W_kappa Prop K.12′ (and thereby of the κ-family's first-order W). Review A did not review this note; it spot-checked WE.1(ii) at the
κ-family's exponents by an independent quadrature (ρ ∈ {⅓, 4/3, 0.7}, deviation ≤ 6·10⁻¹⁸ = quadrature floor) and requested no fix here.
Note (2026-10-22, after Rule R review B, research/G1/review/REVIEW_JZC_W_WE1_K12p_B.md): **Lemma WE.1 is REVIEWED** (independent second
reader B re-derived (i)–(iii) from the write-up, re-ran w_exact_gauge and w_exact_laguerre (identical outputs), checked WE.1 by an
independent Cauchy-integral construction at ρ ∈ {0.15, 0.45, −0.35, 1.6, 5/3, 2.3}; verdict ACCEPT WITH FIXES W1–W3, all applied here and in
checks/w_exact_gauge.py). With it, every input of the κ-family's first-order W (JZC_W_kappa P K.12 + Prop K.12′) is REVIEWED.
Status (2026-10-22): **Lemma WE.1: PROVED + REVIEWED** (Rule R reviewer B, research/G1/review/REVIEW_JZC_W_WE1_K12p_B.md). **WE.2–WE.6, P0–P3, W′
and the rest of this note: NOT REVIEWED** (review B did not review them; they keep their labels). Labels per VERIFICATION_POLICY.md. Novelty: UNCHECKED. No claim about RH:
no measure built from zeta zeros is used. Scope: the two parts of Conjecture W (JZC_W.md) named in JZC_W §5.1 item 4 and §1.3 (W′),
tested with the exact engine of JZC_M4_proof (m4_rh_exact2.py), not with measures.

Checks (all in `checks/`; every `.out` prints the sha256 of its script and of the modules it imports):
- `w_exact_engine.py`: a copy of m4_rh_exact2.py (sha256 2d18e259…cbc06, **not modified**) with two environment switches: PVAL fixes p
  to a rational number, SZOFF sets the Szegő exponent β = α + SZOFF. With neither set it is m4_rh_exact2.
- `w_exact_lag.py`: exact large-n expansions for the Laguerre weight with a branched tilt (helpers).
- `w_exact_gauge.py` → `w_exact_gauge.out` (§1); `w_exact_laguerre.py` → `w_exact_laguerre.out` (§2);
  `w_exact_predict.py` → `w_exact_predict.out`, `w_exact_predictions.json` (§3, pre-registration);
  `w_exact_poles_prereg.py` → `w_exact_poles_prereg_A.out`, `_B.out` (§3, the pre-registered test as run; these two end in
  "IDENTITY FAILURE" **by design of the record**: the registered P2 failed, §3.2);
  `w_exact_poles.py` → `w_exact_poles_A.out`, `_B.out` (§3, final form, with post hoc p; 57 + 57 checks); `w_exact_xfit.py` →
  `w_exact_xfit.out` (§3.4, post hoc); `w_exact_wprime.py` → `w_exact_wprime.out` (§4). All final outputs end with
  "ALL IDENTITIES HOLD" / "ALL N CHECKS PASSED"; each contains controls that must fail. Run times: gauge 1.5 min, Laguerre 6–8 min,
  poles 25–30 min per output (two in parallel), the others < 1 min. Python: the session venv (sympy, mpmath), `-B`.

| # | Statement | Label |
|---|---|---|
| Lemma WE.1 | the E3 gauge of a branched tilt exp(−μz^ρ) splits (c = 1) as M_ρ = A_ρ + tan(πρ)z^{ρ−½}(4−z)^{−½}; the Taylor data of A_ρ at 0 and of M_ρ at 4c are **exactly** the engine's symbolic-j data at j = ρ; (i) for all ρ > −½, (ii), (iii) for all ρ > −½, ρ ∉ ½ + ℤ | PROVED (elementary: Stieltjes form, Beta integrals (DLMF 5.12.3), reflection formula (DLMF 5.5.3), removable singularity, continuation in ρ; Legendre duplication NOT QUOTED, needed only to write the prefactor as C(2ρ,ρ), W2; exact sympy identities for m ≤ 8; decomposition checked numerically to 2·10⁻⁴⁰) + REVIEWED (Rule R reviewer B, research/G1/review/REVIEW_JZC_W_WE1_K12p_B.md; fixes W1–W3 applied) |
| Prop WE.2 | branched E3.7 at the n⁻¹ level: the n⁻¹ coefficient of the response of n^pb_n/c to exp(−μz^ρ) is d₁ + c p M_ρ(4c)μ, exactly linear in μ (zero second- and third-order response), which is W's −(pρW(ρ)/2)t_ρ | PROVED for the analytic (A_ρ) part of the gauge; that the branched remainder does not reach n⁻¹ (it starts at relative n^{−2ρ−1}) is HEURISTIC for general p and exact at p = −1 (§2) |
| Prop WE.3 | at p = −1 the decoupled model M(ν−1, ν) is the Laguerre weight; its symbolic-j zeta-layer response, continued to j = ρ, equals the analytic part of the exact Laguerre response to x^ρ through N⁻⁶, identically in (ν, ρ) | PROVED (exact identity of the engine output with the Laguerre analytic series; the Laguerre two-series form rests on a connection formula and singularity analysis NOT QUOTED, and is checked numerically to 2·10⁻²¹) |
| Finding WE.4 | the first-order response to a branched tilt is **not** the continued series alone: it has a hard-edge companion H(ρ)N^{−2ρ−2}(1 + O(N⁻²)), H = ½(pρ+2ρ+1)(p+2)^{2ρ+1}Φ_ν(ρ)/C(2ρ,ρ), Φ_ν(ρ) = Γ(−1−2ρ)Γ(ν+ρ+1)/(Γ(−ρ)²Γ(ν−ρ)) | exact at p = −1 (Laguerre); general p: CONJECTURE, supported by exact pole-cancellation identities (P0: all p; P1: pre-registered, exact in ν at 5 values of p, plus post hoc p) |
| Refuted P2 | the subleading branched dressing at general p is g(ρ*) with ρ* = ρ + (2ρ+1)/p (the p = −1 "reflection") | REFUTED (pre-registered; fails at all 5 registered p) |
| Obs WE.6 | that dressing at ρ = ½ is X(p, ν) = [9p⁴+642p³+4588p²+11000p+7360 + 12(p+2)(5p³+24p²+44p−32)ν²]/(1536(p+4)(3p+2)) | POST HOC (exact residues at 12 p; rational reconstruction with 7 spare points) |
| W′ closed form | lim_{q→½} of the dressed pole term's n^{−3−pq} coefficient = R_{1/2}W(½)π²(p+2)²(p+4)(1−4ν²)/256 | CONFIRMED (exact limit, identity in p, ν, δ, R, c; two-sided). W′ itself stays a CONJECTURE |
| W′ ladder | W′ is the q₀ = ½ member of a family of finite terms at half-integer poles q₀, 2π²R W(q₀)Res_{q₀}H/q₀ · n^{−2−(p+2)q₀}, all ∝ (ν−q₀)_{2q₀+1} | CONJECTURE (follows from W′'s premise + P0/P1); q₀ = ½ is an identity |
| Finding WE.5 | for a genuine fractional time, W's dressing g(ρ)N⁻² is incomplete: for ρ < ½ the companion (relative N^{−2ρ−1}) precedes it, and at ρ = ½ the two merge into a log: relative 2Res_{½}g·N⁻²log N = −(p+2)²(p+4)(1−4ν²)/(128p)·N⁻²log N | exact at p = −1 (numerically confirmed on exact Laguerre sums); general p CONJECTURE |

## 0. Summary

1. **Branched E3.7 (W(b), fractional times).** The leading coefficient of W's fractional term, −(pρW(ρ)/2)t_ρ, and the exact
   linearity of the n⁻¹ coefficient in μ are confirmed exactly for the analytic part of the branched gauge (Lemma WE.1, Prop WE.2).
   The branched part of the gauge is a side-dependent multiple ±i tan(πρ)z^ρ of the tilt at the hard edge; it is not a conjugation of
   the engine's Laurent data and is outside the engine. In the exactly solvable case p = −1 (Laguerre = M(ν−1, ν)), the full response is
   the continued series (equal to the engine's symbolic-j output through N⁻⁶) **plus** a branched series starting at relative
   N^{−2ρ−1}. For general p the leading branched coefficient H(ρ) (a universality formula) is confirmed by exact pole-cancellation
   identities: the continued series has poles at half-integer ρ (from Γ ratios of the gauge data), the true response is finite there,
   and H's residues cancel them exactly — at ρ = ½ identically in (p, ν), at ρ = 3/2 identically in ν at 5 pre-registered p (and 7
   post hoc p). The companion's own N⁻² dressing is not the naive transport of the p = −1 structure (pre-registered P2, refuted);
   its value at ρ = ½ was reconstructed post hoc (Obs WE.6).
2. **W′.** The closed form R_{1/2}W(½)π²(p+2)²(p+4)(1−4ν²)/256·n^{−3−p/2} is exactly what the symbolic-j dressing continued to w = ½
   gives (exact two-sided limit; shift terms contribute 0). In the language of 1.: W′ = −π²pRW(½)Res_{½}g and Res_{½}g is fixed by
   H(½), so W′ is the q₀ = ½ member of a ladder of finite half-integer-pole terms; the (1−4ν²) factor is Φ_ν's (ν−½)(ν+½). The engine
   cannot represent pole terms, so W′'s premise (pole terms carry the continued dressing and **no** branched companion) is not tested
   here; the q = ½ data of JZC_W §2.4 are consistent with it and inconsistent with a companion ∝ cot(πq)H(q) (that would cancel W′).

## 1. The branched gauge (Lemma WE.1, Prop WE.2; `w_exact_gauge.out`, 14 checks)

**Setting.** E3's gauge for a polynomial tilt V = z^j is G = T[[cosh h, −(z−4c)S], [−zS, cosh h]]T⁻¹, h = RM/2, S = sinh(h)/R,
R = √(z(z−4c)), M = μQ_j, Q_j the polynomial part of z^j/R (check_e3_gauge.py). In the symbolic-j engine (m4_zeta_exact2.py) Q_j/C(2j, j)
enters only through its Taylor data at 0 and at 4c, which are rational in j (c = 1):
  at 0: Π_{i=0}^m (j−i)/(2(2j−2i−1));  at 4: j(j−1)⋯(j−m)/(4^{m+1}(½)_{m+1}).

**The branched analogue (c = 1).** For V = z^ρ (principal branch, cut (−∞, 0]) put M_ρ := z^ρ/R − 2C_ρ with C_ρ the Cauchy
transform of x^ρ/R₊ on [0, 4]. Then z^ρ − RM_ρ = 2RC_ρ has jumps only on [0, 4] and is O(1) at ∞ (it plays the role of V − RQ_j, the Szegő-function exponent
of E3 Lemma E3.4), and M_ρ is analytic off (−∞, 0] with the jump of z^ρ/R there. For −½ < ρ < 1 the Cauchy transform of that jump is

  M_ρ(z) = (sin πρ/π)∫_0^∞ s^{ρ−½}(s+4)^{−½}(s+z)^{−1}ds   (continued in ρ beyond).

**Lemma WE.1.**
(i) [w^m]M_ρ(4+w) = C(2ρ,ρ)ρ(ρ−1)⋯(ρ−m)/(4^{m+1}(½)_{m+1}).
(ii) M_ρ = A_ρ + tan(πρ)z^{ρ−½}(4−z)^{−½} near 0, with A_ρ analytic at 0 and [z^m]A_ρ = C(2ρ,ρ)Π_{i=0}^m(ρ−i)/(2(2ρ−2i−1)).
(iii) Hence R·M_ρ = R·A_ρ ± i tan(πρ)z^ρ near 0, the sign being that of Im z.
*Proof.* (i) Expand (s+4+w)⁻¹ in w; each term is a Beta integral 4^{ρ−m−1}B(ρ+½, m+1−ρ) (DLMF 5.12.3, quoted in RH/CITATIONS.md
(DLMF-2); its hypotheses ℜa = ρ + ½ > 0, ℜb = m + 1 − ρ > 0 hold for −½ < ρ < 1); with B(a, b) = Γ(a)Γ(b)/Γ(a+b) (DLMF 5.12.1, (DLMF-2)),
sin πρ/π = 1/(Γ(ρ)Γ(1−ρ)) (DLMF 5.5.3, (DLMF-2); ρ ∉ ℤ) and Γ(z+1) = zΓ(z) (DLMF 5.5.1, quoted in RH/CITATIONS.md) this is the stated
rational multiple of 4^ρΓ(ρ+½)/(√πΓ(ρ+1)) (Γ(½) = √π: 5.5.3 at z = ½); Legendre duplication (DLMF 5.5.5) identifies that prefactor with
C(2ρ,ρ) = Γ(2ρ+1)/Γ(ρ+1)² — **NOT QUOTED** (the DLMF §5.5 page could not be read in the session applying review B; see *Normalisation*
below) (fixed per Rule R review B, W2). (ii) Put F := M_ρ − tan(πρ)z^{ρ−½}(4−z)^{−½}. On (−4, 0) the jump of z^ρ/R is
−2i sin(πρ)|x|^{ρ−½}(4−x)^{−½} and that of z^{ρ−½} is −2i cos(πρ)|x|^{ρ−½}, so F has no jump there; F is analytic in 0 < |z| < 4 and
O(|z|^{ρ−½} + |log z|) = o(1/|z|) at 0 (ρ > −½), hence analytic at 0. A_ρ := F. Its Taylor coefficients for −½ < ρ < 1: split the
Stieltjes integral at s = 1; ∫_1^∞ is analytic in |z| < 1, and ∫_0^1 termwise with (s+4)^{−½} = Σh_ks^k gives the singular part
tan(πρ)z^{ρ−½}(4−z)^{−½} plus an analytic part. Together the coefficients are the Mellin-continued moments
(−1)^m(sin πρ/π)4^{ρ−m−1}B(ρ−½−m, m+1−ρ). The same identities as in (i) give the formula (fixed per Rule R review B, W1).
(iii) R = z^{½}(z−4)^{½} and (z−4)^{½}/(4−z)^{½} = ±i. ∎
*Range.* For fixed z, M_ρ(z) (defined for ρ > −½ by z^ρ/R − 2C_ρ) and its Taylor coefficients at 4 and those of F at 0 are analytic in
ρ, and the right-hand sides of (i), (ii) are meromorphic with poles only at ½ + ℤ (in (ii)). So (i) holds for all ρ > −½, and (ii), (iii)
for all ρ > −½, ρ ∉ ½ + ℤ (identity theorem in ρ). The κ-family uses ρ = q_m = m − 1/p, m ≤ M, including q₂ ∈ (1, 2) (fixed per Rule R
review B, W1).
*Normalisation* (fixed per Rule R review B, W2). Put N(ρ) := 4^ρΓ(ρ+½)/(√πΓ(ρ+1)) (= W(ρ)/c^ρ in JZC_W §1's Γ-form). The proof above,
without duplication, gives (i)–(ii) with C(2ρ,ρ) replaced by N(ρ); N(j) = C(2j, j) at integers j ≥ 0 by 5.5.1 and Γ(½) = √π. N(ρ) = C(2ρ,ρ) for
non-integer ρ is Legendre duplication, NOT QUOTED. JZC_W_kappa Prop K.12′(c)'s coefficient pρW(ρ)/2 uses only N(ρ) (the Beta value), so it
does not need duplication (review B §2.1); duplication enters only in writing the prefactor as C(2ρ,ρ) and in the identification with the
engine's C(2j, j)-normalised symbolic-j data.
Checks: (i), (ii) as exact sympy identities in symbolic ρ for m ≤ 8; the decomposition (ii) and the Taylor series (i) against direct
quadrature of the Stieltjes form (head by tanh-sinh with the substitution s = t^{2/(2ρ+1)}, tail by exact termwise integration) at
ρ ∈ {0.3, −0.2, 2/3, 0.9} and four z: relative deviation ≤ 2·10⁻⁴⁰ (40 digits, 260 Taylor terms); (iii) to 10⁻³⁰. Controls: sin(πρ) for tan(πρ), no
branched term, (½)_m for (½)_{m+1}: all fail. ρ > 1: Rule R review B, Cauchy-integral check at ρ ∈ {1.6, 5/3, 2.3} (and 0.15, 0.45, −0.35),
relative ≤ 1.6·10⁻²⁶; review A at 4/3 (fixed per Rule R review B, W1).

**Consequence.** The engine run with symbolic j and then j = ρ is *exactly* the RH computation with the gauge built from A_ρ at the
hard edge and M_ρ at the soft edge. What it omits is the branched remainder ±i tan(πρ)μz^ρ/2 in the gauge exponent at the hard
edge. That term is not of the engine's form (a conjugation of the Laurent data on the circle by a matrix analytic in the disc): it
has a jump on the whole real diameter of the disc, so it changes the local (Bessel) parametrix itself. Including it needs the
first-order correction of the Bessel model problem by a |ζ|^ρ jump, i.e. regularised Mellin moments of products of Bessel functions.
This is the obstruction to a full exact test at general p; §2 does the exact test at the one p where the model is a classical weight.

**Prop WE.2 (branched E3.7 at the n⁻¹ level).**
- Route 1 of m3a_e37_decoupled.py (an identity for *arbitrary* M analytic at 4c, all orders in μ) gives
  n⁻¹ coefficient = d₁ + c p M(4c); with (i) and c-scaling, c p M_ρ(4c) = pρW(ρ)/2 per unit μ, W(ρ) = C(2ρ,ρ)c^ρ =
  (4c)^ρΓ(ρ+½)/(√πΓ(ρ+1)) (asserted). With μ = −t_ρn^{−pρ} this is W's −(pρW(ρ)/2)t_ρ·n^{−1−pρ}.
- Route 2 (the engine's own gauge, small-norm recursion and extraction; DECOUPLE = 1, EO = 3, symbolic j): the μ-response of the
  n⁻¹ coefficient is pj/2 per unit μC(2j, j) at first order and **0 at second and third order**, identically in (p, ν, β, j); so the
  same holds at j = ρ for the A-gauge.
- The branched remainder enters through the hard-edge parametrix, whose natural scale is z ~ n⁻²; its contributions carry the extra
  factor n^{−2ρ−1} relative to the leading term (§2.3), so for ρ > −½ they do not reach the n⁻¹ coefficient. HEURISTIC in general,
  exact at p = −1 (§2: the branched series starts at N^{−2ρ−2}).

## 2. An exactly solvable case: p = −1 is Laguerre (Prop WE.3; `w_exact_laguerre.out`, 24 checks)

### 2.1 Identification

At p = −1 the lattice g-function's hard-edge map has 𝔞-denominators a′ + k = k − ½ (no zero), and the engine runs unchanged
(PVAL = −1). With β = ν − 1 (SZOFF = −1), N = n + (β+1)/2 = n + ν/2 and the engine gives the integer layer
F = 1 − ν²/(8N²) − ν⁴/(128N⁴) − ν⁶/(1024N⁶) = √(1 − ν²/(4N²)) through N⁻⁶: the Laguerre recurrence b_n = √(n(n+ν)) in the frame
n^pb_n/c = b_n/n, z = x/n, c = 1 (band [0, 4], the Marchenko–Pastur scaling). The closed forms f₂, f₄, f₆ of JZC_M4 §5 at p = −1
give the same (f₆: c₀, c₂, c₄ carry (p+1), and c₆/((3p+2)²(5p+2)) = −1/1024). So M(ν−1, ν) at p = −1 is the Laguerre weight x^νe^{−x}.

### 2.2 The exact Laguerre response to x^ρ

For the weight x^νe^{−x}e^{tx^ρ}, ∂_t log b_n² = m_n − m_{n−1}, m_n := ⟨x^ρ⟩_n = ∫x^ρπ_n²w/h_n (Toda, JZC_M4 §8; the argument
needs only ∂_tπ_n ⊥ π_n, so it holds for any tilt). With λ = ν + ρ:
- (L1) S_n := ∫x^{λ}e^{−x}L_n^ν(x)²dx = Σ_k Γ(λ+k+1)/k!·[(−ρ)_{n−k}/(n−k)!]² (checked against quadrature, and ρ = 1: m_n = 2n+ν+1);
- (L2) S_n = [x^n]Γ(λ+1)(1−x)^{−λ−1}₂F₁(−ρ, −ρ; 1; x);
- (L3) Gauss's connection formula at x = 1 (c−a−b = 1+2ρ) splits ₂F₁ into an analytic part C(2ρ,ρ)₂F₁(−ρ,−ρ;−2ρ;1−x) and a
  branched part (1−x)^{1+2ρ}Γ(−1−2ρ)/Γ(−ρ)²·₂F₁(1+ρ,1+ρ;2+2ρ;1−x) (NOT QUOTED here; checked numerically to 10⁻⁵⁰);
- (L4) singularity analysis ([x^n](1−x)^{−γ} = Γ(n+γ)/(Γ(γ)n!), termwise; NOT QUOTED; the result is checked numerically).
Result: m_n = m_n^A + m_n^B,
  m_n^A = C(2ρ,ρ)Σ_i (−ρ)_i²/((−2ρ)_i i!)·(λ+1−i)_i·Γ(n+ν+ρ+1−i)/Γ(n+ν+1),
  m_n^B = Φ_ν(ρ)Σ_i (1+ρ)_i²/((2+2ρ)_i i!)·(ν−ρ−i)_i·Γ(n+ν−ρ−i)/Γ(n+ν+1),   Φ_ν(ρ) = Γ(−1−2ρ)Γ(ν+ρ+1)/(Γ(−ρ)²Γ(ν−ρ)).
Numerically (exact finite sums, 50 digits; ν ∈ {0.3, −0.4}, ρ ∈ {0.37, ⅔, 1.3}, n = 100…800): |m_n − m^A − m^B|/|m_n| ≤ 1.9·10⁻²¹,
while m^A alone misses by |m^B|/|m_n| = 8·10⁻⁸ … 3·10⁻⁷ (ρ = 0.37), 6·10⁻¹⁰ … 2·10⁻⁹ (ρ = ⅔), 10⁻¹³ (ρ = 1.3, ν = −0.4) at n = 800
(at ν = 0.3, ρ = 1.3, Φ = 0 since ν − ρ = −1). Φ_ν(ρ) is the regularised Mellin moment ∫_0^∞y^ρJ_ν(2√y)²dy (Weber–Schafheitlin; checked
by quadrature where it converges, 10⁻⁹): the hard-edge Bessel profile of π_n²w.

**The natural-form response.** Per unit μ for the normalised tilt exp(−μz^ρ/C(2ρ,ρ)) (the engine's convention), with
G(N) := (N/n)^{(ρ+1)p}∂_μ(n^pb_n/c) = −½√(1−ν²/(4N²))N^{−ρ}(m_n − m_{n−1})/C(2ρ,ρ) at p = −1:
- **Prop WE.3:** the analytic part G^A = Σ_kG_kN^{−k} equals the engine's symbolic-j output g1[k] at j = ρ for k = 0, …, 6,
  identically in (ν, ρ): G₀ = G₂ = G₄ = G₆ = 0, G₁ = −ρ/2, G₃ = G₁(A_ρ + B_ρν²)|_{p=−1}, and G₅ (a new closed form with denominator
  (2ρ−1)(2ρ−3)). The engine computes the RH model; the Laguerre side is classical — two independent computations.
- **The branched part** is G^B = (Φ_ν(ρ)/C(2ρ,ρ))N^{−2ρ−2}Σ_k rat_kN^{−k} with rat₀ = (ρ+1)/2, rat₁ = rat₃ = 0 and the exact
  *reflection* rat_k = G_{k+1}(ρ → −1−ρ) (k ≤ 5). Equivalently, in raw form, the branched response is (Φ/C)n^{−2ρ−1} times the
  analytic response at the exponent ρ* = −1−ρ.
- **Pole cancellation:** G^A_k has simple poles at half-integers ρ₀ (from (−2ρ)_i), and Res_{ρ₀}G^A_k + Res_{ρ₀}(Φ/C)rat_{k−2ρ₀−2} = 0
  for ρ₀ ∈ {½, 3/2}, k ≤ 6 (exact; the pole at 5/2 first appears in G₇).
- **ρ = ½:** the response contains 2r·N⁻³log N, r = Res_{ρ=½}G₃ = −3(1−4ν²)/1024 (= G₁·Res g at p = −1). Checked on the exact sums
  (n = 1000…8000): the slope of N³(G − G₁/N) against log N between n = 4000 and 8000 is −0.003750000078 (ν = 0.3; 2r = −0.00375)
  and −0.005859375228 (ν = 0; 2r = −0.005859375), converging like N⁻².
Controls: G^A re-expanded in N′ = n + (ν+1)/2 acquires an N′⁻² term; the i = 0 term of the analytic series alone does not give G₃;
the reflection ρ → −ρ fails; m^A alone does not reproduce m_n.

### 2.3 The hard-edge companion at general p (Finding WE.4; HEURISTIC derivation, exact tests in §3)

The branched series is local to the hard edge. Near z = 0 the single-polynomial density π_n²w/h_n has the Bessel profile
n√κ·J_ν(2n√(κz))² (amplitude fixed by matching the arcsine density 1/(2π√z) that π_n²w averages to, Buyarov–Rakhmanov), with
κ the hard-edge scale of the engine's local map: f(z) = −z/(p+2)² + O(z²) (E2 Lemma E2.4; m4_rh_exact2 writes f = v²ĝ, z = −v², and
asserts ĝ(0) = 1/(p+2)²), so
κ = (p+2)⁻² (c = 1; p = −1 gives Laguerre's κ = 1). Hence the branched part of ⟨z^ρ⟩ is n^{−2ρ−1}κ^{−ρ−½}Φ_ν(ρ), that of
⟨x^ρ⟩_n = n^{−pρ}⟨z^ρ⟩ is n^{−pρ−2ρ−1}κ^{−ρ−½}Φ_ν(ρ), and differencing in n gives, per unit μC(2ρ,ρ),

  **H(ρ) N^{−2ρ−2}(1 + O(N⁻¹)),  H(ρ) = ½(pρ + 2ρ + 1)(p+2)^{2ρ+1}Φ_ν(ρ)/C(2ρ,ρ),**

i.e. a term at relative order N^{−2ρ−1} against the leading pρ/2·N⁻¹. At p = −1 this is the exact Laguerre leading branched term.
Properties: Φ_ν has a double zero at integer ρ (1/Γ(−ρ)²), so integer times have no companion (consistent with Theorem N.6);
it carries Γ(ν+ρ+1)/Γ(ν−ρ), which at half-integer ρ₀ is the polynomial (ν−ρ₀)_{2ρ₀+1}; it has simple poles at ρ₀ ∈ {½, 3/2, …}.

## 3. Exact tests of the companion at general p (pre-registered)

### 3.1 Protocol (Rule X)

H(ρ) was written down from §2.3 before any comparison with the general-p engine. `w_exact_predict.py` wrote, at 09:38:30, the
predicted residues of the engine's continued response at the half-integer poles, for p ∈ {½, 3/2, 2, 5/2, 3}:
- P0: Res_{j=½}g1[3] = −Res_{ρ=½}H  (relative N⁻²);
- P1: Res_{j=3/2}g1[5] = −Res_{ρ=3/2}H  (relative N⁻⁴; the leading companion at ρ = 3/2);
- P2: Res_{j=½}g1[5] = −Res_{ρ=½}[H(ρ)g(ρ*)], ρ* = ρ + (2ρ+1)/p (the p = −1 reflection, transported: pρ* = pρ + 2ρ + 1 is the
  exponent of the companion's power);
- P3: g1[4] = 0, and the j-poles of g1[5] are simple and only at ½, 3/2.
The engine runs (`w_exact_poles_prereg.py`, KORD = 5, symbolic (ν, j), p fixed) started at 09:39:09.

### 3.2 Results

| p | P0 | P1 | P2 | P3 |
|---|---|---|---|---|
| ½, 3/2, 2, 5/2, 3 (registered; `w_exact_poles_prereg_A/B.out`) | holds (identity in ν) | **holds** (identity in ν: the quartic (2ν−3)(2ν−1)(2ν+1)(2ν+3) and the constant) | **fails** at all five | holds |
| ⅓, ⅔, 4/3, 4, 5, 6, −1 (post hoc; `w_exact_poles_A/B.out`) | holds | holds | (not registered) | holds |

The pre-registered script and its two outputs are kept unchanged (`w_exact_poles_prereg.py`; its outputs print its sha256 under its
original name `w_exact_poles.py`, a58b45b7…). The final `w_exact_poles.py` re-runs the registered p (P0, P1 against the registered
values, the registered P2 as a check that must fail, labelled REFUTED) and the post hoc p (P0, P1 from H), 12 values of p in all,
and caches the residues (tmp/w_exact/). Engine time 2–7 min per p.

- P0 is in fact an identity in p (`w_exact_wprime.out` (3)): (p/4)Res_{½}g = −Res_{½}H. It is the statement "the continued
  dressing's pole at w = ½ is exactly cancelled by the hard-edge companion".
- P1 is the independent test: it involves κ^{−2} = (p+2)⁴, the factor (3p/2 + 4), Res Γ(−4) and (ν−3/2)₄, against the engine's
  N⁻⁵ coefficient, whose j-dependence was never written down before (denominator (2j−1)(2j−3)). Controls κ^{−ρ} and the opposite sign
  fail.
- **P2 is refuted.** The subleading dressing of the companion at general p is not g(ρ*). The values X(p, ν) := −Res_{½}g1[5]/Res_{½}H
  (the relative N⁻² dressing of the companion at ρ = ½) are, e.g., X(2, ν) = 23/32 + ν²/8 against g(3/2) = 3/2 + 2ν² at p = 2.
  §3.4 identifies X post hoc.

### 3.3 What is exact and what is not

Exact (identities of rational functions): the engine outputs and their residues at fixed rational p; P0 for all p. Not proved: that
the full response at general p is "continued series + companion" (that needs the corrected Bessel parametrix, §1). The pole
cancellation is a strong consistency check: the continued series *must* be completed by something with exactly these residues,
since the response to a tilt x^{1/2} or x^{3/2} is finite.

### 3.4 Post hoc: the companion's N⁻² dressing (`w_exact_xfit.out`)

At ρ = ½ the residue of g1[5] fixes the relative N⁻² coefficient of the companion, X(p, ν) := −Res_{j=½}g1[5]/Res_{ρ=½}H. It is
quadratic in ν at all 12 p, and rational reconstruction with the ansatz P_i(p)/((p+4)(3p+2)) (the denominator was read off the five
registered values: post hoc) gives, with **7 spare points reproduced exactly**,

  X(p, ν) = [9p⁴ + 642p³ + 4588p² + 11000p + 7360]/(1536(p+4)(3p+2)) + (p+2)(5p³ + 24p² + 44p − 32)ν²/(128(p+4)(3p+2)),

e.g. X(2, ν) = 23/32 + ν²/8, X(−1, ν) = −35/512 + 19ν²/128 (= g(−3/2) at p = −1, the Laguerre reflection; P2's form holds at p = −1
and only there). The factor 3p+2 is the hard-edge denominator of f₄ and of the zeta layer's N⁻⁵ dressing (JZC_M4 §5, §6). Label:
NUMERICAL-type reconstruction (exact values, interpolated form), POST HOC. Consequence under W′'s premise: the q = ½ pole term is
W′·(n/N)^pN^{−3−p/2}(1 + X(p, ν)N⁻² + …), i.e. at p = 2, ν = 0 the next correction to the sphere's 3π²R/8 term is ×(23/32)N⁻²
(a prediction for the n⁻⁵ coefficient of M1/K2p, not tested).

## 4. W′ (`w_exact_wprime.out`, 15 checks)

**Exact algebra.** g(w) = A(w) + B(w)ν² has exactly one pole, at w = ½, with Res = −(p+2)²(p+4)(1−4ν²)/(256p) (identity). For the
pole term P(q) = pRW(q)πcot(πq)(n/N)^pN^{−1−pq}[1 + g(q)N⁻²] (N = n + δ), the n^{−3−pq} coefficient is
pRW(q)πcot(πq)[(1+p+pq)(2+p+pq)δ²/2 + g(q)], and sympy's limit q → ½ is
  **R W(½)π²(p+2)²(p+4)(1−4ν²)/256**,
identically in (p, ν, δ, R, c): **W′'s closed form is confirmed exactly** (as the limit of the stated expression). The shift terms
contribute 0; cot(πq)g(q) is analytic at q = ½ (a removable singularity), so the limit is two-sided (values at ½ ± 10⁻¹⁵ agree with
−πRes g to 10⁻¹⁴); JZC_W §3 item 9's earlier mpmath.limit value −0.2107 can only have been a numerical artefact of the 0·∞ form; the limit is unambiguous.
p = 2, c(2) = π²/16: W(½) = 1 and the term is (3π²/8)(1−4ν²)R; R = −1/16 gives −0.2313189 (ν = 0) and −0.1734891 (ν = ¼), JZC_W's values.

**W′ as a ladder member (CONJECTURE beyond q₀ = ½).** By P0, Res_{½}(G₃/G₁) = −Res_{½}H/G₁, so
W′ = −π²pRW(½)Res_{½}g = 4π²RW(½)Res_{½}H (identity). The same mechanism at a half-integer pole q₀ and the order where the analytic
series has its pole at q₀ (relative N^{−2q₀−1}, by P1 for q₀ = 3/2) gives, *if pole terms carry the continued analytic dressing and
no companion* (W′'s premise),
  2π²R_{q₀}W(q₀)Res_{q₀}H/q₀ · n^{−2−(p+2)q₀};
for q₀ = 3/2: −πRc^{3/2}(2ν−3)(2ν−1)(2ν+1)(2ν+3)(p+2)⁴(3p+8)/4096 · n^{−5−3p/2}. Every such term carries (ν−q₀)_{2q₀+1}, so it
vanishes at ν = ±½: the bouncer and Robin at s = 2 (ν = ½) and the Bessel/Lommel family (ν = −½) are unaffected at every
half-integer pole, consistent with the exact Lommel form (Prop N.2) and with JZC_W Rule A item 9. (JZC_W's "at other half-integers g has
no pole" is right for g, but the next dressing coefficient has a pole at 3/2; the resulting term is deep: n^{−8} at p = 2.)
Also at q₀ = ½ the next collision (relative N⁻⁴, g1[5]) gives a further finite term: W′'s own dressing, W′·X(p, ν)N⁻² (§3.4).

**Why W′'s premise matters.** If pole terms had a companion ∝ cot(πq)H(q), then at q = ½ the bracket g N⁻² + (H/G₁)N^{−2q−1}
would be finite (a log) and the cot zero would kill the W′ term. The sphere (n⁻⁴ to 2·10⁻⁸ with W′) and probe 2 (JZC_W §2.4) show the
term, so pole terms have no such companion; pole terms and genuine fractional times differ exactly there. This is the
distinction the engine cannot test: pole terms are not a band-factor gauge (they come from the equilibrium of the non-lattice node
set, JZC_W §5.1 item 3).

**Predictions for q ≠ ½ (W′ for pole terms; NOT tested here).** p = 2, c = π²/16, coefficient of n^{−3−pq} per unit R_q,
pW(q)πcot(πq)g(q): q = ¼: g = 249/256 (ν = 0), 211/256 (ν = ¼); +5.8423418, +4.9507395. q = ¾: g = −41/256, 21/256; +1.1023123,
−0.5645990. q = 3/2: 0 (cot = 0, g regular); the first nonzero half-integer term is the ladder's n^{−8}. A test needs a measure with a
pole at such q and a fit at n^{−3−pq} beyond the second-order pole products (n^{−2−2pq}); for q = ¼ at p = 2 these are n^{−3.5} and
n^{−3}, so the dressing is separable. Exact tests would need the pole mechanism in the engine (not available).

**Genuine fractional times (Finding WE.5).** For a mass or density tilt x^ρ (not a pole), W's "−(pρW(ρ)/2)t_ρ(n/N)^pN^{−1−pρ}
[1 + g(ρ)N⁻²]" is complete to relative O(N⁻²) only for ρ > ½. For ρ < ½ the companion (relative N^{−2ρ−1}, coefficient H/(pρ/2))
comes first: at p = 2, ρ = ¼ it is −0.5395735 (ν = 0), 0 (ν = ¼: Γ(ν−ρ) pole), −0.8444740 (ν = −⅓), at relative N^{−3/2}. At ρ = ½ the
pair becomes 2Res_{½}g·N⁻²log N = −(p+2)²(p+4)(1−4ν²)/(128p)·N⁻²log N (relative). For the cases tested in JZC_W (ρ = ⅔, 4/3) the
companion is at relative N^{−7/3}, N^{−11/3}, beyond W's claimed precision, so W's §2 results are unaffected; e.g. p = 2: H/(pρ/2) =
0.8684704 (ρ = ⅔, ν = 0).

## 5. Rule A log

1. *Rule X.* Predictions P0–P3 (§3.1) were written 09:38:30, before the general-p engine runs (09:39:09); the timestamps are asserted
   by the scripts. P2 failed and is reported as refuted; the final script keeps the registered P2 as a must-fail entry, and the
   pre-registered script and its outputs are kept unchanged (`*_prereg*`). The post hoc material (§3.4, the extra p of §3.2) is labelled.
2. *Is H circular?* H was derived from the Laguerre exact branched term (p = −1) and two p-dependent ingredients read from the engine's
   *integer* data (κ = (p+2)⁻² from g(0) = 1/(p+2)², and the factor pρ+2ρ+1 from differencing n^{−pρ−2ρ−1}); it uses neither g nor
   any zeta-layer output. P0 being an identity in p and P1 holding at five p in the full ν-dependence are therefore tests, not fits.
3. *Is the p = −1 agreement trivial?* No: the engine at p = −1 is the formal RH computation with the lattice g-function's local maps
   (Airy and Bessel series in a′ = 1/p + ½); the Laguerre side is the classical moment formula. They agree on f₂…f₆ and on G₀…G₆
   identically in (ν, ρ). (At p = −1 the soft-edge series S has a single m = 0 term since (1+1/p)_m = 0 for m ≥ 1; checked to run.)
4. *Branches.* z^ρ principal (cut (−∞, 0]); the sign of tan(πρ) and the side-dependent ±i of (iii) are checked numerically, not
   assumed. Using (−z)^ρ (cut along the band) instead would be the natural object for pole terms; it is not analysed here.
5. *Degenerate parameters.* Integer ρ: Φ has a double zero, no companion (consistent with E3.7/Theorem N.6). ρ → 0: trivial.
   ν = ±½: every half-integer residue vanishes. ρ < −½: the Mellin moment and the n⁻¹ argument fail (not claimed).
6. *Convergence of the expansions.* The two-series form for Laguerre is asymptotic; the numerical checks use 14 terms each at
   n ≥ 100 and reach 1.9·10⁻²¹ relative; the control (m^A alone) shows the companion is real.
7. *Second-order response.* "Zero second-order n⁻¹ response" is exact for the A-gauge (route 2, EO = 3); for the companion it is
   a power count (second-order branched terms carry n^{−2ρ}·n^{−2ρ−1} or more). The Laguerre case does not test second order.
8. *W′ limit.* The exact limit removes the "symmetric average" question of JZC_W §3 item 9: cot(πq)g(q) is analytic at ½.

## 6. What remains

- **A proof of the companion at general p:** the first-order correction of the Bessel model problem by the |ζ|^ρ jump on the negative
  axis (Mellin moments of J_ν², J_νY_ν, Y_ν²), matched into the engine's hard-edge circle at order μn^{−2ρ−k}. With it the engine
  could treat branched tilts completely (two formal variables: n⁻¹ and n^{−2ρ}).
- **The companion's dressing:** P2 refuted; the post hoc closed form X(p, ν) of §3.4 needs a derivation (and a pre-registered test,
  e.g. at ρ = 3/2 against g1[7], KORD = 7).
- **Pole terms in the engine:** they need the equilibrium of non-lattice node sets (JZC_W §5.1 items 1, 3); until then W′ (and its
  ladder) is a conjecture about pole terms, confirmed only at q = ½ by measures.
- **Measure tests of the new predictions:** (a) a fractional mass tilt with ρ < ½ (e.g. masses ∝ 1 + bλ^{−ρ}·… with ρ = 0.3 at
  p = 1.5): the companion at n^{−1−pρ−2ρ−1}; (b) a fractional tilt at ρ = ½: the N⁻²log N term; (c) a pole at q = ¼ (p = 2): W′'s
  dressing +5.84R at n^{−3.5}.
