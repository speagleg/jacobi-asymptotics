# REVIEW_RHzeta: Rule R second reading of RH_zeta.md (Plan 13, smooth-ζ model), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus), on branch plan-13-smooth-zeta (HEAD 0c50b6d). It edited no
  repo file except this one.
- **Read:**
  - RH_zeta.md in full, and the Plan 13 file;
  - RH_px.md §§3–5 and REVIEW_RHpx.md;
  - G2 PROOF.md (B*, B0, (P), Optimality);
  - CITATIONS.md;
  - all of zeta/checks/*.py and *.out;
  - WLXZ v1 (1410.3948.txt): (3.2)–(3.9), (4.13)–(4.27), (5.5)–(5.12), §6.1.
- **Probes** (session scratchpad `zrev/`; not committed, because this review may edit only its own file). Each is a
  small patch of check_z_e2e.py or a short script, described precisely below so it can be re-created:
  - `e2e_xi4.py`: the **absolute** end-to-end test, with Ξ included, no free constant, and the A(u) bug fixed (F2);
  - `xi.py`: the size of the omitted far-field scalar Ξ near the band;
  - `tcurve2.py`: the saddle level curve of t;
  - a κ-convergence script;
  - a hard-edge weight script;
  - the gauge test t_c = ½.
  - Re-runs: `MODEL=zeta check_z_e2e.py 10,20` and `MODEL=pp2 … 10,20` reproduce the committed .out files digit for
    digit. `check_px_e2e.py 2 2 40` reproduces the pp2 validation (P5).

**Verdict: ACCEPT WITH FIXES (Phases 1–2). §4 stays a PROOF SKETCH, with one newly identified major gap (F1).**
- **The headline holds.** I re-ran the end to end with the far-field scalar Ξ actually built (Lemma Z's construction),
  with no free normalization constant, and with the A(u) bug of F2 fixed. It gives
  **|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}| = O(1/N)** at all 7 points, with N·err stable to ±10% over N = 10, 20, 40 (P1).
  - This validates, as a package:
    - Lemma E1's μ_N;
    - ℓ;
    - the α-shift K = (β̂ − z)^{−1/8};
    - the continued D̃ and B;
    - F_out, Ξ and the normalization at ∞.
  - It is a strictly stronger test than the doc's, which is blind to constant diagonal factors.
- **The α-shift is right.** α_W = 5/8 matches WLXZ (3.7) and (4.19)–(4.20) exactly. Without it, Lemma Z's ratio jumps
  by exactly the missing phase 3π/4 at x_m, and the absolute test fails at O(1) (P3).
- **Problems found:**
  - **F1 (major, §4.3):** the hard edge is *not* RH_px §4.1 verbatim. The band weight carries an unbounded factor
    log(1/x) at 0. h_N is not Hölder, and the continued weight has a non-constant O(1/log N) jump on (−δ, 0).
    - So px Lemmas 4.2(iii) and 4.3 fail as stated.
    - A repair is sketched, and heuristically the effect is o(1/N).
  - **F2 (moderate, a probe bug):** check_z_e2e's A(u) is wrong, even negative, for u beyond about x(2), because its
    quadrature breakpoints are unsorted. The doc's normalized test is blind to the resulting error (F3), so the
    conclusion survives. But the N = 40 row of the table must be regenerated.
  - **F5 (moderate):** the cut t = 3/8 is a *gauge*, not canonical. E4's coefficient 0.27 depends on it (t_c = ½ gives
    0.43, P4).
  - F6 is a wrong closed form for κ; the numerical value is right.
  - The rest are minor.

| Item | Verdict | Findings |
|---|---|---|
| §0 model, t, x_e, Lambert-W inverse | ACCEPT | — (t(x_e) = 3/8, t(4) = 11/8, W₀ branch ⇔ t ≥ 3/8 re-derived) |
| Lemma E1 (i)–(iv), incl. strictness | ACCEPT | F5 (gauge wording); F8 (hypothesis check) |
| Cor. E2 | ACCEPT | — (re-derived; check [0] agrees to 11 digits) |
| Cor. E3 + hypotheses for σ_ζ | ACCEPT WITH FIX | F8 (the monotonicity argument as written is insufficient; the formula fixes it) |
| Prop. E4 | ACCEPT (NUMERICAL) | **F5** (the 0.27 is convention-dependent) |
| Prop. E5 | ACCEPT WITH FIX | **F6** (closed-form typo; weak convergence evidence, now replaced by a 5-digit fit) |
| §2 design note | SUPERSEDE | F7 |
| §3(a) α-shift | ACCEPT | verified against WLXZ; P3 control |
| §3(b) continued D̃ | ACCEPT | — |
| §3 probe and table | ACCEPT WITH FIX | **F2** (bug), **F3** (test blind to constant diagonals; Ξ not invisible) |
| §4.1 transformations, bounded support | ACCEPT | — (T = I + O(1/z), and V → I confirmed by P1) |
| §4.2 F_in/F_out, Lemma Z | ACCEPT WITH FIX (sketch) | **F4** (B_r endpoint, Ξ sign, saddle curve, growth of log-ratio) |
| §4.3 hard edge | **GAP** | **F1** |
| §4.3 soft edge, top end | ACCEPT (sketch) | — |
| §4.4 extraction | ACCEPT | — ((N₁)₁₂(N₁)₂₁ = (β̂/4)², a = β̂/2, Szegő-invariant) |
| Labels / status lines | FIX | F9 |

## What was verified (and holds)

**Lemma E1.**
- **Abel pair.** A(u) = ∫_u^{x_e} f(x)(x − u)^{−1/2}dx with f = √xρ. The inversion is πf(x) = ∫_x^{x_e}(−A′)(u − x)^{−1/2}du,
  which is valid because A(x_e) = 0. It is the derivative form minus the boundary term A(x_e)(x_e − x)^{−1/2}.
- **(i).** With ω_{[0,b]} = dx/(π√(x(b − x))) and τ = A(u), dτ = −A′du, one gets
  ψ(x) = (πx^{1/2})^{−1}∫_{max(x,β)}^{x_e}(−A′)(u − x)^{−1/2}du. So ψ = ρ on [β, x_e]. On (0, β), the missing piece
  over (x, β) is strictly positive, because −A′ > 0. The mass is ∫₀¹dτ = 1.
- **A strictly decreasing.** Write A(u) = ∫₀^{x_e−u}f(u + v)v^{−1/2}dv. The integrand decreases in u, and so does
  the range. Also A(0⁺) = ∫ρ = ∞.
  - Note that A(x_e⁻) = 0 needs only bounded f near x_e. Linear vanishing of ρ is sufficient but not necessary (F5).
- **(iii).** The Stieltjes transform of ω_{[0,b]} is 1/√(z(z − b)). Its boundary value is purely imaginary on (0, b)
  and positive for x > b. So Re g′(x) = ∫_{β(τ)<x}dτ/√(x(x − β(τ))) > 0. The integrand is integrable at β(τ) → x
  because A′ ≠ 0. U^μ is strictly increasing on (β, ∞), so U^μ > ℓ/2 on (β, x_e].
- **(iv).** I(ν) = I(μ) + 2∫(U^μ − ℓ/2)d(ν − μ) + I(ν − μ):
  - the middle term is ≤ 0 (= 0 on the band; on (β, x_e], ν − μ ≤ 0 and U^μ > ℓ/2; both measures vanish beyond x_e);
  - the last term is ≤ 0 by (P).
  - So G2's argument does carry over.
- **Sign conventions.** U^μ = ∫log|x − y| (= −V^μ). In those terms the conditions are the Dragnev–Saff ones:
  equality on the band, V ≤ F on the saturated set.

**E2, E3.**
- E2: β^{1/p} = (1/p)B(1/p, ½) = √πΓ(1 + 1/p)/Γ(1/p + ½) = π/(2I(p)).
- E3: substituting x = x(s), |t′|dx = ds, gives (1/N)∫_{3/8}^T(1 − β/x(s))^{−1/2}ds.
- For σ_ζ: √x|t′| = log(γ/2π)(γ² + ¼)^{3/2}/(4πγ), which is increasing in γ > 2π, so √xρ_N is decreasing in x (F8).

**E5 derivation.**
- x(T)/x(Tu) = u^{2−ε}(1 + o(1)) gives T_N·J(2 − ε) ~ N, and β_N/x_N = J(2 − ε)^{2−ε}.
- J(p) = (1/p)B(1/p, ½) = √πΓ(1 + 1/p)/Γ(1/p + ½), and J(2) = π/2.
- (log J)′(p) = −p^{−2}[ψ(1 + 1/p) − ψ(1/p + ½)]. At p = 2 this is −(1 − log 2)/2, since ψ(3/2) − ψ(1) = 2 − 2log 2.
- d/dp[p log J] at p = 2 is log(π/2) − (1 − log 2) = 0.14473.
- With ε ≈ 2/log N, κ = −2·0.14473 = **−0.28946** (the sign is right). The printed closed form is not (F6).

**WLXZ α-dependence (scrutiny item 3).**
- **Nodes.** WLXZ (3.7) has θ = nπ/z² − πα, with nodes n/X_k² = k + α, k ≥ 0. Their constraint mass beyond z is n/z²
  (the jump e^{2nπi/z²} of (4.20)), i.e. (node index from 0) + α.
- **Ours.** The mass beyond x is t − 3/8 = (j − 1) + 5/8. So **α_W = 5/8** is correct.
- **K.** On (β̂, ∞), K₊/K₋ = e^{−2πiκ}, and D₊/D₋ = −e^{2iθ}. T's jump is e^{−2πi(t − 3/8)σ₃}, so we need
  −e^{−2πiκ}e^{−3πi/4} = 1, i.e. κ ≡ −1/8 (mod 1). That is ½ − α_W, as in E = (4 − z²)^{1/2−α}.
- **w₀ and the soft edge.** w₀ ∝ (β̂ − x)^{1/4} = (β̂ − x)^{2α_W−1}, as in WLXZ (5.9). The soft-edge local behaviour
  (z − β̂)^{−σ₃/8} = (z − β̂)^{(1/2−α_W)σ₃} matches (5.7).
- **Should D̃ take WLXZ's α-form (4.15)? No, and it does not matter.**
  - (4.15) is √(2π)(τ + α − 1)^{τ−1/2}e^{−(τ+α−1)}/Γ(τ), with τ = t. It differs from the doc's Stirling D̃(t) by a
    factor 1 + O(1/t) that is analytic and zero-free where it is used.
  - Both satisfy D̃ = D(1 − e^{∓2iθ}).
  - In WLXZ the base n/z² vanishes at their far end z = ∞, which is why their D and E have compensating powers there
    ((4.18)). For us the analogous base t − 3/8 has a *double* zero at x_e. The (4.15) form would put a branch point
    (z − X_e)^{−1/4} at X_e.
  - The doc's D̃ is regular at X_e, and F_out takes over the far end. This is the better choice.

**§4.1 and §4.4.**
- supp μ_N ⊂ [0, x_e] is bounded, so g = log z + O(1/z) and T = I + O(1/z).
- F_out → 1, and Ξ → 1 at ∞. So V → I and no F_∞ (px F3) is needed. P1 confirms this with no free constant.
- (N₁)₁₂(N₁)₂₁ = (β̂/4)² and a(N) = β̂/2 follow from REVIEW_RHpx's hand expansion with 4c ↦ β̂. Both are invariant
  under the Szegő conjugation (diagonal 1/z terms cancel in a(·) and do not enter the off-diagonal product).
- The far field enters b_N only through R, at O(1/N).

**Numbers.** Every number in §§0–3 matches its .out file. The e2e true side is exact:
- the e2e b_N/(β_N/4) − 1 = 0.0280018, 0.0139461, 0.0069665 (N = 10, 20, 40) equals the toolkit's smooth_zeta(J) value
  to 7 digits for J = 2·10⁵ and 8·10⁵;
- so the "60N exact + EM tail" construction is adequate (scrutiny item 4c).

## Probe results

### P1. Absolute end-to-end test, with Ξ included (the decisive probe)

**Construction** (`e2e_xi4.py` = check_z_e2e.py plus five changes):
1. **A(u) fixed** (F2): breakpoints [0, 0.1vmax, 0.5vmax, 0.9vmax, vmax].
2. **u-panels** refined near β: extra breakpoints β·{1.0001, 1.001, 1.01, 1.05, 1.1, 1.2, 1.5, 2, 3, 5, 8, 12, 20, 35,
   60, 100}, with 16-point Gauss–Legendre.
3. **B** with 16 GL points per half-unit in u = log|y|.
4. **Ξ built as in Lemma Z:**
   - C is the circle through −r = x_cross/2 and x_m = (X₁ + X_e)/2, where x_cross = −s/(4π²e² − ¼);
   - log(F_out/F_in) is sampled at 400 midpoint angles and unwrapped continuously;
   - F_out = exp(∫_{β̂}^{X_e}(t − 3/8)dy/(y − z)), and F_in = D·B·K, with B the *full-axis* continued B of §3(b);
   - log Ξ is the trapezoid Cauchy integral;
   - then F := F_in·Ξ, and log w₀ gets −2log Ξ before the Szegő function and D_∞ are built.
5. **The test** is the absolute one, with no reference point: max over the four entries of
   |D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}|.

**N × error**, at the 7 points of the doc:

| N | 1.2+i | 0.5+0.8i | −1+0.5i | −1.5+0.5i | 2.5i | 3−1.2i | 4.5+1.5i |
|---|---|---|---|---|---|---|---|
| 10 | 0.228 | 0.178 | 0.070 | 0.066 | 0.093 | 0.281 | 0.141 |
| 20 | 0.234 | 0.181 | 0.078 | 0.073 | 0.100 | 0.311 | 0.154 |
| 40 | 0.239 | 0.183 | 0.084 | 0.078 | 0.105 | 0.337 | 0.166 |

- Clean O(1/N). The diagonal of VN^{−1} − I is of the same small size, so the "constant" of the doc's test is I.
- Insensitive to the number of C nodes (200 vs 800) and to a finer F_out quadrature (identical to 4 digits).
- **Without the F2 fix, N = 40 shows a z-independent offset VN^{−1} ≈ e^{−0.019σ₃}** (N·err ≈ 0.77 at every point).
  With a finer u-grid alone the offset flips sign (+0.008). It disappears only when A(u) is fixed. This is the F2/F3
  failure mode in action.

### P2. Size of the omitted far-field scalar (`xi.py`)

log Ξ(z) − log Ξ(0), with Ξ built as in P1:

| N | sup_C abs(log(F_out/F_in)) | at 1.2+i | at −1.5+0.5i | at 4.5+1.5i |
|---|---|---|---|---|
| 20 | 3.82 | 0.0049 | 0.0048 | 0.0154 |
| 40 | 5.52 | 0.0019 | 0.0019 | 0.0059 |
| 80 | 7.14 | 0.00072 | 0.00072 | 0.0022 |

- The decay per doubling is ≈ 2.6, consistent with O(log^k N/N²). So Ξ is asymptotically negligible, as Lemma Z says.
- But at N ≤ 40 it is **the same size as the doc's diagonal-ratio entries**. For example, at N = 20 and z = 4.5 + 1.5i,
  abs(log Ξ(z) − log Ξ(z₀)) ≈ 0.011, against the reported |M₁₁/M₁₁(z₀) − 1| = 0.0107.
- So the claim "invisible at this accuracy" is false (F3). It does not change the conclusion.

### P3. No-α control

Take κ = −½ (the px exponent) with t_c = 3/8, with Ξ:
- the closure jump of log(F_out/F_in) around C is **2.34i ≈ 3π/4·i**, the uncancelled constant phase;
- Lemma Z's hypothesis fails exactly there;
- N·err = 15–28 (N = 10) and 49–83 (N = 20).

This confirms both the α-shift and that Lemma Z's continuity at x_m *is* the α-shift condition.

### P4. Gauge test: t_c = ½ instead of 3/8 (`TMIN=0.5`, K ≡ 1, constraint on (0, x(½)])

- **Absolute test with Ξ:**
  - N = 10: N·err = 0.32, 0.24, 0.11, 0.10, 0.13, 0.36, 0.18;
  - N = 20: N·err = 0.33, 0.25, 0.12, 0.11, 0.14, 0.40, 0.20.
  - The relative test is also O(1/N).
- **b_N/(β_N^{(t_c=½)}/4) − 1** = 0.0429, 0.0219, i.e. N·dev ≈ 0.43–0.44, against 0.28 for t_c = 3/8.
- So the cut point is a gauge: (t_c, α_W = 1 − t_c, K = (β̂ − z)^{t_c−1/2}) all work (F5).

### P5. pp2 validation

`check_px_e2e.py 2 2 40` (the absolute, ∞-normalized RH_px probe) gives N·err = 0.37671, 0.28626, 0.18563, 0.19314,
0.32217, 0.64074. pp2's relative test gives 0.3768, 0.2861, 0.1856, 0.1932, 0.3219, 0.6421. They agree to 3–4 digits,
as the doc claims. No committed .out exists for (p, s) = (2, 2) (F9).

### P6. E5 convergence (edge equation only, N up to 10⁶⁰)

- log N·(β_N/(4x_Nc₂) − 1) = −0.3588 (10⁴), −0.3307 (10¹⁰), −0.3144 (10²⁰), −0.3076 (10³⁰), −0.3039 (10⁴⁰), −0.2999 (10⁶⁰).
- The correct secondary model is a + b·log log N/log N + c/log N, because ε(T) = 2/log T·(1 + O(log log/log)). Fitted
  on 10³⁰, 10⁴⁰ and 10⁶⁰ it gives **a = −0.289472**, against κ = −0.289460 (agreement 1.2·10⁻⁵).
- Also, J(2 − ε)^{2−ε}/(4c₂) − 1 with the *exact local* ε(N) tracks the measured value to 0.002 at 10⁴⁰.
- ε·log N/2 = 1.25 at N = 10⁴, so "κ/log N" is a poor description at reachable n. The doc says so.

### P7. Hard-edge weight

- **Jump on (−δ, 0).** W(z) ∝ z·dt/dz is the band weight up to constants. A pure z^{−1/2} would give W₊/W₋ = −1. The
  computed ratio is:

  | N | x = 10⁻¹ | x = 10⁻³ | x = 10⁻⁶ |
  |---|---|---|---|
  | 20 | −0.69 + 0.72i | −0.87 + 0.49i | −0.95 + 0.32i |
  | 10⁶ | −0.97 + 0.25i | −0.98 + 0.21i | −0.99 + 0.17i |

  The deviation is ≈ π/Λ, with Λ = log(γ/2π) ~ log N.
- **h_N := abs(W)x^{1/2}/abs(W(1))** is unbounded at 0. For N = 1000:

  | x | 10⁻¹ | 10⁻³ | 10⁻⁶ | 10⁻¹² |
  |---|---|---|---|---|
  | h_N | 1.21 | 1.64 | 2.27 | 3.55 |

  At the Bessel scale x ~ N^{−2}, h_N ≈ 2.3: an O(1) variation inside the disc.

### P8. Saddle level curve of t (`tcurve2.py`)

- t′(x_e) = 0, so the level set Im t = 0 has a second branch leaving x_e vertically into ℂ±.
- Traced through t = 3/8 → 0 → −1 → −2, it ends at the t-axis crossing x_cross (t = −2.89).
  - At t = 0, −1, −2, D has poles: 1 − e^{∓2πit} = 0.
  - There D̃'s principal log t is cut.
- In x-units the curve stays **outside** C, with abs(z − c₀)/R ≥ 1.21. Inside C, max abs(arg t) = 2.77 < π (grid
  scan). C is N-independent in x-units, so this holds for all N.

## Findings

**F1 (MAJOR; blocks the §4 theorem): the hard edge has a logarithmic weight, so "RH_px §4.1 verbatim" is false.**
- **The weight.** The band weight is W = 2iθ′w, with w = 2z and θ′ = πt′:

    abs(W) = 4πabs(t′)z = log(γ/2π)·√s·z^{−1/2},  log(γ/2π) = ½log(s/z) − log 2π.

  So w₀ = C_N z^{−1/2}(β̂ − z)^{1/4}h_N, with h_N ∝ 1 + log(1/z)/(log s − 2log 2π). This h_N is **unbounded at 0**
  (P7). The doc says "h_N is Hölder at 0" and "log h_N Hölder with exponent ½ − ε". Both are false. log h_N ~ log log(1/z).
- **The jump on (−δ, 0).** The continuation of W across (−δ, 0) has jump −(Λ − iπ/2)/(Λ + iπ/2), not the constant −1
  (P7). So:
  - **(a)** RH_px Lemma 4.2(iii) (Ẽ_N = analytic + O(e^{−cN})) fails: Ẽ_N's (h2) jump on (−δ, 0) is O(1/log N), not
    super-small;
  - **(b)** Lemma 4.3 (mismatch ≤ C_K N^{−K}) fails. With any W̃ for which W̃₊W̃₋ = w₀ holds exactly, the lip entries
    of V and P₀ differ by e^{2Nφ}(1/W − e^{±iπα_x}/W̃²) = e^{2Nφ}O(1/(W log N)).
- **Why the numerics are still clean.**
  - The mismatch is localized by e^{2Nφ} to abs(z) ≲ N^{−2}.
  - Conjugated by P₀, whose entries are O(N^{1/2}abs(z)^{−1/4}) there, it gives a jump of O(N/log N) on a set of
    length O(N^{−2}).
  - So it contributes O(1/(N log N)) to R. Heuristically that is o(1/N), consistent with P1 and with E4's clean N·dev.
- **Fix.**
  - Take **W̃ := D_w** (the Szegő function of w₀ on [0, β̂]). Then Ẽ_N = D_∞^{σ₃}N₀ M f^{σ₃/4}(2πN)^{σ₃/2}, with M
    from (6.53). It has an exact band jump and *no* jump on (−δ, 0). Its removability at 0 must be re-checked with the
    log factor: D_w ~ z^{−1/4}(log 1/z)^{1/2}, which still gives at most a square-root singularity.
  - Replace Lemma 4.3 by a **lip-mismatch lemma** bounding the R-jump by O(N^{−1}(log N)^{−1}) in L¹ ∩ L^∞ on Σ ∩ U(0, δ).
  - Alternatively, cite and adapt the log-endpoint literature (e.g. Conway–Deift, "Asymptotics of polynomials
    orthogonal with respect to a logarithmic weight", SIGMA 14 (2018) 056; verify before citing).
  - Until then, the §4 theorem is conditional on this lemma.

**F2 (MODERATE; probe bug): check_z_e2e.py `Afun` integrates over unsorted breakpoints.**
- The code is `mp.quad(f, [0, 0.1, 0.5, 0.9, vmax])` with vmax = √(1 − 3/(8T)).
- When vmax < 0.9 (T = t(u) ≲ 1.97, i.e. u beyond about x(2), out to x_e), mp.quad integrates past vmax, where the
  Lambert-W argument < −1/e and mp.re(W) is garbage, and back.
- At N = 40, A(u) at the 90% point of [β, x_e] is −4.55·10⁻⁴ (true +1.35·10⁻³).
- **Effect.** A far-u error δI shifts g (near the band) and ℓ/2 by the same constant. So φ = ℓ/2 − g is unchanged and
  V acquires a pure left factor e^{−NδIσ₃}. The doc's normalized test is invariant under that factor (F3), so it
  cannot see it.
- P1 shows the factor, e^{−0.019σ₃} at N = 40, and its removal by the fix.
- After the fix, the doc's relative-test numbers at N = 10 and 20 change by ≤ 0.01. The **N = 40 row was computed with
  the bug** and must be regenerated.
- **Fix:** use breakpoints [0, 0.1vmax, 0.5vmax, 0.9vmax, vmax] (Eedge too, defensively). Re-run and re-commit
  check_z_e2e_zeta.out.
- The other checks are unaffected:
  - check_z_edge2, check_z_kappa and check_z_farfield call the same pattern only at T ≈ N/J, where vmax ≈ 1;
  - check_z_farfield never calls Afun.

**F3 (MODERATE): the doc's test is blind to constant diagonal factors, and Ξ is not invisible.**
- **What the test misses.** |M_ii(z)/M_ii(z₀) − 1| and D_∞^{∓2}M_ij/M_ii are invariant under M ↦ C₁MC₂ with C₁
  constant diagonal (and under a C₂ of D_∞ type). So:
  - an error in any left-normalization constant (ℓ, the far field, F2's δI) is undetectable;
  - "b_N/(β_N/4)" is an equilibrium statement (E4), not a parametrix test, so it does not close the gap.
- **What it reports.** The diagonal-ratio entries it does report are dominated, at N ≤ 40, by the omitted Ξ (P2), not
  by the parametrix.
- **Fix.** Adopt P1's absolute test (Ξ built, F_in·Ξ, the Ξ^{−2}-corrected w₀, no reference point) as
  check_z_e2e's canonical output. Delete "invisible at this accuracy". P1 numbers can be quoted after re-running.

**F4 (MODERATE; Lemma Z as stated).**
- **(a) The B_r endpoint.** With B_r cut on (−r, 0) only, B_r ~ (z + r)^{−ℓ̂(−r)/2π} at the junction −r. That is a
  power singularity of F_in on C, so log(F_out/F_in) is log-singular there and "Ξ bounded at the crossing points"
  fails.
  - check_z_farfield and P1 actually use the **full-axis B** (continued ℓ̂ on all of (−∞, 0), §3(b)). With it, D·B is
    continuous, hence analytic, across the whole negative axis inside C, and the ratio is analytic at −r.
  - Fix: define F_in with the full-axis B. This needs §3(b)'s continuation beyond x_cross, outside C, where only its
    boundedness matters.
- **(b) The sign of Ξ.** With C counterclockwise, Ξ₊/Ξ₋ = Ξ_in/Ξ_out = F_out/F_in. So the jump on C is removed by
  **F ↦ F·Ξ on both sides** (F_inΞ_in = F_outΞ_out), not by "F·Ξ^{∓1} (inside/outside)". Then F → 1 at ∞, and w₀
  gets Ξ^{−2}. P1 uses exactly this.
- **(c) Hypothesis (iii)'s growth.** sup_C abs(log(F_out/F_in)) grows with N (3.8, 5.5, 7.1 at N = 20, 40, 80; P2).
  The bound is therefore Ξ(z)/Ξ(0) − 1 = O(abs(z)·sup_C abs(L)/R), i.e. O(log^k N/N²), not the stated O(log²N/N²).
  It is harmless.
- **(d) A missing hypothesis on C.** C must stay inside the saddle level curve of P8, which carries D's poles at
  t = 0, −1, −2 and D̃'s cut. "r below the t-axis crossing" is not sufficient by itself. It holds with margin 1.21.
- **(e) What remains for Lemma Z to be a proof.**
  - In x-units, C, D̃, D and B (up to its normalization constant) are N-independent. K changes only by the constant
    −(1/8)log s. log F_out converges as β_N → 0, because t̂ ~ y^{−1/2}log(1/y) is integrable.
  - So the winding/continuity statement reduces to **one N-independent computation** (the limit L_∞ on C) plus a
    uniform perturbation bound (L_N − L_∞ → 0 uniformly on C, with explicit rate).
  - The single computation should be certified: interval arithmetic, or an argument-principle count of zeros/poles
    of the ratio's analytic extension inside C. 10⁻⁸ floating-point evidence at N = 20 and 40 is not that.
  - Hölder continuity at the junctions then follows, since the ratio is analytic near x_m and near −r.

**F5 (MODERATE; E1/E4 wording): the cut t_c = 3/8 is a gauge, not "canonical".**
- Any t_c ∈ [3/8, 1) gives an E1-admissible constraint ρ_N·1_{(0, x(t_c)]}: √xρ is decreasing, and A(x_c⁻) = 0 holds
  without linear vanishing.
- The matching α-shift is α_W = 1 − t_c, K = (β̂ − z)^{t_c−1/2}. P4 verifies t_c = ½ end to end.
- β_N moves by O(1/N), so **the 0.27 in E4 is convention-dependent** (0.43 for t_c = ½). The "extra constraint mass" beyond
  the top node, (1 − t_c)/N (5/(8N) for t_c = 3/8), is exactly what α_W = 1 − t_c absorbs. What is canonical is
  b_N = (β_N/4)(1 + O(1/N)), and E5's κ (an O(1/N) change of β_N does not affect it).
- The choice 3/8 is the natural one: it is the unique cut at which the constraint density vanishes (linearly), F_out
  is smooth at X_e, and t is analytic there.
- Fix:
  - say this in E1/E3 and in E4's convention note;
  - the integration over (0, 4) of check_z_edge [1] is *not* a gauge member, because √xρ is not monotone there.

**F6 (MINOR; E5): wrong closed form.**
- The doc prints κ = −2(log(π/2) − (1/2)(1 − log 2)), which evaluates to −0.5963.
- The correct form is κ = −2(log(π/2) − (1 − log 2)) = −0.28946, since 2J′(2)/J(2) = −(1 − log 2). check_z_kappa.py
  codes the right one.
- Also replace the two-point fit "a ≈ −0.300" by P6's three-term fit (a = −0.289472).

**F7 (MINOR): §2 is superseded but reads as current.**
- Its F_far, a Cauchy integral on (x_m, x_e), is what §4.2 rejects (a cut starting at x_m creates a power singularity).
  Its "z^{κσ₃} normalization at ∞" is unnecessary (§4.1: T = I + O(1/z)).
- Mark §2 "superseded by §4.2", or delete it.
- Rename the clashing κ's: the K exponent, E5's κ, and the Airy κ̃_N.

**F8 (MINOR; E3 hypotheses).**
- "Checked: |t′| increases with γ" does not by itself give √xρ_N decreasing, because √x decreases in γ.
- Use the explicit √x|t′| = log(γ/2π)(γ² + ¼)^{3/2}/(4πγ), increasing for γ > 2π. Note that A(x_e⁻) = 0 needs only
  boundedness (F5).

**F9 (MINOR; labels and bookkeeping).**
- The status line says "Phase 1 is written; it is a proof sketch". E1–E3 are complete enough for PROVED-mod-G2 (see
  the labels).
- §4's heading should name F1 alongside Lemma Z as an open step. "The uniform-in-N versions of the two edge
  parametrices — routine" is not accurate for the hard edge (F1).
- Commit `check_px_e2e.py 2 2 10,20,40` output, cited as the pp2 reference (P5).
- §4.3 "α_x = −½ + o(1)" should say α_x = −½ exactly, with a log factor (F1).

## Recommended labels

| Claim | Label |
|---|---|
| Lemma E1 (i)–(iv) | **PROVED-mod-G2** (B0, B*, (P), Optimality), REVIEWED, after the F5 wording |
| Cor. E2 | PROVED, REVIEWED |
| Cor. E3 (+ σ_ζ hypotheses) | PROVED, REVIEWED, after F8 |
| Prop. E4 | NUMERICAL (convention t_c = 3/8 stated; F5) |
| Prop. E5 | DERIVATION (formal regular variation) + NUMERICAL (5-digit, P6), after F6. PROVED needs the uniform RV lemma |
| Phase 2 (§3) | **NUMERICAL, CONFIRMED** by an independent stronger (absolute, Ξ-included) probe (P1), after F2/F3 re-runs |
| §4 theorem: b_N = (β_N/4)(1 + O(1/N)), a_N/(2b_N) = 1 + O(1/N) | **PROOF SKETCH (conditional)**. Open: Lemma Z (F4(e)), the log-weight hard-edge lemma (F1), uniform soft-edge Airy, Rule R of the written proofs. Not PROVED |
| Corollary b_n/x_n = π²/16 + O(1/log n) | conditional on the §4 theorem + E5's RV lemma |

No PROVED label may be attached to §4 until F1 and F4(e) are written out and re-reviewed.
