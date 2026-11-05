# Rule R review B: the p < 1 fixed-n inputs of Theorem H (JZC_M3a_H_G3.md and JZC_M3a_H_G23plt1.md)

Reviewer: independent second reader (Rule R), reviewer **B**. Date: 2026-10-22. Branch plan-e2-d2 (HEAD c961b47).
- Targets:
  1. research/G1/RH/spectral/JZC_M3a_H_G3.md (Lemmas 1–3 incl. the (ii′)/(iii′) addendum, Prop 4, Cor 5, §§5–7), with its
     checks checks/m3a_g3_seam.py/.out and checks/m3a_g3_model.py/.out; and whether review A's fixes F1–F9 were applied correctly
     (research/G1/review/REVIEW_JZC_M3a_H_G3_A.md).
  2. research/G1/RH/spectral/JZC_M3a_H_G23plt1.md (L2.1′–L2.5, P2.6; Lemma M, Lemma F.1_δ (i)–(iv), Remark H, §2.2 table), with
     checks/m3a_g23_apriori.py/.out and checks/m3a_g23_F1.py/.out.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; JZC_M3a_H.md (statement, §§3–4); JZC_M3a_H_G12.md §1 (L1.1, L1.2) and §2 (as the
  p > 1 template); JZC_M3a_Hd.md §6 item 6; papers/paper2/app_outer.tex §outer-plt1 (Lemma seam with proof, Lemma corner),
  sec_5.tex (standing assumptions, eq:angles, eq:Zn), app_c.tex (Lemma lenssector proof, the arc sentence);
  second_order/E_plt1.md §3 (Lemma F.1 and proof, Remarks); RH/plt1/RH_plt1b.md §2; RH/CITATIONS.md entries (DLMF) §5.11,
  (DLMF-5.5/5.11, Plan 54), (DLMF-zeta, Plan 67).
- I edited no file except this report. My own scripts and outputs are in the session scratchpad (`…/scratchpad/reviewB/spot.py`,
  `spot.out`; repo re-runs in `…/scratchpad/rerun/`).

## Overall verdicts

| Memo | Verdict | MAJOR | MINOR / typo / INFO |
|---|---|---|---|
| JZC_M3a_H_G3.md | **ACCEPT WITH FIXES** | none | B3-1 – B3-7 (status texts made stale by G23plt1; numerics wording and rounding; one script docstring) |
| JZC_M3a_H_G23plt1.md | **ACCEPT WITH FIXES** | none | B23-1 – B23-9 (overlap with G3's addendum not recorded; numerics wording and misquoted precisions; a missing τ₀; η range; CITATIONS line; docstrings) |

No mathematical error was found in either memo. Every key step listed below was re-derived from the write-up and the quoted
sources, and every check was re-run (§4). With the fixes below applied (all are wording/status/bookkeeping), both memos meet the
REVIEWED criterion of VERIFICATION_POLICY.md (Rule R: independent re-derivation + re-run checks), within the scope stated in §5.

## 1. Review A's fixes in JZC_M3a_H_G3.md (verification)

| A-fix | Required | Applied? |
|---|---|---|
| F1 (MAJOR, scope) | Cor 5 restricted to H-d (i)–(iii); the false "(iv) F_δD_W^{(α)} bounded" sentence deleted; §7 bullet for H-d (iv) | **Yes**: header row "Cor 5", §0 last sentence, Cor 5 statement + proof ("The former '(iv) …' clause is deleted"), §7 bullet 2. |
| F2 (proof gap at ∞ near the seams) | (ii′), (iii′) added; Paper 2 wording gap recorded for FIXES | **Yes**: "Addendum to Lemma 3 (ii), (iii)", text verbatim from A; Lemma 3 (iii) and Prop 4 point to it; §6 item 9; JZC_M3a_H.md §4 "For FIXES" (2). |
| F3 (typo) | "\|G²\|^{±1} ≤ C\|z\|^{4N}, and the same for G^{−2}" | **Yes** (Lemma 1 proof). |
| F4 | log in the Lemma 2 error term | **Yes** ("1 + O(\|z\|^{−min(1,1/p)}log\|z\|) + O(\|z\|^{−1})"). |
| F5 | §0: (O1)+(O5)-at-∞ for F♮, (O2)–(O4)+(O5)-near-0 for F_δ | **Yes** (§0 text verbatim from A). |
| F6 | Lindelöf clause for the limit at 0 near the seams | **Yes** (Prop 4 statement). |
| F7 | moments = Fourier sums (unconditional), ζ(−kp, 1+δ) form = Remark 3.3 (NOT QUOTED) | **Yes** (header row and Cor 5). |
| F8 | 1 < s < 1 + 2p | **Yes** (header). |
| F9 | "Also used in: JZC_M3a_H_G3" lines in CITATIONS | **Yes** (RH/CITATIONS.md lines 100 and 509; the header points to both entries). |

All nine fixes are applied correctly; I checked that the inserted texts are mathematically right (re-derived (ii′), (iii′) below).
What the A-fixes did not touch, and what has gone stale since G23plt1 was written, is B3-1.

## 2. JZC_M3a_H_G3.md: re-derivations and findings

### 2.1 Re-derived
- **§2, the decay of χ_±^δ at ∞.** On Σ^s_+, t = −i|t|, Log t = ln n − (1/p)Log ζ (arg consistent: −π/2 = −(1/p)(πp/2)). As t → 0 with
  Re(t − δ) = |δ| > 0: j_δ(t) → LnΓ(−δ) + (δ+½)Log t − ½ln 2π. 1 − e^{2πiδ} = 2 sin(πδ)e^{i(πδ−π/2)} = 2|sin πδ|e^{i(π/2+πδ)}, and
  π/2 + πδ ∈ (−π/2, π/2), so −Log(1 − e^{2πiδ}) = −ln(2|sin πδ|) − i(π/2+πδ), as in the memo. arg(−ζ/2πn) =
  πp/2 − π ∈ (−π, 0). Log ζ coefficient: (δ+½)/p + (ϖ_δ+1) − 1 − (½+δ) = 0 with ϖ_δ = (1 − 1/p)(½+δ). Imaginary constant:
  −(π/2+πδ) + (½+δ)π = 0. Real constant: −LnΓ(−δ) + (1+δ)ln 2π − ln(2|sin πδ|) − ln λ_δ = 0, which *defines* λ_δ; reflection
  Γ(−δ)Γ(1+δ) = π/|sin πδ| gives λ_δ = Γ(1+δ)(2π)^δ. All confirmed.
- **§0 (OBSTRUCTION).** With the lattice B's the coefficient is (δ+½)/p + ϖ − ½ = δ/p and the constant is
  −LnΓ(−δ) + ln 2π − ln(2|sin πδ|) − δ ln n − iπδ = lnΓ(1+δ) − δ ln n − iπδ = c_+. Confirmed; log ζ/ζ is not integrable, so (eq. chi)
  diverges: the verbatim route is correctly rejected.
- **Small ζ.** r_δ(t) = (t−δ−½)Log(1−δ/t) + δ = O(1/|t|) (G12 L1.2(b) gives ⅔/|t|, δ-uniform); |j(t−δ)| ≤ 1/(6|t|) by binet-bound at φ = π/2
  (|arg(t − δ)| < π/2, |t − δ| ≥ |t|); the exponential term is O(e^{−2π|t|}); the three elementary Logs are O(|ζ|). Hence |χ_±^δ| ≤ C|ζ|,
  C n-free for n ≥ 2. Confirmed.
- **Lemma 1, Lemma 2.** Re-derived as written (G² rather than G across 𝒵_n since only F̃² is analytic there; κ_δ+/κ_δ− = −e^{2iθ_δ}, so
  F̃₊ = −F̃₋ for every δ; Lemma 2 jump bookkeeping e^{2πi(t−δ)}·e^{2πiδ}·e^{−2πit} = 1 on (R, ∞), with ((−z)^{−δ})₊/((−z)^{−δ})₋ = e^{2πiδ}).
- **Addendum (ii′).** j_δ′(t) = ψ(t − δ) − ln t + (δ+½)/t; so t·j_δ′ = O(1) for |t| ≤ 2 (ψ analytic near Re(t − δ) ≥ |δ|) and
  j_δ′ = O(|t|^{−2}) for |t| ≥ 2 (ψ(u) = ln u − 1/(2u) + O(u^{−2}) with u = t − δ); the Log term's derivative is bounded by
  2π/s_δ. With dt/dζ = −t/(pζ) this is |χ_±^δ′| ≤ C_n/|ζ| on |ζ| ≥ 1. Confirmed.
- **Addendum (iii′)** (window argument). Re-derived in the sharper form of G23plt1 L2.5 (§3.1 below).
- **Prop 4.** In S_out, B_out^δK = (−z/2πn)^{½+δ}(1 − 2πn/z)^{½+δ}(−z)^{−½}(1 − 4c/z)^{−½}, principal branches compatible because
  |arg(−z)| < π − πp/2 there; so F_δ = (2πn)^{−½−δ}(−z)^δ(1 + O(1/z))e^{χ_δ} on every S_out ray, χ_δ → 0 off the seams by dominated
  convergence (χ_±^δ/ζ ∈ L¹). Lemma 2 (hypothesis: polynomial bounds on a full neighbourhood of ∞, now (iii′)) gives m = 0 and the
  constant uniformly. Confirmed, and confirmed numerically by my own quadrature (§4.2: the deviation is exactly O(1/|z|) with the
  same value on all five rays, including 10⁻⁹ rad from both sides of both seams).
- **Cor 5.** H-d §3's proof uses only the listed inputs; within Z_n ⊂ S_in (θ_w = 3πp/8 < πp/2) F_δ = D_δB_in^δKe^{χ_δ} has the κ_δ
  structure of p > 1. Confirmed for (i)–(iii).

### 2.2 Findings (G3)

**B3-1 (MINOR; status texts made stale by JZC_M3a_H_G23plt1.md).** Four places in G3 still describe as open/in progress what
G23plt1 now supplies (NOT REVIEWED until this review):
- header table row "Cor 5": "H-d (i)–(iii) only, (iv) open: §7";
- Cor 5, *Band factor*, last clause: "F.1 (iv)'s remainder bound was not re-derived for complex ℓ_± (expected verbatim: …)";
- §7 bullet 1: "E_plt1 Lemma F.1 (iv) with complex ℓ_± (expected verbatim)";
- §7 bullet 2: "… being worked on in JZC_M3a_H_G23plt1.md (in progress)".

*Fix (exact text):*
- table row: replace "(iv) open: §7" by "(iv) is JZC_M3a_H_G23plt1.md P2.6".
- Cor 5, last clause: replace "F.1 (iv)'s remainder bound was not re-derived for complex ℓ_± (expected verbatim: |ℓ_±| is bounded at
  ∞ and super-small at 0)." by "F.1 (iv) with the complex ℓ_± is JZC_M3a_H_G23plt1.md Lemma F.1_δ (iv) (constants δ-free, via Lemma M);
  F.1 (iii) gives the Fourier sums, not ζ(−kp)/(kn^{kp})."
- §7 bullet 1: delete "E_plt1 Lemma F.1 (iv) with complex ℓ_± (expected verbatim)."; §7 bullet 2: replace "(in progress)" by
  "(done there: L2.1′–L2.5, P2.6)".
- §7 bullet 3 ("Inherited from H-d: G2 …"): add "(G2 for p < 1 is G23plt1 L2.1′; G5 is JZC_M3a_H.md §3.3)".

**B3-2 (MINOR; precision quoted for Remark 3.3).** Cor 5 says "NUMERICAL to 2·10⁻¹⁶". That is the worst error in
spec_hurwitz_moments_plt1.out (2.16·10⁻¹⁶: its k = 3 rows are at the double-precision level), whereas m3a_g23_F1.out [E] gives
≤ 1.5·10⁻²⁴ (maximum over its 45 printed values) for the same identity, and JZC_M3a_H.md Remark 3.3 says "10⁻²⁷ … (and p < 1)",
which neither p < 1 file supports.
*Fix:* G3 Cor 5: "(NOT QUOTED; NUMERICAL: ≤ 2·10⁻²⁴ relative, m3a_g23_F1.out [E]; 2·10⁻¹⁶ in spec_hurwitz_moments_plt1.out)";
JZC_M3a_H.md Remark 3.3: "to 10⁻²⁷ for p ∈ {1.25, 1.5, 3} … ; for p < 1 to 2·10⁻²⁴ (m3a_g23_F1.out [E])".

**B3-3 (MINOR; §5, what m3a_g3_model actually discriminates).** I re-ran the script (byte-identical, §4). Three facts the memo
should state:
- all 11 in-range rows (−1 < δ ≤ 0) are at the single value **δ = −½**, where β′ = α − 1. So within Theorem H's range the test cannot
  distinguish β′ = α + 2δ from any rule agreeing at δ = −½ (e.g. α − 1); the δ-dependence is tested only on the δ = ½, 1 rows, which
  are outside the theorem (phantom nodes);
- the ε_j rows give identical values for H1–H4 (the zeta layer is insensitive to (β, ν) at this order), so only the d₁ and n⁻² rows
  discriminate;
- "H2 (α+2δ, α+2δ) 3 009 tol" is attained on an out-of-range row (p = 0.6, δ = 1, n⁻²); on in-range rows H2 is excluded by 58 tol
  (p = 0.6, δ = −½, n⁻²), H3 by 30 000, H4 by 15 000.
Also, the model's band factor is mp.zeta(−jp, 1+δ) (Remark 3.3's form), not the Fourier sums; that is acceptable for a NUMERICAL test
(the two agree to 10⁻²⁶) but should be said.
*Fix:* append to the m3a_g3_model paragraph of §5: "All in-range rows are at δ = −½ (β′ = α − 1); the ε_j rows do not discriminate
between H1–H4; in-range exclusions: H2 58 tol, H3 30 000, H4 15 000 (the 3 009 for H2 is on the δ = 1 row). The band factor uses
ζ(−jp, 1+δ) (Remark 3.3, NUMERICAL), not the Fourier sums." Optionally, a p < 1 Hurwitz fit at a second in-range δ (e.g. −¼) would
make the δ-dependence testable inside the range (not required for the label: the proof does not rest on it).

**B3-4 (typo; checks/m3a_g3_model.py docstring).** "JZC_M3a_H_G3.md Prop 3.2" does not exist. *Fix:* "JZC_M3a_H_G3.md Cor 5".

**B3-5 (INFO; §5 (C), (F)).** The memo reports |F_in/F_out − 1| ≤ 2.2ε and the (F) deviation ≤ 6·10⁻²⁶; the script asserts ≤ 50ε and
≤ 10⁻¹², respectively. Both assertions are meaningful (a discontinuity would give ~1/ε; a wrong jump ~10⁻²), and the printed values
match the memo. Suggest "(asserted ≤ 50ε)" / "(asserted ≤ 10⁻¹²)" for transparency. No fix needed.

**B3-7 (typo; §5 bounds rounded down).** Parsing m3a_g3_seam.out (stored = re-run), the maxima over the 9 (p, δ) are
|χ_+^δ(10⁻⁶e^{iπp/2})| = 6.3·10⁻⁷, lattice-B deviation 5.4·10⁻²⁴ and the (E) deviation at 0 2.2·10⁻⁹; §5 writes "≤ 6·10⁻⁷",
"≤ 5·10⁻²⁴", "≤ 2·10⁻⁹". *Fix:* "≤ 7·10⁻⁷", "≤ 6·10⁻²⁴", "≤ 3·10⁻⁹". (The other §5 numbers — 2·10⁻²⁴, 2.2ε, 7·10⁻¹⁴, 7·10⁻¹¹,
6·10⁻²⁶ — are upper bounds of the printed values.)

**B3-6 (INFO; m3a_g3_seam's Jpure).** It evaluates ℓ_± as −log((1 − Q) − Q·expm1(−u)), the form that G23plt1 §4's Rule N note found to
lose relative accuracy when q underflows. In G3's (F) check the kernel is bounded near r = 0 (no r^{−k−1} amplification), so the
absolute error stays ≤ 10⁻²⁵ and the check is unaffected. No fix needed.

## 3. JZC_M3a_H_G23plt1.md: re-derivations and findings

### 3.1 Re-derived
- **L2.1′.** Each of the six audited lines checked: plane geometry (|z − X| ≥ sin φ₁·max(|z|, X)); X_k ≥ |z| ⟺ τ_k ≤ T; w(X_k)/X_k = τ_k^γ
  and w(X_k)/|z| = T^pτ_k^{−s}; γ = p − s < 0 for p < 1 < s (one monotone case); tail ≤ T^{−s} + T^{1−s}/(s−1); T^{1+γ} = n^{1+p−s}|z|^α
  (since −(1+p−s)/p = α) and 1 + γ = −pα. The exponent is α, δ-free; p only in 1/sin(πp/8). Confirmed.
- **L2.2′.** Poles: on |arg t| ≤ π/4 the solutions of t − δ ∈ ℤ are real, t = δ + k, k ≥ 1 (the Hurwitz nodes); t = δ − m has arg t = π,
  i.e. arg z = ±πp ∈ S_out. Lip ray: |e^{2iθ_δ}| = e^{2π|t|sin(π/4)} there, so the inverse is super-small; (eq:imtheta) needs only
  πp/4 < πp. Arcs: |t| − Re t = v²/(|t| + Re t) ≤ 1/16 for |v| < ¼, |t| ≥ 1, so dist(u′, ℤ) ≥ 7/16 and |e^{2πi(t−δ)} − 1| =
  2e^{−πv}|sin π(u′+iv)| ≥ 2e^{−π/4}sin(7π/16) = 0.894; for |v| ≥ ¼, ≥ 1 − e^{−π/2} = 0.792. Confirmed; my brute-force minimum over
  δ ∈ {−0.05, …, −0.95}, N ≤ 29, 801 angles is 0.9967, so c_arc = 0.7921 is valid (not sharp). The correction to G12 L2.2's constant
  (the |v| ≥ ¼ case) is right; Paper 2 app_c.tex line 133 indeed says "if |v| ≥ ¼ this is clear".
- **L2.3′.** Pointwise algebra; F_δ is one analytic function across the seams (Paper 2 Lemma seam (iv), quoted correctly: "extends
  analytically across Σ^s_±"). Confirmed.
- **L2.4.** (a) as Paper 2 (O5) near 0 (quote at app_outer.tex 216–219 checked), with κ_δ → 1 off the lens (|arg t| ≥ 3π/16) and j_δ → 0
  (G12 L1.2(b) at φ = π/2, C_J = 1). (b) For |z| ≤ 1: |j_δ| ≤ C|z|^{1/p}/n, |log B_in^δ| ≤ C|z| (|1 + λ_δz| ≥ 1 on S̄_in), corner (ii):
  total ≤ C|z|^{1/2}, derivative ≤ C|z|^{−1/2}, exactly Paper 2's (O3) computation (app_outer.tex 208–212, "Since ν_p = ½, this is
  (O3)", quoted correctly). (c) Lemma szego (vi) for the α-frame weight. Confirmed (see B23-5 for a missing τ₀).
- **L2.5.** Derivative: ρ_δ′ = j_δ′ − (δ+½)/t = ψ(t − δ) − Log t (G12 L1.2(c)), and the 1/ζ coefficients of the elementary terms
  plus ((δ+½)/p)Log ζ sum to (δ+½)/p + ϖ_δ − ½ − δ = 0; so |ζχ_+^δ′(ζ)| → 0. Window: |z − z*| ≤ τ|z| ≤ τr/(1−τ) ≤ r/4 (τ ≤ 1/5);
  off the window |ζ − z| ≥ |ζ − z*|/2 and ||ζ| − r| ≥ (|ζ| + r)/6 when ||ζ| − r| > r/2, giving (|ζ| + r)/12; inside, |ζ − z| ≥ |ζ − z*|
  (orthogonality) bounds the Lipschitz part by sup|χ′|·length; the constant part is |χ_+(z*)| times a log with bounded modulus and
  argument change < π. The opposite seam: angle ≥ πp − arcsin τ ≥ πp/2 and |ζ − z| ≥ sin(angle/2)(|ζ| + |z|). Polynomial bound: in
  S_in, |t| ≤ n(X₁ + δ′)^{−1/p} < a, the zeros δ + ℤ of 1 − e^{∓2πi(t−δ)} keep distance ≥ min(ε_n, |δ|) from the closed half-disc.
  Confirmed. Numerically |ζχ_+^δ′(ζ)| = 3.5·10⁻⁶, 3.5·10⁻¹² at |ζ| = 10⁶, 10¹² (p = 0.45, δ = −0.37; my script).
- **P2.6.** The substitutions are complete: det; (i) column bounds from L2.3′/L2.4/L2.1′/L2.2′ (|arg z| ≥ ¾ϑ_lip > φ₁ off the lens);
  (ii) 4c ∈ Z_n at positive distance from the seams, Lemma normalisation with (O1) for F♮, L2.5 and Prop 4; (iii) seams carry no
  jump. Cor L2 margin: 2(|α|/2 + η) < 1 with η = (1 − |α|)/4. Confirmed.
- **Lemma M.** (M2) from the series, (M3) from ℓ_±′ = e^{±2πiδ}q′/(1 − w) and |1 − w| ≥ 1 − q, (M4) via |Log(1 − w)| ≤
  |ln|1 − w|| + π/2 with s_δ ≤ |1 − w| ≤ 2; s_δ is the distance from 1 to the segment [0, e^{2πiδ}]: |sin 2πδ| if cos 2πδ ≥ 0, else 1.
  Confirmed (random grid of 4000 (δ, q): max |ℓ_+|/ℓ = 1, max |ℓ_+′|/ℓ′ = 1, s_δ formula = brute-force minimum).
- **F.1_δ (i), (ii).** Jump: log B_out^δ + χ_+^δ + j_δ − log B_in^δ = −Log(1 − e^{−2πi(t−δ)}) = −Log(1 − e^{2πiδ}e^{−2π|t|}) = ℓ_+;
  conjugation gives ℓ_− = conj ℓ_+ on Γ₋. Plemelj is linear, ℓ_± real-analytic. The Liouville growth step: −j_δ = (δ+½)ln t + O(1) for
  small t, so O_n(1 + log ρ); |ℓ_±| ≤ ℓ. Each line of the §2.2 table checked against E_plt1.md §3 (quotations exact).
- **F.1_δ (iii).** (1/2πi)[ℓ_+e^{−ikθ} − conj(ℓ_+e^{−ikθ})]r^{−k−1} = (1/π)r^{−k−1}Im(ℓ_+e^{−ikθ}); u = 2πnr^{−1/p} gives
  r^{−k−1}dr = p(2πn)^{−kp}u^{kp−1}du; Fubini with majorant Γ(kp)ζ(1+kp); Im(e^{2πimδ}e^{−iπkp/2}) = −sin(πkp/2 − 2πmδ). So
  m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ), reducing to E_plt1 at δ = 0. Confirmed; also Hurwitz's formula (not quoted) would give
  ζ(−kp, a)/(kn^{kp}) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ), consistent with Remark H.
- **F.1_δ (iv), δ-freeness.** Every estimate of E_plt1's (iv) (far part ∫ℓr^{−K−2}, near part super-smallness of ℓ and ℓ′ on
  [0, 2R₁], window subtraction near the seams, Cauchy estimate, real-axis derivative, continuity at 0) uses the density only through
  |ℓ_±| and |ℓ_±′|, which (M2)–(M3) bound by the δ-free ℓ, ℓ′; n₀ comes from "ℓ ≤ 2e^{−2πn(2R₁)^{−1/p}} ≤ 1" (δ-free). Confirmed.

### 3.2 Findings (G23plt1)

**B23-1 (MINOR; overlap with G3's addendum not recorded).** G23plt1 §0 ("One input was not covered by any written lemma: the bound on
e^{χ_δ} at ∞ next to the seams"), L2.5's "Why Lemma 2.5 is needed" ("G3 Lemma 3 (iii) quotes 'the polynomial bound at ∞' as verbatim
from Paper 2 …"), and Rule A item 7 ("No written lemma covered e^χ next to the seams at ∞ … G3 quotes it") predate G3's addendum
(ii′)/(iii′), added on 2026-10-21 per review A F2, which proves exactly the polynomial bound (|χ_±^δ′| ≤ C_n/|ζ| and the window
argument). L2.5 is a strengthening (χ_δ → 0 uniformly, from |χ_±^δ′| = o(1/|ζ|)); the polynomial bound alone already follows from
G3 (iii′). *Fix:* in §0 replace "One input was not covered by any written lemma: … Lemma 2.5 supplies it" by "One input is new
relative to Paper 2: the bound on e^{χ_δ} at ∞ next to the seams. G3's addendum (ii′)/(iii′) (review A F2) gives the polynomial bound;
Lemma 2.5 re-proves it with the sharper conclusion χ_δ → 0 uniformly in arg z"; make the same change in L2.5's "Why" paragraph
("G3 Lemma 3 (iii) quotes …" → "G3 Lemma 3 (iii′) proves the polynomial bound by the same window argument; L2.5 adds the uniform limit")
and in Rule A item 7. Add G3 (ii′)/(iii′) to L2.5's PROVED-mod-cite line.

**B23-2 (MINOR; §4 [W] wording).** "χ_δ bounded next to the seams on |z| ∈ [1, 10⁵]" is sampled at the four radii 1, 10, 10³, 10⁵
(m3a_g23_apriori.py, variable `mid`). *Fix:* "max|χ_δ| ≤ 0.75 at |z| ∈ {1, 10, 10³, 10⁵} next to the seams".

**B23-3 (MINOR; "What would fail" after P2.6).** "the cancellation of L2.3′ is essential; checked numerically by the control in [A]".
The [A] control asserts that the exponent of the Cauchy sum |U_{j2}(iy)| is min(α, 0) and not min(α + 2δ, 0); that tests L2.1′ (the
sum bound sees α, not β′), not the D_W cancellation of L2.3′ itself (which is algebra). *Fix:* "… essential (it is algebra:
D_W = D_W^{(α)}D_{x^{2δ}}); the numerical control in [A] shows the matching fact on the U side: |U_{j2}| has exponent min(α, 0), not
min(α + 2δ, 0)".

**B23-4 (MINOR; L2.5 constant-part distances).** "end points z* ± (r/2)e^{iθ_seam}, which are at distance in [r/4, 3r/4] from z": the
distances are in [r/2, (√5/4)r] (|z − z*| ≤ r/4, orthogonal to the seam). The stated interval is true but loose; the log bound
(log 3 + π) holds either way. *Fix (optional):* "at distance in [r/2, 0.56r]".

**B23-5 (MINOR; L2.4 (b), corner (ii) needs a τ₀).** L2.4 (b) applies "corner (ii) for χ_δ" on Z_n; corner (ii) is stated for
dist(z, Σ^s_±) ≥ τ₀|z| (app_outer.tex, Lemma corner (ii)). *Fix:* add "(Z_n ⊂ {|arg z| < 3πp/8}, so corner (ii) applies with
τ₀ = sin(πp/8), as in Paper 2's proof of (O3))".

**B23-6 (typo; F.1_δ (iv)).** "the derivative of the left side is ≤ Cn^{−(K+1)p}/η for |z| ≤ R₁ − η" omits E_plt1's "η ∈ (0, 1]".
*Fix:* "for η ∈ (0, 1], |z| ≤ R₁ − η, dist(z, Γ₊ ∪ Γ₋) ≥ η".

**B23-7 (MINOR; Rule C.2 bookkeeping).** F.1_δ (iii) uses DLMF 5.2.1 and 25.2.1 (and Fubini instead of Tonelli) but RH/CITATIONS.md
"(DLMF-zeta, Plan 67)" has no "Also used in: JZC_M3a_H_G23plt1" line (G3 got its lines per review A F9). *Fix:* add under
(DLMF-zeta, Plan 67): "**Also used in: JZC_M3a_H_G23plt1** (Lemma F.1_δ (iii)): 5.2.1 at Re(kp) > 0 after u ↦ mu, and 25.2.1 at
s = 1 + kp (Re s > 1) only as the majorant Σ_m m^{−1−kp} for Fubini and for |S_k(δ)| ≤ ζ(1+kp); 25.4.1 not used."

**B23-8 (typo; check docstrings).** m3a_g23_apriori.py: "(JZC_M3a_H_G23plt1.md §2)" → "§1"; "[W] Lemma 2.6" → "Lemma 2.5";
"the input of Prop 2.4(i)" → "P2.6 (i)". m3a_g23_F1.py: "(JZC_M3a_H_G23plt1.md §3)" → "§2". (Changing a docstring changes the
script hash only; outputs are unaffected.)

**B23-9 (MINOR; numbers in Remark H, Rule A 17 and §4 [E] do not match m3a_g23_F1.out).** Parsing the stored output (= re-run):
the literal (iii)_δ integral vs the Fourier sum, and vs ζ(−kp, 1+δ)/(kn^{kp}), agree to ≤ 1.5·10⁻²⁴ relative (max over 45 values),
not "≤ 4·10⁻²⁶" (§4 [E], twice); Remark H's "≤ 10⁻²⁴" is also slightly low. The d-dropped control's relative mismatch ranges over
0.0100–222, not "0.06–25" (Remark H, Rule A item 17). The assertions themselves (≤ 10⁻²⁰; control > 10⁻³) pass as stated. *Fix:*
§4 [E]: "to ≤ 2·10⁻²⁴ relative" (both places); Remark H: "Agreement to ≤ 2·10⁻²⁴ (relative)"; Remark H and Rule A 17:
"(relative mismatch 0.01–220 for the d-dropped control)".

**I-1 (INFO; scope of δ-uniformity).** F.1_δ (iv) is δ-uniform; L2.1′–P2.6 are fixed-n, fixed-δ (constants through a^{p−s}, λ_δ, s_δ,
1/|sin πδ|), as §1 "What changes" says. Note also that Z_n ⊃ (0, X₁ + δ′) requires e^{c₀} > 1/a = 1/(1 + δ): free for ℓ₁ ≡ 1
(H-d §6 item 6), but c₀ (hence Z_n) depends on δ as δ → −1. Nothing in either memo claims otherwise.

## 4. Checks re-run (Rule R) and my own spot checks

### 4.1 Repo checks re-run
Interpreter `…/scratchpad/venv/bin/python -B` (mpmath, sympy, numpy), run from research/G1/RH/spectral/checks, stdout to
`…/scratchpad/rerun/<name>.out`, then `diff` against the stored .out.

| Script (sha256 prefix of .py) | Result of re-run | vs stored .out | Wall (2 shared cores, under load from other sessions) |
|---|---|---|---|
| m3a_g3_seam.py (5fe55aff422a) | ALL 81 CHECKS PASSED | **byte-identical** (`cmp`; sha256 583f0810…) | 55 min |
| m3a_g3_model.py (576fd1126a5b) | ALL 25 CHECKS PASSED | **byte-identical** (sha256 210310c5…) | 55 min |
| m3a_g23_apriori.py (948c3a40206c) | ALL 132 CHECKS PASSED | **byte-identical** | 103 min |
| m3a_g23_F1.py (baa1ecb3405e) | ALL 398 CHECKS PASSED | **byte-identical** | 89 min |

No differences. I also parsed the stored outputs to check every number quoted in G3 §5 and G23plt1 §4 against them (B3-7, B23-9:
a few quoted bounds are rounded down or misquoted; none affects an assertion). I read all four scripts: every pass/fail value is
computed (Rule N.3), the controls are genuine (they fail by at least 4× their thresholds; the tightest is [A]'s exponent control, 0.4 vs 0.1), and the data read by
m3a_g3_model are the stored Hurwitz fits (Rule X).

### 4.2 Independent spot checks (my code, fresh parameters; `…/scratchpad/reviewB/spot.py`, dps 30–40, n = 5, c = 1)
- λ_δ: the defining form (2π)^{1+δ}/(2|sin πδ|Γ(−δ)) equals Γ(1+δ)(2π)^δ to ≤ 2·10⁻⁴¹ at (p, δ) = (0.45, −0.37), (0.8, −3/7), (0.45, −0.9).
- Density decay: |χ_+^δ(10³⁰e^{iπp/2})| = 3.5·10⁻³⁰, 1.8·10⁻³⁰, 1.2·10⁻²⁹ (O(1/|ζ|)); |χ_+^δ(10⁻⁴e^{iπp/2})|/10⁻⁴ = 0.12, 0.28, 0.34
  (O(|ζ|)); lattice-B density minus (δ/p)Log ζ − c_+ at |ζ| = 10³⁰: ≤ 1.6·10⁻²⁹.
- L2.5's o(1/|ζ|): |ζχ_+^δ′(ζ)| = 3.5·10⁻⁶ → 3.5·10⁻¹² (p = 0.45, δ = −0.37), 1.4·10⁻⁶ → 1.6·10⁻¹² (0.8, −3/7), 1.2·10⁻⁵ → 1.2·10⁻¹¹
  (0.45, −0.9) for |ζ| = 10⁶ → 10¹².
- F.1_δ (iii): literal seam integral with the complex densities vs the Fourier sum (S_k via mpmath polylog, independent of the repo's
  residue-class code) vs ζ(−kp, 1+δ)/(kn^{kp}), k ≤ 3, (p, δ) ∈ {(0.45, −0.37), (0.8, −3/7), (0.2, −0.9)}: relative ≤ 2·10⁻²⁹ for both;
  Im ≤ 10⁻³⁰; |S_k|/ζ(1+kp) ≤ 0.62.
- Lemma M on 4000 random (δ, q): max|ℓ_+|/ℓ = 1, max|ℓ_+′|/ℓ′ = 1; s_δ formula = brute-force min over q (difference ≤ 0).
- L2.2′ arcs: brute-force minimum 0.9967 ≥ c_arc = 0.7921.
- Prop 4 / L2.5 by my own quadrature of (eq. chi) (subtraction on [|z|/3, 3|z|]): |F_δ(z)(−z)^{−δ}(2πn)^{½+δ} − 1| at |z| = 10⁶, 10¹⁰ on
  arg z ∈ {θ_s(1 ∓ 10⁻⁹), θ_s/3, −θ_s(1 − 10⁻⁹), 0.9π}: 5.0·10⁻⁷, 5.0·10⁻¹¹ (p = 0.45, δ = −0.37) and 1.0·10⁻⁵, 1.1·10⁻⁹ (p = 0.8, δ = −3/7),
  identical on all five rays (O(1/|z|), constant (2πn)^{−½−δ} in both sectors and next to the seams). Gluing across Σ^s_+ at |z| = 7,
  ε = 10⁻⁷: |F_in/F_out − 1| = 1.2·10⁻⁷ = O(ε).

## 5. Scope, labels, Rule X, novelty
- Scope covered: G3 Lemmas 1, 2, 3 (incl. (ii′), (iii′)), Prop 4, Cor 5 (H-d (i)–(iii) and the band-factor paragraph), §§5–7;
  G23plt1 L2.1′, L2.2′, L2.3′, L2.4, L2.5, P2.6, Lemma M, Lemma F.1_δ (i)–(iv), Remark H (as NUMERICAL), §2.2 table, §§3–5.
  Not covered: JZC_M3a_H_G1u_plt1.md, Hc.5, G12 itself (only L1.1, L1.2 and the §2 template were read, as inputs).
- Labels: with the fixes, G3 Lemmas 1–2 PROVED + REVIEWED; Lemma 3, Prop 4, Cor 5 PROVED-mod-cite (Paper 2) + REVIEWED; G23plt1 L2.1′,
  L2.2′, Lemma M PROVED + REVIEWED; L2.3′–L2.5, P2.6, F.1_δ PROVED-mod-cite + REVIEWED; Remark H stays NUMERICAL (Hurwitz's formula NOT
  QUOTED). G23plt1's inputs G12 L1.2 (c) and L1.1 are used as stated; their own review status is that of G12 (review A, not re-run
  by me), which the memos already record.
- Rule X: m3a_g3_model reads fits of the actual Hurwitz measures from spec_hur*.out (provenance not re-checked beyond the scripts'
  regexes and the memo); nothing is fitted in the four checks.
- No RH claim is made or needed. Novelty: not assessed.
