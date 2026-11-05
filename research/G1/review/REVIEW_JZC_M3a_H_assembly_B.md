# Rule R review B: Theorem H — G12 (gaps G1–G2, p > 1), the exact checks behind §3.3, and the assembly of JZC_M3a_H.md

Reviewer: independent second reader (Rule R), reviewer **B**. Date: 2026-10-22. Branch plan-e2-d2, HEAD c961b47.
- Targets:
  - **A.** research/G1/RH/spectral/JZC_M3a_H_G12.md; checks/m3a_g12_outer.py/.out, checks/m3a_g12_apriori.py/.out; review A
    (REVIEW_JZC_M3a_H_G12_A.md) and whether its fixes F1–F6 were applied.
  - **B.** checks/m3a_e37_decoupled.py/.out, checks/m3a_g5_exact.py/.out, checks/m4_shift_exact.py/.out (KORD=4, SHI=14, as in
    run_all.sh), and the engine checks/m4_rh_exact2.py (DECOUPLE=1).
  - **C.** research/G1/RH/spectral/JZC_M3a_H.md as an assembly of JZC_M3a_H_Ha.md, JZC_M3a_Hd.md, JZC_M3a_H_G12.md, JZC_M3a_H_G3.md,
    JZC_M3a_H_G23plt1.md, JZC_M3a_H_G1u.md, JZC_M3a_H_G1u_plt1.md, JZC_M3a_H_Hc.md and JZC_M4_proof.md Theorem N.6.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; the targets; REVIEW_JZC_M3a_H_G12_A.md, REVIEW_JZC_M3a_H_pgt1_chain_A.md
  (verdicts, C-1, C-2); JZC_M4.md §7 (decoupled model, Theorem R, Prop S, Conjecture Σ); second_order/checks/check_e3_gauge.py;
  RH/CITATIONS.md (the two "Also used in: JZC_M3a_H_G12" entries).
- I edited no file except this report. I did not commit. My own scripts and outputs are in the session scratchpad
  (`…/scratchpad/revB/rev_e37.py`, `rev_nat.py`, `rev_c15.py` and their `.out`); they are not repo code. Re-run outputs of the repo
  scripts are in `…/scratchpad/rr/`. Python: the session venv (mpmath, sympy), `-B`.
- Machine note: 2 cores, load average 12–14 throughout (other reviewers' jobs), so all wall times below are 10–30× the stored ones.

## Overall verdicts

| Part | Verdict | Findings |
|---|---|---|
| **A.** JZC_M3a_H_G12.md | **ACCEPT** (Rule R satisfied: key steps re-derived, both checks re-run with identical output; review A's fixes correctly applied). Two MINOR text fixes (A-1, A-2), one INFO (A-3). | A-1, A-2, A-3 |
| **B.** exact checks for §3.3 | **ACCEPT WITH FIXES.** All four re-runs reproduce the stored outputs (only timings differ). The assertions test what §3.3 claims, "identically" means exact zero in the field Q(p, α, j, β) (resp. sympy-zero of rational expressions), the controls of m3a_e37_decoupled genuinely fail. Fixes: m4_shift_exact and m3a_g5_exact have **no controls**, and two claims of §3.3 are attributed to the wrong script or overstate what the engine tests. | B-1 … B-5 |
| **C.** assembly JZC_M3a_H.md | **ACCEPT WITH FIXES.** No mathematical inconsistency between the statement of Theorem H and its inputs (hypotheses, β′ = α + 2δ, ν = α, N, μ^δ = 2m_j(δ), ε_j, remainder exponents all check out). There are **stale/contradictory status lines** (one MAJOR-for-bookkeeping: §2 still says H-b′ for p < 1 is OPEN while §4 says it is done; N.6 is used as if REVIEWED), a Setting that omits δ < 0 for p < 1, and the statement (ii) uses ζ(−jp, a) where §3.2 says the theorem uses the Fourier sum. | C-1 … C-12 |

No mathematical error found anywhere. No RH claim is made or needed.

---

## A. JZC_M3a_H_G12.md

### A.1 Re-runs (Rule R)

| script | result | vs stored .out | wall (loaded) |
|---|---|---|---|
| m3a_g12_outer.py | ALL 58 CHECKS PASSED | **byte-identical** | ≈ 50 min |
| m3a_g12_apriori.py | ALL 67 CHECKS PASSED | **byte-identical** | ≈ 95 min |

(Neither script prints a provenance line, so the whole output is compared.)

### A.2 Review A's fixes — applied?

| fix | where | applied correctly? |
|---|---|---|
| F1 ν_p = min(1/p, ½) ≤ 1/p | P1.4(a) | yes, verbatim |
| F2 δ = 0 in P1.4(c) (κ a power of \|z\|; limit via (eq:binet-small)) | P1.4(c), both insertions | yes, verbatim; I re-checked the δ = 0 limit (below) |
| F3 §5 (4) "holds in ℂ_± with principal branches" | G12 §5 and H.md §4 "Corrections" | yes, both places |
| F4 CITATIONS pointers | G12 §0 and RH/CITATIONS.md l. 97 (DLMF §5.11) and l. 506 (DLMF-5.5/5.11, Plan 54) | yes |
| F5(a) delete "·const"; (b) H°_n; (c) radius min(δ_s/2, r_G) | L2.3(ii), P2.4(ii), P2.4(i) | yes, all three |
| F6 s ∈ (1, 1+2p) in H.md Setting | H.md §1 | yes |

### A.3 Independent re-derivations

- **L1.1 (shift identity).** From the definition of j, LnΓ(t−δ) = j(t−δ) + (t−δ−½)ln(t−δ) − (t−δ) + ½ln 2π; subtracting from the definition of
  j_δ gives j_δ(t) − j(t−δ) = (t−δ−½)(ln(t−δ) − ln t) + δ. For −δ ≥ 0, arg(t + |δ|) lies between 0 and arg t, so the difference of principal
  logs has imaginary part in (−π, π) and equals Log(1 − δ/t). Correct. Independent check (rev_c15.py, own code) at the extreme corner
  p = 1.05, |arg t| = π/p (Re t < 0), δ ∈ {−0.001, −½, −0.999}, |t| ∈ [2, 10⁸]: residual ≤ 3.6·10⁻²² at dps 30.
- **L1.2(b) constants.** With w = δ/t and Log(1−w) = −w − w²/2 − R: (t−δ−½)Log(1−w) + δ = δ(1+δ)/(2t) + (δ+½)(w²/2 + R) − tR (the
  O(1) and O(w) terms cancel because tw = δ). |R| ≤ |w|³/(3(1−|w|)) ≤ ⅔|w|³ for |w| ≤ ½. With |δ(1+δ)| ≤ ¼, |δ+½| ≤ ½, |t| ≥ 2 the four
  terms are ≤ 1/(8|t|), 1/(4|t|²) ≤ 1/(8|t|), 1/(3|t|³) ≤ 1/(12|t|), 2/(3|t|²) ≤ 1/(3|t|): total ⅔/|t|. The Binet part:
  |t−δ| ≥ |t| − 1 ≥ |t|/2 ≥ 1 and |arg(t−δ)| ≤ |arg t| ≤ φ, so (eq:binet-bound) gives sec²(φ/2)/(6|t|). Derivative:
  d/dt[(t−δ−½)Log(1−δ/t)] = Log(1−w) + w − δ/(2t(t−δ)) (re-derived), |Log(1−w)+w| ≤ |w|², |δ/(2t(t−δ))| ≤ 1/|t|². All as stated.
  Independent sup|t j_δ| at p = 1.05 on the grid above: 0.251 ≤ C_J = 30.5.
- **C1.5 normalisation constant.** Re-derived from scratch along z = iY in ℂ₊, t = nz^{−1/p} → 0:
  - log κ_δ+ → −Log(1 − e^{2πiδ}) = −ln(2|sin πδ|) − i(π/2 + πδ) (δ < 0: 1 − e^{2πiδ} = 2|sin πδ|e^{i(π/2+πδ)});
  - −j_δ(t) = −(δ+½)(ln n − (1/p)Log z) − LnΓ(−δ) + ½ln 2π + o(1) (L1.2(c));
  - log B_δ = −(𝔟_∞/2π)(Log z − ln 2) + I_r + o(1), using ∫_{−∞}^{−1}[1/(y−z) − 1/(y−1)]dy = Log((1+z)/2);
  - −½Log(4c − z) = −½Log(−z) + o(1); and −δLog(−z) from (−z)^{−δ}.
  The Log z coefficient is (δ+½)/p − 𝔟_∞/2π = ½ + δ (with 𝔟_∞ = 2[(δ+½)π/p − π/2 − πδ], which I re-derived from Im(−(δ+½)Log t₊) =
  (δ+½)π/p and arg(1 − e^{2πiδ}) = π/2 + πδ). Writing Log z = Log(−z) + iπ, the Log(−z) terms cancel and the imaginary constants
  iπ(½+δ) − i(π/2 + πδ) cancel. The real constant is −ln(2|sin πδ|) − LnΓ(−δ) + ½ln 2π − (δ+½)ln n + (𝔟_∞/2π)ln 2 + I_r, and the reflection
  formula at z = −δ, Γ(−δ)Γ(1+δ) = π/|sin πδ|, turns the first two terms into lnΓ(1+δ) − ln 2π. This is the memo's L_δ. At δ = 0,
  κ₊ ∼ 1/(2πit) and −j(t) ∼ ½ln t + ½ln 2π give −½Log t − ½ln 2π − iπ/2, again the same formula.
  *Independent numerics* (rev_c15.py, own code, parameters **not** used by the repo check, which has n = 4 only):

  | (n, p, δ) | L_δ (closed form) | log F♮(iY) − L_δ at Y = 10¹², 10²⁰, 10²⁸ |
  |---|---|---|
  | (7, 2.5, −0.4) | −1.78291062931 | 3.7·10⁻⁴, 2.3·10⁻⁷, 1.5·10⁻¹⁰ (rate Y^{−1/p}: ratio 1585 = 10^{8/2.5}) |
  | (2, 1.2, −0.85) | 1.38252095239 | 1.2·10⁻⁹, 2.7·10⁻¹⁶, 5.8·10⁻²³ |
  | (7, 2.5, −0.05) | −4.41758820038 | same as δ = −0.4 (the leading o(1) term is δ-free) |
  | (3, 1.2, 0) | −1.77520501771 | 1.9·10⁻⁹, 4·10⁻¹⁶, 1.3·10⁻¹⁰ (last: my quadrature, not the formula) |

  So the n-dependence −(δ+½)ln n and the δ = 0 case are confirmed independently.
- **L2.1 (sum bound).** |z − X| ≥ sin φ₁·max(|z|, X) for X > 0, φ₁ ≤ |arg z| ≤ π (distance to the ray, both cases). w(X_k)/X_k = τ_k^{p−s},
  w(X_k)/|z| = T^pτ_k^{−s} with T^p = n^p/|z|, and X_k ≥ |z| ⇔ τ_k ≤ T: this is I₁. Spacing-1 nodes from a: Σ_{a≤τ≤T}f(τ) ≤
  max(f(a), f(T)) + ∫_a^T f for monotone f; Σ_{τ>T}τ^{−s} ≤ T^{−s} + T^{1−s}/(s−1) (first node in (T, T+1]); T^{1+γ} = n^{1+γ}|z|^α since
  −(1+γ)/p = (s−1−p)/p = α. Correct; δ enters only through a^γ, a^{1+γ}/|1+γ| and M_n.
- **L2.3 (column factorisation).** D_W = D_W^{(α)}D_{x^{2δ}} (multiplicativity, W₀^{(β′)} = W₀^{(α)}x^{2δ} on (0, 4c)); D_{x^{2δ}}(∞) = c^δ and
  4cz/Υ → c fix the root; |G| = |z|^{−δ}|z|^{δ}|4c/Υ|^δ; F♮D_W = F_δ(−z)^{−δ}D_W^{(α)}D_{x^{2δ}} = F_δD_W^{(α)}G exactly. Near 4c:
  W/F̃♮² = W₀^{(α)}(−z)^{2δ} = W₀^{(β′)}e^{∓2πiδ} in ℂ_±, hence (F̃♮D_W)² = Wω♮e^{±2πiδ}. All re-derived.
- **P2.4.** Off the lens the columns are ≤ C|z|^{α/2} and ≤ C|z|^{−η}(1 + |z|^α)|z|^{−α/2}; in the lens the first column is
  ≤ C(1 + |z|^{−α}|R_{·2}|)|z|^{α/2}; each is ≤ C|z|^{−|α|/2−2η} for both signs of α. With η = (1−|α|)/4 the exponent is (1+|α|)/4 < ½, so
  |Q♮|² is integrable on Σ near 0 (Cor L2). The bookkeeping of radii (F5(c)) is now right: |G|^{±1} ≤ 2 only on |z| < r_G, the annulus
  is covered by (ii).

### A.4 Findings

**A-1 (MINOR, numerical misquote; G12 §3).** "A and B agree to 6·10⁻⁵¹". The output (stored and re-run) gives 3.72·10⁻⁵⁰ (p = 3/2) and
5.67·10⁻⁵¹ (p = 3). *Fix:* "A and B agree to 4·10⁻⁵⁰".

**A-2 (MINOR, stale; G12 header and §5 "Remains").**
- Header: "Status (2026-10-21): NOT REVIEWED. Rule R needs the second reader to re-run the checks …". *Fix (after this review):*
  "Status (2026-10-22): PROVED-mod-cite + **REVIEWED** (Rule R: review A re-derived and spot-checked; review B
  (research/G1/review/REVIEW_JZC_M3a_H_assembly_B.md §A) re-derived L1.1, L1.2, C1.5, L2.1, L2.3, P2.4 and re-ran both checks with
  identical output)."
- §5 "Remains": "Rule R second reader …; G4 …; G5 (N.6 for M(β′, ν)); the n-uniform hard-edge comparison with Szegő exponent β′ … not
  touched here". G5 is JZC_M3a_H §3.3 and the comparison is JZC_M3a_H_G1u.md / JZC_M3a_H_G1u_plt1.md. *Fix:* replace by "Remains (as of
  2026-10-22): nothing for G1–G2. G3: JZC_M3a_H_G3.md; G4: resolved by the Fourier-sum route (JZC_M3a_H §3.1–3.2); G5: JZC_M3a_H §3.3;
  the n-uniform comparison: JZC_M3a_H_G1u.md (p > 1), JZC_M3a_H_G1u_plt1.md (p < 1) — it is run in the α-frame of L2.3, as anticipated."

**A-3 (INFO; m3a_g12_outer.py).** C1.5 is checked at n = 4 only, so the factor −(δ+½)ln n in L_δ is not exercised by the repo check.
My n = 2, 3, 7 runs (A.3) confirm it. Optionally add one n ≠ 4 case.

**Verdict A: ACCEPT.** With A-1, A-2 applied, G12 meets Rule R (VERIFICATION_POLICY.md: re-derivation + re-run) and may be labelled
PROVED-mod-cite + REVIEWED (its table labels unchanged).

---

## B. The exact computer-algebra checks

### B.1 Re-runs

| script (env) | result | vs stored .out | wall (loaded) |
|---|---|---|---|
| m3a_e37_decoupled.py (sets DECOUPLE=1 KORD=1 EO=3 SHI=10 itself) | ALL IDENTITIES HOLD, ALL 36 CHECKS PASSED (25 identities, 11 controls that fail) | identical except the "(…s)" timing lines; sha256 lines identical (m3a_e37_decoupled.py 7220fc25…, m4_rh_exact2.py 2d18e259…) | 675 s |
| m3a_g5_exact.py (DECOUPLE=1, EO=1, KORD=4, SHI=14 defaults) | ALL IDENTITIES HOLD (16 identities: f₁ = f₃ = 0, f₂, f₄ closed forms; j = 1, 2, 3: lead, N^{−2−jp} = 0, dressing A_j + B_jα², N^{−4−jp} = 0) | identical except the three "(…s)" timing lines; sha256 lines identical (m3a_g5_exact.py 3445d560…, m4_rh_exact2.py 2d18e259…) | 3814 s |
| KORD=4 SHI=14 m4_shift_exact.py | ALL IDENTITIES HOLD (f₁…f₄ β-free, f₁ = f₃ = 0, reflection d₁…d₄) | identical except timing lines; sha256 fb5d9ceb… identical | 645 s |
| m4_rh_exact2.py DECOUPLE=1 | exercised through the three scripts above (it has no standalone .out for DECOUPLE=1; its `__main__` is the coupled JMU run) | — | — |

### B.2 Reading the code against JZC_M3a_H.md §3.3

- **β enters only through ρ² = φ^{2(β+1)} and the soft-edge factor.** In m4_rh_exact2.py the Szegő symbol SZ (= β when DECOUPLE=1)
  occurs in exactly three places: `h2/ih2 = base^{∓(2+2SZ)}` (soft edge, l. 195), `rho2 = (v/2 + √(1+v²/4))^{2(SZ+1)}` (hard edge, l. 218),
  and `delta = SZ/2 + ½` (the natural index, l. 312). The Bessel order `al` occurs only in `bessel_ab` (DLMF 10.17 coefficients). The
  same holds in m4_shift_exact.py (l. 185, 208, 279). So the decoupling is exactly M(β, ν) of JZC_M4 §7. **But this is a property of the
  model as encoded, not something the checks test** (B-3).
- **Natural index.** `inv_n = x/(1 − δx)` with x = 1/N is 1/n for n = N − δ, and `(1 − δx)^{−p}` = (N/n)^p; with δ = SZ/2 + ½ this is
  N = n + (β+1)/2. For the zeta layer `(1 − δx)^{−(mj+1)p}` = (N/n)^{(mj+1)p}: the μ_{n,j} ∝ n^{−jp} factor converted to N^{−jp} plus the
  overall (N/n)^p. I re-derived: μ_{n,j}Σ_k e_kn^{−k} = (n/N)^pε_jN^{−jp}Σ_k g_kN^{−k} ⇔ Σg_kN^{−k} = (N/n)^{(j+1)p}Σe_kn^{−k}. Correct.
- **"Identically".** m3a_g5_exact and m4_shift_exact compare elements of the sympy rational function field K = ℚ(p, α[, j], β) with
  K(0) (`v == ZERO`, `e.has(B)` on the factored expression): exact. m3a_e37_decoupled route 2 also compares field elements (converted
  by `as_expr`, then `simplify(expand(·)) == 0`); route 1 is sympy expressions with √2 from T, decided by `simplify(expand(·)) == 0`.
  A `True` there is a proof of zero; a spurious `False` would make an identity fail (safe) or a **control pass vacuously** (unsafe). I
  therefore evaluated every route-1 control at random rational points (rev_e37.py (4)): all are nonzero (e.g. e − e₀ − pM(0) = 23.7,
  −102, −110.6; shift(ν) residual 28.1, 200, 463; A_r(β) − A_r(ν) 13.9, 37.2, 255; [G(4c), A_r] 33.0, 202, 124), while both identities
  are exactly 0 at the same points. The route-2 controls are field elements, so they are exact. **The controls genuinely fail.**
- **Independent re-derivation of E3.7 for M(β, ν) (link C-2).** The cleanest argument is a renaming, which the check supports but does
  not state:
  1. Engine data (verified exactly, rev_e37.py (2), all entries, all Laurent orders): A_r, B_r equal check_e3_gauge.py's data with
     α ↦ β, and A₀ equals its data with α ↦ ν. (The repo check verifies the lowest Laurent order only for D0[0][0]; I checked every entry:
     lowest orders −2 at 4c and −1 at 0.)
  2. Hard edge: G(0) = I + cM(0)·[[1, i], [i, −1]] (since T[[0,1],[0,0]]T⁻¹ = ½[[1, i], [i, −1]]) and A₀ ∝ [[1, i], [i, −1]], so
     [G(0), A₀] = 0 for **every** ν: it depends only on the shape of A₀. And A₀ contributes nothing to e (its off-diagonal entries are equal).
  3. Soft edge: check_e3_gauge.py's identity e(M) − e(0) = cpM(4c) is a polynomial identity in its symbol α that enters only through A_r;
     renaming α ↦ β gives it for M(β, ν).
  4. e(0) = i((A_r)₂₁ − (A_r)₁₂)/2 = −p(β+1)/2 = d₁ (by hand from A_r).
  So E3.7 holds for M(β, ν), all orders in μ. *Numerical cross-check with an independent implementation* (rev_e37.py (3)): exact gauge
  G = T·expm((M_μ(z)/2)[[0, −(z−4)], [−z, 0]])·T⁻¹ (mpmath expm, no series), residues by the trapezoid rule on circles of radius ½, four
  (p, β, ν) incl. p = 3/5, β = −2.2 and β = −2.1, four μ incl. μ₂ = 1.1, μ₁ = −0.7: |e − e₀ − pM_μ(4)| ≤ 7·10⁻²⁰ (dps 25), |Res₀ − A₀| ≤ 3·10⁻²⁶,
  e₀ = −p(β+1)/2 to 10⁻²⁶; control |e − e₀ − pM_μ(0)| = 0.48–13.2 whenever μ_j ≠ 0 for some j ≥ 2.
- **Prop S / natural form, with controls (rev_nat.py, the engine unmodified, raw d_k and e_k captured).** At KORD = 4, SHI = 14, j = 1,
  re-expanding the raw 1/n coefficients myself:
  - N = n + (β+1)/2: f₁…f₄ β-free, f₁ = f₃ = 0, f₂ = −(3α²p + 6α² − 2p − 2)/24, f₄ = the closed form; zeta layer g₁ = p, g₂ = g₄ = 0,
    g₃/g₁ = (p³ + 4p² + p − 2 + 3α²(p+2)(p² + 2p + 2))/(24p) = A₁ + B₁α² (checked against JZC_M4_proof's A_j, B_j). Reproduces the repo.
  - **Controls:** N = n + (α+1)/2 (Bessel order in the index): f₁ = p(α − β)/2, f₂…f₄ β-dependent, g₂, g₄ ≠ 0, g₃/g₁ β-dependent — all
    identities FAIL. N = n: likewise (f₁ = −p(β+1)/2). Zeta layer with (N/n)^p instead of (N/n)^{(j+1)p}: FAILS.
  - **δ-lattice:** substituting β = α + 2δ (δ a symbol) and N = n + α/2 + ½ + δ: every f_k and g_k is δ-free. This is JZC_M3a_Hd's
    convention β′ = α + 2δ, ν = α, and matches H.md §1 (ii).
  - **Symbolic j** (decoupled, KORD = 4, SHI = 14, field ℚ(p, α, j, β), μ normalised by C(2j, j); 5521 s on the loaded machine):
    with N = n + (β+1)/2, g₁ = jp/2, g₂ = g₄ = 0, and g₃/g₁ is β-free and equals A_j + B_jα² identically in (p, α, j) (sympy simplify of
    the difference = 0, with JZC_M4_proof's A_j, B_j). The same controls fail and the δ-lattice substitution is δ-free. So **the first-order
    zeta layer of M(β, ν) is β-free in its natural form for every j ≥ 1 to N⁻⁴ relative**, not only for j ≤ 3. This is my run, not a repo
    check (see B-1 for adding it).

### B.3 Findings

**B-1 (MINOR, Rule A/N practice; m4_shift_exact.py, m3a_g5_exact.py).** Neither script has a control. A β-freeness test is vacuous if β
did not enter the data, and an index test is only meaningful against a wrong index. (β does enter: d₁ = −p(β+1)/2 and the reflection
identity is nontrivial, so the tests are not vacuous — but the scripts do not show it.) *Fix:* add to m3a_g5_exact.py, after the j-loop,
the controls of rev_nat.py: re-expand with δ_N = (α+1)/2 and with the prefactor (N/n)^p, and assert that f₁ ≠ 0 resp. g₂ ≠ 0 / g₃/g₁
β-dependent (my run: f₁ = p(α − β)/2). Also assert g₁[0] = 0 (the N^{−jp} term), which the script uses implicitly by starting at g₁[1].
Also add the symbolic-j case (`X.run(jmu='sym')`, assert g₁[1] = jp/2, g₁[2] = g₁[4] = 0, g₁[3]/g₁[1] = A(j) + B(j)α² with the
script's own A, B), which my rev_nat.py run shows holds (≈ 1.5 h on a loaded 2-core machine; probably 5–10 min unloaded). That would
make the first-order zeta layer of (ii) exact for all j (see C-9).

**B-2 (MINOR, attribution; H.md §3.3, third bullet).** "integer layer β-free in N = n + (β+1)/2, with f_odd = 0, f₂ and f₄ in closed form,
and the reflection identity of Theorem R, to order 4 (m4_shift_exact.out …)". m4_shift_exact **prints** f₂, f₄ but does not assert them;
the closed forms are asserted in m3a_g5_exact (its first four lines). *Fix:* "… with f_odd = 0 and the reflection identity of Theorem R,
to order 4 (m4_shift_exact.out, ALL IDENTITIES HOLD); f₂, f₄ equal their closed forms at the Bessel order (asserted in m3a_g5_exact.out)."

**B-3 (MINOR, scope of the exact checks; H.md §3.3, first bullet).** "β enters only through ρ² = φ^{2(β+1)} and the soft-edge factor
φ^{−2(β+1)}, both analytic and bounded above and below on the circles." Two points.
- The first half is how the model is **defined** (engine l. 195, 218); the checks verify its consequences, not that the Hurwitz problem
  reduces to it (that is H-d + G1u/G1u_plt1 + Hc).
- "analytic … on the circles" is inaccurate: ρ² and φ^{∓2(β+1)} have a jump where each circle crosses the band (ρ♮₊ρ♮₋ = 1 on the band,
  G1u L1). What is true is that they are bounded above and below, and that the Δ_k^{mod} built from them are meromorphic in the discs
  (N.6b; in the engine, `u_to_w` asserts the parity exactly).
*Fix:* "β enters the model only through ρ² = φ^{2(β+1)} (hard edge) and φ^{−2(β+1)} (soft edge) (definition of M(β, ν), JZC_M4 §7;
m4_rh_exact2 l. 195, 218). Both are bounded above and below on the circles and jump across the band (ρ₊ρ₋ = 1 there); the Δ_k^{mod}
are nonetheless meromorphic in both discs (N.6b; the engine asserts the parity in u_to_w)." The same wording fix applies to
JZC_M3a_Hd.md §7 G5 ("bounded, analytic on the circles").

**B-4 (INFO; m3a_e37_decoupled.py check [1]).** The Laurent-depth check tests `D01[0][0].lo` only, so a deeper pole in another entry at 0
would go unnoticed. I checked all entries (lowest orders −2 at 4c, −1 at 0). *Fix:* use `min(D01[i][j].trim().lo …)` over all entries.

**B-5 (INFO; independence).** m4_shift_exact.py and m4_rh_exact2.py share the μ = 0 code path line for line (diff: only `SZ` vs `be` and the
gauge). The exact results are therefore one implementation; independence comes from (a) check [5] of m3a_e37_decoupled (engine data =
check_e3_gauge.py's hand data at β = ν), (b) the float engine m4_rh4 (m4_shift_num.out, review A's C-2 check) and (c) my contour-integral
check above. Worth one sentence in §3.3.

Also INFO: H.md says "34 s" for m3a_e37_decoupled; the stored output says "total 33s".

**Verdict B: ACCEPT WITH FIXES** (B-1 … B-3 MINOR). With this review, m3a_e37_decoupled (E3.7 for M(β, ν), link C-2) meets Rule R
(re-run + independent re-derivation) and its label can read "PROVED (exact computer algebra) + REVIEWED".

---

## C. Assembly review of JZC_M3a_H.md

### C.1 What is consistent (checked)

- **β′, ν, N.** β′ = α + 2δ = α − 2ζ(0, a) − 1 (ζ(0, a) = ½ − a = −½ − δ); ν = α (Hd §0, G3 Cor 5, G1u, G1u_plt1); lip limit
  e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα}; N = n + (β′+1)/2 = n + α/2 + ½ + δ (Hd §0; engine `delta`; my δ-lattice run).
- **μ^δ_{n,j} = 2m_j(δ).** Matches Hd §0, Hc.2/Hc.3, G1u_plt1 L P5, G23plt1 F.1_δ (iii). m_k(δ) = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ) is n-dependent
  (the "fixed per H-c" remark is right). Hurwitz's formula ζ(1−σ, a) = 2Γ(σ)(2π)^{−σ}Σ cos(πσ/2 − 2πma)/m^σ at σ = 1 + kp gives
  ζ(−kp, a) = −(kp/π)Γ(kp)(2π)^{−kp}S_k(δ) (a = 1 + δ, 2πma ≡ 2πmδ), so Remark 3.3's m_k = ζ(−kp, a)/(kn^{kp}) is the right normalisation.
- **ε_j.** The n⁻¹ response is cpμ_jQ_j(4c) = pc^jjC(2j, j)μ_j/2 (E3.7 for M(β, ν), above); with μ_j = 2m_j this is
  C(2j, j)pc^j·j·m_jn^{jp}·n^{−1−jp}, i.e. ε_j(δ) = C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)) as in §3.2, = C(2j, j)pc^jζ(−jp, a) by Remark 3.3.
- **Remainder of (i).** O(n^{−K−1} + n^{−1−(J+1)p}) from Prop G1u (B) / Prop G1u′ (B); the n^{−2−(B+1)p} term from E3.7 for M(β′, α) and
  |μ^δ_n| = O(n^{−p}) as in N.6's proof (§6 (i)). Same three terms as N.6(i). Consistent.
- **Hypotheses.** −1 < δ ≤ 0, 1 < s < 1 + 2p, p ≠ 1 appear in Ha, G12, G1u, Hc; δ < 0 for p < 1 in G3, G23plt1, G1u_plt1, Hc.5. N.6 needs only
  p ≠ 1, s > 1. δ > 0 excluded (phantom node, Ha), p = 1 not covered.
- **Check counts quoted in §4** (m3a_g1u_hardedge 110/34, m3a_g1u_endtoend 29/8, m3a_g1up_hardedge 157/34, m3a_g1up_endtoend 29/9,
  m3a_g23_apriori 132, m3a_g23_F1 398, m3a_ha_interp 298, m3a_hd_model 42, m3a_g3_model 25, m4_shift_num 108, m4_shift_zeta 40) all match the
  "ALL N CHECKS PASSED" lines of the stored outputs.
- **REVIEWED markers.** H.md marks REVIEWED: Ha (all), Hd (i)–(iii), G1u (p > 1), Hc.1–Hc.4 (p > 1). REVIEW_JZC_M3a_H_pgt1_chain_A.md re-ran
  all seven of their checks (byte-identical) and re-derived the steps, so these satisfy VERIFICATION_POLICY.md Rule R. No other part of
  H.md is marked REVIEWED. (But see C-6 for a wording conflict with that review.)

### C.2 Inconsistencies, with fix text

**C-1 (MAJOR for bookkeeping; §2 table, row H-b′).** "p < 1: OPEN (= H-d (iv) for p < 1; G3 Cor 5 covers H-d (i)–(iii) only …)". §4 item 2
says H-b′ for p < 1 is done in JZC_M3a_H_G23plt1.md §1. The table contradicts §4 and the claim that (i) is PROVED-mod-cite for p < 1.
*Fix:* "p > 1: G12 L2.1–P2.4 (PROVED-mod-cite; REVIEWED after review B); p < 1: JZC_M3a_H_G23plt1.md L2.1′–P2.6 (PROVED-mod-cite,
NOT REVIEWED; this is H-d (iv) for p < 1, which G3 Cor 5 does not cover)".

**C-2 (MINOR; §2 table, row H-e).** Names the hard-edge circle data for p > 1 only. *Fix:* append "; for p < 1 they are
JZC_M3a_H_G1u_plt1.md L P3 (glued parametrix; NOT REVIEWED)". Row H-b similarly: "p > 1: G12 L1.1–C1.5" has no label; add
"(PROVED-mod-cite; REVIEWED after review B)".

**C-3 (MINOR; §1 Setting).** "−1 < δ ≤ 0" without the p < 1 restriction; every p < 1 input assumes −1 < δ < 0. At δ = 0 Theorem H is
Theorem N.6 itself (β′ = α, μ⁰ = μ_n, ε_j(1) = ε_j), so nothing is lost, but the Setting must say how δ = 0, p < 1 is covered.
*Fix:* "−1 < δ ≤ 0, a := 1 + δ, p > 0, p ≠ 1 (for p < 1 the inputs G3, G23plt1, G1u_plt1, Hc.5 assume δ < 0; at δ = 0 Theorem H is
JZC_M4_proof Theorem N.6 for the lattice)".

**C-4 (MINOR, Rule C; §1 (ii) vs §3.2).** (ii) writes "ε_j(a) = C(2j, j)pc^jζ(−jp, a)", while §3.2 says "Theorem H uses … ε_j(δ) :=
C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)) in place of C(2j, j)pc^jζ(−jp, a)", because Hurwitz's formula is NOT QUOTED. As stated, (ii)
depends on an unquoted formula. *Fix (in (ii)):* "ε_j(δ) := C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)) (§3.2); = C(2j, j)pc^jζ(−jp, a)
by Remark 3.3 (classical; NOT QUOTED under Rule C; NUMERICAL to 10⁻²⁷)". Likewise in §1's μ^δ bullet append "(NUMERICAL; NOT QUOTED)"
after "Remark 3.3".

**C-5 (MINOR; §3.2).** "This needs only DLMF 5.2.1, DLMF 25.2.1, and absolute convergence; the Fubini bound is that of E3 Lemma F.1′."
For p > 1 the Mellin step is DLMF 5.9.1 (complex constant, as the bullet above it and Hc.2 say), and for p < 1 the Fubini bound is
E_plt1 Lemma F.1 / G23plt1 F.1_δ. *Fix:* "This needs only DLMF 5.2.1 (p < 1) or 5.9.1 (p > 1), DLMF 25.2.1, and absolute convergence;
the Fubini bound is that of E3 Lemma F.1′ (p > 1; Hc.2) or E_plt1 Lemma F.1 with complex densities (p < 1; G23plt1 F.1_δ)."

**C-6 (MINOR, status wording; header and §4 "Rule R reviews").** H.md says review A of the p > 1 chain "makes H-a, H-d (i)–(iii), G1u (p > 1)
and H-c (p > 1) REVIEWED". That review itself ends: "Under Rule R the labels can become 'PROVED-mod-cite + REVIEWED (reviewer A)' once the
fixes are applied and a second reader re-runs the checks. Per JZC_M3a_H.md §4's own convention, that second reader is still pending."
Under VERIFICATION_POLICY.md (Rule R and the REVIEWED row) a reader who re-derives and re-runs **is** the second reader, and review A did
both, so the REVIEWED markers are policy-compliant — but H.md should not silently contradict its source. Meanwhile JZC_M4_proof.md, whose
review A also re-ran its exact checks, still says "A second reader is pending before REVIEWED". The repo applies two standards.
*Fix (H.md §4, after "…within the scope the review covered"):* "(Review A's last paragraph anticipated a further reader. Under
VERIFICATION_POLICY.md Rule R, a reader who re-derives the key steps and re-runs the checks suffices, and review A did both; the REVIEWED
markers rest on that. JZC_M4_proof.md is held to the stricter reading: see C-7.)" A human should decide which reading the repo uses and
make JZC_M4_proof.md and the H chain consistent.

**C-7 (MINOR, status of an input; header, §2 row H-e, §4 "(i)").** Theorem N.6 (and Lemmas N.6a–c, E3.7 as used in N.6's proof) is an
input of (i) for all p, but H.md never gives its status. JZC_M4_proof.md: "PROVED-mod-cite … Rule R review A done … A second reader is
pending before REVIEWED." The §4 sentence "With C-1 and C-2 closed … its remaining unreviewed links are G12 (H-b, H-b′) and
m3a_e37_decoupled" therefore omits N.6. *Fix:* replace that clause by "its remaining links not marked REVIEWED are JZC_M4_proof Theorem
N.6 / Lemmas N.6a–c (PROVED-mod-cite; Rule R review A done, second reader pending) — G12 and m3a_e37_decoupled are REVIEWED by review B
(REVIEW_JZC_M3a_H_assembly_B.md)". And in the header list "…G12, G3, G23plt1 and the new check m3a_e37_decoupled are not" →
"G3, G23plt1, G1u_plt1, Hc.5 and G1u's p < 1 paragraph are not; G12 and m3a_e37_decoupled are REVIEWED by review B; Theorem N.6 is
PROVED-mod-cite with review A done (second reader pending)".

**C-8 (MINOR, misstatement; §4 "Status by part", (i)).** "Every other ingredient is PROVED-mod-cite (Paper 2, E-series lemmas) and NOT
REVIEWED." The E-series lemmas used (E_pgt1 L E.2, E3 L F.1′, E3.4, E3.5, E3.7, E_plt1 L F.1, E′.3) are REVIEWED (JZC_M4_proof table,
Hc table); Paper 2 is cited, not reviewed here. *Fix:* "Every other ingredient keeps its own label: Paper 2 results are cited (Rule C,
quoted in the memos); the E-series lemmas are REVIEWED; JZC_M4_proof N.6a–c and Theorem N.6 are PROVED-mod-cite (review A done, second
reader pending)."

**C-9 (MINOR, (ii) scope).** (ii)'s display ends in "+ …", and the text says exactness covers "the integer layer to N⁻⁴ and the
first-order zeta layer with its N⁻²-relative dressing, j ≤ 3". Two clarifications are needed so (ii) does not overclaim:
- the first-order zeta layer is exact for **j ≤ 3 only** (m3a_g5_exact); for j ≥ 4 the β-free form ε_jN^{−1−jp}(1 + g_jN⁻²) in the
  display is CONDITIONAL on Σ (NUMERICAL for j = 1, 2 in m4_shift_zeta) **as the repo stands**. My symbolic-j run (B.2) shows it holds
  exactly for every j to N⁻⁴ relative; once that is a repo check (B-1), the restriction j ≤ 3 can be dropped.
- the "…" contains f₆N⁻⁶ (NUMERICAL, m4_shift_num) and the second-order ε₁²N^{−2−2p}(3p+1)/(2p) layer, whose β-independence in the
  natural form is **not** checked for M(β, ν) at all (m4_shift_zeta is first order; N.6d's μ₁² layer is at β = ν). For p < 2/3 the ε₁²
  term is larger than f₄N⁻⁴.
*Fix (end of (ii)):* "The terms shown are exact (Prop S at exact orders) for f₂, f₄ and for ε_jN^{−1−jp}(1 + g_jN⁻²) with j ≤ 3
(every j once a symbolic-j decoupled check is added, REVIEW_JZC_M3a_H_assembly_B B-1); for larger j, for f₆ and for the second-order layer ε₁²N^{−2−2p}(3p+1)/(2p) + … of N.6(iii), the natural form in N is
CONDITIONAL on Conjecture Σ."

**C-10 (typo; §4 item 1, Prop G1u (B) bullet).** "It is uses H-a and item 5" → "It uses H-a and item 5".

**C-11 (INFO, stale inputs that H.md cites).**
- JZC_M3a_H_G1u_plt1.md §4: "G1u L1–L4 (PROVED-mod-cite, NOT REVIEWED)", "H-a (JZC_M3a_H_Ha.md, NOT REVIEWED)", "For p > 1, (i) rests on
  H-c (JZC_M3a_H_Hc.md Cor Hc.4, in progress)", and the Prop G1u′ table row "(inputs §4: H-a, G3, G23plt1, all NOT REVIEWED)". G1u (p > 1),
  H-a and Hc (p > 1) are REVIEWED and Hc.4 is done. *Fix:* update those four phrases accordingly.
- JZC_M3a_Hd.md §5 and §7: "the μ-layers (m4_shift_zeta.out, NUMERICAL)" — the first-order zeta layer j ≤ 3 is now exact
  (m3a_g5_exact). *Fix:* "… plus the μ-layers (first order, j ≤ 3: exact, m3a_g5_exact; otherwise NUMERICAL, m4_shift_zeta.out)".
- JZC_M4.md §7: Prop S's heading says "exact computer algebra to order 6", and Theorem R's line says "m4_shift_exact.out … orders ≤ 6";
  the stored run reports orders ≤ 4 (H.md §3.3 states this correctly). *Fix (JZC_M4.md):* "to order 4 (an order-6 run did not finish)".

**C-12 (INFO).** §3.3's E3.7 paragraph: "Label: … NOT REVIEWED (new check)" and §4's "(NOT REVIEWED: the new check awaits a second
reader)" become "REVIEWED (review B: re-run, controls verified nonzero at random points, independent derivation by renaming α ↦ β in
check_e3_gauge.py's identity plus an independent contour-integral check)".

**Verdict C: ACCEPT WITH FIXES.** Theorem H (i), (ii) as stated are consistent with their inputs: the hypotheses, β′ = α + 2δ, ν = α,
N = n + (β′+1)/2, μ^δ_{n,j} = 2m_j(δ), ε_j and the three remainder terms all match. The fixes are to status lines (C-1, C-2, C-6, C-7, C-8,
C-12), the Setting (C-3), Rule C hygiene in (ii) (C-4, C-5), and the scope of (ii)'s exactness (C-9). With them applied, the honest
label of (i) is: PROVED-mod-cite for p ≠ 1; for p > 1 every memo-level link is REVIEWED except Theorem N.6 (review A done, second
reader pending); for p < 1 G3, G23plt1, G1u_plt1, Hc.5 are NOT REVIEWED.

## Reproducibility (reviewer's commands)
- `cd research/G1/RH/spectral/checks; $PY -B m3a_g12_outer.py`, `$PY -B m3a_g12_apriori.py`, `$PY -B m3a_e37_decoupled.py`,
  `$PY -B m3a_g5_exact.py`, `KORD=4 SHI=14 $PY -B m4_shift_exact.py`; outputs diffed against the stored .out.
- `…/scratchpad/revB/rev_e37.py` (engine data vs check_e3_gauge data; contour-integral E3.7; controls at random rationals),
  `JM=1 …/rev_nat.py` and `JM=sym …/rev_nat.py` (natural-index identities, controls, δ-lattice), `…/rev_c15.py` (C1.5 at n = 2, 3, 7;
  L1.1/L1.2 corner).

Novelty: not assessed (outside remit). No RH claim is made or needed.
