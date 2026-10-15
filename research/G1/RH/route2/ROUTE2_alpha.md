# ROUTE2_alpha: Route II for s ≥ 1 + 2p (GAP-α of ROUTE2.md §6) via Christoffel transfer (Plan 52)

Status: **Rule R ACCEPT WITH FIXES (../../review/REVIEW_Plan52.md), fixes applied — REVIEWED.** Fixes F1–F7 applied (F1 chain-sequence
attribution, F2 base window, F3 numerics scope, F4 sharpness example, F5 tilt label, F6 scope sentences, F7 CITATIONS).
Novelty: UNCHECKED (no Rule L search; the transfer formula of §2 is classical — Christoffel's
theorem / the Darboux (LU ↔ UL) transformation of Jacobi matrices — and is re-proved here, not cited; Lemma CS is very likely
KNOWN in chain-sequence form, §3.1).

*(Plan 55 note, 2026-10-15: the rate clauses "rate O(1/n) if Ψ satisfies (H_an)" hold with (H_an) weakened to (A_ϑ) for any ϑ > 0 (the base window by Theorem AS, the shift SH-r unchanged); verified on Paper 2's consolidated write-up (papers/paper2), see ../../PROOF.md §3.24 (Theorem AS, PROVED-mod-cite, Rule R pending). This file is unchanged and proves its results as stated.)*

Source: ROUTE2.md §6 "GAP-α" (Plan 48, REVIEWED; review/REVIEW_Plan48.md). Numerics:
`checks/check_r2alpha_christoffel.py/.out`, `checks/check_r2alpha_law.py/.out`.

**Result in one line.** Multiplying the measure by x = k^{−p} shifts s by p: x·σ_s = σ_{s+p} exactly. The Jacobi
coefficients of x·σ are explicit in those of σ and the chain sequence g_n = −P_{n+1}(0)/P_n(0); the positivity of g_n and
the parabolic fixed point of the chain recursion force n^pg_n → c from Law P alone, so **Law P (with or without a rate)
passes from σ to x·σ, for every positive measure on [0, ∞) with infinite support**. Since Theorem RII / Corollary B_{p>1} cover an s-interval of length
2p > p, every s > 1 is reached. No information on P_n(0) from the RH analysis is needed.

**Labels.**

| Item | Statement (short) | Label |
|---|---|---|
| Lemma CP (§2.1) | σ ≥ 0 on [0, ∞), infinite support ⇒ all zeros of P_n are simple and in (0, ∞); (−1)^nP_n(0) > 0 | PROVED (self-contained) |
| Lemma CT (§2.2) | Christoffel transfer: α_n = g_n + h_n, β_n = g_{n−1}h_n; x·σ has α̃_n = g_n + h_{n+1}, β̃_n = g_nh_n | PROVED (self-contained; classical, novelty not claimed) |
| Lemma CS (§3.1) | n^pα_n → 2c, n^p√β_n → c (c > 0) ⇒ n^pg_n → c, n^ph_n → c | PROVED (self-contained); very likely KNOWN (chain sequences: Wall; Chihara 1978 Ch. I, III — not read, pointer only) |
| **Theorem SH** (§3.2) | Law P(c) for σ ⇒ Law P(c) for x·σ | PROVED (self-contained) |
| Lemma CS-r (§4.1) | rate r_n (regular) ⇒ \|n^pg_n − c\| = O(√r_n), \|n^pg_n − (n−1)^pg_{n−1}\| = O(r_n) | PROVED (self-contained) |
| **Theorem SH-r** (§4.2) | Law P(c) with rate r_n for σ ⇒ the same rate for x·σ (in particular O(1/n) ⇒ O(1/n)) | PROVED (self-contained) |
| Remark SH-1/n (§4.3) | exact identity n^p√β̃_n = n^p√β_n·κ_n^{1/2}(G_n/G_{n−1})^{1/2}; the 1/n coefficient of n^pb_n shifts by −p/2 iff n(G_n/G_{n−1} − 1) → 0 | identity and equivalence PROVED; the hypothesis NUMERICAL (p = 2); tilt-law transfer CONDITIONAL (implication PROVED) |
| **Corollary B_all** (§5) | p > 1, **every s > 1**, Ψ sequence-form slowly varying: n^pb_n → c(p), n^pa_n → 2c(p); rate O(1/n) if Ψ satisfies (H_an) | PROVED-mod-cite (inherits Theorem RII / Corollary B_{p>1}: WLXZ v1, KMVV §6, C–D, DLMF, G2 μ*, B*(i)–(ii)); the shift step PROVED. For s > 1 + p/2 only the \|α_x\| ≤ ½ part of RII (plus Lemma W′) is needed (§5, Rule R F2) |
| **GAP-α** (ROUTE2 §6) | the law for s ≥ 1 + 2p | **CLOSED for the law** (Corollary B_all). Still open: an RH analysis of the weight itself for α_x ≥ 1 (not needed for the law) |
| Route (a) frame change (§6) | Q·((z − a)/z)^{mσ₃} | not pursued; superseded for the law; HEURISTIC link to §2 recorded |
| GAP-rate | the 1/n coefficient (tilt law) | GAP; unchanged at the base, but **transferred** under SH if n(G_n/G_{n−1} − 1) → 0 (Remark SH-1/n) |

---

## 1. Setting and conventions

σ is a positive Borel measure on [0, ∞) with infinite support and finite moments (all measures here have support in
[0, 1]). P_n are the monic orthogonal polynomials, P_{−1} := 0, P_0 := 1,

  xP_n = P_{n+1} + α_nP_n + β_nP_{n−1}  (n ≥ 0),  β_n > 0 (n ≥ 1).

(Toolkit convention, `jacobi_asym.jacobi.result`: α_n = a[n], β_n = b2[n−1]. In the repo's 1-based notation b_n² = β_n
couples P_{n−1}, P_n, and a_n is α_{n−1} or α_n depending on the file.) **Index shifts are harmless here**: if
(n^pα_n, n^p√β_n) → (2c, c) with rate r_n, r_n regular in the sense of §4 (non-increasing, n·r_n non-decreasing), then the
same holds with n replaced by n ± 1, with rate O(r_n), because (n/(n ± 1))^p = 1 + O(1/n), 1/n ≤ r_n/r_1 and r_{n−1} ≤ 2r_n.
In particular RII's form "n^pb_n = c(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n)" is equivalent to |n^pα_n − 2c| + |n^p√β_n − c| =
O(1/n).

**Law P(c) for σ** (scale n^p, c > 0): n^pα_n → 2c and n^p√β_n → c. **With rate r_n**: |n^pα_n − 2c| + |n^p√β_n − c| ≤ Mr_n.

Measures: σ_s := Σ_{k≥1}k^{−s}Ψ(k)δ_{k^{−p}} (s > 1). **Shift identity:** x·σ_s = Σ k^{−p}k^{−s}Ψ(k)δ_{k^{−p}} = σ_{s+p}. This
holds exactly, also for every truncation k ≤ K. (Normalization of the measure does not change α_n, β_n.)

---

## 2. The Christoffel transfer

### 2.1 Lemma CP (zeros, PROVED)

Let σ be as in §1. Then P_n (n ≥ 1) has n simple zeros in (0, ∞). Hence (−1)^nP_n(0) > 0.

*Proof.* Let y₁ < … < y_m be the zeros of P_n in (0, ∞) of odd multiplicity, π(x) := ∏(x − y_j) (π := 1 if m = 0), and
suppose m < n. Then deg π < n, so ∫P_nπ dσ = 0. On (0, ∞), P_nπ does not change sign: every remaining factor of P_n is
(x − y)^{2j} (y real), (x − y) with y ≤ 0 (positive on (0, ∞)), or a pair (x − z)(x − z̄) = |x − z|² (z ∉ ℝ). Since P_n is
monic, P_nπ ≥ 0 on (0, ∞), hence on supp σ ⊂ [0, ∞) except possibly at 0, where P_nπ(0) is a finite value; P_nπ ≥ 0 on
[0, ∞) by continuity. P_nπ is a non-zero polynomial and σ has infinite support, so ∫P_nπ dσ > 0, a contradiction. So m = n:
P_n has n distinct zeros in (0, ∞), all simple, and P_n(0) = ∏(−y_j) has sign (−1)^n. ∎

### 2.2 Lemma CT (Christoffel transfer, PROVED)

Define g_n := −P_{n+1}(0)/P_n(0) > 0 (n ≥ 0; Lemma CP), h_0 := 0, h_n := β_n/g_{n−1} > 0 (n ≥ 1). Then

- (i) α_n = g_n + h_n (n ≥ 0) and β_n = g_{n−1}h_n (n ≥ 1). Equivalently g_0 = α_0, g_n = α_n − β_n/g_{n−1}.
- (ii) σ̃ := x·σ has infinite support, and its monic OPs are Q_n(x) := (P_{n+1}(x) + g_nP_n(x))/x, with Jacobi coefficients

    α̃_n = g_n + h_{n+1} (n ≥ 0),  β̃_n = g_nh_n (n ≥ 1).

*Proof.* (i) Evaluate the recurrence at x = 0: 0 = P_{n+1}(0) + α_nP_n(0) + β_nP_{n−1}(0). Divide by P_n(0) ≠ 0:
α_n = g_n − β_nP_{n−1}(0)/P_n(0) = g_n + β_n/g_{n−1} = g_n + h_n (n ≥ 1); for n = 0, α_0 = g_0 = g_0 + h_0.

(ii) supp σ̃ = supp σ ∖ {0} is infinite. P_{n+1} + g_nP_n vanishes at 0, so Q_n is a monic polynomial of degree n. For
j ≤ n − 1, ∫Q_nx^j dσ̃ = ∫(P_{n+1} + g_nP_n)x^j dσ = 0. So Q_n are the monic OPs of σ̃. Next, for n ≥ 1, P_n − Q_n has degree
≤ n − 1 and ∫(P_n − Q_n)x^j dσ̃ = ∫P_nx^{j+1}dσ − ∫Q_nx^jdσ̃ = 0 for j ≤ n − 2; hence P_n − Q_n = h′_nQ_{n−1} for a constant
h′_n. (P_0 = Q_0 = 1.) Then
  xP_n = xQ_n + h′_nxQ_{n−1} = (P_{n+1} + g_nP_n) + h′_n(P_n + g_{n−1}P_{n−1}),
and comparing with the recurrence (the P_j are linearly independent): α_n = g_n + h′_n, β_n = h′_ng_{n−1}; so h′_n = h_n by
(i). Finally
  xQ_n = P_{n+1} + g_nP_n = (Q_{n+1} + h_{n+1}Q_n) + g_n(Q_n + h_nQ_{n−1}),
so α̃_n = g_n + h_{n+1} and β̃_n = g_nh_n. ∎

(In matrix form: J = LU with L unit lower bidiagonal (subdiagonal h_n) and U upper bidiagonal (diagonal g_n, superdiagonal 1),
and J̃ = UL — the Darboux transformation. Not used beyond the formulas.)

*NUMERICAL check* (`check_r2alpha_christoffel.out`): [1] mpmath RKPW at 60 digits, K = 1200, n ≤ 300, for (p, s) = (2, 3)
with Ψ = 1 and Ψ = exp √log(k + e), (1.5, 2.5) with exp √log, (½, 1.5) with Ψ = 1: max relative difference between the
transferred coefficients and the directly computed coefficients of σ_{s+p} is ≤ 2·10⁻⁵⁹; min g_n, min h_n > 0. [2]
binary128 RKPW, K = 4·10⁴, n ≤ 600, s → s + 2 for s = 3, 4, 5 (p = 2): ≤ 8·10⁻¹⁶ (the floor set by passing the atoms and
weights to the kernel in double). (A first version computed the coefficients with the discretized Stieltjes procedure, which
is unstable for these clustered atoms; its O(1) discrepancies were an artefact of that procedure, not of Lemma CT.)

---

## 3. Law P transfers (no rate)

Notation: A_n := n^pα_n, B_n := n^p√β_n, G_n := n^pg_n, H_n := n^ph_n, κ_n := ((n − 1)/n)^p (n ≥ 1). Lemma CT(i) reads

  G_n + H_n = A_n,  G_{n−1}H_n = κ_nB_n²  (n ≥ 1)  (since n^ph_n(n − 1)^pg_{n−1} = n^{2p}β_n·κ_n).

### 3.1 Lemma CS (chain-sequence limit, PROVED)

If A_n → 2c and B_n → c with c > 0, then G_n → c and H_n → c.

*Proof.* *A priori bounds.* G_n, H_n > 0 (Lemma CP), so G_n < A_n and H_n < A_n; then G_{n−1} = κ_nB_n²/H_n > κ_nB_n²/A_n →
c/2. Hence there is n₁ with G_n ∈ [c/3, 3c] for n ≥ n₁.

*Recursion.* For n > n₁, G_n = A_n − κ_nB_n²/G_{n−1} = F(G_{n−1}) + η_n with F(G) := 2c − c²/G and
η_n := (A_n − 2c) − (κ_nB_n² − c²)/G_{n−1}, so |η_n| ≤ |A_n − 2c| + (3/c)|κ_nB_n² − c²| → 0. F is increasing on (0, ∞), and

  F(G) − G = −(G − c)²/G,  F(c + t) = c + ct/(c + t)  (t > −c).

Fix δ ∈ (0, c/3) and put d := δ²/(3c); for G ∈ [c/3, 3c] with |G − c| ≥ δ, F(G) − G ≤ −d. Take n₂ > n₁ with |η_n| <
min(d/2, δ) for n ≥ n₂.
- *Lower bound.* If G_m < c − δ for some m ≥ n₂, then G_{m+1} ≤ G_m − d + |η_{m+1}| < G_m − d/2 < c − δ, and by induction
  G_{m+j} < G_m − jd/2 → −∞, contradicting G > 0. So G_n ≥ c − δ for all n ≥ n₂.
- *Upper bound.* If G_n ≥ c + δ (n ≥ n₂), then G_{n+1} < G_n − d/2. If G_n < c + δ, then G_{n+1} < F(c + δ) + δ < c + 2δ
  (F increasing, F(c + δ) < c + δ). So the sequence cannot stay ≥ c + δ forever (it would decrease by d/2 per step while
  staying ≥ c/3), and once some G_m < c + δ (m ≥ n₂), we get G_n < c + 2δ for all n > m: by induction, if G_n < c + δ then
  G_{n+1} < c + 2δ, and if c + δ ≤ G_n < c + 2δ then G_{n+1} < G_n < c + 2δ.

So c − δ ≤ liminf G_n ≤ limsup G_n ≤ c + 2δ for every small δ: G_n → c, and H_n = A_n − G_n → c. ∎

*Why it works.* The limiting map F has a **double** (parabolic) fixed point at c, with F(G) ≤ G everywhere. A chain sequence
that settles below c would be pushed to 0 (impossible: g_n > 0 by Lemma CP); one above c is pulled down to c. So positivity
of g_n — i.e. supp σ ⊂ [0, ∞) — plus the law at σ determine the limit of n^pg_n. **No hard-edge information on P_n(0) is
needed.**

*Chain-sequence form (Rule R F1).* Put a_n := β_n/(α_{n−1}α_n) (n ≥ 1) and m_n := h_n/α_n (so 1 − m_n = g_n/α_n). Lemma CT(i)
gives a_n = (1 − m_{n−1})m_n with m_0 = 0, 0 < m_n < 1 (n ≥ 1): (a_n) is a chain sequence and (m_n) is its **minimal parameter
sequence** (Wall; Chihara, *An Introduction to Orthogonal Polynomials* (1978), Ch. I kernel polynomials and Ch. III chain
sequences — **not read**, pointer only). Law P gives a_n = κ_nB_n²/(A_{n−1}A_n) → ¼, and Lemma CS ⟺ m_n → ½: the parabolic
chain-sequence limit (the map m ↦ a/(1 − m) at a = ¼ has the double fixed point ½, and m_n < 1 is the barrier). Convergence
of parameter sequences of convergent chain sequences is classical, and this case is **very likely KNOWN**; not checked
(no Rule L). The proof above is self-contained and does not use that literature.

### 3.2 Theorem SH (shift lemma, PROVED)

Let σ be a positive measure on [0, ∞) with infinite support, p > 0 and c > 0. If σ satisfies Law P(c) (n^pα_n → 2c,
n^p√β_n → c), then so does σ̃ = x·σ. Consequently, for x_k = k^{−p}: Law P(c) for σ_s ⇒ Law P(c) for σ_{s+mp}, m = 1, 2, ….

*Proof.* Lemma CT(ii) and Lemma CS: n^pα̃_n = G_n + (n/(n + 1))^pH_{n+1} → 2c and n^{2p}β̃_n = G_nH_n → c². Iterate (each
x^jσ_s again has infinite support in [0, 1]). ∎

*Remarks.* (1) Only κ_n → 1 is used: n^p may be replaced by any scale s_n > 0 with s_{n−1}/s_n → 1 (with κ_n := s_{n−1}/s_n
and the factor (n/(n + 1))^p replaced by s_n/s_{n+1}). (2) The converse (Geronimus direction, σ̃ ⇒ σ) is **not** claimed;
it is not unique (σ = σ̃/x + mδ₀, any m ≥ 0) and not needed.

---

## 4. Rates

**Regular rates.** r_n > 0 is *regular* if r_n is non-increasing, n·r_n is non-decreasing, and r_n → 0. (Then 1/n ≤ r_n/r_1,
r_{n−1} ≤ 2r_n and r_n ≤ r_{n−1}.) Any rate ρ_n ↓ 0 with ρ_n ≥ 1/n has a regular majorant: r_n := max_{m≤n}(mρ_m)/n. (n·r_n
is non-decreasing by definition; r_{n+1} ≤ max(r_n·n/(n + 1), ρ_{n+1}) ≤ r_n since ρ_{n+1} ≤ ρ_n ≤ r_n; r_n ≥ ρ_n; and
r_n → 0: for m ≤ √n, mρ_m/n ≤ ρ_1/√n, and for √n < m ≤ n, mρ_m/n ≤ ρ_{⌈√n⌉}.) The rate 1/n is regular.

### 4.1 Lemma CS-r (PROVED)

Let r_n be regular and |A_n − 2c| + |B_n − c| ≤ Mr_n (n ≥ 1). Then |G_n − c| = O(√r_n) and |G_n − G_{n−1}| = O(r_n).

*Proof.* As in §3.1, with u_n := G_n − c and G_n ∈ [c/3, 3c] for n ≥ n₁. Now |κ_n − 1| ≤ p/(n − 1) = O(r_n) and
|B_n² − c²| = O(r_n), so |η_n| ≤ M₁r_n (n > n₁), and u_{n+1} = cu_n/(c + u_n) + η_{n+1} = u_n − u_n²/G_n + η_{n+1}.
- *Lower.* Let λ² := 6cM₁. If u_m ≤ −λ√r_m (m > n₁), then u_m²/G_m ≥ λ²r_m/(3c) = 2M₁r_m, so u_{m+1} ≤ u_m − M₁r_m ≤ u_m ≤
  −λ√r_m ≤ −λ√r_{m+1}. By induction u_{m+j} ≤ u_m − M₁Σ_{i<j}r_{m+i} → −∞ (Σr_n ≥ r_1Σ1/n = ∞), contradicting G > 0. So
  u_n ≥ −λ√r_n for n > n₁.
- *Upper.* By Lemma CS, u_n → 0; take n₃ > n₁ with |u_n| ≤ c/2 for n ≥ n₃ (so u_n > −c and G_n ≤ 2c there), and Λ > 0 with Λ²/(2c) ≥ 2M₁ + Λ/(2√r_1)
  (possible: the left side is quadratic in Λ). Put n₄ ≥ n₃ with Λ√r_n ≤ c for n ≥ n₄.
  (α) *Step.* If n ≥ n₄ and u_n ≤ t := Λ√r_n, then (u ↦ cu/(c + u) increasing on (−c, ∞)) u_{n+1} ≤ ct/(c + t) + M₁r_{n+1}
  ≤ t − t²/(2c) + M₁r_n = t − (Λ²/(2c) − M₁)r_n ≤ t − Λr_n/(2√r_1) (t ≤ c, choice of Λ). And t − Λ√r_{n+1} ≤ Λ√r_n(1 − √(n/(n + 1))) ≤ Λ√r_n/(2n) ≤ Λr_n/(2√r_1)
  (using r_{n+1} ≥ r_nn/(n + 1) and 1/n ≤ r_n/r_1 ≤ √r_n/√r_1). So u_{n+1} ≤ Λ√r_{n+1}.
  (β) *Entry.* If u_n > Λ√r_n for some n ≥ n₄, then (G_n ≤ 2c) u_n²/G_n ≥ u_n²/(2c) ≥ (Λ²/(2c))r_n ≥ 2M₁r_n, so u_{n+1} ≤ u_n − M₁r_n:
  u decreases by a non-summable amount while it stays above Λ√r_n ≥ 0. Hence some m ≥ n has u_m ≤ Λ√r_m, and (α) gives
  u_k ≤ Λ√r_k for all k ≥ m.
  So u_n = O(√r_n) from above as well (for n < m there are finitely many terms).
- Finally |G_n − G_{n−1}| ≤ u_{n−1}²/G_{n−1} + |η_n| = O(r_n). ∎

### 4.2 Theorem SH-r (PROVED)

Let r_n be regular. If σ satisfies Law P(c) with rate r_n, then x·σ satisfies Law P(c) with rate O(r_n). In particular
(r_n = 1/n): n^pb_n = c(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) for σ ⇒ the same for x·σ.

*Proof.* n^p√β̃_n = √(G_nH_n) = B_n(κ_nG_n/G_{n−1})^{1/2} = c + O(r_n), since B_n = c + O(r_n), κ_n = 1 + O(1/n), and
G_n/G_{n−1} = 1 + O(r_n) (Lemma CS-r, G ≥ c/3). n^pα̃_n = G_n + (n/(n + 1))^p(A_{n+1} − G_{n+1}) = A_{n+1} − (G_{n+1} − G_n) +
O(1/n) = 2c + O(r_n). ∎

Note what is used: the rate on |u_n| is only O(√r_n) (which is all the elementary argument gives), but only the
**increments** G_n − G_{n±1} = O(r_n) enter the transferred coefficients; u_n itself enters only through u_n²/G = O(r_n)
inside those increments.

### 4.3 Remark SH-1/n (the 1/n coefficient)

Exact identity (Lemma CT): n^p√β̃_n = n^p√β_n·κ_n^{1/2}(G_n/G_{n−1})^{1/2}, κ_n^{1/2} = 1 − p/(2n) + O(n^{−2}). Hence, if the
law at σ holds with rate O(1/n),

  n(n^p√β̃_n/c − 1) − n(n^p√β_n/c − 1) = −p/2 + (n/2)(G_n/G_{n−1} − 1) + O(1/n),

so **the 1/n coefficient of n^pb_n shifts by exactly −p/2 iff n(G_n − G_{n−1}) → 0** (PROVED as an equivalence; the
hypothesis is not proved). The pure-power value d₁ = −(s − 1)/2 (Plan 10 Phase 0) shifts by −p/2 under s ↦ s + p, which is
consistent; and the tilt law (ROUTE2 §5, CONJECTURE) n(n^pb_n/c − 1) = −(s − 1 − ϑ_n)/2 + o(ϑ_n) is mapped to itself at s + p
if n(G_n − G_{n−1}) = o(ϑ_n). Precisely (Rule R F5; implication PROVED, conclusion CONDITIONAL): if the tilt law holds at s,
n(G_n − G_{n−1}) = o(ϑ_n) and nϑ_n → ∞ (so that the O(1/n) remainder is o(ϑ_n); true for exp √log, ϑ_n ≍ (log n)^{−1/2}),
then the tilt law holds at s + p with the same ϑ_n (same Ψ). So the tilt law for s ∈ (1, 1 + 2p) would give it for all
s > 1, CONDITIONAL on that hypothesis at each step.
NUMERICAL (`check_r2alpha_law.out`, p = 2): dB := n(n^pb_n/c − 1)|_{s} − (same)|_{s−2} = −0.980 … −0.983, −0.990 … −0.992, −0.995 (n =
100, 200, 400; s = 5 and 6, Ψ = 1 and exp √log; K-stable to 2·10⁻³), i.e. → −p/2 = −1. The chain sequence itself is much closer
to c than Lemma CS-r guarantees: e_n := ½log(g_n/h_n) satisfies n·e_n ≈ 0.50, 1.48, 2.46, 3.44 at n = 100 for the bases
s = 3, 4, 5, 6 (Ψ = 1; ≈ s − 5/2 for p = 2). K-convergence (Rule R F3): at n = 100 for all bases, and at n = 200 only for
s ≥ 4 (for s = 3, n·e_200 = 0.676, 0.543, 0.509 at K = 6, 12, 24·10⁴), since P_n(0) is tail-sensitive. This is **consistent
with** e_n = O(1/n) rather than O(n^{−1/2}) on these n only; no formula and no asymptotic claim is made.

---

## 5. Corollary B_all: Law P for all s > 1, p > 1, Ψ slowly varying (closes GAP-α for the law)

**Corollary B_all (PROVED-mod-cite; the citations are those of Theorem RII / Corollary B_{p>1}).** Let p > 1, s > 1, and
Ψ > 0 slowly varying in sequence form (PROOF.md §3.8/§3.14: δ_n(λ) → 0 for every λ ≥ 1; no boundedness, no D(γ) < ∞; e.g.
exp(√log k), exp((log k)^θ) (θ < 1), exp(√log k·sin log log k)). Then

  n^pb_n(k^{−s}Ψ) → c(p),  n^pa_n(k^{−s}Ψ) → 2c(p),

with rate O(r_n), r_n the regular majorant (§4) of 1/n + ρ(⌈n/M₀⌉) (ρ the RedA smoothing error of Ψ, M₀ = M₀(p)). If Ψ
satisfies (H_an) itself (e.g. exp √log(k + e)), the rate is O(1/n): n^pb_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n) — the
conclusion of Theorem RII for **every s > 1**.

*Proof.* Let m ≥ 0 be the least integer with s₀ := s − mp < 1 + 2p. If m ≥ 1 then s − (m − 1)p ≥ 1 + 2p, so s₀ ≥ 1 + p > 1;
if m = 0 then s₀ = s > 1. So s₀ ∈ (1, 1 + 2p) and Corollary B_{p>1} (resp. Theorem RII under (H_an)) gives Law P(c(p)) for
σ_{s₀} with rate 1/n + ρ(⌈n/M₀⌉) (resp. 1/n), hence with the regular rate r_n ≥ that rate. σ_s = x^mσ_{s₀} (§1). Apply Theorem
SH-r m times (each x^jσ_{s₀} = σ_{s₀+jp} is a positive measure on [0, 1] with infinite support; the regular rate is kept up to
constants). The index conventions are immaterial (§1). ∎

Remarks.
- *Dependency footprint (Rule R F2).* Any half-open s-window of length p inside (1, 1 + 2p) serves as a base. For
  s > 1 + p/2 one may take s₀ := the unique point of s − pℕ₀ in (1 + p/2, 1 + 3p/2], i.e. α_x ∈ (−½, ½]; on that window
  Theorem RII is covered by the **original** UR′ argument (|α_x| ≤ ½), so for every s > 1 + p/2 Corollary B_all does not
  depend on UR′(b′) (Plan 48 Rule R F1) at all. UR′(b′) is needed only for 1 < s ≤ 1 + p/2, which is Corollary B_{p>1}'s own
  range. Lemma W′ (α_x = 0) cannot be avoided: every α-window of length 1 in (−1, 1) contains 0, and for s ∈ 1 + p + pℕ₀ the
  chain passes through α_x = 0. (The proof above, with m least, uses s₀ ∈ [1 + p, 1 + 2p); both choices are valid since RII is
  REVIEWED for all |α_x| < 1.) A base window of length < p would leave gaps.
- What remains of GAP-α is only the RH analysis of the weight k^{−s}Ψ itself for α_x ≥ 1 (e.g. to compute the 1/n term by
  Route II, or QL along the path). The law does not need it.
- p ≤ 1 (WP5): Theorem SH applies to every p > 0, but there is no base case for slowly varying Ψ with D(γ) = ∞ at p ≤ 1
  (Route II needs p > 1); it would transfer one if found. For pure powers and for bounded / log-type Ψ the law is already
  known for all s > 1 (RH_px, RH₁(r), RH_plt1b; T3-all, T3-log), so SH adds nothing there.
- SH is not specific to Route II: any statement "Law P (with a regular rate) for σ_s, s in an interval of length ≥ p"
  propagates to all larger s. SH is node-agnostic (any atoms x_k > 0: the law for (x_k, w_k) ⇒ the law for (x_k, x_kw_k)), works
  for every p > 0 and every scale s_n with s_{n−1}/s_n → 1; so any future base case at p ≤ 1 (or for other node families)
  propagates upward in s (Rule R F6).

---

## 6. Route (a): the frame change Q·((z − a)/z)^{mσ₃} (evaluated, not pursued)

ROUTE2 §6 sketched fixing the exponents at 0 by Q ↦ Q·((z − a)/z)^{mσ₃}, at the price of a pole at a. On the RH side,
multiplying the weight by x corresponds to a Schlesinger (discrete Darboux) transformation of the RH problem: left
multiplication of Y_σ by a matrix R(z) rational in z, built from the values of Y_σ at z = 0 (the Christoffel–Darboux kernel
at 0), i.e. from P_n(0), P_{n+1}(0) — the quantities g_n of Lemma CT — together with the change x of the jump. Route (b) does the same transformation on the coefficient side, where the only data needed
(n^pg_n → c, and increments O(r_n)) follow from the law itself (Lemma CS, CS-r). Route (a) would need the hard-edge asymptotics
of Y_σ(0) with an error term from the comparison problem, which Theorem C′/Proposition D′ do not provide pointwise at z = 0.
So (a) is **superseded for the law** and was not pursued; the identification "frame change ↔ Christoffel step" is HEURISTIC
(not checked against a source). OBSTRUCTION for (a) as an RH argument (heuristic, scoped to this route): the comparison
estimates of ROUTE2 §4 control Q in L² of the contour, not at the point z = 0 where the Schlesinger factor is anchored.

---

## 7. Numerics (NUMERICAL; `checks/check_r2alpha_law.out`)

p = 2, s = 5, 6 (α_x = 1, 3/2: outside RII's range), Ψ = 1 and Ψ = exp √log(k + e); long double RKPW, K = 6·10⁴, 1.2·10⁵,
2.4·10⁵. Columns nB := n(n^pb_n/c − 1) (b_n = √b2[n−1]) and E := n(a[n]/(2√b2[n]) − 1) (check_fine pairing).

| Ψ | s | nB (n = 100, 200, 400) | E (n = 100, 200, 400) |
|---|---|---|---|
| 1 | 5 | −1.973, −1.986, −1.993 | 1.004, 1.002, 1.001 |
| 1 | 6 | −2.462, −2.481, −2.491 | 1.025, 1.013, 1.007 |
| exp √log | 5 | −1.864, −1.882, −1.894 | 1.001, 1.001, 1.000 |
| exp √log | 6 | −2.354, −2.377, −2.391 | 1.021, 1.011, 1.006 |

(For the s = 5, 6 rows of this table, K = 1.2·10⁵ vs 2.4·10⁵ differ by ≤ 6·10⁻⁴ (nB) and ≤ 10⁻³ (E) at n ≤ 400. For the
bases s = 3, 4, which enter dB, the differences at n = 400 are 2–3·10⁻³ (e.g. Ψ = 1, s = 3: nB −1.0002 vs −0.9982, E 1.0008
vs 0.9981); dB itself is K-stable to 2·10⁻³ (Rule R F3); n = 800 is not K-converged — e.g. Ψ = 1, s = 5: −2.013 vs −1.999 —
and is not used.) The law holds with bounded n·deviation, consistent with Corollary B_all's O(1/n). Pure power: nB → −(s − 1)/2
= −2, −2.5 (Plan 10 Phase 0's d₁); exp √log: close to the tilted baseline −(s − 1 − ϑ_n)/2 = −1.887, −1.893, −1.899 (s = 5)
and −2.387, −2.393, −2.399 (s = 6), ϑ_n = L′(log n), as at s = 2 (ROUTE2 §5). E → p/2 = 1 for all s. dB and e_n: §4.3.

---

## 8. Rule A (adversarial pass)

- (a) *Two-point / finite measures.* CT needs infinite support (P_n for all n). For a K-atom truncation the identity holds for
  n < K − 1 and is what check [1]–[2] verify (exactly, to 10⁻⁵⁹).
- (b) *Mass at 0.* Lemma CP's proof allows σ({0}) > 0 (P_nπ ≥ 0 on [0, ∞)); x·σ simply loses that atom. Fine.
- (c) *c = 0 or ∞.* Lemma CS uses c > 0 (the lower bound G_{n−1} > κB²/A → c/2 > 0, and the map F). Not needed otherwise.
- (d) *Could G_n converge to something else, or oscillate?* F's only fixed point is c (F(G) = G ⟺ (G − c)² = 0); oscillation
  is excluded by the monotone-band argument. Tested: numerically G_n/c − 1 = O(1/n) (§4.3).
- (e) *Rate loss.* Lemma CS-r gives only |u_n| = O(√r_n). The transferred coefficients involve u_n only through increments
  and through u_n² (a-law), both O(r_n): no rate loss. **The O(√r_n) bound is sharp** under the lemma's hypotheses (Rule R F4):
  take G_n := c + a/√n (a > 0), B_n := c, A_n := G_n + κ_nc²/G_{n−1}; then g_n, h_n > 0, so (Favard + LU positivity) these are
  the coefficients of a positive measure on [0, ∞), A_n − 2c = (a²/c − pc)/n + O(n^{−3/2}) = O(1/n), yet G_n − c ≍ n^{−1/2}.
  So the "only increments enter" structure of SH-r is essential. The pure-power data have u_n = O(1/n) (§4.3). A sign error in κ_n or an index slip would show as a dB ≠ −p/2; the
  numerics give −0.995 → −1.
- (f) *Converse.* Not used; it can fail to be unique (Geronimus parameter m).
- (g) *Is the shift identity exact?* x_kw_k = k^{−p}k^{−s}Ψ(k): yes, with the same Ψ. Corollary B_{p>1} already gives the
  law for σ_{s₀} with the original Ψ (RedA is used inside it); SH is then applied to σ_{s₀}(Ψ) itself, so no smoothing
  interacts with the shift.
- (h) *Generality check.* p = ½ in check [1] (transfer exact) — SH holds for every p > 0; the corollary is stated only for
  p > 1 because the base (RII) is.
- No counterexample found.
