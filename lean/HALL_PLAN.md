# Plan 60 — formalizing Theorem H_all (pure powers) in Lean

Goal: turn the named input `TheoremHPure p κ_p s` (JacobiAsym/Inputs.lean) into a theorem for all p > 0, s > 1,
with κ_p = 3p/2 + log c(p), c(p) = ¼(π/(2I(p)))^p, I(p) = (√π/2)Γ(1/p+1/2)/Γ(1/p+1).

Mathematical source: papers/paper1/main.tex (Lemmas 2.1–2.4, §3 Theorem 1.3 = `thm:equilibrium`, §4 Lemma `lem:disc`,
Corollary `cor:head`, Theorem `thm:upper`, §5 Theorem `thm:lower`, §6), and research/G2/PROOF.md (Lemma B0, Lemma EP,
Theorem B\*, Lemma A1, Corollary A2, Theorems A-U, A-L, Corollary H-input).

## 0. Design decisions (deviations from the paper, all elementary)

1. **Constant.** Lean defines `hallLam p := ∫ s in 0..1, arccos (2 s^p − 1)` and
   `hallC p := (π / hallLam p)^p / 4`, `hallKappa p := 3p/2 + log (hallC p)`, so that (4c)^{1/p} = π/Λ(p) holds by
   definition. Integration by parts and v = s^p give Λ(p) = p∫_0^1 s^{p/2}(1 − s^p)^{−1/2}ds = B(1/p+1/2, 1/2) = 2I(p) (stage S6), which
   identifies `hallKappa p` with the paper's κ_p. Everything else uses only the defining identity.
2. **The maximiser as a push-forward.** μ\*_u := image of ν\* := Leb|(0,1] ⊗ (1/π)Leb|(0,π] under
   (t, φ) ↦ X(t,φ)^{−1/p}, X(t,φ) := β_t(1 − cos φ)/2, β_t := 4c t^{−p}. Then (paper Thm 1.3 def.) μ\* = ∫ω_{β_t}dt is the
   x-image, ω_β being the image of dφ/π under φ ↦ β(1 − cos φ)/2. No density formula is needed:
   * admissibility μ\*_u(a, b] ≤ b − a (and = on (0, u_s], u_s = Λ/π) follows from the explicit tail
     ν\*{X < y} = (1/π)∫_0^1 arccos(1 − 2y/β_t) dt and the substitution t = (4c/y)^{1/p}s, which turns
     (1/π)∫_0^1 arccos(1−2y/β_t)dt + y^{−1/p} into 1 + (πr)^{−1}∫_r^1 (π − arccos(1 − 2s^p))ds, r = (y/4c)^{1/p}
     (nonincreasing in y; = 1 for r ≥ 1);
   * the arcsine potential (Lemma `lem:arcsine` / B0) ∫_0^π log|β(1−cos φ)/2 − y|dφ = π log(β/4) (0 ≤ y ≤ β) is proved
     from Mathlib's `integral_log_sin_zero_pi`, the product formula cos a − cos b = −2 sin((a+b)/2) sin((a−b)/2) and
     π-periodicity of log|sin|, instead of the Fourier series.
3. **Energy positivity (Lemma EP)** is proved with Frullani's integral (Mathlib `Frullani.integral_Ioi_eq`):
   2 log|x − y| = ∫_0^∞ (e^{−t} − e^{−t(x−y)²}) dt/t, and positive definiteness of the Gaussian kernel
   e^{−t(x−y)²} = √(4t/π)·∫ e^{−2t(x−z)²}e^{−2t(y−z)²}dz, instead of the Fourier transform. Only the inequality
   (not the equality case) is needed for TheoremHPure; uniqueness of the maximiser is not formalized.
4. **Lower bound (A-L) by monotone block comparison.** For u < v, F(u,v) = log(u^{−p} − v^{−p}) is decreasing in u
   and increasing in v. With quantile points t_m (θ(0, t_m] = m/2n) and k_i = ⌈n t_{2i+1}⌉, every pair with j ≥ i+4
   satisfies F(u_i, u_j) ≥ n²∫_{B_{i+2}×B_{j−1}} F dθ² *exactly* (no error terms); near pairs cost O(log n) each; the
   leftover region has θ²-measure ≤ 7/n, so its contribution is o(1) by absolute continuity of the integral. This
   replaces the error analysis (a)–(d) and the lower density bound d_U of `thm:lower` Step 3.
5. **Upper bound (A-U)** follows the paper (Lemma `lem:disc`, Corollary `cor:head`, Theorem `thm:upper`); the
   head/tail split reuses the H7 machinery (`heineK_tail_split`, `phi_bound`).

## 1. Stages and exact Lean statements

All in namespace `JacobiAsym`; `Fp p u v := Real.log |u ^ (-p) - v ^ (-p)|`,
`Jp p μ := ∫ z, Fp p z.1 z.2 ∂(μ.prod μ)`.

| Stage | Module | Main statement (Lean) | Paper |
|---|---|---|---|
| S0 constants | `HallConst.lean` | `hallLam_pos : 0 < p → 0 < hallLam p`, `hallLam_lt_pi`, `four_hallC_rpow : (4 * hallC p) ^ (1/p) = π / hallLam p` | (1.2) |
| S2a arcsine | `Arcsine.lean` | `arcsine_pot : 0 < β → 0 ≤ y → y ≤ β → ∫ φ in 0..π, log |β*(1-cos φ)/2 - y| = π * log (β/4)`; `arcsine_pot_ge` (y ≥ β, ≥); interval integrability | Lemma 3.2 |
| S2b maximiser | `Equilibrium.lean` | `muStar p : Measure ℝ`; `muStar_prob`; `muStar_Ioc_le : μ*(Ioc a b) ≤ ofReal (b-a)`; `muStar_Ioc_eq` on (0,u_s]; `muStar_energy_integrable`; **`muStar_energy : Jp p (muStar p) = hallKappa p`** | Thm 1.3(i),(iii) value |
| S2c potential | `Equilibrium.lean` | `starPot_eq : 0 < x → x ≤ 4c → U*(x) = log c + p`; `starPot_ge : 0 < x → log c + p ≤ U*(x)` | Thm 1.3(ii) |
| S1a quantile lower | `QuantileLower.lean` | for θ probability, θ(Iic 0) = 0, θ(Ioi U) = 0, θ(Ioc a b) ≤ b − a, Fp integrable: ∀ η > 0, ∀ᶠ n, ∃ S ⊆ range (⌈U⌉₊ n + n), S.card = n ∧ 2Σ_{pairs} log(x_a − x_b) ≥ −p n(n−1) log n + n²(Jp θ − η) | Thm 5.2 Steps 2–3 |
| S1b truncation | `HallLower.lean` | ∀ η > 0, ∃ θ as in S1a with Jp p θ ≥ hallKappa p − η (truncate μ\*_u, rescale, Lemma 3.1 scaling) | Thm 5.2 Step 1 |
| S1 lower bound | `HallLower.lean` | **`hall_lower : 0 < p → 1 < s → ∀ η > 0, ∀ᶠ n in atTop, -η ≤ hnorm p (hallKappa p) (heineD (powSeq p) (powSeq s)) (fun _ => 0) n`** | Thm A-L |
| S4 EP | `EnergyPos.lean` | **`energy_pos`**: finite A, B on ℝ, A univ = B univ, log\|x−y\| integrable for A⊗A, B⊗B, A⊗B, diagonals null ⇒ `∫ L dA² + ∫ L dB² ≤ 2 ∫ L d(A⊗B)` | Lemma 3.3 (inequality) |
| S4b optimality | `Optimality.lean` | **`Jp_le_kappa`**: μ probability, μ(Iic 0) = 0, μ(Ioi M) = 0, μ ≤ Leb on intervals ⇒ `Jp p μ ≤ hallKappa p` | Thm 1.3(iii) optimality |
| S3 discretisation | `Discretize.lean` | `disc_upper`: S ⊆ [1, Mn], \|S\| = N ≤ n ⇒ Σ_{i≠j} F(u_i,u_j) ≤ n² Jp p μ̄_S + C_M n (log n + 1) | Lemma 4.1 |
| S3b head + upper | `HallUpper.lean` | **`hall_upper : 0 < p → 1 < s → ∀ η > 0, ∀ᶠ n, hnorm … n ≤ η`** (via Cor. 4.2, Thm 4.3) | Thm A-U |
| S5 assembly | `TheoremHall.lean` | **`theoremHPure_all : 0 < p → 1 < s → TheoremHPure p (hallKappa p) s`** | Cor. H-input |
| S6 constant | `HallConst.lean` | `hallLam_eq_gamma : hallLam p = √π * Γ(1/p + 1/2) / Γ(1/p + 1)`, hence `hallKappa p = 3p/2 + log(¼(π/(2I(p)))^p)` | (1.2) |

Mathlib provides: `integral_log_sin_zero_pi`, `intervalIntegrable_log_sin`, `Function.Periodic.intervalIntegral_add_eq`,
`integral_log`, `Frullani.integral_Ioi_eq`, `integral_gaussian`, Fubini/Tonelli (`integral_prod`, `lintegral_prod`),
`integral_map`, dominated convergence, `Real.arccos`, `Real.Gamma`, `Complex.betaIntegral` /
`Complex.Gamma_mul_Gamma_eq_betaIntegral`. Must be built: everything in the table.

Dependency order: S0 → S2a → S2b/S2c → S1a, S1b → S1; S4 → S4b (uses S2c, S2b) → S3 → S3b → S5; S6 independent.

## 2. Progress

| Stage | Status | Lean (main statements) | Named hypotheses remaining |
|---|---|---|---|
| S0 | DONE (sorry-free) | `hallLam_pos`, `hallLam_lt_pi`, `hallC_pos`, `four_hallC_rpow` | — |
| S2a | DONE | `arcsine_pot`, `arcsine_pot_ge` | — |
| S2b | DONE | `muStar_Ioc_le`, `muStar_Ioc_eq`, `muStar_Iic_zero`, `muStar_energy_integrable`, `muStar_energy` | — |
| S2c | DONE | `starPot_eq`, `starPot_ge`, `muStar_restrict_us`, `le_volume_of_lip` | — |
| S1a | DONE | `quantile_sum_ge`, `quantile_lower` | — |
| S1b | DONE | `Jp_scaleM`, `exists_good_theta` | — |
| S1 | DONE | `hall_lower` | — |
| S4, S4b | DONE | `energy_pos` (Frullani + Gaussian kernel), `Jp_le_kappa` | — |
| S3, S3b | planned | | |
| S5 | planned | | upper half of `TheoremHPure` |
| S6 | planned | | — |
