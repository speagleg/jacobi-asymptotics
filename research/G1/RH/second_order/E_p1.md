# E_p1: the 1/n coefficient (E) for pure powers at p = 1 (Plan 66)

Status (2026-10-15): written by the Plan 66 agent. Rule R: research/G1/review/REVIEW_Plan66_A.md (Route C) and REVIEW_Plan66_B.md
(Route A, constants), both ACCEPT WITH FIXES; fixes A1–A5, A7, B F1–F5 applied (A6 recorded in §8); **not yet REVIEWED** (pending
the coordinator's diff-check). Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert throughout. This file closes, for p = 1, the GAP "(E)" of SECOND.md §4 (the p > 1 case is
E_pgt1.md), and proves the "−1/24" second-order conjecture of RH_p1.md §0 / THEOREMS.md §4 item 13. §10 (Integration) lists the changes made to SECOND.md and THEOREMS.md.

**Which route worked.** Two routes, with different strengths:
- **Route A (comparison with Tricomi–Carlitz), elementary, no RH at all.** At p = 1 the node function 1/k is the variable x
  itself, so a weight factor 1 + ε/k is the polynomial 1 + εx: its effect on h_n is an *exact* Christoffel transform
  (Lemma E1.2), and the remaining factor 1 + O(x²) is controlled by the minimum (variational) sandwich of UL Lemma V through
  E_n[x²] = α_n² + b_n² + b_{n+1}² = O(n⁻²) (Lemma E1.3). This gives the transfer Proposition E1.4: a weight factor
  (1 + εx)e^{O(x²)} changes log b_n² by exactly ε(α_n − α_{n−1}) + O(n⁻³). With the explicit coefficients of TC and x·TC
  (Lemma E1.5) it proves (E) with remainder O(n⁻²) **and** the second-order constant −1/24 at s = 3/2 and s = 5/2
  (Theorem E1.6). Route A cannot leave the lattice s ∈ 3/2 + ℕ₀: a factor k^{−β} with β ∉ ℤ is not of the form
  (1 + εx)e^{O(x²)}, and only m ∈ {0, 1} have a reference x^m·TC with known second-order coefficients.
- **Route C (direct second-order RH in the symmetric frame of RH₁(r)), all s > 1.** The obstruction recorded in E_pgt1 §9
  (the classical *x-frame* hard-edge parametrix fails at p = 1, Paper 2's comparison parametrix has no rate) does not arise in
  the symmetric frame: there the point 0 is an interior Fisher–Hartwig point of the band, RH₁(r) already builds an explicit
  Bessel-type parametrix (KV/Vanlessen) there, and with the Stirling truncation order m ≥ 1 every mismatch outside the three
  circles is O(N⁻³). Two-term expansions of the Airy and Bessel models then give jumps I + Δ₁/N + O(N⁻²) on the circles with
  Δ₁ independent of N **except for a factor (−1)^N** (the phase e^{Nφ₊(0)σ₃}, φ₊(0) = −iπ/2, Lemma E1.7). Hence
  Nβ_N = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²) for the symmetric chain (Theorem E1.9), the alternating part cancels in the fold,
  and (E) holds with ε = 1 for every s > 1. The value d₁ = −(s−1)/2 is then forced by the proved log-average law
  (UL Cor UL-3.10); no residue is computed. The alternating constant κ₁ = k₁ is *not* determined (GAP, except s = 3/2, 5/2).
- Route B (Tauberian from the averaged law) was not needed and was not pursued.

**Summary of labels.** σ_s := σ_{1,s} = Σ_{k≥1}k^{−s}δ_{1/k}, s > 1; c(1) = ½; standard pairing α_n/(2b_n), repo pairing
α_{n−1}/(2b_n) (SECOND §0).

| # | Statement | Label |
|---|---|---|
| Lemma E1.1 | comparability: c₁ν ≤ ν′ ≤ c₂ν on the nodes ⇒ h_n, b_n², g_n comparable, α_n(ν′) ≤ (c₂/c₁)²α_n(ν); E_n^ν[x²] = α_n² + b_n² + b_{n+1}² | PROVED (elementary) |
| Lemma E1.2 | Christoffel by 1 + εx: h_n((1+εx)ν)/h_n(ν) = ερ_n, ερ_n = 1 + εα_n − ε²b_n²/(ερ_{n−1}) ∈ [1, 1+ε] | PROVED (elementary) |
| Lemma E1.3 | minimum sandwich −log E_n^{ν′}[e^{−f}] ≤ log(h_n(ν′)/h_n(ν)) ≤ log E_n^ν[e^{f}] for ν′ = νe^f | PROVED (elementary; = the argument of UL Lemma V) |
| Prop E1.4 | transfer: w = Kv(1+εx)e^{f₀}, \|f₀\| ≤ Cx² ⇒ log(b_n(w)²/b_n(v)²) = ε(α_n(v) − α_{n−1}(v)) + O(n⁻²); with f₀ = r₂x² + O(x³) and (R1) for v, xv: the same with O(n⁻³), and log(g_n(w)/g_n(v)) = ε(α_n(xv) − α_n(v)) + O(n⁻³) | PROVED (elementary) |
| Lemma E1.5 | TC (α_W = 1) and x·TC: exact coefficients and chains; chain of x·TC: γ′²_{2j+1} = (2j+5)/((2j+2)(2j+3)), γ′²_{2j} = j/((j+1)(2j+3)) | PROVED-mod-cite (WLXZ v1 (1.4)–(1.9): Carlitz's orthogonality as stated there) + exact computer algebra (check_e1_exact) |
| **Thm E1.6** | s = 3/2 and s = 5/2: b_n, α_n, g_n, h̃_n of σ_s equal those of TC, resp. x·TC, times 1 − 1/(24n²) + O(n⁻³). Hence (E) with remainder O(n⁻²), d₁ = −(s−1)/2, e₁ˢ = −½, e₁ = ½, k₀ = ½ − s, k₁ = −3(s − 3/2), d₂(1, 3/2) = 5/96, d₂(1, 5/2) = 53/96; **the −1/24 conjecture of RH_p1 §0 (b and a)** | PROVED-mod-cite (Lemma E1.5's input; DLMF 5.11.1 + §5.11(ii), real argument) |
| Lemma E1.7 | second-order matching on the three circles of RH₁(r): J_S = I + Δ^{±}/N + O(N⁻²) on ∂U(±2, ε), J_S = I + (Δ^{0,e} + (−1)^NΔ^{0,o})/N + O(N⁻²) on ∂U(0, ε), Δ's independent of N; all other jumps O(N⁻³) or O(e^{−cN}) | PROVED-mod-cite (RH₁(r) §§2–6 [REVIEWED]; WLXZ v1 (6.8), (6.10)–(6.21), (2.1)–(2.3), (4.3) and the proof of Prop. 4.2; KV (5.23), (5.26)–(5.30); Vanlessen (4.26)–(4.33), (4.43)–(4.46); DLMF 5.11.1 + §5.11(ii), 9.7.5–6, 10.17.5–6, 10.40.1–2) |
| Prop E1.8 | S₁ = (Σᵉ + (−1)^NΣᵒ)/N + O(N⁻²), Σᵉ, Σᵒ constant matrices | PROVED-mod-cite (Lemma E1.7; first-order small norm of RH₁(r) §7 = WLXZ v1 (6.35)–(6.37)) |
| **Thm E1.9** | every s > 1: symmetric chain Nβ_N = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²) for some real κ₀, κ₁ | PROVED-mod-cite (as Prop E1.8; RH₁(r) §3 extraction) |
| **Thm E1.10 (main)** | every s > 1: nb_n = ½(1 − (s−1)/(2n) + O(n⁻²)), nα_n = 1 − s/(2n) + O(n⁻²), α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²), α_{n−1}/(2b_n) = 1 + 1/(2n) + O(n⁻²); κ₀ = k₀ = ½ − s; ng_{n−1} = ½(1 + (1 + κ₀ − κ₁)/(2n) + O(n⁻²)). I.e. **(E) holds at p = 1 with ε = 1**, and Conjecture P62 holds at p = 1 for d₁, e₁, e₁ˢ, k₀ with remainder O(n⁻²) | PROVED-mod-cite (Thm E1.9 + UL Cor UL-3.10 [REVIEWED] for the value; SECOND Lemma 2.1) |
| §8 GAP | k₁(s) = κ₁ for s ∉ {3/2, 5/2} (conjectured −3(s − 3/2), NUMERICAL); d₂(1, s) for s ∉ {3/2, 5/2}; 0 < p < 1 | GAP |

NUMERICAL cross-checks (not used in the proofs): `checks/check_e1_tc.out` (Theorem E1.6: all six ratios n²(r − 1) → −1/24),
`checks/check_e1_rate.out` (Theorem E1.10: second-order residuals bounded at s ∈ {1.25, 1.5, 2, 3, 4.5}; no N mod 4
oscillation beyond (−1)^N), `checks/check_e1_models.out` (inputs of Lemma E1.7: G_TC = G₀H_N^{−1} and the model identity behind
WLXZ (6.14); φ₊(0) = −iπ/2; two-term Airy and Bessel-model expansions in every sector); `checks/check_e1_exact.out` (exact
computer algebra of Lemma E1.5, of the coefficient differences used in Theorem E1.6, and of its constants ε = 1/12, r₂ = 1/288,
−1/24 (b, g, h̃, α, β_N), 5/96, 53/96; plus an exact-moment Stieltjes corroboration of Lemma E1.5 for n ≤ 12).

Novelty: UNCHECKED (Rule L not done). Lemmas E1.1–E1.3 are classical in kind (comparison of Christoffel-type extremal
quantities; Christoffel's formula; minimum principle); novelty not claimed for them.

## 0. Setting and conventions

- p = 1, nodes x_k = 1/k (k ≥ 1), c = c(1) = ½. For a positive measure ν = Σν_kδ_{x_k} with Σν_k < ∞ (all measures below are of
  this kind, with infinitely many positive masses): monic OPs xπ_n = π_{n+1} + α_nπ_n + b_n²π_{n−1}, h_n(ν) = ∫π_n²dν,
  b_n² = h_n/h_{n−1} (SECOND §0). The **chain** (G1 Lemma CT; SECOND Lemma 2.1): g_n(ν) := −π_{n+1}(0)/π_n(0) > 0, h̃_n := b_n²/g_{n−1}
  (n ≥ 1), α_n = g_n + h̃_n (n ≥ 1), α₀ = g₀. (SECOND writes h_n for h̃_n; here h_n is the norm.) In the symmetric variable
  y (x = y²) with monic OPs R_N and yR_N = R_{N+1} + β_NR_{N−1} (β_N = γ_N² of SECOND Lemma 2.1): β_{2m} = h̃_m, β_{2m+1} = g_m,
  hence b_m² = β_{2m−1}β_{2m}, α_m = β_{2m} + β_{2m+1}.
- **Christoffel at 0** (SECOND Prop 3.1 / Lemma CT): h_n(xν) = g_n(ν)h_n(ν). (Proof as Lemma E1.2 with z₀ = 0.)
- E_n^ν[f] := Σ_kf(x_k)ν_kπ_n(x_k)²/h_n(ν) (a probability expectation). E_n^ν[x] = α_n, and since xπ_n = π_{n+1} + α_nπ_n + b_n²π_{n−1},
  E_n^ν[x²] = ‖xπ_n‖²/h_n = b_{n+1}² + α_n² + b_n².
- σ_s := Σ_{k≥1}k^{−s}δ_{1/k} (s > 1). **TC** := Σ_{k≥1}v_kδ_{1/k}, v_k := k^{k−1}e^{−k}/k! (Tricomi–Carlitz at α_W = 1, folded;
  Lemma E1.5). H(t) := Γ(t+1)e^t/(√(2π)t^{t+1/2}) (t > 0), so that k^{−3/2} = √(2π)H(k)v_k (RH_p1 §1; elementary).
- **Targets** (SECOND §0): d₁ in nb_n/c = 1 + d₁/n + …, e₁ˢ in α_n/(2b_n) = 1 + e₁ˢ/n + …, e₁ in α_{n−1}/(2b_n) = 1 + e₁/n + …,
  and k₀, k₁ in γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + …) (SECOND §0); at p = 1, c = ½ and γ_N² = β_N this reads
  Nβ_N = 1 + (k₀ + k₁(−1)^N)/N + ….
  (E_ε): nb_n/c = 1 + d₁/n + O(n^{−1−ε}).

## 1. Main results

**Theorem E1.10 (main; PROVED-mod-cite).** Let p = 1 and s > 1. Then, as n → ∞,

  nb_n = ½(1 − (s−1)/(2n) + O(n⁻²)),   nα_n = 1 − s/(2n) + O(n⁻²),

hence α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²) (e₁ˢ = −½) and α_{n−1}/(2b_n) = 1 + 1/(2n) + O(n⁻²) (e₁ = ½). The symmetric chain satisfies
Nβ_N = 1 + (k₀ + κ₁(−1)^N)/N + O(N⁻²) with k₀ = ½ − s = −(s−1) − p/2 and some real κ₁ = κ₁(s). In particular (E) of SECOND §4
holds at p = 1 with ε = 1, d₁ = −(s−1)/2, and Conjecture P62 holds at p = 1 for d₁, e₁, e₁ˢ, k₀ with its conjectured remainder
O(n^{−1−min(1,p)}) = O(n⁻²). (κ₁ = k₁ = −3(s − 3/2) is proved only for s ∈ {3/2, 5/2}, Theorem E1.6.)

**Theorem E1.6 (s = 3/2, 5/2: second order; PROVED-mod-cite, no RH).** Let (w, v) = (σ_{3/2}, TC) or (σ_{5/2}, x·TC). Then

  b_n(w)/b_n(v), α_n(w)/α_n(v), g_n(w)/g_n(v), h̃_n(w)/h̃_n(v) = 1 − 1/(24n²) + O(n⁻³),

and β_N(w)/β_N(v) = 1 − 1/(6N²) + O(N⁻³), where (Lemma E1.5) b_n(TC)² = 1/(2n(2n+1)), α_n(TC) = 1/(2n+1) + 1/(2n+2),
g_n(TC) = 1/(2n+2); b_n(xTC)² = 1/((2n+1)(2n+2)), α_n(xTC) = 1/(2n+2) + 1/(2n+3), g_n(xTC) = (2n+5)/((2n+2)(2n+3)). Consequently
nb_n(σ_{3/2}) = ½(1 − 1/(4n) + 5/(96n²) + O(n⁻³)) and nb_n(σ_{5/2}) = ½(1 − 3/(4n) + 53/(96n²) + O(n⁻³)), and all of d₁, e₁, e₁ˢ,
k₀, k₁ of Conjecture P62 hold at (p, s) = (1, 3/2), (1, 5/2) (k₁ = 0, −3). The case (σ_{3/2}, TC) is the "−1/24" conjecture of
RH_p1 §0: n²(b_n^σ/b_n^{TC} − 1) → −1/24, and the same for a_n = α_{n−1}.

## 2. Route A: elementary comparison on the nodes 1/k

**Lemma E1.1 (comparability; PROVED).** Let ν, ν′ be measures on {x_k} with c₁ν_k ≤ ν′_k ≤ c₂ν_k for all k (0 < c₁ ≤ c₂).
Then for all n: c₁h_n(ν) ≤ h_n(ν′) ≤ c₂h_n(ν); b_n(ν′)² ≤ (c₂/c₁)b_n(ν)² and b_n(ν′)² ≥ (c₁/c₂)b_n(ν)²; g_n(ν′) ∈ [c₁/c₂, c₂/c₁]·g_n(ν);
α_n(ν′) ≤ (c₂/c₁)²α_n(ν). If moreover α_n(ν), b_n(ν) ≤ C/n (n ≥ 1), then E_n^{ν′}[x^j] ≤ C_j n^{−j} for j = 2, 4 and
E_n^{ν′}[x³] ≤ (E_n^{ν′}[x²]E_n^{ν′}[x⁴])^{1/2} ≤ C₃n⁻³.

*Proof.* h_n(ν) = min{∫π²dν : π monic of degree n}, and c₁∫π²dν ≤ ∫π²dν′ ≤ c₂∫π²dν for every π; take minima. b_n² = h_n/h_{n−1}.
The same applies to xν, xν′ (same constants), and g_n = h_n(x·)/h_n(·) (§0), so g_n(ν′) ∈ [c₁/c₂, c₂/c₁]g_n(ν). Then
α_n(ν′) = g_n(ν′) + b_n(ν′)²/g_{n−1}(ν′) ≤ (c₂/c₁)g_n(ν) + (c₂/c₁)²b_n(ν)²/g_{n−1}(ν) ≤ (c₂/c₁)²α_n(ν) (and α₀ = g₀). For the moments:
in the orthonormal basis, E_n[x^{2j}] = Σ_i|(J^j)_{in}|² with J the Jacobi matrix of ν′; the entries of J^j in row n involve
only coefficients with indices in [n − j, n + j], each ≤ C′/n by the bounds just proved, so E_n[x^{2j}] ≤ C_j n^{−2j} (n ≥ 2j; smaller n are absorbed in C_j since x ≤ 1); E_n[x³] by
Cauchy–Schwarz. ∎

**Lemma E1.2 (Christoffel by 1 + εx; PROVED).** Let ε > 0, z₀ := −1/ε, ν as above. Then π_n(z₀) ≠ 0,
ρ_n := −π_{n+1}(z₀)/π_n(z₀) > 0, and

  h_n((1 + εx)ν) = ερ_n·h_n(ν),  ερ₀ = 1 + εα₀,  ερ_n = 1 + εα_n − ε²b_n²/(ερ_{n−1}) (n ≥ 1),  1 ≤ ερ_n ≤ 1 + ε.

*Proof.* The zeros of π_n lie in (0, 1) ∌ z₀, so π_n(z₀) ≠ 0 and sign π_n(z₀) = (−1)^n, whence ρ_n > 0. q_n := (π_{n+1} + ρ_nπ_n)/(x − z₀)
is a monic polynomial of degree n (the numerator vanishes at z₀), and ∫q_nx^j(x − z₀)dν = ∫(π_{n+1} + ρ_nπ_n)x^jdν = 0 for j < n,
so q_n is the n-th monic OP of (x − z₀)ν, and h_n((x − z₀)ν) = ∫q_n(π_{n+1} + ρ_nπ_n)dν = ρ_n∫q_nπ_ndν = ρ_nh_n(ν). Multiply by ε.
The recurrence at z₀ gives ρ_n = α_n − z₀ + b_n²π_{n−1}(z₀)/π_n(z₀) = α_n + 1/ε − b_n²/ρ_{n−1}. The bounds follow from
ν ≤ (1 + εx)ν ≤ (1 + ε)ν and Lemma E1.1. ∎

**Lemma E1.3 (minimum sandwich; PROVED; this is the argument of UL Lemma V).** If ν′_k = ν_ke^{f(k)} with f real and
Σν′_k < ∞, then −log E_n^{ν′}[e^{−f}] ≤ log(h_n(ν′)/h_n(ν)) ≤ log E_n^ν[e^{f}].

*Proof.* h_n(ν′) ≤ ∫π_n^ν(x)²dν′ = Σ_kν_ke^{f(k)}π_n^ν(x_k)² = h_n(ν)E_n^ν[e^f], and symmetrically h_n(ν) ≤ h_n(ν′)E_n^{ν′}[e^{−f}]. ∎

**Hypothesis (R1) on a reference v.** There are A, B > 0 with nα_n(ν) = A + O(1/n) and nb_n(ν) = B + O(1/n) for both ν = v and
ν = xv.

**Proposition E1.4 (transfer; PROVED).** Let v be a measure on {x_k} with α_n(v), b_n(v), α_n(xv), b_n(xv) ≤ C/n, and
w_k := Kv_k(1 + εx_k)e^{f₀(k)} with K > 0, ε ≥ 0, |f₀(k)| ≤ C₀x_k² for all k. Then:

(i) log h_n(w) − log h_n(v) = log K + εα_n(v) + O(n⁻²); hence log(b_n(w)²/b_n(v)²) = ε(α_n(v) − α_{n−1}(v)) + O(n⁻²) and
  log(g_n(w)/g_n(v)) = ε(α_n(xv) − α_n(v)) + O(n⁻²).
(ii) If v satisfies (R1), then b_n(w), g_n(w), h̃_n(w), α_n(w) equal the corresponding quantities of v times 1 + O(n⁻²); in
  particular w satisfies (R1) with the same A, B.
(iii) If v satisfies (R1) and f₀(k) = r₂x_k² + O(x_k³) uniformly in k, then

  log(b_n(w)²/b_n(v)²) = ε(α_n(v) − α_{n−1}(v)) + O(n⁻³),  log(g_n(w)/g_n(v)) = ε(α_n(xv) − α_n(v)) + O(n⁻³).

*Proof.* The constant K multiplies every h_n and changes no coefficient; take K = 1. If ε = 0 skip the Christoffel step
(ερ_n := 1 below). Put v′ := (1 + εx)v, so w = v′e^{f₀}, and split

  log h_n(w) − log h_n(v) = log(ερ_n(v)) + Δ′_n,  Δ′_n := log h_n(w) − log h_n(v′)   (Lemma E1.2).

The measures v′ and w are comparable with v (constants 1, 1 + ε, e^{±C₀}), so by Lemma E1.1 their coefficients are ≤ C/n and
their moments E_n[x^j] ≤ C_jn^{−j} (j = 2, 3, 4); the same holds for xv′, xw against xv.
(i) |e^{±f₀} − 1| ≤ C₁x² (x ≤ 1), so by Lemma E1.3, |Δ′_n| ≤ 2C₁max(E_n^{v′}[x²], E_n^w[x²]) = O(n⁻²). By Lemma E1.2,
ερ_n − 1 = εα_n − ε²b_n²/(ερ_{n−1}) = O(1/n), so log(ερ_n) = εα_n(v) + O(n⁻²). This is the first claim; the second follows from
log b_n² = log h_n − log h_{n−1}. The third is the first applied to the pair (xw, xv) (xw = K·xv·(1 + εx)e^{f₀}), minus the first.
(ii) Under (R1), α_n(v) − α_{n−1}(v) = O(n⁻²) and α_n(xv) − α_n(v) = O(n⁻²), so (i) gives b_n(w)/b_n(v), g_n(w)/g_n(v) =
1 + O(n⁻²); then h̃_n = b_n²/g_{n−1} and α_n = g_n + h̃_n (α₀ = g₀) follow.
(iii) Second order in the sandwich: e^{±f₀} = 1 ± r₂x² + O(x³) uniformly, so with Lemma E1.1's moment bounds
log E_n^{v′}[e^{f₀}] = r₂E_n^{v′}[x²] + O(n⁻³) and −log E_n^w[e^{−f₀}] = r₂E_n^w[x²] + O(n⁻³). By (ii) (applied to w and to v′, which is w
with f₀ ≡ 0), the coefficients of w and v′ are those of v times 1 + O(n⁻²); by SECOND Lemma 2.2 (α_n(xν) = g_n(ν) + h̃_{n+1}(ν),
b_n(xν)² = h̃_n(ν)g_n(ν)) so are those of xw and xv′ relative to xv. Hence v′ and w satisfy (R1) with the A, B of v, and
E_n^{ν}[x²] = (A² + 2B²)/n² + O(n⁻³) for ν ∈ {v′, w} (and the same for xv′, xw) by the §0 formula for E_n[x²]. Hence Δ′_n = r₂(A² + 2B²)/n² + O(n⁻³), and Δ′_n − Δ′_{n−1} = O(n⁻³). Second order in the Christoffel factor:
ερ_{n−1} = 1 + O(1/n) gives ερ_n = 1 + εα_n − ε²b_n² + O(n⁻³), so log(ερ_n) = εα_n − ε²b_n² − ½ε²α_n² + O(n⁻³). Under (R1),
b_n² − b_{n−1}² and α_n² − α_{n−1}² are O(n⁻³), so log(ερ_n) − log(ερ_{n−1}) = ε(α_n − α_{n−1}) + O(n⁻³). Adding gives the b-claim.
For g, apply the same expansions to the pairs (xw, xv) and (w, v) and subtract: the Δ′ terms cancel to O(n⁻³) (same A, B for v
and xv by (R1)), and so do −ε²b_n² − ½ε²α_n² (b_n(xv)² − b_n(v)², α_n(xv)² − α_n(v)² = O(n⁻³) by (R1)). ∎

**Lemma E1.5 (TC data; PROVED-mod-cite: WLXZ v1 (1.4)–(1.9), quoted in RH/CITATIONS.md "(WLXZ-v1, Plan 66)"; exact
computer algebra `checks/check_e1_exact.py`).**
(a) For TC = Σ_kv_kδ_{1/k}: β_N = 1/(N + 1) (N ≥ 1), hence b_n² = 1/(2n(2n+1)), α_n = 1/(2n+1) + 1/(2n+2) (n ≥ 1), α₀ = ½,
  g_n = 1/(2n+2), h̃_n = 1/(2n+1).
(b) x·TC: b_n² = 1/((2n+1)(2n+2)), α_n = 1/(2n+2) + 1/(2n+3) (n ≥ 0); its chain is γ′²_{2j+1} = (2j+5)/((2j+2)(2j+3)) (j ≥ 0),
  γ′²_{2j} = j/((j+1)(2j+3)) (j ≥ 1), so g_n(xTC) = (2n+5)/((2n+2)(2n+3)).
(c) x²·TC: α_n = γ′²_{2n+1} + γ′²_{2n+2} = (4n+7)(2n²+7n+8)/(2(n+1)(n+2)(2n+3)(2n+5)), b_n² = γ′²_{2n}γ′²_{2n+1} = n(2n+5)/(2(n+1)²(2n+3)²).
(d) Expansions (exact series): for ν ∈ {TC, xTC, x²TC} (s = 3/2, 5/2, 7/2): 2nb_n = 1 − (s−1)/(2n) + O(n⁻²), nα_n = 1 − s/(2n) + O(n⁻²),
  α_n − α_{n−1} = −1/n² + O(n⁻³), b_n² − b_{n−1}² = O(n⁻³); α_n(xTC) − α_n(TC) = α_n(x²TC) − α_n(xTC) = −1/(2n²) + O(n⁻³);
  the symmetric chains of TC and xTC have Nβ_N = 1 + (k₀ + k₁(−1)^N)/N + O(N⁻²) with (k₀, k₁) = (−1, 0), (−2, −3). So TC and xTC
  satisfy (R1) with A = 1, B = ½.

*Proof.* (a) WLXZ (1.4)–(1.5) (quoted): f_n^{(α)} are orthogonal for the step function ψ^{(α)} with jumps (k+α)^{k−1}e^{−k}/k! at
x = ±x_k, x_k = (k+α)^{−1/2}, k ≥ 0, α > 0; they satisfy (1.6) (n+1)f_{n+1} − (n+α)xf_n + f_{n−1} = 0 (n ≥ 1), f₀ = 1, f₁ = αx, and
have leading coefficient (1.9) γ_n = Γ(n+α)/(Γ(α)Γ(n+1)). Dividing (1.6) by γ_N gives the monic recurrence
yR_N = R_{N+1} + β_NR_{N−1} with β_N = γ_{N−1}/((N+α)γ_N) = N/((N+α)(N+α−1)) (check_e1_exact [0], symbolic); at α = 1, β_N = 1/(N+1).
The folded measure (SECOND Lemma 2.1: ∫f(y²)dψ = ∫f dσ) has atoms 1/(k+1) =: 1/j (j ≥ 1) with masses 2j^{j−2}e^{−(j−1)}/(j−1)! = 2e·v_j,
a constant multiple of TC; constants change no coefficient. SECOND Lemma 2.1 gives b_m² = β_{2m−1}β_{2m}, α_m = β_{2m} + β_{2m+1},
g_m = β_{2m+1}. (b) SECOND Lemma 2.2 (Darboux step) gives the coefficients of x·TC from β. The stated chain satisfies the three
chain relations of x·TC (γ′²₁ = α₀(xTC), γ′²_{2m−1}γ′²_{2m} = b_m(xTC)², γ′²_{2m} + γ′²_{2m+1} = α_m(xTC)) as identities of rational
functions (sympy `cancel`, check_e1_exact [2]) and is positive, so by the uniqueness remark after SECOND Lemma 2.2 it is the chain.
(c) Lemma 2.2 again. (d) Exact series, check_e1_exact [3] (all assertions pass). ∎

(The orthogonality (1.4) is Carlitz's theorem as stated by WLXZ; the repo's earlier uses of TC — RH_p1 §0–§1, check_p1_tc — rest on
the same statement. NUMERICAL corroboration: RH/checks/check_p1_tc.out [2] and check_e1_tc.out [2] reproduce b_n, α_n of TC and xTC
from the masses v_k to 3·10⁻¹⁰ and 3·10⁻¹³.)

**Proof of Theorem E1.6.** *Weights.* log H(t) = LnΓ(t+1) + t − (t + ½)ln t − ½ln(2π) equals LnΓ(t) − (t − ½)ln t + t − ½ln(2π) by DLMF 5.5.1 (Γ(t+1) = tΓ(t)), i.e. the
remainder in 5.11.1 after the leading terms, and
DLMF 5.11.1 with the §5.11(ii) remainder bound (real t > 0, first neglected term) gives |log H(t) − 1/(12t)| ≤ 1/(360t³) (t > 0).
So k^{−3/2} = √(2π)H(k)v_k = √(2π)v_k(1 + x_k/12)e^{f₀(k)} with f₀(k) := log H(k) − log(1 + x_k/12) = x_k²/288 + O(x_k³) uniformly in
k ≥ 1 (x_k ≤ 1; |f₀| ≤ C₀x_k² for all k). Thus σ_{3/2} = K·TC·(1 + x/12)e^{f₀} and σ_{5/2} = xσ_{3/2} = K·(xTC)·(1 + x/12)e^{f₀}, with
K = √(2π), ε = 1/12, r₂ = 1/288.
*Application.* For (w, v) = (σ_{3/2}, TC): xv = xTC; for (σ_{5/2}, xTC): xv = x²TC. By Lemma E1.5(d), v and xv satisfy (R1) with
A = 1, B = ½ and all coefficients are ≤ C/n. Proposition E1.4(iii) and Lemma E1.5(d) give

  log(b_n(w)²/b_n(v)²) = (1/12)(−1/n²) + O(n⁻³),  log(g_n(w)/g_n(v)) = (1/12)(−1/(2n²)) + O(n⁻³),

i.e. b_n(w)/b_n(v) = 1 − 1/(24n²) + O(n⁻³) and g_n(w)/g_n(v) = 1 − 1/(24n²) + O(n⁻³). Then h̃_n = b_n²/g_{n−1} has ratio
(1 − 1/(12n²))(1 + 1/(24(n−1)²)) + O(n⁻³) = 1 − 1/(24n²) + O(n⁻³), and α_n = g_n + h̃_n (both summands with the same ratio) as well;
β_{2m} = h̃_m, β_{2m+1} = g_m give β_N(w)/β_N(v) = 1 − 4/(24N²) + O(N⁻³). The expansions of nb_n follow from Lemma E1.5:
2nb_n(TC) = (1 + 1/(2n))^{−1/2} = 1 − 1/(4n) + 3/(32n²) + O(n⁻³), and 3/32 − 1/24 = 5/96; 2nb_n(xTC) = (1 + 1/(2n))^{−1/2}(1 + 1/n)^{−1/2}
= 1 − 3/(4n) + 19/(32n²) + O(n⁻³), and 19/32 − 1/24 = 53/96. The P62 constants are those of the references (Lemma E1.5(d)), since
the ratios are 1 + O(n⁻²). Finally a_n = α_{n−1} has ratio 1 − 1/(24(n−1)²) = 1 − 1/(24n²) + O(n⁻³). ∎

*Remarks.* (1) No RH input is used: Theorem E1.6 reproves Theorem RH₁ (b_n = b_n^{TC}(1 + O(1/n))) with the sharper O(n⁻²) and the
exact second-order constant. (2) The mechanism of −1/24: the 1/(12k) Stirling term of the masses is the polynomial factor 1 + x/12,
which changes log h_n by exactly (1/12)α_n + O(n⁻²) (Christoffel), and α_n − α_{n−1} ≈ −1/n². The O(x²) remainder of the masses
shifts log h_n by r₂(A² + 2B²)/n², which is the same at n and n − 1 to O(n⁻³) and therefore drops out of b_n. This is the pointwise
form of SECOND Cor 3.6 Remark (c), which was HEURISTIC there. (3) At s = 7/2 (reference x²TC, Lemma E1.5(c)) Proposition E1.4(i) still
gives b_n(σ_{7/2}) = b_n(x²TC)(1 + O(n⁻²)), because it only needs coefficient bounds O(1/n) for x³TC (true by comparability with
σ_{9/2}, Lemma E1.1, and Law P) and α_n(x²TC) − α_{n−1}(x²TC) = O(n⁻²). The second-order statement (iii) and the chain need (R1) for
x³TC, which is not available in closed form. Not used below (Theorem E1.10 covers s = 7/2).

## 3. Route C: second-order RH analysis in the symmetric frame of RH₁(r)

### 3.1 The first-order analysis that is used (RH₁(r), REVIEWED)

Fix s > 1 and put a := s − 3/2 > −½ (RH₁(r)'s Fisher–Hartwig exponent; r = s). Fix an integer **m ≥ max(1, ⌈|a|/2⌉)**
(RH₁(r) §3 fixes m := ⌈|a|/2⌉ and states "Any larger m also works"; m ≥ 1 is the only change made here). For each
degree N of the symmetric problem, RH₁(r) (RH_p1_general.md) — which runs WLXZ v1 §§3–6 at α_W = 1 with σ_s's weight — gives:

- (G) the global parametrix N_r := D_{Q,∞}^{σ₃}N D^{−σ₃}, D = D_aD_Q (RH₁(r) §3), with N WLXZ's (5.11) (N-independent),
  D_a(z) = (z/Φ(z))^a (N-independent), D_Q the Szegő function of the entire function Q_m(z) = exp(2Σ_{k=1}^m
  B_{2k}/(2k(2k−1))·(z²/N)^{2k−1}); and (N_{r,1})₁₂(N_{r,1})₂₁ = (N₁)₁₂(N₁)₂₁ = 1 (RH₁(r) §3 "Extraction value");
  (N₁)₁₂ = −ie^L, (N₁)₂₁ = ie^{−L} (WLXZ (5.11) at α_W = 1; RH_p1 §3).
- (Ai) Airy parametrices P_r at ±2 (RH₁(r) §4): P_r = D_{Q,∞}^{σ₃}·A·P^{(3/2)}·q^{−σ₃/2}, q = (z²)^a, A = Ng^{σ₃}N^{−1},
  g = (qQ_m)^{1/2}/D, P^{(3/2)} the parametrix of RH₁ step 4 (WLXZ (6.12)–(6.21) with σ_{3/2}'s weight); P_r has exactly the jumps
  of V inside U(±2, ε), and on ∂U(±2, ε)

    P_rN_r^{−1} = D_{Q,∞}^{σ₃}·A·[P^{(3/2)}N^{−1}]·A^{−1}·[NQ_m^{σ₃/2}N^{−1}]·D_{Q,∞}^{−σ₃}   (RH₁(r) §4).

- (Be) the origin parametrix (RH₁(r) §5, KV frame): P₀ = E_NΨ_a(Nf)W_h^{−σ₃}e^{−Nφ_{KV}σ₃}, E_N = E·e^{Nφ_{KV,+}(0)σ₃}
  e^{−πiσ₃/4}(1/√2)[[1, i], [i, 1]] (KV (5.26)), E = P^∞W_h^{σ₃}e^{±aπiσ₃/2} (with the anti-diagonal factor in sectors V–VIII, KV
  (5.27)–(5.30)), P^∞ := σ₃N_rσ₃, W_h = W·h₀^{1/2}, h₀ = e^L(4 − z²)Q_m; f(z) = iφ_KV(z) − iφ_{KV,+}(0) in ℂ₊ (KV (5.6)) is
  N-independent and conformal on U(0, ε), f′(0) > 0; E_N, E_N^{−1} are analytic and bounded uniformly in N (Lemma B).
- (S) S := V·(parametrix)^{−1} (N_r outside the discs) solves a RH problem on Σ_S = (Σ ∖ discs) ∪ ∂U(0, ε) ∪ ∂U(±2, ε) ∪
  (Σ ∩ U(0, ε)), with no jump inside U(±2, ε) (RH₁(r) §7), and:
  - (S1) on the band pieces (−2+ε, −ε) ∪ (ε, 2−ε): J_S = N_{r,−}diag(κ_N^{−1}, κ_N)N_{r,−}^{−1}, κ_N := H_N²/Q_m, H_N(z) := H(N/z²)
    (RH₁(r) §3);
  - (S2) on Σ ∩ U(0, ε): J_S = J_H with the structured mismatch of RH₁(r) Lemma M;
  - (S3) on the lips and saturated pieces outside the discs: |J_S − I| ≤ Ce^{−cN}, on pieces of total length O(√N) (Lemma W1(r);
    WLXZ (5.8), (6.34));
  - (SN) the first-order small-norm conclusion: S = I + O(1/N) uniformly, in the sense used by RH₁(r) §7 and RH_p1 W1 step 6,
    i.e. WLXZ (6.36)–(6.37): S₋ = I + u_S with u_S = (I − C_{Δ})^{−1}C₋Δ, and ‖u_S‖_{L²(Σ_S)} = O(1/N) (this uses that C₋ is
    bounded on L²(Σ_S) uniformly in N, which is WLXZ's "standard procedure" after (6.35) and the same reliance as RH₁ and
    RH₁(r) §7; alternatively, a uniform bound sup_{Σ_S}|S₋ − I| = O(1/N) together with ‖J_S − I‖_{L¹(Σ_S)} = O(1/N) would give
    the same O(N⁻²) bound in Prop E1.8); and S₁ := lim z(S(z) − I) = −(1/2πi)∫_{Σ_S}S₋(J_S − I)ds;
  - (Id) identification of S with the small-norm solution (RH₁(r) §6, Lemmas O1, X).
- (Ex) extraction (RH_p1 §3, RH₁(r) §7): Nβ_N = (U₁)₁₂(U₁)₂₁ = (V₁)₁₂(V₁)₂₁ exactly (the transformations U → V in Ω_∞ are left
  multiplication by constant diagonal matrices and right multiplication by scalar diagonal functions tending to constants, which
  preserve the product of the off-diagonal z^{−1}-coefficients), and V₁ = N_{r,1} + S₁.

### 3.2 Two-term model expansions

**Lemma E1.7a (Airy model; PROVED-mod-cite: WLXZ (6.8), (6.13); DLMF 9.7.5–9.7.6).** Let Ψ be WLXZ's Airy matrix (6.8),
M₀ := [[1, −i], [−i, 1]], ξ := (2/3)ζ^{3/2}. For each of the four sectors j of (6.8) there is a constant matrix X_j with

  M₀·√π ζ^{−σ₃/4}σ₂Ψ(ζ)σ₂e^{−ξσ₃} = I + X_j/ξ + O(|ξ|⁻²),  ζ → ∞ in the closed sector j.

*Proof.* In each sector, each column of (6.8) consists of Ai(ω^kζ) and a constant times Ai′(ω^kζ) for one k ∈ {0, 1, 2}, and
ph(ω^kζ) stays in [−5π/6, 5π/6] on the closed sector (sector (0, π/2): k = 0, 2 with ph ω²ζ ∈ [−2π/3, −π/6]; (π/2, π): k = 1, 2, phases
[−5π/6, −π/3] and [−π/6, π/3]; the lower sectors by conjugation). DLMF 9.7.5–9.7.6 with two terms (|ph| ≤ π − δ, δ = π/6) give each
entry as e^{∓ξ}ζ^{∓1/4}·(const + const/ξ + O(ξ⁻²)) with the same exponential in each column, so the left side is
L₀ + L₁/ξ + O(ξ⁻²) with constant L₀, L₁; L₀ = I is WLXZ (6.13); X_j := L₁. ∎
(check_e1_models.out [3]: |ξ||M₀R − I| ≤ 0.0838 and |ξ|²|M₀R − I − X_j/ξ| ≤ 0.0404 for |ξ| ≥ 83 in all four sectors.)

**Lemma E1.7b (Bessel/Fisher–Hartwig model; PROVED-mod-cite: Vanlessen (4.26)–(4.33), (4.43)–(4.46) = KV (5.23); DLMF 10.17.5–6,
10.40.1–2).** Let Ψ_a be the model of KV (5.17)–(5.23) = Vanlessen's Ψ_λ (λ = a > −½), B := (1/√2)[[1, −i], [−i, 1]], and C_q the
constant factor of Vanlessen (4.43)–(4.46) in quadrant q. For each of the eight sectors j of Vanlessen's Figure 5 there is a constant
matrix Ψ₁^{(j)} with

  Ψ_a(ζ) = B(I + Ψ₁^{(j)}/ζ + O(|ζ|⁻²))e^{πiσ₃/4}e^{−iζσ₃}C_q,  ζ → ∞ in the closed sector j.

*Proof.* By (4.26)–(4.33), in each sector each column of Ψ_a is ζ^{1/2} (or (−ζ)^{1/2}) times a constant multiple of one Bessel kind
— H^{(2)}_{a±½}(ζ), H^{(1)}_{a±½}(ζ) (sectors I, VIII), H^{(1,2)}_{a±½}(−ζ) (IV, V), I_{a±½}(ζe^{∓πi/2}), K_{a±½}(ζe^{∓πi/2}) (II, III,
VI, VII) — evaluated at an argument whose phase lies in [−π/4, π/4] on the closed sector. This is inside the sectors of
DLMF 10.17.5 (−π + δ ≤ ph ≤ 2π − δ), 10.17.6 (−2π + δ ≤ ph ≤ π − δ), 10.40.1 (|ph| ≤ π/2 − δ), 10.40.2 (|ph| ≤ 3π/2 − δ), δ = π/4.
Taking two terms of each expansion, every entry of Ψ_a(ζ)C_q^{−1}e^{iζσ₃}e^{−πiσ₃/4} is const + const/ζ + O(ζ⁻²) uniformly; the
constant term is B by Vanlessen (4.43)–(4.46) (which are this computation to leading order); Ψ₁^{(j)} := B^{−1}·(the 1/ζ term). ∎
(check_e1_models.out [4]: for λ ∈ {−0.25, 0.5, 1.5} and all eight sectors, |ζ||K − I| and |ζ|²|K − I − Ψ₁^{(j)}/ζ| are bounded,
K := B^{−1}Ψ_a(e^{πiσ₃/4}e^{−iζσ₃}C_q)^{−1}.)

### 3.3 The jumps of S to second order

**Lemma E1.7 (PROVED-mod-cite; inputs in the summary table).** Uniformly on the respective contours, as N → ∞:
(i) on ∂U(±2, ε): J_S = I + Δ^{±}(z)/N + O(N⁻²), with Δ^{±} bounded and independent of N;
(ii) on ∂U(0, ε): J_S = I + (Δ^{0,e}(z) + (−1)^NΔ^{0,o}(z))/N + O(N⁻²), with Δ^{0,e}, Δ^{0,o} bounded and independent of N;
(iii) on the band pieces (S1) and on Σ ∩ U(0, ε) (S2): |J_S − I| ≤ CN^{−2m−1} ≤ CN⁻³;
(iv) elsewhere: (S3).
(Each circle is oriented as in RH₁(r); for the opposite orientation J_S is replaced by its inverse, whose expansion is
I − Δ/N + O(N⁻²).)

*Proof.* *Three N-smooth scalars.* (a) H_N(z) = H(N/z²): log H(t) = 1/(12t) + O(|t|⁻³) uniformly in |ph t| ≤ 2π/3 (DLMF 5.11.1 with
the §5.11(ii) bound, sec²(π/3)-factor; as RH₁(r) Lemma S), so H_N = 1 + z²/(12N) + O(N⁻²) uniformly on compact subsets of
{|arg(±z)| ≤ π/3}, in particular on ∂U(±2, ε). (b) log Q_m = z²/(6N) + O(N⁻³) uniformly on compacts (B₂ = 1/6, m ≥ 1). (c) log D_Q =
𝒮[log Q_m] with 𝒮 the linear Szegő operator of [−2, 2]; by the representation used in RH₁(r) Lemma G(iii) (Cauchy integral of
the difference quotient of the entire function log Q_m), 𝒮 maps O(N⁻³)-small entire functions to O(N⁻³)-small functions uniformly
on the circles, including boundary values on (−2, 2); so D_Q = 1 + 𝒮[x²/6]/N + O(N⁻²) and D_{Q,∞} = 1 + δ_∞/N + O(N⁻²) with
N-independent 𝒮[x²/6], δ_∞. Consequently every factor built from Q_m, D_Q, D_{Q,∞} below is (its N = ∞ value) + O(1/N) uniformly,
with bounded inverse.
*(i), at +2.* First the σ_{3/2}-parametrix. With w̃_σ the WLXZ (4.27) weight of σ_{3/2} (= TC's times H_N, constants dropped as in
RH_p1 §1) put G_σ := D̃²/w̃_σ; then (6.12), (6.15) read P^{(3/2)} = G_σ^{−σ₃/2}m_r f̃_N^{−σ₃/4}·√πσ₂Ψ(f̃_N)σ₂e^{Nφ̃σ₃}·G_σ^{σ₃/2},
f̃_N = N^{2/3}f̃₁, f̃₁ := (−(3/2)φ̃)^{2/3} N-independent ((2.4), (2.5), (6.10)), so that the Airy variable has ξ = (2/3)f̃_N^{3/2} =
−Nφ̃. Here φ̃ = φ ± πi/z² (WLXZ (4.29)) vanishes at 2 ((6.11)), although φ₊(2) = −πi/4; likewise φ̂ ((4.30)) vanishes at −2. So
no constant phase e^{Nφ₊(±2)σ₃} (which would give an i^N dependence) enters the Airy matching. The only lattice phase,
e^{2iθ} = e^{2πiN/z²} (α_W = 1), is an analytic function of z absorbed in φ̃, φ̂. Two facts at α_W = 1, both elementary from the quoted formulas (and checked to 10⁻⁴⁰, check_e1_models.out [1]):
(F1) G_TC = G₀·H_N^{−1} with G₀ := e^{−L}(z² − 4)^{1−2α_W} (from (4.15) D̃ = 1/H_N, (2.15), (3.4), (3.7), (4.24), (4.27)), hence
G_σ = G₀H_N^{−2}; (F2) G₀^{σ₃/2}NG₀^{−σ₃/2}M₀ = m_r exactly ((5.11), (6.16)), i.e. (6.14) is exact for the model G₀. By Lemma E1.7a,
on ∂U(2, ε) (where |ξ| ≍ N and f̃₁ lies in a fixed sector pattern)

  P^{(3/2)}N^{−1} = H_N^{σ₃}·N G₀^{−σ₃/2}(I − X_j/(Nφ̃) + O(N⁻²))G₀^{σ₃/2}·H_N^{−σ₃}·N^{−1}
                 = I + (1/N)[−NG₀^{−σ₃/2}X_jG₀^{σ₃/2}N^{−1}/φ̃ + (z²/12)(σ₃ − Nσ₃N^{−1})] + O(N⁻²) =: I + Δ^{(3/2)}/N + O(N⁻²),

using (a), N, N^{−1}, G₀^{±1} bounded on ∂U(2, ε) and |φ̃| bounded below there. Then in the display (Ai): A = A_∞ + O(1/N) with
A_∞ := N(q^{1/2}/D_a)^{σ₃}N^{−1} (bounded with bounded inverse, RH₁(r) §4), NQ_m^{σ₃/2}N^{−1} = I + (z²/(12N))Nσ₃N^{−1} + O(N⁻²) by (b),
and D_{Q,∞}^{σ₃}(I + Y/N)D_{Q,∞}^{−σ₃} = I + Y/N + O(N⁻²) by (c). So Δ^{+} = A_∞Δ^{(3/2)}A_∞^{−1} + (z²/12)Nσ₃N^{−1}. The disc at −2 is
the same with WLXZ (6.17)–(6.21) (the reflected construction σ₁Ψ(−·)σ₁, φ̂).
*(ii).* In the KV frame (RH₁(r) works with σ₃Vσ₃ there; J_S is the σ₃-conjugate, which does not affect the claim), by KV's
construction of E_N (Vanlessen (4.47)–(4.52), Remark 4.4: E_N is chosen so that the leading terms cancel exactly) and Lemma E1.7b,

  P₀(P^∞)^{−1} = E·e^{Nφ_{KV,+}(0)σ₃}e^{−πiσ₃/4}(I + Ψ₁^{(j)}/(Nf(z)) + O(N⁻²))e^{πiσ₃/4}e^{−Nφ_{KV,+}(0)σ₃}E^{−1}

on ∂U(0, ε) ∩ f^{−1}(sector j): for z ∈ f^{−1}(I ∪ II) this is the identity e^{−iζσ₃}C₁W_h^{−σ₃}e^{−Nφ_{KV}σ₃}(P^∞)^{−1} =
e^{−Nφ_{KV,+}(0)σ₃}E^{−1} (ζ = Nf, C₁ = e^{−aπiσ₃/2}, E = P^∞W_h^{σ₃}e^{aπiσ₃/2}, f = iφ_KV − iφ_{KV,+}(0)), and the other sectors are
KV (5.28)–(5.30) in the same way. *The phase.* φ_KV = −φ (RH₁(r) §5), and φ₊(0) = l/2 − g₊(0). On the band g′₊ = −πiψ (WLXZ (4.3)) and g₊(2) = l/2 + πi/4
(proof of WLXZ Prop. 4.2), so g₊(x) = l/2 + πi/4 + πi∫_x^2ψ and φ₊(x) = −πi/4 − πi∫_x^2ψ = −πiμ([x, ∞)) ((2.3)); and
∫_0^2ψ = ¼ (with ∫_2^∞ψ = ¼) by (2.1) (check_e1_models.out [2]). So φ₊(0) = −iπ/2. So φ_{KV,+}(0) = iπ/2 and e^{Nφ_{KV,+}(0)σ₃} = i^{Nσ₃}; conjugation by
it multiplies the off-diagonal entries by i^{±2N} = (−1)^N and fixes the diagonal. E = E_∞ + O(1/N) (through P^∞ and W_h, by (b),
(c)), E_∞ bounded with bounded inverse, and |f| is bounded below on ∂U(0, ε). Hence (ii) with
Δ^{0,e} = E_∞ŶᵈE_∞^{−1}/f, Δ^{0,o} = E_∞Ŷᵒᶠᶠ E_∞^{−1}/f, Ŷ := e^{−πiσ₃/4}Ψ₁^{(j)}e^{πiσ₃/4} split into diagonal and off-diagonal parts.
*(iii).* With m ≥ 1, Lemma S of RH₁(r) gives |κ_N − 1| ≤ C(|z|²/N)^{2m+1} uniformly in |arg(±z)| ≤ π/3, so on the band pieces
|J_S − I| ≤ C·4^{2m+1}N^{−2m−1} (N_r, N_r^{−1} bounded there). On Σ ∩ U(0, ε), RH₁(r) Lemma M's proof gives, for ρ := N|f| ≥ 1,
|J_H − I| ≤ C(|z|²/N)^{2m+1} ≤ Cε^{4m+2}N^{−2m−1} (the amplification is bounded for ρ ≥ 1), and for ρ ≤ 1 (|z| ≲ 1/N)
|J_H − I| ≤ CN^{−2m−1−2|a|}|z|^{4m+2−2|a|}(1 + |log(N|z|)|)² = CN^{−6m−3}ρ^{δ}(1 + |log ρ|)² ≤ C′N^{−6m−3} (ρ ≍ N|z| ≤ 1,
δ = 4m + 2 − 2|a| > 0); the discarded lip terms (J2) are O(N^{−K}). ∎

### 3.4 Second-order small norm and extraction

**Proposition E1.8 (PROVED-mod-cite).** S₁ = (Σᵉ + (−1)^NΣᵒ)/N + O(N⁻²) with constant matrices

  Σᵉ := −(1/2πi)[∮_{∂U(2,ε)}Δ⁺ + ∮_{∂U(−2,ε)}Δ⁻ + ∮_{∂U(0,ε)}Δ^{0,e}],  Σᵒ := −(1/2πi)∮_{∂U(0,ε)}Δ^{0,o}

(orientations as in RH₁(r)).

*Proof.* S₁ = −(1/2πi)∫(J_S − I)ds − (1/2πi)∫(S₋ − I)(J_S − I)ds. By Lemma E1.7, ‖J_S − I‖_{L¹∩L²(Σ_S)} = O(1/N) (the circles and the
pieces in (iii) have bounded length; the pieces in (iv) have length O(√N) and J_S − I = O(e^{−cN})), so the second integral is
≤ ‖S₋ − I‖_{L²}‖J_S − I‖_{L²} = O(N⁻²) by (SN). In the first, the circles give (1/N)∮(Δ's) + O(N⁻²), the pieces of (iii) give
O(N⁻³) and those of (iv) O(√Ne^{−cN}). ∎

**Theorem E1.9 (PROVED-mod-cite).** For every s > 1 there are real κ₀ = κ₀(s), κ₁ = κ₁(s) with

  Nβ_N = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²)  (N → ∞).

*Proof.* By (Ex), Nβ_N = ((N_{r,1})₁₂ + (S₁)₁₂)((N_{r,1})₂₁ + (S₁)₂₁). By (G), (N_{r,1})₁₂(N_{r,1})₂₁ = 1, (N_{r,1})₁₂ = D_{Q,∞}²(N₁)₁₂ =
−ie^L(1 + O(1/N)) and (N_{r,1})₂₁ = ie^{−L}(1 + O(1/N)). With Prop E1.8 (S₁ = O(1/N)):
Nβ_N = 1 + (−ie^L(S₁)₂₁ + ie^{−L}(S₁)₁₂) + O(N⁻²) = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²), κ₀ := −ie^LΣᵉ₂₁ + ie^{−L}Σᵉ₁₂,
κ₁ := −ie^LΣᵒ₂₁ + ie^{−L}Σᵒ₁₂. Along even and along odd N the left side is real, so κ₀ ± κ₁ ∈ ℝ. ∎

### 3.5 Proof of Theorem E1.10

*Fold.* β_{2m−1} = (2m−1)^{−1}(1 + (κ₀ − κ₁)/(2m−1) + O(m⁻²)), β_{2m} = (2m)^{−1}(1 + (κ₀ + κ₁)/(2m) + O(m⁻²)), so
b_m² = β_{2m−1}β_{2m} = (4m²)^{−1}(1 + 1/(2m) + κ₀/m + O(m⁻²)): mb_m = ½(1 + (κ₀ + ½)/(2m) + O(m⁻²)). κ₁ cancels. Likewise
α_m = β_{2m} + β_{2m+1} gives mα_m = 1 + (κ₀ − ½)/(2m) + O(m⁻²). So (E) holds with ε = 1 and d₁ = (κ₀ + ½)/2.
*Value.* Under (E) at s, 𝒟_n := Σ_{j≤n}log(2jb_j) = d₁log n + O(1); UL Cor UL-3.10 (PROVED-mod-cite, REVIEWED) gives
𝒟_n = −((s−1)/2)log n + O(1) (indeed + const + o(1)) for every s > 1 at p = 1. Hence d₁ = −(s−1)/2 (this is UL Cor UL-3.9 at p = 1,
whose only hypothesis, (E) at s, is now proved), κ₀ = 2d₁ − ½ = ½ − s, and mα_m = 1 − s/(2m) + O(m⁻²).
*Pairings.* α_n/(2b_n) = (1 − s/(2n))/(1 − (s−1)/(2n)) + O(n⁻²) = 1 − 1/(2n) + O(n⁻²); and α_{n−1}/(2b_n) = (α_{n−1}/(2b_{n−1}))(b_{n−1}/b_n)
with b_{n−1}/b_n = 1 + 1/n + O(n⁻²) gives 1 + 1/(2n) + O(n⁻²).
*Chain.* ng_{n−1} = nβ_{2n−1} = ½(1 + 1/(2n))(1 + (κ₀ − κ₁)/(2n)) + O(n⁻²) = ½(1 + (1 + κ₀ − κ₁)/(2n)) + O(n⁻²). ∎

*Consistency.* κ₀ = ½ − s is k₀ = −(s−1) − p/2 of Conjecture P62 at p = 1; with the conjectured κ₁ = −3a = −(p+2)a, ng_{n−1} =
½(1 + a/n), the form of E_pgt1 Cor E.6. Theorem E1.6 gives κ₁ = 0 at s = 3/2 and κ₁ = −3 at s = 5/2 (Lemma E1.5(d)), in agreement.
The (−1)^N term is present (κ₁ ≠ 0 at s = 5/2) but invisible in b_n, α_n at first order — exactly the structure seen numerically in
RH₁(r) §0 (k₁ ≈ −3a) and SECOND §1.1.

## 4. Why p = 1 works here although E_pgt1 §9 recorded a failure

E_pgt1 §9 worked in the **x-frame** (Paper 2 / RH_px at p = 1): there the hard edge is the band endpoint 0, the classical quotient
parametrix needs the band weight continued across (−δ, 0), which fails at p = 1 (Paper 2 Remark rem:quotient-p1: unimodular
lens-scalar ratio −e^{−2iθ} and double poles of the continued H_n at −n/m), and Paper 2's Conway–Deift comparison parametrix has no
rate. In the **symmetric frame** (WLXZ, RH₁(r)) the same point is the band centre, the lattice lies on both sides, iℝ (where
t = N/z² < 0 and Γ has its poles) carries no jump, and the local problem is a Fisher–Hartwig point with an explicit KV/Vanlessen
parametrix whose mismatch is controlled by the Stirling truncation Q_m (RH₁(r) Lemmas S, M) — to any power N^{−2m−1}. The non-flat
band factor H_N = 1 + z²/(12N) + … (the analogue of E_pgt1 Lemma E.2 fails at p = 1, as E_pgt1 §9 says) enters Δ^{±} at order 1/N
with an N-independent coefficient, which is all that existence needs.

## 5. Consequences for SECOND.md (as updated by Plans 64, 65)

- **SECOND §4 (E) for p = 1:** closed (Theorem E1.10), with ε = 1. (E) remains GAP only for 0 < p < 1.
- **SECOND Cor 3.3** at p = 1 (needs (E) at s and s + 1): unconditional; n(G_n − G_{n−1}) = O(1/n) directly from Theorem E1.9.
- **SECOND Thm 3.4** at p = 1: unconditional, and superseded by Theorem E1.10 (O(n⁻²)).
- **SECOND Cor 3.6 (ii)–(iii):** unconditional; and Cor 3.6 Remark (b) ("−1/24 … CONJECTURE") is Theorem E1.6; Remark (c)
  (HEURISTIC) is made precise by Proposition E1.4(iii) and Remark (2) after Theorem E1.6.
- **SECOND Cor 3.9** at p = 1: unconditional; g(1) = 0 PROVED-mod-cite.
- **Conjecture P62 at p = 1:** PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀ (all s > 1, remainder O(n⁻²)); k₁ PROVED for s ∈ {3/2, 5/2}
  (elementary), GAP otherwise.
- **RH_p1 §0 −1/24 conjecture:** PROVED-mod-cite (Theorem E1.6), both for b_n and a_n.

## 6. Numerics (NUMERICAL; not used in the proofs)

- `checks/check_e1_exact.py` (.out) — exact computer algebra for Lemma E1.5, the coefficient differences of Theorem E1.6 and its
  constants (ε = 1/12, r₂ = 1/288 from the series of log H; −1/24 for b, g, h̃, α; −1/6 for β_N; d₂ = 5/96, 53/96), and an exact-moment
  corroboration of Lemma E1.5(a),(b) (tree-function moments of TC, exact Stieltjes procedure, n < 12): all assertions pass.
- `checks/check_e1_tc.py` (.out) — Theorem E1.6 (b, α, g; h̃ and β_N are covered by check_e1_exact and REVIEW_Plan66_B §1.6). Each pair through the same pipeline (that of RH/checks/check_p1_tc.py), M = 1500,
  K = 2·10⁵, tails to 10¹² and 10¹⁶ (identical to the printed digits): n²(r − 1) at n = 1499 is −0.04165 (b), −0.04162 (α), −0.04161 (g)
  for σ_{3/2}/TC and −0.04162, −0.04160, −0.04150 for σ_{5/2}/xTC, approaching −1/24 = −0.041667 with O(1/n) corrections. Reference
  pipeline vs exact formulas: 3·10⁻¹⁰ (TC), 3·10⁻¹³ (xTC) at tend = 10¹⁶.
- `checks/check_e1_rate.py` (.out) — Theorem E1.10, σ_{1,s} from so_coeffs.py (nmax = 800, K = 8·10⁴ and 1.6·10⁵, K → 2K
  differences ≤ 5·10⁻⁵). The second-order residuals rb = n²(2nb_n − 1 + (s−1)/(2n)) and ra = n²(nα_n − 1 + s/(2n)) stay bounded
  for n = 50…798 at s = 1.25, 1.5, 2, 3, 4.5 (rb(798) = −0.1119, 0.05207, 0.3330, 0.7082, 0.8102; ra(798) = 0.645, 0.583, 0.833,
  2.826, 9.53; at s = 4.5 rb still drifts slowly, 0.920 → 0.810). At s = 3/2, rb → 0.05207 against the proved d₂ = 5/96 =
  0.052083 (Thm E1.6). The chain residual rc = N²(Nβ_N − 1 − (k₀ + k₁(−1)^N)/N) with k₀ = ½ − s and the *conjectured* k₁ = −3(s − 3/2)
  stays bounded for even and for odd N at all five s (e.g. s = 3: 33.8 → 35.2 and −9.39 → −9.65), which supports the k₁
  conjecture (an error δ in k₁ would make rc grow like δN). Period-4 test: the N mod 4 class means of N(Nβ_N − 1) − k₀ − k₁(−1)^N
  over N ∈ [1180, 1220) agree between classes 0 and 2 and between 1 and 3 to ≤ 1.6·10⁻⁴ (the drift of the window), whereas an
  i^N term at order 1/N would separate them by O(1).
- `checks/check_e1_models.py` (.out) — inputs of Lemma E1.7: [1] G_TC/(G₀H_N^{−1}) − 1 ≤ 3·10⁻⁴⁰ and the (6.14) model identity to 9·10⁻⁴¹
  on |z − 2| = 0.3; [2] ∫_0^2ψ = ∫_2^∞ψ = ¼, φ₊(0) = −iπ/2; [3] Airy two-term expansion in all four sectors; [4] Bessel-model
  two-term expansion in all eight sectors for λ ∈ {−0.25, 0.5, 1.5}. Both test **one** constant for all rays and all sectors (Rule R A5):
  the 1/ξ and 1/ζ coefficients are X = [[−1/72, i/12], [i/12, 1/72]] and Ψ₁ = (a/2)σ₁ − (ia²/2)σ₃ (NUMERICAL; |ξ|²- resp.
  |ζ|²-scaled residuals ≤ 0.041 resp. ≤ 0.48 for |ζ| = 25…400) (Hankel functions evaluated through K_ν, DLMF 10.27.8, to avoid
  cancellation — an evaluation device only).

## 7. Rule A (adversarial pass) — log

- *Proposition E1.4, sign and size.* ε enters log h_n with α_n(v) of the **reference** (Christoffel is exact for v); the
  second-order claim needs (R1) for both v and xv with the same A, B — for v = TC, xv = xTC this is Lemma E1.5(d). Tested
  numerically for all three of b, α, g at two lattice points (check_e1_tc): all → −1/24, none → −1/12 or 0 (which a sign or
  factor-2 slip in ε(α_n − α_{n−1}) or in the g-formula would give).
- *Where Proposition E1.4 fails.* For s ∉ 3/2 + ℤ the weight ratio to any TC-Christoffel transform is x^β·(1 + O(x)), β ∉ ℤ, not
  (1 + εx)e^{O(x²)}; Lemma E1.3 then gives only an O(1) sandwich (E[x^{±β}] is not 1 + O(1/n)). This is why Route C is needed.
- *Could the 1/N term of β_N oscillate with period 4 (which would put a (−1)^n term into b_n)?* Only the phase e^{Nφ_{KV,+}(0)σ₃}
  depends on N non-smoothly; φ₊(0) = −iπμ([0, ∞)) = −iπ/2 because the equilibrium measure is even with total mass 1 — an exact
  fact, not a numerical one ((2.1); check [2]). If the band mass to the right of 0 were irrational, the first-order term would be
  quasi-periodic and (E) could fail. check_e1_rate prints the N mod 4 class means of N(Nβ_N − 1) − k₀ − k₁(−1)^N: their spread is
  O(1/N).
- *The (−1)^N term is real and does not cancel in the chain.* κ₁ = −3 at s = 5/2 (exact, Lemma E1.5(d) + Thm E1.6); it cancels in
  b_m² = β_{2m−1}β_{2m} and α_m = β_{2m} + β_{2m+1} only because the fold pairs one odd and one even index.
- *Choice m ≥ 1.* With m = 0 (allowed in RH₁(r) for |a| < 3/4) the band mismatch κ_N − 1 = H_N² − 1 = z²/(6N) + … is only
  O(1/N), and inside U(0, ε) it is amplified by Ψ_a(Nf); whether this still gives Theorem E1.9 was not checked. m ≥ 1 makes all
  non-circle jumps O(N⁻³) uniformly, which is what §3.4 uses.
- *Second-order small norm without a new operator bound.* Only the first-order output ‖S₋ − I‖_{L²} = O(1/N) (which already contains the
  uniform L² boundedness of the Cauchy operator inherited from WLXZ/RH₁(r)) is used, multiplied by ‖J_S − I‖_{L²} = O(1/N). No uniformity of the Cauchy operator beyond what
  RH₁(r) §7 already uses.
- *Uniformity of the model expansions on the circles.* The sectors in ζ = Nf(z) (Bessel) and f̃_N(z) (Airy) correspond to fixed arcs
  of the circles (f, f̃₁ N-independent and conformal); the DLMF expansions are uniform in closed sectors; at sector boundaries both
  adjacent formulas apply (the model jumps there are exponentially close to I after conjugation, or exact constant jumps).
- *Value of d₁ without computing residues.* Existence alone fixes d₁ via the log-average law; independent confirmation: the elementary
  Theorem E1.6 at s = 3/2, 5/2 (same values), and check_e1_rate at five s.
- *Hidden N-dependence.* WLXZ's D, D̃, D̂, E depend on N only through N/z² (H_N) and the lattice phases e^{±2iθ}, θ = πN/z² − π;
  the latter appear only in jumps that are O(e^{−cN}) (S3) or are removed exactly by the parametrices (Airy discs; KV absorption);
  the Airy-disc weight is G₀·H_N^{−2} exactly (F1), with no lattice phase.
- *Converse / scope.* Theorem E1.10 is stated for pure powers at p = 1 only (RH₁(r)'s setting). For slowly varying factors the
  tilt law (G1 §3.17) predicts a different 1/n term; nothing is claimed.

## 8. What remains open (GAP)

- **k₁(s) = κ₁(s) for s ∉ {3/2, 5/2}** (GAP; CONJECTURE −3(s − 3/2) = −(p+2)a, NUMERICAL: RH₁(r) §0 fits, SECOND §1.1, check_e1_rate
  rc column). It needs the actual residues: κ₁ = −ie^LΣᵒ₂₁ + ie^{−L}Σᵒ₁₂ with Σᵒ from the off-diagonal part of the first correction
  Ψ₁ of the Fisher–Hartwig model at the band centre (computable from DLMF 10.17.1 a₁(a ± ½), as in E_pgt1 Lemma E.5).
  Numerically k₁ = −3(s − 3/2) to 10 digits at s ∈ {1.25, 1.5, 2, 2.5, 3} (500/1000-digit Jacobi coefficients from the exact moments
  ζ(s + j), REVIEW_Plan66_B.md §1.7; NUMERICAL, still GAP).
  *Route (Rule R A6, INFO).* check_e1_models [4] indicates that Ψ₁ = (a/2)σ₁ − (ia²/2)σ₃ is the same in all eight sectors (NUMERICAL).
  If so, Δ^{0,o} = E_∞ŶᵒᶠᶠE_∞^{−1}/f is one meromorphic function in U(0, ε) with a simple pole at 0 (E_∞ analytic, f(0) = 0,
  f′(0) = πψ(0)), so Σᵒ is a single residue, ±E_∞(0)ŶᵒᶠᶠE_∞(0)^{−1}/f′(0), and the k₁ GAP reduces to evaluating E_∞(0) (from P^∞, W_h,
  D_a near 0). Note Ψ₁ᵒᶠᶠ ∝ a, consistent with κ₁ ∝ a and κ₁(3/2) = 0. Not done here.
- **d₂(1, s) for s ∉ {3/2, 5/2}** (second order; the method of §3 would need Δ₂ and the O(1/N) parts of H_N, Q_m, D_Q in Δ₁).
- **(E) for 0 < p < 1** (GAP, unchanged; E_pgt1 §9).
- **Rule L** (novelty) not done; in particular for Theorem E1.6 (a closed second-order constant for a discrete measure with an
  accumulation point via Tricomi–Carlitz).

## 9. Citations (Rule C)

New quotes (read 2026-10-15; recorded in RH/CITATIONS.md, entry "(WLXZ-v1, Plan 66)"): WLXZ v1 (1.4)–(1.9) (TC orthogonality,
recurrence, leading coefficient), (6.8), (6.12)–(6.16) (Airy parametrix and matching), (6.34)–(6.37) (small norm), (2.1)–(2.3),
(4.3)–(4.4) (equilibrium density and φ); Vanlessen (4.26)–(4.33), (4.43)–(4.46), (4.47)–(4.52), Remark 4.4 (entry "(Van, Plan 66)").
Reused entries (hypotheses re-checked above): (KV) (5.23), (5.26)–(5.30); (DLMF) §5.11; (DLMF-9, Paper 2) 9.7.5–9.7.6;
(DLMF-10.17, Plan 55) 10.17.5–10.17.6; (DLMF-10.40, Paper 2) 10.40.1–10.40.2; DLMF 5.5.1 (Γ(t+1) = tΓ(t), to rewrite log H as the remainder of 5.11.1).
Internal (REVIEWED): RH₁(r) (RH_p1_general.md), RH₁ (RH_p1.md), SECOND Lemmas 2.1, 2.2, UL Lemma V and Cor UL-3.10.

## 10. Integration (applied after the Rule R fixes, reconciled with master cb054bc (Plans 65, 69 wording); labels tagged
"(Plan 66, E_p1.md; not yet REVIEWED)" for the coordinator's diff-check)

Tag every changed label "(Plan 66, E_p1.md; not yet REVIEWED)".

**SECOND.md**
1. Status block: add a line "*Plan 66 update (2026-10-15, not yet REVIEWED):* `E_p1.md` (same directory) proves (E) at p = 1 for every
   s > 1 (remainder O(n⁻²)) and the −1/24 constant at s = 3/2; rows marked "Plan 66" carry its labels."
2. Summary row **Conj. P62**: "CONJECTURE for 0 < p ≤ 1" → "CONJECTURE for 0 < p < 1; at p = 1 PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀
   (E_p1 Thm E1.10, remainder O(n⁻²)) and for k₁ at s ∈ {3/2, 5/2} (E_p1 Thm E1.6); k₁ at other s GAP (Plan 66)".
3. Row **Cor 3.3**: append "; unconditional for p = 1 (E_p1 Thm E1.10) (Plan 66)".
4. Row **Thm 3.4**: append "; for p = 1 unconditional and superseded by E_p1 Thm E1.10 (α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²)) (Plan 66)".
5. Row **Cor 3.6**: (ii)–(iii) → "PROVED-mod-cite (E_p1 Thm E1.10, or elementary Thm E1.6 at s = 3/2, 5/2) (Plan 66)"; add
   "Remark (b) (−1/24): PROVED-mod-cite, E_p1 Thm E1.6 (Plan 66)".
6. Row **Cor 3.9**: append "; unconditional for p = 1 (E_p1 Thm E1.10), g(1) = 0 PROVED-mod-cite (Plan 66)".
7. Row **§4 (E)**: "GAP for 0 < p ≤ 1" → "PROVED-mod-cite for p = 1 with ε = 1 (E_p1 Thm E1.10; RH₁(r) frame, second-order matching;
   value from UL Cor UL-3.10) (Plan 66); GAP for 0 < p < 1".
8. Row **§4 g(p)**: "p = 1: g(1) = 0 CONDITIONAL on (E) (Cor 3.9)" → "p = 1: g(1) = 0 PROVED-mod-cite (E_p1 Thm E1.10) (Plan 66)".
9. New row after "Thm E.1, Cor E.6": "| Thm E1.6, E1.10 (Plan 66) | p = 1: every s > 1: nb_n = ½(1 − (s−1)/(2n) + O(n⁻²)), nα_n = 1 − s/(2n) +
   O(n⁻²), α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²), Nβ_N = 1 + (½ − s + κ₁(−1)^N)/N + O(N⁻²); s = 3/2, 5/2: b_n, α_n, g_n = TC resp. xTC
   values × (1 − 1/(24n²) + O(n⁻³)) | E1.10: PROVED-mod-cite (RH₁(r); WLXZ v1 (6.8), (6.12)–(6.16), (6.34)–(6.37); KV (5.23), (5.26)–(5.30);
   Vanlessen (4.26)–(4.33), (4.43)–(4.52); DLMF 5.11, 9.7.5–6, 10.17.5–6, 10.40.1–2; UL Cor UL-3.10); E1.6: PROVED-mod-cite (WLXZ v1
   (1.4)–(1.9); DLMF 5.11) + exact computer algebra (Plan 66) |".
10. Conjecture P62 heading (§1): append "Plan 66: at p = 1 PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀ (E_p1.md Thm E1.10)."
11. Cor 3.6 Remarks (b), (c): add "(Plan 66: (b) is E_p1 Thm E1.6; (c) is made precise by E_p1 Prop E1.4(iii).)"
12. Cor 3.9 bullet list: add "*Plan 66:* for p = 1, (E) holds at every s (E_p1 Thm E1.10), so the corollary is unconditional there."
13. §4: after the Plan 65 paragraph add "*Plan 66:* for p = 1 the GAP is closed by `E_p1.md` (Thm E1.10): the obstruction of
   E_pgt1 §9 concerns the x-frame; in the symmetric frame of RH₁(r) the second-order matching works (E_p1 §§3–4). The text below
   remains the GAP statement for 0 < p < 1." In the paragraph "**p ≤ 1.**" replace "p = 1: RH₁(r) … x-frame;" by "p = 1: done (E_p1);".
14. §6 checks list: add "`checks/check_e1_exact.py`, `check_e1_tc.py`, `check_e1_rate.py`, `check_e1_models.py` (.out) — E_p1.md (Plan 66)."

**THEOREMS.md**
1. §2.10 heading: append "and Plan 66: (E) at p = 1 (research/G1/RH/second_order/E_p1.md; not yet REVIEWED)".
2. Row **Conjecture P62**: "CONJECTURE (0 < p ≤ 1)" → "CONJECTURE (0 < p < 1); p = 1: PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀ (E_p1 Thm E1.10)
   and k₁ at s ∈ {3/2, 5/2} (E_p1 Thm E1.6) (Plan 66)".
3. Row **Cor 3.3, Thm 3.4**: append "; unconditional for p = 1, Thm 3.4 superseded there by E_p1 Thm E1.10 (Plan 66)".
4. Row **Prop 3.5, Cor 3.6**: (ii)–(iii) → "PROVED-mod-cite (E_p1, Plan 66)".
5. Row **Prop 3.7, Thm 3.8, Cor 3.9**: append "; for p = 1 3.9 unconditional, g(1) = 0 (E_p1) (Plan 66)".
6. Row **(E), g(p)**: "GAP for 0 < p ≤ 1" → "PROVED-mod-cite for p = 1 (E_p1.md Thm E1.10) (Plan 66), GAP for 0 < p < 1".
7. New row after "Thm E.1, Cor E.6 (Plan 65)": the row of SECOND item 9 above, Location "research/G1/RH/second_order/E_p1.md,
   checks/check_e1_*.out".
8. Row **RH₁** (§2, line "σ = Σk^{−3/2}δ_{1/k}"): append "; sharpened (Plan 66, E_p1 Thm E1.6, elementary): b_n = b_n^{TC}(1 − 1/(24n²) + O(n⁻³)),
   same for a_n".
9. §4 item 13: append "*Update (Plan 66, not yet REVIEWED; E_p1.md):* (E) is PROVED-mod-cite at p = 1 for every s > 1 (remainder O(n⁻²);
   d₁, e₁, e₁ˢ, k₀ of P62), and the −1/24 conjecture is PROVED-mod-cite (elementary comparison with Tricomi–Carlitz; also at s = 5/2 vs
   x·TC). Still open: k₁ at p = 1 for s ∉ {3/2, 5/2}; (E) and g(p) for 0 < p < 1."

**RH/CITATIONS.md** (added in this plan's commit; append-only): entries "(WLXZ-v1, Plan 66)", "(Van, Plan 66)" and "(Plan 66 reuse)".

**RH_p1.md §0** (optional, integrator's choice): after "consistent with a limit −1/24 (conjecture, not proved)" add "— proved in
second_order/E_p1.md Thm E1.6 (Plan 66)".
