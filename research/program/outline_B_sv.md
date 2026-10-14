# Problem B — pointwise Law P for weights k^{−s}Ψ with Ψ slowly varying and D(γ) = ∞

Research-program outline (2026-10-14). Source state: jacobi-asymptotics G1 PROOF.md §§0, 3.3–3.4, 3.8–3.9 (Plans 29–36).
Numerics in this directory: `check_sv_B1.py/.out`, `check_sv_B2.py/.out`, `check_sv_B3.py/.out` (p = s = 2, NUMERICAL).

---

## 0. Bottom line

- **The law is almost certainly true** (my estimate: ≥ 95%). Numerically, the deviation from the pure power is
  explained to 2–3 digits by a *local tilt*. Near scale n, Ψ behaves like (k/n)^{ε_n} with ε_n = L′(log n), where
  L(τ) := log Ψ(e^τ). The pure-power 1/n coefficient d₁ = −(s−1)/2 (RH_px baseline) then predicts
  β_n(w)/β_n(v) − 1 ≈ ε_n/(2n). Observed ratio: 0.49–0.495 (§6).
- **The existing toolbox reaches log-type and stops there.** §4 shows why. Every TV/Grönwall scheme pays a factor
  e^{4H_n}, with H_n := osc_{[nR_n, n^γ]} log Ψ → ∞ exactly when D = ∞. The best "floor" these schemes can make small
  is polynomial in 1/log n. No choice of truncation window wins. Exponent tilting does not help either: it removes
  log-type obstructions only.
- **Exact gap.** Everything except one lemma is routine or reused (§2). The missing lemma is **QL**: a μ-level
  (single-n) logarithmic-moment localization bound on the hard-edge range [n, n^γ], uniform along the path vΨ^t.
  Conditional theorem: QL ⇒ Theorem B (§2, B-cond).
- **Most credible full route: a direct Riemann–Hilbert analysis.** Do RH_px with an analytic, smoothed slowly varying
  weight; reduction RedA makes the smoothing free. The new piece is a hard-edge Bessel parametrix with an
  N-dependent order α_x + L₁′(log N)/p and a non-Fisher–Hartwig, slowly varying factor at 0. The closest precedent
  in the repo is RH_ζ's log weight at the hard edge, via the Conway–Deift comparison.

---

## 1. Target theorems (precise)

Setting: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), w = vΨ with Ψ > 0 on ℕ.

**Definition (sequence-form slow variation, §3.8/§3.9(i)).** δ_n(λ) := max{|log Ψ(k) − log Ψ(n)| : k ∈ ℕ ∩ [n/λ, λn]}
→ 0 for every λ ≥ 1. There is no boundedness assumption and no D(γ) assumption.

**Theorem B (main target).** If Ψ is slowly varying in sequence form, then n^p b_n(w) → c(p) and n^p a_n(w) → 2c(p),
for all n and all p > 0.
- *Corollary B1 (Karamata).* This holds for Ψ(k) = ℓ(k) with ℓ a measurable slowly varying function. ℓ restricted to ℕ
  is sequence-form slowly varying by the Uniform Convergence Theorem. Citation gate: Bingham–Goldie–Teugels (BGT)
  Thm 1.2.1, hypotheses to be quoted.
- *Corollary B2 (regular variation).* The same holds for w = k^{−s}k^{ρ}ℓ(k) with s − ρ > 1, by renaming s.
- Theorem B contains T3-all and T3-log.

**Theorem B-rate (stretch; p > 1 first).** Let Ψ₁ = exp(L₁(log k)) be the smoothed version (RedA below), and suppose
Ψ/Ψ₁ → 1 at a summable rate. Then
  n^p b_n(w)/c(p) = 1 − (s − 1 − L₁′(log n))/(2n) + o(1/n), and a_n/(2b_n) = 1 + p/(2n) + o(1/n).
- NUMERICAL support: B1, B3 in §6. The residual w/tilt decays like n^{−1.5} (B2(a)).
- It is only plausible via Route II, and it needs care: "o(1/n)" is a guess, and the baseline d₁, e₁ is itself
  NUMERICAL in RH_px §0.

**Partial targets** (publishable on their own; §8):
- B-cond (QL ⇒ B);
- RedA;
- QLP (quantitative hard-edge localization for pure powers, uniform in M and s);
- B for p > 1 only (if Route II works only for p > 1).

---

## 2. Lemma chain

Notation: g_n := log Ψ − log Ψ(n). The path is w(t) = vΨ^t, t ∈ [0, 1]. μ_m^{(t)} = q_m² for w(t). M₀ = M₀(p) is the
head margin of T3-sv.

**L0 (Potter, sequence form) — new, elementary, PROVABLE NOW.** Put ε_n := sup_{m ≥ n/2} δ_m(2) → 0. Then for
k ≥ n/2,
  |g_n(k)| ≤ ε_n(1 + log₂ max(k/n, n/k)).
For every η > 0 there is C_η with C_η^{−1}k^{−η} ≤ Ψ(k) ≤ C_η k^{η}.
- *Proof:* dyadic chaining n, 2n, 4n, …; each step costs ≤ δ_{2^i n}(2) ≤ ε_n. Polynomial bounds follow by taking n
  large enough that ε_n ≤ η log 2.
- Consequence: Σw < ∞ and w_k ≥ c₁k^{−s−η}. So H_all and every Sat_p⁺ use apply, with W/w_k ≤ n^{O(1)} for k ≤ n.

**L1 (head) — reuse.** The T3-log step 3 "Head" bullet applies verbatim, with polylog factors replaced by n^{O(1)} from
L0:
  sup_t (μ_n + μ_{n−1})^{(t)}({k < n/M₀}) ≤ n^{O(1)}e^{−2(n−1)}.
The T3a step 1 bound a_n^{(t)}, b_n^{(t)} ≤ 2M₀^p(n−1)^{−p} also holds unchanged. It uses only Sat_p⁺, and the n^{O(1)}
factor is absorbed.

**L2 (far tail) — reuse TLw.** For k > n^γ ≥ T″,
  μ_m^{(t)}(k) ≤ 1156(T″/k)^s · Φ_t(k)/min_{T′≤j≤T″}Φ_t(j) ≤ C_η n^{s(2+2/p)+O(η)}k^{−s+η}.
- Choose γ with γ(s − 1 − η) > s(2 + 2/p) + p + 2η. Then Σ_{k>n^γ}(1 + log k)(μ_n + μ_{n−1})^{(t)}(k) · n^p → 0.
- The K-cutoff argument of T3-log step 3 (F1) is reused for unbounded f.

**L3 (RedA, smoothing reduction) — new, easy.** Let L be the piecewise-linear interpolant of τ ↦ log Ψ(e^τ) at the
nodes τ = log k. Put L₁ := L * φ (φ the standard Gaussian) and Ψ₁(k) := exp L₁(log k). Then:
- (i) Ψ/Ψ₁ → 1;
- (ii) L₁ is entire, with L₁^{(j)}(τ) → 0 for all j ≥ 1, and sup_{|Im u| ≤ π/2}|L₁(τ + u) − L₁(τ)| → 0;
- (iii) the law for vΨ₁ ⇔ the law for vΨ.

*Proof of (iii).* T3-conv's proof is base-independent. Run it with base vΨ₁ and ψ = Ψ/Ψ₁ → 1. It uses only centering,
|g| ≤ ε beyond k_ε, and the head bound (L1 for the base vΨ₁). (i) and (ii) follow from L0: Gaussian tails beat the
Potter growth ε|u|.
- Use: Route II needs an analytic weight. Routes I/III may use L₁′, L₁″.

**L4 (window/bulk) — reuse.** T3-log step 2 applies to the truncation of Ψ to [n/M₀, nR_n] whenever
D*_n := osc_{[n/M₀, nR_n]} log Ψ stays bounded. If R_n → ∞ slowly enough that δ_n(R_n) → 0 (diagonal choice), it is
even trivial: FV with |g| ≤ δ_n(R_n) → 0 everywhere.

**L5 = QL (THE CRUX) — open.** Two equivalent-strength formulations:
- **QL-a (log-moment).** For m ∈ {n − 1, n},
    Λ_n := sup_{t∈[0,1]} Σ_{n ≤ k ≤ n^γ} log(k/n)·μ_m^{(t)}(k) = o(1/ε_n).
  The natural form is Λ_n = O(1).
- **QL-b (power tail).** There are α > 0 and C with sup_t μ_m^{(t)}((Mn, ∞)) ≤ C M^{−α} for 1 ≤ M ≤ n^{γ−1} and
  n ≥ n₀. QL-b ⇒ QL-a with Λ_n = O(1).

**Theorem B-cond (PROVABLE NOW from L0–L2 + FV/FVa).** QL-a ⇒ Theorem B.

*Proof sketch.* No truncation is needed. By FV (with the K-cutoff),
  |log b_n²(w) − log b_n²(v)| ≤ sup_t Σ_k|g_n|(μ_n + μ_{n−1})^{(t)}
    ≤ ε_n(2 + log₂M₀) + (ε_n/log 2)·2Λ_n + head(L1) + far tail(L2) → 0.
For a_n, use FVa. n^p|x_k − a_n| ≤ C_p and n^pb_n ≤ C_p off the head (L1/T3a step 1), so the same bound times 3C_p
holds. Finish with the pure-power laws. ∎
- *Note.* The trivial bound Λ_n ≤ γ log n recovers precisely "ε_n log n bounded", i.e. essentially log-type. So
  T3-log is the trivial case of B-cond.

**L6 = QLP (pure-power input for any proof of QL) — new; derivable from the RH work.** For σ in a compact subset of
(1, ∞), μ_m^{v_σ}((Mn, ∞)) ≤ C M^{−p/2}·(1 + o(1)) for M ≤ n^{c}, uniformly in σ. The large-M range below the Bessel
scale has a different (σ-dependent) exponent, and we only need some α > 0.
- *Source:* the hard-edge Bessel parametrix of RH_px §4.1 (p > 1), RH₁(r) (p = 1) and RH_plt1b (p < 1), giving
  |π_N(x)|²w on the disc, with error terms uniform in σ. Uniformity in σ must be checked against each small-norm
  estimate.
- It improves Lemma LP (which is limit-only, fixed M).

---

## 3. What to reuse (and what does NOT transfer)

| Item | Status | Use in Problem B |
|---|---|---|
| FV, FVa, TV (§3.2, 3.5, 3.8) | PROVED, REVIEWED | verbatim |
| Sat_p⁺ (§3.3) | REVIEWED | head, with W/w_k ≤ n^{O(1)} (L0) |
| TLw (§3.9) | PROVED | far tail (L2) |
| T3-conv proof | REVIEWED | RedA (base-independent) |
| T3-log steps 2–3 incl. K-cutoff | REVIEWED | L4, L2 |
| LP (§3.8) | PROVED-mod-cite | the fixed-M case of QLP |
| RH_px / RH₁(r) / RH_plt1b | PROVED-mod-cite | QLP; Route II template |
| RH_ζ (Conway–Deift hard-edge log weight) | REVIEWED | closest precedent for a non-FH hard-edge factor |
| Theorem L Grönwall | REVIEWED | does NOT transfer: factor e^{4G}, G = ∞ |
| T3-log truncation | REVIEWED | does NOT transfer: sandwich constant D* = ∞ |

---

## 4. Hardest step and why the obvious ideas fail (quantitative)

The hardest step is QL. It asks for μ-level localization deep in the hard-edge region k ∈ [nR, n^γ], along a path whose
weights are not uniformly sandwiched. The perturbation f = log Ψ is o(log k) there, but unbounded.

**(a) Scale-dependent truncation [n/M₀, nR_n] + Grönwall on the tail (the prompt's first idea).**
- On the truncation path, h_n vanishes on the window. Theorem L's argument is then floor-free:
  y(1) ≤ e^{4H_n}(y(0) + tiny), with H_n := osc_{[nR_n, n^γ]} log Ψ.
- It needs y(0) = μ^{vΨ̃_n}((nR_n, ∞)) ≤ o(e^{−4H_n}/H_n).
- y(0) is obtained by transporting from v (or from a tilted v). Every available transport (TV + Cauchy–Schwarz)
  leaves an additive floor: √y(0) ≤ e^{2G}(√μ^v + δ) with δ := the size of f on the *bulk* [n/M₀, Mn].
  Centering at nR_n instead makes the floor O(G). The floor is ≥ δ_n(R_n), and that is polynomial in 1/log n at best.
- Requiring log R_n ≳ (4/α)H_n (so that the R_n^{−α} part is small) forces δ_n(R_n) ≈ L′·log R_n ≈ L′·H_n.
  - Ψ = exp((log k)^θ): H ≍ τ^θ, floor ≍ τ^{2θ−1}, and floor²·e^{4H} → ∞ for every θ ∈ (0, 1).
  - Ψ = exp((log log k)²): e^{4H} = τ^{8 log γ}, floor² ≈ τ^{−2}(log τ)⁴. This would need γ < e^{1/4}, but γ > 2 + 2/p.
- Conclusion: this route covers nothing beyond D(γ) < ∞, even with a sharp TL (γ ≈ 1 + 2/p).

**(b) Layered Grönwall on A_j = (2^j n, ∞) (the prompt's second idea).**
- TV gives ż_j ≤ ε[(j+2)z_j/2 + ½Σ_{i>j}z_i + Λ + Λ²z_j], where z_j = √μ(A_j) and Λ² ≍ Σ(2i+5)z_i².
- The (j+2) factor is harmless: it gives an M^{O(ε)} loss.
- The fatal term is the Cauchy–Schwarz bound |⟨1_Aq_m, K_m(fq_m)⟩| ≤ √y‖fq_m‖. It feeds a non-decaying forcing εΛ
  into every layer, so y_j ≳ ε²j² up to j ≤ J ≍ log n.
- Then ε Σ_j y_j ≳ ε³J³. That is bounded only in the log-type case (ε ≍ 1/log n) and diverges otherwise. Bootstrapping
  Λ needs εJ = O(1), which is again log-type.

**(c) Tilt comparison (using Karamata smoothness to localize).**
- Compare with v_{σ_n}, σ_n = s − L₁′(log n). This removes the log-singular leading part of f exactly. It requires
  QLP and the pure-power law uniformly in σ (L6).
- The residual r_n(k) = L₁(log k) − L₁(log n) − L₁′(log n)log(k/n) has oscillation over [n, n^γ] of order τ²|L₁″|.
  That is bounded iff L₁′(τ) = c/τ + O(1/τ²)-type, i.e. log-type (up to an exact power, which is just s → s − ρ).
- So tilting plus (a)/(b) covers only "log-type × k^ρ": nothing new.

**(d) Moment / Chebyshev–Markov–Stieltjes (CMS) bootstrap.**
- Lemma LP made quantitative: if the coefficients are known in a window |j − m| ≤ d to relative precision η ≪ d^{−2},
  CMS gives μ_m([0, y]) ≤ F(y) + O(1/d), resolving only y ≳ d^{−2}.
- Closure needs ε_n² log n → 0 and η ≪ d^{−2} simultaneously. It fails at θ = ½ and does not close for θ ≥ ½. It would
  give at most a niche window θ < ½, and even that is doubtful once η ≪ d^{−2} is enforced.

**Structural reason.** Below y ≈ η in the scaled variable, the o(1) law cannot see the hard edge. Hard-edge
localization at depth M is a statement at the *1/n level* of the coefficients: e₁ = p/2 and d₁ = −(s−1)/2 determine
the Bessel order. So QL is genuinely second-order information, and that is why RH (which supplies 1/n-level
structure) is the natural tool.

**Could the law FAIL?** I see no mechanism.
- (i) Theorem R needs Ω(1) roughness at scale n, which slow variation excludes locally.
- (ii) The hard-edge factor enters only through 1/n terms in the tilt picture.
- (iii) A Rakhmanov-type heuristic: the a.c. scaled limit is positive on the band.
- (iv) The adversarial oscillating test (B3, L = √τ·sin log τ, D = ∞) follows the tilt prediction, including the
  sign change between n = 1600 and 3200.

Recommendation: do NOT spend effort on counterexamples. One cheap stress test is optional:
L(τ) = τ^{0.95}·sin(log log τ), at p = 1 and p = 0.5.

---

## 5. Candidate methods for QL (or for B directly)

**Route II — direct RH for an analytic slowly varying weight (RECOMMENDED for the full theorem).**
- *Plan.*
  1. RedA reduces to Ψ₁ = exp(L₁(log k)), analytic in the slit plane, with L₁^{(j)} → 0.
  2. In RH_px §1, the weight becomes w(z) = N^p t(z)^{−s}Ψ₁(t(z)), with t = Nz^{−1/p}. The band weight W picks up the
     factor Ψ₁(Nx^{−1/p}).
  3. Szegő function: D_Ψ := exp(Szegő integral of log Ψ₁(N x^{−1/p}) on [0, 4c]). This is finite because
     log Ψ₁ = o(log(1/x)).
  4. Hard edge: write Ψ₁(Nz^{−1/p}) = Ψ₁(N)·(z)^{−L₁′(log N)/p}·e^{ρ_N(z)}. Use a Bessel parametrix of order
     α_x − L₁′(log N)/p. Then check that e^{ρ_N} is "Szegő-absorbable" in U(0, δ): it is analytic off (−δ, 0], and
     its jump across (−δ, 0) is O(sup|L₁′|) (small, not super-exponentially small as in RH_px Lemma 3.2(v)).
  5. Small norm, uniform in the N-dependent order.
- *Pros.*
  - Gives Theorem B for all n with a rate, and plausibly B-rate.
  - The repo has run 5 RH analyses, including a non-FH log weight at the hard edge (RH_ζ, Conway–Deift comparison).
  - Gives QLP as a by-product.
- *Cons / risks.*
  - The jump of e^{ρ_N} across (−δ, 0) is only O(L₁′(log N)) → 0, with no rate. It must be shown to be harmless,
    e.g. by a Conway–Deift-type comparison. **This is the single biggest technical risk.**
  - Bessel order depending on N: uniformity of KMVV's construction must be checked.
  - Three regimes: p > 1 (RH_px), p = 1 (RH₁(r)), p < 1 (RH_plt1b seam).
  - Citation gate: Conway–Deift's hypotheses must be quoted exactly.

**Route I′ — commutator transport (elementary alternative; speculative).**
- Replace the Cauchy–Schwarz step in TV by the identity
    ⟨1_Aq_m, K_m(fq_m)⟩ = ⟨1_Aq_m, [K_m, f]q_m⟩ (since K_mq_m = 0).
- New lemma needed (CB): |⟨1_{A}q_m, [K_m, f]q_m⟩| ≤ C·ε·μ_m(A)·(1 + log M) + (head/far-tail terms), for f with
  Potter-ε structure. It is multiplicative: no floor.
- With CB, the layered Grönwall of §4(b) gives y_j ≤ C 2^{−αj}e^{O(εj)}, hence QL-b. The heuristic is that f is smooth
  in y = n^p x on the bulk, so [K_m, f] is nearly banded (Jacobi structure). But f ≈ ε log(1/y) is log-singular at the
  hard edge.
- *Pros:* stays in the repo's elementary framework (TV/FV), and works for all p at once.
- *Cons:* CB is itself a hard-edge statement (a commutator with a log-singular multiplier), and no tool for it is known
  here. It is likely as hard as QLP for w.

**Route III — second-order bootstrap with discrete WKB at the hard edge (conceptual; not recommended first).**
- Bootstrap on all rows j ≥ N₀ with the second-order hypothesis
    β_j = 1 − (s−1−L₁′(log j))/(2j) + r_j, Σ|r_j| < ∞,
  together with a_j/(2b_j) = 1 + p/(2j) + r′_j.
- The eigenvector ψ_k(m) = q_m(k) is a unit vector solving the recurrence at x_k ≪ m^{−p}. Under the hypothesis the
  recurrence is a discretized Bessel equation, and discrete Levinson/WKB (Janas–Naboko type; citation gate) gives
  |ψ_k(m)|², hence QL-b.
- Closing the loop uses FV with the *difference* μ_n − μ_{n−1}, by summation by parts against Δg ≈ ε/k, to recover a
  1/n-order change.
- *Pros:* explains the tilt numerics, and needs no analytic continuation.
- *Cons:*
  - Requires summable second-order errors.
  - FV-difference control at O(ε/n) is itself a precise asymptotic.
  - Continuity of the bootstrap in t with sup over infinitely many j is delicate.

**Route IV — tilt comparison.** Covers only log-type × k^ρ (§4(c)). Use it only as a sanity check inside Routes II/III.

---

## 6. Numerics run (de-risking; NUMERICAL, p = s = 2, long-double RKPW / float64 Lanczos as in check_log_weights.py and check_mn_loc.py)

**B1 (`check_sv_B1.out`).**
- Ψ = exp(√log(k+e)):
  - |β_n(vΨ)/β_n(v) − 1| = 1.09e−3, 5.2e−4, 2.5e−4, 1.2e−4, 5.6e−5, 2.7e−5 (n = 100 … 3200).
  - n·dev/ε_n with ε_n = 1/(2√log n): 0.470, 0.481, 0.487, 0.490, 0.490/0.492, 0.487/0.492 (K = 1.2e5 / 4.8e5).
- Ψ = exp((log(k+e))^{0.8}): same table, n·dev/ε_n → 0.495.
- The a_n deviations are the same size.
- Converged in K, up to a third-digit drift at n ≥ 1600.

**B2 (`check_sv_B2.out`).**
- (a) Tilt test: β_w/β_{k^{−(2−ε_n)}} − 1 = −5.1e−5, −5.2e−6, −7.2e−7 (n = 100, 400, 1600), versus β_w/β_v − 1 ≈ 1e−3 …
  6e−5. The tilt explains 95–99% of the deviation, and the residual is ≈ n^{−1.5}.
- (b) Lanczos, K = 1e5, n ≤ 400:
  - μ_n((Mn, ∞)) for w, the path midpoint t = ½, and v agree to 3 digits at M = 2, 8, 32, 128.
  - They track F_p(M) ~ M^{−1}. The n = 100, M = 128 entries are truncation-affected.
  - The log-moment E[log₊(k/n)] = 0.414–0.422 is essentially t-independent.
- So QL-a holds numerically with Λ_n ≈ 0.42, flat in t and n.

**B3 (`check_sv_B3.out`, oscillating, D = ∞: L(τ) = √τ·sin log τ).**
- dev = +1.11e−3, 3.9e−4, 1.2e−4, 3.0e−5, 2.1e−6, −4.2e−6.
- Tilt prediction L′/(2n) = +1.25e−3, 4.3e−4, 1.4e−4, 3.6e−5, 4.6e−6, −3.3e−6, including the sign change. K-converged.

**Further numerics worth doing** (cheap, before committing to Route II):
- (N1) Repeat B1/B3 at p = 1 and p = 0.5, to check that the tilt picture holds where d₁ differs.
- (N2) QL-b slope: fit log μ_n^{(t)}((Mn, ∞)) against log M up to M ≈ n^{1+2/p}, with a larger K. This tests α and
  where the Bessel crossover sits.
- (N3) For Route I′: compute |⟨1_Aq_m, K_m(fq_m)⟩|/μ_m(A) against M and n. If the ratio is bounded by C·ε·log M, CB is
  plausible; if it scales like √(1/μ_m(A)), Route I′ is dead.

---

## 7. Effort and probability

| Work package | Effort (plans) | P(success) |
|---|---|---|
| WP1: L0, RedA, L1, L2, Theorem B-cond (write-up + Rule A/R) | 1 | 95% |
| WP2: numerics N1–N3 | 0.5 | 100% (decides Route I′ go/no-go) |
| WP3: QLP from RH_px / RH₁(r) / RH_plt1b (uniform M ≤ n^c, σ compact) | 1–2 | 70% |
| WP4: Route II, p > 1 (RH_px with an analytic slowly varying weight) | 3–4 | 45% |
| WP5: Route II, p = 1 and p < 1 (seam) | 2–4 more | 60% given WP4 |
| WP6 (alternative): Route I′ commutator lemma CB | 2–3 | 15% |

- Overall P(Theorem B for all p > 0 within about 8 plans): about 30–35%.
- P(Theorem B for p > 1): about 45%.
- P(B-cond + QLP + numerics, a clean conditional paper section): about 90%.

**Stop conditions to pre-register** (AGENTS.md):
- (i) The e^{ρ_N} jump at the hard edge cannot be made small-norm without a rate on L₁′. Stop Route II and record it.
- (ii) Uniformity of the KMVV Bessel construction in an N-dependent order needs an unreadable or uncited source. Stop.
- (iii) N3 shows the CB ratio blowing up. Drop Route I′.

---

## 8. Publishable partial results (in order of availability)

1. **Theorem B-cond + RedA + Potter (L0).**
   - The pointwise Law P for every slowly varying Ψ reduces to one logarithmic-moment localization bound.
   - The reduction to analytic smoothed weights is free.
   - T3-log is the trivial case Λ_n ≤ γ log n.
   - Also Corollary B2 at the log-type level: k^{−s+ρ}ℓ with ℓ log-type, s − ρ > 1 (immediate from T3-log).
2. **QLP.** Quantitative, uniform-in-s hard-edge localization μ_n((Mn, ∞)) ≲ M^{−p/2} for pure powers. This sharpens
   Lemma LP (limit only) and Lemma TL (polynomial loss). It may be of independent interest for discrete OPs with
   accumulating nodes.
3. **The tilt law (conjecture + numerics).**
   - β_n(k^{−s}Ψ)/β_n(k^{−s}) − 1 = L′(log n)/(2n) + o(L′/n).
   - The p = 2 numerics match to 2–3 digits for three D = ∞ examples, including an oscillating one.
   - This is a sharp, falsifiable statement of how a slowly varying weight enters the coefficients.
4. **The "why it stops" analysis (§4).** TV/Grönwall/truncation methods are limited to D(γ) < ∞ because the hard-edge
   localization they need is 1/n-order information. This is a methodological remark, phrased as heuristic like G1 §4.
5. **(If WP4 succeeds) Theorem B for p > 1 with rate:** a genuinely new RH analysis with a non-Fisher–Hartwig, slowly
   varying hard-edge factor.
