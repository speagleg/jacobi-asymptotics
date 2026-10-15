# UL: uniformity in s for the pure powers — the Cesàro s-law, a uniform Law P, and (UΛ) (Plan 64)

Status (2026-10-15): written by the Plan 64 agent; Rule R: research/G1/review/REVIEW_Plan64.md, ACCEPT WITH FIXES; fixes
F1–F12 applied; **not REVIEWED** until the diff check (then: REVIEWED, with REVIEW_Plan64.md). Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert. This file upgrades SECOND.md §3.3–3.4 (Theorem 3.8, Corollary 3.9, Theorem 3.10(d)) and
settles hypothesis (UΛ) of SECOND §3.3 in its stated (o(log n)) form. The integration into SECOND.md and THEOREMS.md
is recorded in §7. No external source was newly read: every input is an internal result of G1 PROOF.md or SECOND.md,
which carry their own citations (RH/CITATIONS.md).

**Summary of labels.** Setting of SECOND §0: σ_s := σ_{p,s} = Σ_{k≥1}k^{−s}δ_{x_k}, x_k = k^{−p}, p > 0 fixed, s > 1;
h_n(s) = ∫π_n²dσ_s; μ_n^{(s)}(k) = k^{−s}π_n^{(s)}(x_k)²/h_n(s); c = c(p);
**F_n(s) := log h_n(s) + s·log n** (n ≥ 1); Λ_n(s) = Σ_k log(k/n)μ_n^{(s)}(k) = −F_n′(s) (Prop 3.7). K ⊂ (1, ∞) is a
compact interval.

| # | Statement | Label |
|---|---|---|
| Lemma V | variational sandwich: −log E_t[(k/n)^{s−t}] ≤ F_n(s) − F_n(t) ≤ log E_t[(k/n)^{t−s}] (E_t := E_{μ_n^{(t)}}), all n, s, t | PROVED (elementary) |
| Thm UF | sup_{n≥1} sup_{s,s′∈K}\|F_n(s) − F_n(s′)\| < ∞ | PROVED-mod-cite (Law P and QLP(c) at finitely many fixed σ) |
| Lemma W | for fixed t, E_t[g(n^px)] → ∫g dν_arc for continuous g with \|g(y)\| ≤ C(y^{−a} + y^b), pa < min(p/2, t − 1), b < 2 | PROVED-mod-cite (Lemma LP's weak convergence; QLP(c); Law P) |
| **Thm UF-lim** | F_n(s) − F_n(s₀) → ((s − s₀)/p)·log c(p), **uniformly** for s, s₀ ∈ K; i.e. h_n(s)/h_n(s₀) = c^{(s−s₀)/p}n^{−(s−s₀)}(1 + o(1)) | PROVED-mod-cite ((P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma W; Lemma CS) |
| **Cor UL-3.8** | Σ_{j≤n}log(b_j(s₁)/b_j(s₀)) = −((s₁ − s₀)/2)log n + ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1), every p > 0, s₀, s₁ > 1 (SECOND Thm 3.8 with O(1), in fact with the limit) | PROVED-mod-cite |
| Cor UL-3.9 | (E) at s₀ and s₁ ⇒ d₁(s₁) − d₁(s₀) = −(s₁ − s₀)/2; with the anchors, d₁(2, s) = d₁(1, s) = −(s − 1)/2 for every s > 1 under (E) at s | CONDITIONAL on (E) only (+ PROVED-mod-cite) |
| **Cor UL-3.10** | for every p > 0 and s, s₀ > 1: 𝒟_n(p, s) − 𝒟_n(p, s₀) + ((s − s₀)/2)log n → ((s−s₀)/(2p))log c − ½log(ζ(s)/ζ(s₀)). Hence σ_{2,s} and σ_{1,s} have log-average coefficient −(s − 1)/2 for **every** s > 1 (𝒟_n + ((s−1)/2)log n convergent) | PROVED-mod-cite (UF-lim; SECOND §2 Input (VA, DLMF-Lommel); SECOND Cor 3.6(i) (RH_p1 §1, DLMF 5.11)) |
| **Thm UP** | uniform Law P on compacts: sup_{s∈K}\|n^pb_n(s) − c\|, \|n^pg_n(s) − c\|, \|n^pα_n(s) − 2c\| → 0 | PROVED-mod-cite (Thm UF-lim, hence (P), (LP), (QLP-c) at fixed points; Lemma CT) |
| Prop UΛ⁻ | inf_{s∈K}Λ_n(s) ≥ −C for all n | PROVED-mod-cite |
| **Thm UΛ** | (UΛ) of SECOND §3.3 holds on every K: sup_{s∈K}\|Λ_n(s)\| = o(log n) | PROVED-mod-cite (Thm UP; Lemma LP's method; Lemma TL) |
| Prop UΛ-L¹ | Λ_n(s) → −(log c)/p for each s, and ∫_K\|Λ_n(s) + (log c)/p\|ds → 0 | PROVED-mod-cite |
| (UΛ-O(1)) | sup_K\|Λ_n\| = O(1) | **GAP**; ⇐ (RU) (uniform QLP(c); PROOF SKETCH level, Audit U), ⇐ (SCVX), ⇐ (CVX) (Prop R) |
| (SCVX) | ∃C, n₀: (log h_n)″ ≥ −C on K for n ≥ n₀ | HYPOTHESIS (⇐ (CVX)) |
| Prop SV | ∂_s²log h_n = Σ_{j>n}f_{nj}² − Σ_{i<n}f_{in}², f_{ij} := ⟨P_i, (log k)P_j⟩_{σ_s} | PROVED (elementary) |
| Remark CVX-fin | for the N-atom truncation of σ_s, (log h_{N−1})″ < 0: (CVX) is not a structural property of the family x^{s/p}dσ₀ | PROVED |
| (CVX) for σ_{p,s} | | HYPOTHESIS (unchanged); NUMERICAL; no longer needed for Thms 3.8–3.10 |

Novelty: UNCHECKED throughout (no Rule L search). Lemma V (minimum/duality sandwich) and Prop SV (second variation
of log h_n) are elementary variational computations; novelty not claimed.

Checks: `checks/check_ul.py` (.out), NUMERICAL sanity checks of Lemma V, Prop SV, Remark CVX-fin, Thms UF/UF-lim/UP (§6).

## 0. Inputs (all internal; each carries its own label)

- **(P) Law P for σ_{p,t}, each fixed t > 1**: n^pb_n(t) → c, n^pα_n(t) → 2c. PROVED-mod-cite (Paper 2 Cor. thm:pure;
  RH_p (p > 1), RH₁(r) (p = 1), RH_plt1b (0 < p < 1)); as used in SECOND Thm 3.2 and G1 Lemma LP.
- **(LP) weak convergence** (G1 PROOF §3.8, proof of Lemma LP; PROVED-mod-cite (P) + method of moments, REVIEWED): for fixed
  t, the image ν_n^{(t)} of μ_n^{(t)} under k ↦ Y := n^px_k = (n/k)^p converges weakly to the arcsine law ν_arc on
  [0, 4c], density 1/(π√(y(4c − y))). The proof only uses that n^pα_m → 2c and n^pb_m → c for |m − n| ≤ j, j fixed; we
  reuse this ("LP's method") with s varying in Thm UΛ.
- **(QLP-c)** (G1 PROOF §3.16, Theorem QLP(c); PROVED-mod-cite for each fixed σ, REVIEWED): for fixed t and every
  ϑ < ϑ(p, t) := min(p/2, t − 1) there are C_ϑ, n₀ with μ_m^{(t)}((Mn, ∞)) ≤ C_ϑM^{−ϑ} for all M ≥ 1, n ≥ n₀,
  m ∈ {n − 1, n}. Only fixed t are ever used (finitely many for each grid; countably many in UF-lim); **no uniformity in σ, so (RU) is not used**.
- **(CS/CT)** (G1 §3.21, Lemmas CT, CS, PROVED, REVIEWED; SECOND §0, Prop 3.1, Thm 3.2): with the chain
  g_n := −π_{n+1}(0)/π_n(0), h_n^{ch} := b_n²/g_{n−1}: α_n = g_n + h_n^{ch}; and h_n(s + p)/h_n(s) = g_n(s) (SECOND Prop
  3.1: Π_{m≤n}(b_m(s+p)/b_m(s))² = g_n/g_0 with g_0 = ζ(s+p)/ζ(s), and h_n(s) = ζ(s)Π_{m≤n}b_m(s)²); n^pg_n(t) → c
  for each fixed t (SECOND Thm 3.2's proof).
- **(TL)** (G1 §3.4, Lemma TL, PROVED, REVIEWED) with w = k^{−s} (sandwich constants c = C = 1): for n ≥ 2,
  T′ := ⌈8pn²⌉, T″ := ⌈T′n^{2/p}⌉ and every k ≥ T″, ρ_{n+1}^{(s)}(k) ≤ 1156(T″/k)^s; and μ_n ≤ ρ_{n+1} pointwise.
- **Prop 3.7** (SECOND, PROVED): s ↦ h_n(s) is real-analytic on (1, ∞), ∂_slog h_n = −L_n, so F_n′ = −Λ_n.

## 1. The variational sandwich and the bounded form

**Lemma V (PROVED, elementary).** For n ≥ 1 and s, t > 1, with E_t := E_{μ_n^{(t)}} (values in (0, ∞]),

  (U) F_n(s) − F_n(t) ≤ log E_t[(k/n)^{t−s}],   (D) F_n(s) − F_n(t) ≥ −log E_t[(k/n)^{s−t}].

*Proof.* Write π_t := π_n^{(t)}, ⟨·,·⟩_s for the inner product of L²(σ_s).
(U) h_n(s) is the minimum of ∫π²dσ_s over monic π of degree n (π = π_n^{(s)} + r with deg r < n gives
∫π²dσ_s = h_n(s) + ∫r²dσ_s). Taking π = π_t: h_n(s) ≤ Σ_kk^{−s}π_t(x_k)² = h_n(t)E_t[k^{t−s}]. Add s·log n − t·log n
to the logarithms.
(D) If E_t[k^{s−t}] = ∞ there is nothing to prove. Otherwise put φ(x_k) := k^{s−t}π_t(x_k). Then
‖φ‖_s² = Σ_kk^{−s}k^{2(s−t)}π_t(x_k)² = h_n(t)E_t[k^{s−t}] < ∞, and for every polynomial P,
⟨P, φ⟩_s = Σ_kk^{−t}P(x_k)π_t(x_k) = ⟨P, π_t⟩_t (absolutely convergent: polynomials are bounded on [0, 1]). Hence φ ⊥_s
P_{n−1} and ⟨x^n, φ⟩_s = ⟨π_t, π_t⟩_t = h_n(t). Write x^n = π_n^{(s)} + r, deg r < n: ⟨x^n, φ⟩_s = ⟨π_n^{(s)}, φ⟩_s ≤
h_n(s)^{1/2}‖φ‖_s. So h_n(t)² ≤ h_n(s)·h_n(t)E_t[k^{s−t}], i.e. h_n(s) ≥ h_n(t)/E_t[k^{s−t}]. ∎

In terms of Y := n^px_k = (n/k)^p: (k/n)^{t−s} = Y^{(s−t)/p} and (k/n)^{s−t} = Y^{−(s−t)/p}. So for s ≥ t, (U) involves a
**positive** moment of Y under μ_n^{(t)} (the band side, controlled by Law P) and (D) a **negative** one (the hard edge,
controlled by QLP(c)); both at the single base point t.

**Theorem UF (PROVED-mod-cite: (P), (QLP-c) at finitely many fixed points).** Let p > 0 and K = [a, b] ⊂ (1, ∞). Then
C_K := sup_{n≥1}sup_{s,s′∈K}|F_n(s) − F_n(s′)| < ∞.

*Proof.* Put u₀ := ½min(p/2, a − 1) and ϑ₀ := ¾min(p/2, a − 1); for every t ∈ K, u₀ < ϑ₀ < ϑ(p, t), and u₀ ≤ p/4.
Choose a grid a = t_0 < t_1 < … < t_J = b with t_{i+1} − t_i ≤ u₀. For each of the finitely many t = t_i:
- A_t := sup_{n≥1}n^pα_n(t) < ∞ by (P) (finitely many n are finite).
- B_t := sup_{n≥1}E_t[(k/n)^{u₀}] < ∞. For n ≥ n₀(t), by (QLP-c) with ϑ = ϑ₀ and Tonelli,
  E_t[(k/n)^{u₀}] ≤ 1 + Σ_{k>n}μ_n(k)(1 + ∫_1^{k/n}u₀M^{u₀−1}dM) ≤ 2 + ∫_1^∞u₀M^{u₀−1}C_{ϑ₀}M^{−ϑ₀}dM
  = 2 + C_{ϑ₀}u₀/(ϑ₀ − u₀). For n < n₀ each term is finite because t − u₀ > 1.
Let s ∈ [t_i, t_{i+1}], t := t_i, r := (s − t)/p ∈ [0, ¼]. By (U) and Jensen (y ↦ y^r concave),
F_n(s) − F_n(t) ≤ log E_t[Y^r] ≤ r·log E_t[Y] = r·log(n^pα_n(t)) ≤ ¼log⁺A_t (E_t[x] = α_n(t)). By (D), using
y^{pr} ≤ 1 + y^{u₀} for y > 0, 0 ≤ pr ≤ u₀: F_n(s) − F_n(t) ≥ −log(1 + B_t). So |F_n(s) − F_n(t_i)| ≤ c_i on the cell,
uniformly in n, and chaining over the J cells gives |F_n(s) − F_n(a)| ≤ Σ_ic_i for all s ∈ K. ∎

*Remark.* The step restriction is necessary for this argument: E_t[(k/n)^u] = ∞ for u ≥ t − 1 (μ_n(k) ≍ k^{−t} as k → ∞),
and for u ≥ p/2 it is not bounded in n: liminf_n E_t[(k/n)^u] ≥ ∫y^{−u/p}dν_arc = ∞ (Lemma LP's weak convergence and
Fatou; the arcsine density is ≍ y^{−1/2} at 0). Chaining through fixed intermediate points
replaces any uniformity in s.

## 2. The limit: the Cesàro s-law with exact constant

**Lemma W (PROVED-mod-cite: (LP), (QLP-c), (P)).** Fix t > 1, and let g be continuous on (0, ∞) with
|g(y)| ≤ C(y^{−a} + y^b), where a ≥ 0, pa < ϑ(p, t), 0 ≤ b < 2. Then E_t[g(Y)] → ∫g dν_arc (Y = n^px under μ_n^{(t)}).

*Proof.* Choose a′ with a < a′ and pa′ < ϑ(p, t). Then V₋ := sup_{n≥n₀}E_t[Y^{−a′}] < ∞ (as for B_t above, with
u = pa′) and V₊ := sup_nE_t[Y²] = sup_nn^{2p}(α_n² + b_n² + b_{n+1}²)(t) < ∞ by (P) (E_t[x²] = (J²)_{nn}). The arcsine law
has the same two bounds (its density is ≍ y^{−1/2} at 0 and pa′ < p/2, i.e. a′ < ½; compact support). For 0 < ε < 1 < R
let g_{ε,R}(y) := g(min(max(y, ε), R)), bounded and continuous on [0, ∞); ν_n^{(t)} lives on (0, ∞) and ν_arc has no atom
at 0, so E_t[g_{ε,R}(Y)] → ∫g_{ε,R}dν_arc by (LP). For any of these measures,
E|g − g_{ε,R}| ≤ E[(|g(Y)| + |g(ε)|)1_{Y<ε}] + E[(|g(Y)| + |g(R)|)1_{Y>R}]. On Y < ε: |g(Y)| + |g(ε)| ≤ 2C(Y^{−a} +
ε^{−a} + 1) ≤ 2C(2 + 1)Y^{−a′}ε^{a′−a} (Y^{−a} ≤ Y^{−a′}ε^{a′−a}, ε^{−a} ≤ Y^{−a′}ε^{a′−a}, 1 ≤ Y^{−a′}ε^{a′}); so this part is
≤ 6CV₋ε^{a′−a}. On Y > R, likewise ≤ 6CV₊R^{b−2}. Both → 0 uniformly in n as ε → 0, R → ∞. ∎

Let φ(r) := log ∫Y^r dν_arc (r > −½). It is finite and C² on [−¼, ¼], convex, φ(0) = 0, φ′(0) = ∫log Y dν_arc, and
|φ(r) − rφ′(0)| ≤ A₀r² on [−¼, ¼] with A₀ := ½max_{[−¼,¼]}φ″ < ∞ (differentiation under the integral is dominated by
Y^{±1/4}(1 + log²Y), ν_arc-integrable; φ″ is a variance under the tilted law, bounded by ∫Y^r log²Y/∫Y^r).

**Theorem UF-lim (PROVED-mod-cite: (P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; (CS)).** For every p > 0 and
compact K ⊂ (1, ∞),

  sup_{s,s₀∈K} |F_n(s) − F_n(s₀) − ((s − s₀)/p)·log c(p)| → 0  (n → ∞).

Equivalently h_n(s)/h_n(s₀) = c(p)^{(s−s₀)/p}·n^{−(s−s₀)}·(1 + o(1)), uniformly on K × K.

*Proof.* Enlarge K so that b ≥ a + p (harmless). Let 0 < u ≤ u₀ (u₀ as in Theorem UF), r_u := u/p ≤ ¼, and take the grid
t_i = a + iu (last cell shorter). For the cell [t_i, t_{i+1}] and n ≥ 1 put φ_n(r) := log E_{t_i}[Y^r]: convex
(Hölder), φ_n(0) = 0, finite for |r| ≤ r_u (Theorem UF's proof). For s in the cell, r := (s − t_i)/p ∈ [0, r_u],
Lemma V and convexity give

  −(r/r_u)φ_n(−r_u) ≤ −φ_n(−r) ≤ F_n(s) − F_n(t_i) ≤ φ_n(r) ≤ (r/r_u)φ_n(r_u).

By Lemma W (g(y) = y^{±r_u}: pa = u < ϑ(p, t_i), b = r_u < 2), φ_n(±r_u) → φ(±r_u) = ±r_uφ′(0) + e_±, |e_±| ≤ A₀r_u². Hence
|F_n(s) − F_n(t_i) − rφ′(0)| ≤ (r/r_u)(A₀r_u² + η_{n,i}) with η_{n,i} → 0, uniformly for s in the cell. Summing over the
cells between a and s (finitely many for fixed u):

  limsup_n sup_{s∈K}|F_n(s) − F_n(a) − ((s − a)/p)φ′(0)| ≤ A₀r_u·(b − a)/p = A₀u(b − a)/p².

u is arbitrary in (0, u₀], so the limsup is 0. Finally, at s = a + p, F_n(a + p) − F_n(a) = log(h_n(a+p)/h_n(a)) + p log n
= log(n^pg_n(a)) → log c by (CS). So φ′(0) = log c (consistent with the direct value ∫log y dν_arc = log(4c) − 2log 2 = log c,
not needed). Differences of two points of K follow. ∎

*Remarks.* (i) Theorem UF follows again from UF-lim (plus continuity in s for each finite n); its separate proof needs only
boundedness. (ii) The case s − s₀ = p is SECOND Theorem 3.2; UF-lim interpolates it to all real shifts. (iii) Numerically
(`checks/check_ul.out` [4], p ∈ {1, 2}, s ∈ [3/2, 4] step ¼, n ≤ 400) sup_s|F_n(s) − F_n(3/2) − (s − 3/2)log c/p| =
2.8·10⁻³ (p = 1) and 6.6·10⁻³ (p = 2) at n = 400, halving with each doubling of n (an O(1/n) rate is suggested, not proved).

## 3. Consequences for SECOND §3.3–3.4

**Corollary UL-3.8 (SECOND Theorem 3.8, unconditional and with the constant; PROVED-mod-cite as UF-lim: (P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; (CS)).** For p > 0 and
s₀, s₁ > 1:

  Σ_{j=1}^n log(b_j(s₁)/b_j(s₀)) = −((s₁ − s₀)/2)log n + ½log(c(p)^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1).

*Proof.* h_n(s) = ζ(s)Π_{j≤n}b_j(s)², so 2Σ_{j≤n}log(b_j(s₁)/b_j(s₀)) = F_n(s₁) − F_n(s₀) − (s₁ − s₀)log n −
log(ζ(s₁)/ζ(s₀)); apply UF-lim. ∎ (s₁ − s₀ = p recovers Theorem 3.2's constant ½log(cζ(s)/ζ(s + p)).)

**Corollary UL-3.9 (SECOND Corollary 3.9 without (UΛ)/(CVX); CONDITIONAL on (E) at the points named, + PROVED-mod-cite).**
If (E) holds at s₀ and s₁, then d₁(s₁) − d₁(s₀) = −(s₁ − s₀)/2. Hence: p = 2: d₁(2, s) = −(s − 1)/2 under (E) at s
(the anchor s₀ = 2 is exact, SECOND Thm 2.3); p = 1: d₁(1, s) = −(s − 1)/2 under (E) at s (SECOND's (O1): the anchor
s₀ = 3/2 enters through Thm 3.10(b), so (E) at 3/2 is not needed — see Cor UL-3.10); every p: d₁(p, s) = −(s − 1)/2 + g(p)
with g(p) independent of s, under (E) at the points used. g(p) = 0 for p ∉ {1, 2} remains GAP.
*Proof.* Under (E) at s₀, s₁ the left side of Cor UL-3.8 is (d₁(s₁) − d₁(s₀))log n + O(1). For p = 1 use Cor UL-3.10:
under (E) at s, 𝒟_n(1, s) = d₁(1, s)log n + O(1) and = −((s − 1)/2)log n + O(1). ∎

Recall 𝒟_n(p, s) := Σ_{j≤n}log(j^pb_j(s)/c) = ½log h_n(s) − ½log ζ(s) + p log n! − n log c (SECOND §3.4).

**Corollary UL-3.10 (SECOND Theorem 3.10(c)–(d) for all real shifts; PROVED-mod-cite: UF-lim; SECOND §2 Input (VA, DLMF-Lommel); SECOND Cor 3.6(i) (RH_p1 §1, DLMF 5.11)).**
- (c′) For p > 0 and s, s₀ > 1: 𝒟_n(p, s) − 𝒟_n(p, s₀) + ((s − s₀)/2)log n → ((s − s₀)/(2p))log c − ½log(ζ(s)/ζ(s₀)).
  In particular σ_{p,s} has a log-average coefficient iff σ_{p,s₀} has, and they differ by −(s − s₀)/2; the same holds
  with "𝒟_n − d·log n converges" in place of "= d·log n + O(1)".
- (d′) p = 2 and p = 1: for **every** s > 1, σ_{p,s} has log-average coefficient −(s − 1)/2, and in fact
  𝒟_n(p, s) + ((s − 1)/2)log n converges. Equivalently, with D_n = det(ζ(s + p(i + j)))_{0≤i,j<n} and h_n = D_{n+1}/D_n,
  log h_n = log ζ(s) − 2p log n! + 2n log c(p) − (s − 1)log n + O(1) (indeed + const + o(1)).

*Proof.* (c′): 𝒟_n(s) − 𝒟_n(s₀) = ½(F_n(s) − F_n(s₀)) − ½(s − s₀)log n − ½log(ζ(s)/ζ(s₀)); UF-lim. (d′): anchors with
convergent remainder: p = 2, s₀ = 2, the exact b_n (SECOND Thm 2.3 input) gives 𝒟_n(2, 2) = −½log n + const + o(1)
(n²b_n/c = 1 − 1/(2n) + O(n⁻²) summed); p = 1, s₀ = 3/2: SECOND Cor 3.6(i) (O(1/n) remainder) and the exact TC
coefficients nb_n^{TC} = ½(1 + 1/(2n))^{−1/2} give 𝒟_n(1, 3/2) = −¼log n + const + o(1). Then (c′). ∎

**Theorem UP (uniform Law P on compacts; PROVED-mod-cite: Thm UF-lim, hence (P), (LP), (QLP-c) at fixed points; Lemma CT).** For p > 0 and compact
K ⊂ (1, ∞):

  sup_{s∈K}|n^pb_n(s) − c| → 0,  sup_{s∈K}|n^pg_n(s) − c| → 0,  sup_{s∈K}|n^pα_n(s) − 2c| → 0.

*Proof.* Fix s₀ ∈ K, Δ_n(s) := F_n(s) − F_n(s₀). For n ≥ 2, log b_n(s)² = log h_n(s) − log h_{n−1}(s), so
log(b_n(s)²/b_n(s₀)²) = Δ_n(s) − Δ_{n−1}(s) − (s − s₀)log(n/(n − 1)). By UF-lim, Δ_n and Δ_{n−1} have the same uniform
limit, so b_n(s)/b_n(s₀) → 1 uniformly on K; with n^pb_n(s₀) → c (P) this is the b-part. g: n^pg_n(s) =
exp(F_n(s + p) − F_n(s)) (from h_n(s + p)/h_n(s) = g_n(s)), and UF-lim on the interval [a, b + p] gives → c uniformly. α: α_n =
g_n + b_n²/g_{n−1} (Lemma CT), each term uniformly ~ cn^{−p}. ∎

*Remarks.* (i) This is the "Law P uniform on compacts" (both parts) that SECOND §3.3's status paragraph (after review F10)
attributes to (RU); it is obtained here without (RU). It gives no rate. (ii) Numerically ([4]) sup_s|n^pb_n(s)/c − 1| =
3.7·10⁻³ at n = 400 for p ∈ {1, 2}, s ∈ [3/2, 4] (≈ (s − 1)/(2n) at s = 4), and sup_s|n^pα_n(s)/(2c) − 1| =
5.0·10⁻³ (p = 1), 6.2·10⁻³ (p = 2) at n = 400, halving per doubling. The g-part is not printed.

## 4. (UΛ)

**Proposition UΛ⁻ (PROVED-mod-cite: Thm UP).** There is C with Λ_n(s) ≥ −C for all n ≥ 1, s ∈ K.
*Proof.* For k < n, 0 ≤ log(n/k) ≤ (1/p)(n/k)^p = (1/p)n^px_k, so Λ_n(s) ≥ −Σ_{k<n}log(n/k)μ_n(k) ≥ −(1/p)n^pα_n(s)
(SECOND §3.3), and sup_{n,K}n^pα_n(s) < ∞ by Thm UP (finitely many n by continuity). ∎

**Theorem UΛ (hypothesis (UΛ) of SECOND §3.3 holds; PROVED-mod-cite: Thm UP, LP's method, Lemma TL).** For p > 0 and
compact K ⊂ (1, ∞): sup_{s∈K}|Λ_n(s)| = o(log n).

*Proof.* Lower half: Prop UΛ⁻. Upper half: Λ_n(s) ≤ Σ_{k>n}log(k/n)μ_n^{(s)}(k).
1. *Uniform localization at each fixed scale.* For every M ≥ 1, sup_{s∈K}|μ_n^{(s)}((Mn, ∞)) − F_p(M)| → 0, F_p as in
   Lemma LP. Otherwise there are ε > 0, n_j → ∞, s_j ∈ K with |μ_{n_j}^{(s_j)}((Mn_j, ∞)) − F_p(M)| ≥ ε. The i-th moment
   of the image of μ_{n_j}^{(s_j)} under x ↦ n_j^px is n_j^{pi}(J_{s_j}^i)_{n_jn_j}, a finite sum over lattice paths
   using α_m(s_j), b_m(s_j) with |m − n_j| ≤ i; by Thm UP, n_j^pα_m(s_j) → 2c and n_j^pb_m(s_j) → c for each such m. So the
   moments converge to those of ν_arc, and (method of moments, as in LP) the images converge weakly to ν_arc, which has no
   atoms; hence μ_{n_j}^{(s_j)}((Mn_j, ∞)) = ν((0, M^{−p})) → F_p(M), a contradiction.
2. *Deep tail.* Let m := ⌈(a + 1)/(a − 1)⌉ (≥ (s + 1)/(s − 1) for s ≥ a) and T := T″^m (T″ of Lemma TL; T ≥ T″ ≥ 3). By
   TL with w = k^{−s}, for n ≥ 2: Σ_{k>T}log(k/n)μ_n(k) ≤ Σ_{k>T}log k·ρ_{n+1}(k) ≤ 1156T″^sΣ_{k>T}k^{−s}log k.
   As y^{−s}log y is decreasing for y ≥ e^{1/s}, in particular for y ≥ e, and T ≥ T″ ≥ 3, Σ_{k>T}k^{−s}log k ≤ ∫_T^∞y^{−s}log y dy =
   T^{1−s}(log T/(s − 1) + (s − 1)^{−2}); so the deep tail is ≤ 1156T″^{s−m(s−1)}(m log T″ + 1)(1 + (a − 1)^{−2})
   ≤ 1156(m log T″ + 1)(1 + (a − 1)^{−2})/T″ → 0, uniformly on K (s − m(s − 1) ≤ −1).
3. *Middle.* By Tonelli (log(k/n) = ∫_1^{k/n}dM/M), Σ_{n<k≤T}log(k/n)μ_n(k) ≤ ∫_1^{T/n}μ_n((Mn, ∞))dM/M. Given ε > 0 pick M_ε
   with F_p(M_ε) ≤ ε/2 (F_p(M) → 0) and, by step 1, n_ε with sup_Kμ_n^{(s)}((M_εn, ∞)) ≤ ε for n ≥ n_ε. The tail is
   nonincreasing in M, so the integral is ≤ log M_ε + ε·log(T/n) ≤ log M_ε + εm·log T″ ≤ log M_ε + εmC_p log n
   (T″ ≤ (8p + 2)n^{2+2/p}).
So limsup_n sup_KΛ_n(s)/log n ≤ εmC_p for every ε > 0. ∎

**Proposition UΛ-L¹ (PROVED-mod-cite: Lemma W, UF-lim, Prop UΛ⁻).** For each fixed s > 1, Λ_n(s) → λ := −(log c)/p; and
∫_K|Λ_n(s) − λ|ds → 0. In particular, for every ε > 0, the Lebesgue measure of {s ∈ K : |Λ_n(s) − λ| > ε} tends to 0.
*Proof.* Λ_n(s) = −(1/p)E_s[log Y]; Lemma W with g = log (|log y| ≤ C_δ(y^{−δ} + y^δ), δ small) gives → −(1/p)∫log y dν_arc
= λ (φ′(0) = log c, UF-lim's proof). Put f_n := Λ_n + C ≥ 0 on K (Prop UΛ⁻). ∫_Kf_n = F_n(a) − F_n(b) + C(b − a) →
∫_K(λ + C) by UF-lim, and f_n → λ + C pointwise. Then ∫|f_n − f| = 2∫(f − f_n)⁺ − ∫(f − f_n) → 0, since 0 ≤ (f − f_n)⁺ ≤ f
and dominated convergence (Scheffé's argument, written out). ∎

**What stays open: (UΛ-O(1)) sup_K|Λ_n| = O(1) — GAP.** The upper half needs a hard-edge bound uniform in s, e.g.
sup_{s∈K}sup_nE_s[(k/n)^δ] < ∞ for some δ > 0 (uniform QLP(c)). This is what (RU) of G1 §3.16 would supply (PROOF SKETCH
level, Audit U); the soft arguments above control the hard edge only at fixed base points (Lemma V puts the negative
moment at the base point) or at a fixed scale M (step 1). It is no longer needed for SECOND Theorems 3.8–3.10.

**Proposition R (reductions; PROVED-mod-cite: Prop UΛ⁻, QLP-Λ and (P) at one fixed point).** On K = [a, b]:
(UΛ-O(1)) ⇔ sup_n Lip_K(F_n) < ∞; and (UΛ-O(1)) ⇐ (SCVX): ∃C, n₀ with (log h_n)″ ≥ −C on K for n ≥ n₀; in particular
⇐ (CVX).
*Proof.* F_n′ = −Λ_n. Under (SCVX), F_n′(s) ≥ F_n′(a) − C(s − a), i.e. Λ_n(s) ≤ Λ_n(a) + C(b − a), and Λ_n(a) = O(1) at
the fixed point a (SECOND §3.3 status: QLP-Λ for k ≥ n, Law P for k < n). With Prop UΛ⁻ this bounds |Λ_n|. ∎

## 5. (CVX): what can and cannot be said

Let P_j = P_j^{(s)} be the orthonormal polynomials of σ_s and f_{ij} := ⟨P_i, (log k)P_j⟩_{σ_s} (finite: Σk^{−s}log²k < ∞).

**Proposition SV (second variation; PROVED, elementary).** For n ≥ 0 and s > 1,

  ∂_s²log h_n(s) = Var_{μ_n^{(s)}}(log k) − 2Σ_{i<n}f_{in}² = Σ_{j>n}f_{nj}² − Σ_{i<n}f_{in}²,

and Λ_n′(s) = −∂_s²log h_n(s) ∈ [−Var_{μ_n}(log k), Var_{μ_n}(log k)].

*Proof.* The coefficients of P_n are rational functions of the moments ζ(s + pj) (with positive denominators), so they are
real-analytic in s; all series Σ_kk^{−s}(log k)^dx_k^j (d ≤ 2) converge locally uniformly on s > 1, which justifies the termwise
differentiations below (as in SECOND Prop 3.7). Write Ṗ_n := ∂_sP_n = Σ_{i≤n}c_iP_i (degree ≤ n) and L := log k; note
∂_s∫G dσ_s = −∫GL dσ_s. Differentiating ⟨P_n, P_i⟩_s = δ_{ni}: for i < n, 0 = ⟨Ṗ_n, P_i⟩ + ⟨P_n, Ṗ_i⟩ − f_{ni} = c_i − f_{in}
(deg Ṗ_i ≤ i < n); for i = n, 0 = 2c_n − f_{nn}. Then L_n(s) = f_{nn} = ⟨P_n, LP_n⟩ and
L_n′ = −⟨P_n, L²P_n⟩ + 2⟨Ṗ_n, LP_n⟩ = −(L²)_{nn} + 2Σ_{i<n}f_{in}² + f_{nn}². With Prop 3.7, ∂_s²log h_n = −L_n′ =
Var_{μ_n}(L) − 2Σ_{i<n}f_{in}². Since σ_s has compact support, polynomials are dense in L²(σ_s) (Weierstrass), so {P_j} is
an orthonormal basis and Var_{μ_n}(L) = ‖LP_n‖² − f_{nn}² = Σ_{j≠n}f_{nj}² (Parseval); this gives the second form and
0 ≤ Σ_{i<n}f_{in}² ≤ Var. ∎

So (CVX) says: the "upward flux" of log k out of P_n dominates the "downward flux". (This is the Var_{n+1} − Var_n form of
SECOND §3.3 written at level n.)

**Remark CVX-fin (PROVED).** (CVX) is not a consequence of the exponential-family structure σ_s = x^{s/p}σ₀. For the N-atom
truncation σ_s^{(N)} := Σ_{k≤N}k^{−s}δ_{x_k} (N ≥ 2) and n = N − 1, L²(σ^{(N)}) has dimension N, so there is no j > n
and Prop SV (same proof; finite sums) gives ∂_s²log h_{N−1} = −Σ_{i<N−1}f_{i,N−1}² < 0. The sum is positive: otherwise
LP_{N−1} = f_{N−1,N−1}P_{N−1}, so P_{N−1} would vanish at all atoms but one, contradicting ⟨P_{N−1}, 1⟩ = 0
(orthogonality to constants, N − 1 ≥ 1). Checked in `check_ul.out` [3] (p ∈ {1, 2}, N ∈ {3, 5, 8}). So any proof of (CVX)
for σ_{p,s} must use a property of σ₀ that fails for finite truncations (the failure shown is at the top level n = N − 1,
the "saturated" last level).

**Status of (CVX) for σ_{p,s}: HYPOTHESIS (unchanged), NUMERICAL.** SECOND's data (`check_so_convex.out` [2]) give
n·(second divided difference of log h_n at n = 1600) = 1.996, 0.4996, 0.2222, 0.1250, 0.0556, 0.0313 for p = ½, 1, 3/2, 2,
3, 4, i.e. n·dd ≈ 1/(2p²), and since dd ≈ f″/2 (standard second divided difference), (log h_n)″ ≈ 1/(p²n)
(NUMERICAL observation): an O(1/n) quantity, so (CVX) is a statement at the level of
the 1/n coefficient (SECOND §4), not a soft one. No counterexample for σ_{p,s} is known. After UF-lim, (CVX) is needed only
for (UΛ-O(1)) (Prop R).

## 5′. Rule A (adversarial pass) — log

- Lemma V: both directions tested exactly ([1]: p ∈ {½, 1, 2}, t ∈ {3/2, 2, 3}, s − t ∈ {±¼, ±0.4}, n ∈ {1, 2, 4, 8};
  min slack 8.8·10⁻³ > 0). Degenerate case E_t[k^{s−t}] = ∞ (s − t ≥ t − 1): (D) is vacuous, handled. The test function
  φ is not a polynomial; only φ ⊥ P_{n−1} is used, and that holds by the change of weight.
- Theorem UF: the step u₀ < ϑ(p, a) ≤ ϑ(p, t) for every base point; the base points are fixed before n → ∞, so only
  fixed-σ constants enter. Checked that no constant depends on s inside a cell (Jensen uses only n^pα_n(t_i); (D) only
  B_{t_i}).
- Lemma W: the truncation g_{ε,R} must be continuous on [0, ∞) including 0 — it is (constant g(ε) near 0); ν_n has no mass
  at Y = 0 since x_k > 0. The exponent condition pa < ϑ(p, t) ≤ p/2 ensures the arcsine law also has the moment.
- UF-lim: the error per cell is O(r·r_u), so the total is O(u) — this is why the grid must be refined (u → 0) *after*
  n → ∞; a single fixed grid would only give Theorem UF. Identification φ′(0) = log c via Theorem 3.2 is independent
  of the arcsine computation; both agree, and the numerics ([4]) agree with (s − s₀)log c/p to 3·10⁻³–7·10⁻³ at n = 400.
- Thm UP: derived from F_n-differences in n; the n-differences Δ_n − Δ_{n−1} → 0 need the *uniform* limit of Δ_n (a bound
  alone would give only bounded ratios). (P) at s₀ is used directly only for the value c (UF-lim itself uses (P), (LP), (QLP-c) at fixed points).
- Thm UΛ step 1: the contradiction argument needs the moment convergence along arbitrary sequences s_j — provided by the
  uniformity in Thm UP and the fixed path length i. Step 2 uses TL with c = C = 1 (exact pure power), valid for every s.
  Does o(log n) hide a log n? The middle bound is ε·m·C_p log n with ε arbitrary; m, C_p depend on K, p only.
- Prop UΛ-L¹: Scheffé needs f_n ≥ 0 — provided by Prop UΛ⁻; pointwise convergence at *every* s by Lemma W.
- Converse checks: (UΛ-O(1)) is not claimed; Λ_n could a priori have narrow spikes of height ≤ o(log n) on sets of
  vanishing measure — nothing here excludes them. Numerically ([4], secant proxy on cells of width ¼) Λ_n ∈ [0.69, 0.70]
  (p = 1) and [0.243, 0.245] (p = 2) at n = 400, versus λ = 0.6931, 0.2416.
- Prop SV: verified to 10⁻⁵⁰ against numerical second derivatives of exact Hankel ratios ([2]).

## 6. Checks

`checks/check_ul.py` (.out), NUMERICAL (finite checks of proved statements; not certified):
- [1] Lemma V, exact (mpmath, dps 60, Hankel matrices of ζ-values).
- [2] Prop SV, exact small n (f_{ij} from ζ′, ζ″ Hankel matrices).
- [3] Remark CVX-fin, truncations N ∈ {3, 5, 8}.
- [4] Theorems UF, UF-lim, UP (b- and α-parts; the g-part is not printed), and a secant proxy of Λ_n: binary128 RKPW on atoms k ≤ 4·10⁴ plus the Gauss–Jacobi tail of
  `so_coeffs.measure`, p ∈ {1, 2}, s ∈ {1.5, 1.75, …, 4}, n ≤ 400. Needs `make -C csrc` (gitignored build). Runtime ≈ 3 min.

## 7. Integration (applied, with the labels as corrected by REVIEW_Plan64 F2, F3, F12)

All changed rows and paragraphs are marked "Plan 64" / "not REVIEWED" until the diff check. Label wording used everywhere:
- dependency footprint of UF-lim and everything built on it (Thm 3.8, UP, UΛ): "(P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used";
- Thm 3.10(d)/(c′): "UF-lim; SECOND §2 Input (VA, DLMF-Lommel); SECOND Cor 3.6(i) (RH_p1 §1, DLMF 5.11)".

**SECOND.md.**
- Status block: a "Plan 64 update" note pointing to UL.md.
- Summary table: Thm 3.8 → PROVED-mod-cite (UL.md Cor UL-3.8, with the constant); Cor 3.9 → CONDITIONAL on (E) only +
  PROVED-mod-cite; Thm 3.10 (d) and (c) for all real shifts → PROVED-mod-cite (UL.md Cor UL-3.10); (CVX) row: no longer needed
  for Thms 3.8–3.10, sufficient for sup_K|Λ_n| = O(1); new rows (UΛ) (PROVED-mod-cite; O(1) GAP), UF-lim, UP.
- §3.3: (UΛ) heading and status paragraph (proved without (RU); the F10 α-part is Thm UP; O(1) GAP); (CVX) "Why it is
  natural" cites Prop SV and Remark CVX-fin, and the divided-difference factor (dd ≈ (log h_n)″/2, F11); "(CVX) suffices"
  marked as no longer needed; Theorem 3.8 heading/statement (the earlier (UΛ)/(CVX) proof kept as the earlier route);
  Corollary 3.9 heading and bullets ((UΛ)/(CVX) dropped).
- §3.4: Theorem 3.10 heading (d), bullet (d), new bullet (c′), the "Equivalently … in cases (a), (b)" sentence (now also every
  s > 1 at p ∈ {1, 2}, const + o(1)), proof of (d), closing paragraph.
- §4: "(via (UΛ) off the lattices)", "s-independent under (E), (UΛ)", "Soft routes tried: s-derivative" updated.
- §6: `checks/check_ul.py` (.out) added. §5 unchanged.

**THEOREMS.md.**
- §2.10 heading: adds "Plan 64 … UL.md; NOT REVIEWED — Rule R ACCEPT WITH FIXES, REVIEW_Plan64.md, fixes applied, diff check
  pending" (to become "REVIEWED <date>" after the diff check).
- §2.10 rows "Prop 3.7, Thm 3.8, Cor 3.9" and "Thm 3.10" relabelled as above; new rows UF-lim, UP, UΛ, "SV, CVX"; Novelty
  line extended.
- §4 item 13: Plan 64 update (dependencies on (UΛ)/(CVX) removed; open: sup_K|Λ_n| = O(1), (CVX)).
- Thm QLP row (G1 §3.16): note that Law P is uniform on compacts in σ without (RU) (UL.md Thm UP); QLP uniformity still
  needs (RU).

**Pending (coordinator):** UL.md Status line and the "Plan 64 / not REVIEWED" markers → REVIEWED after the diff check.

**Not changed:** Prop 3.7, Cor 3.3, Thm 3.4, Prop 3.5, Cor 3.6, Conjecture P62, §4 (E) GAP, g(p) GAP.
