# JZC TODA: Theorem T — the layers of the lattice model are the Toda flow of the integer layers (full proof; T_H for Hurwitz)

Status (2026-10-23): **NOT REVIEWED** (no Rule R reader). Every item below carries NOT REVIEWED in addition to its label. Labels per
VERIFICATION_POLICY.md. Novelty: the Toda hierarchy for exponential tilts is KNOWN (§9); the statements about the lattice layers are
UNCHECKED (Rule L not done). No claim about RH: the "zeta times" t_j = −2ζ(−jp)/j are the band-factor constants of the formal model
(E3 Lemma F.1′), and the proof below never uses their values — the tilts make all times free parameters. Branch plan-e2-d2; nothing
committed. Scope: JZC_M4 §8 Theorem T (a sketch, PROVED-mod-cite, NOT REVIEWED until now) and its Hurwitz version (T_H), which JZC_SHIFT
(Thm SH, Lemmas D, R, H, Prop DR, Cor SH.3) and Paper IV use.

Inputs, with their labels: JZC_M4_proof **Theorem N.6** and Lemmas N.6a–d (PROVED-mod-cite + REVIEWED); E3 **Lemma E3.4** (PROVED,
REVIEWED), Lemma F.1′ and E_plt1 Lemma F.1 (PROVED-mod-cite, REVIEWED); JZC_M3a_H **Theorem H (i)** (PROVED-mod-cite; every memo-level
link REVIEWED); Paper 2 (papers/paper2, read for this note: sec_front.tex Definition A, sec_2.tex T1 (eq:Y-extract), sec_5.tex Lemmas
interp, bandweight, weightdomain, (O1)–(O5), (eq:W0), sec_6.tex Proposition frame F1–F8, sec_7.tex introduction); E_pgt1 §0, §6, §7.1
(REVIEWED); RH_px §4 (REVIEWED). External theorems: **none** — the Toda hierarchy (Lemma T.1), the Baire step and the polynomial and
power-series facts of Lemma T.2 are proved here in full (Rule C: nothing to quote).

Checks (`checks/`, Python = the session venv, `-B`; caches in `tmp/toda/`; every `.out` prints the sha256 of its scripts):
- `toda_measures.py` → `toda_measures.out`: Lemma T.1 exactly (rational arithmetic) on finite truncations of σ_{2,3}, σ_{3,2}, the
  Hurwitz lattice σ^{−1/2} (p = 2, s = 3) and a random rational measure; times x^j (j = 1, 2, 3) and multi-times (1, 2), (1, 2, 3).
- `toda_engine.py`: a copy of `w2_engine.py` (not modified) with one addition: the second moment R_2 and the α_n-extraction (Lemma T.B).
- `toda_layers.py` → `toda_layers.out`: Theorem T (ii) (the formal Toda hierarchy, with ∂_μ = −n^{jp}∂_u) on the exact engine layers,
  identically in (p, α) on the lattice line and in (p, α, β) for the decoupled model; controls that must fail.

| # | Statement | Label |
|---|---|---|
| **Lemma T.1** | Toda hierarchy for exponential tilts of a compactly supported positive measure: ∂_{t_j}π_n = −Σ_{m<n}(L^j)_{nm}π_m, ∂_{t_j}log h_n = (J^j)_{nn}, ∂_{t_j}b_n = ½b_n[(J^j)_{nn} − (J^j)_{n−1,n−1}], ∂_{t_j}a_n = F_j(n) − F_j(n−1), F_j(n) = b_{n+1}(J^j)_{n+1,n}; also for finite measures with b_M := 0 | **PROVED** (elementary, self-contained, §2) + exact check `toda_measures` (736 identities, 864 controls fail); KNOWN (§9) |
| **Lemma T.A** | for every fixed tilt τ ∈ ℝ^J, Theorem N.6 (i) holds for σ_τ := e^{Στ_jx^j}σ_{p,s} with the **same layers** and μ_n replaced by μ_n − τn^{−p·}; likewise Theorem H (i) for σ^δ_τ | **PROVED-mod-cite by transfer** (Paper 2 F1–F8 apply to σ_τ directly, since σ_τ = σ_{p,s,ℓ₁} with ℓ₁ ∈ (A_ϑ) for every ϑ; the REVIEWED ℓ₁ ≡ 1 chain behind N.6 / H (i) with H_n ↦ H_nr_n, r_n entire; §3.1; for σ^δ_τ the frame itself is a bounded-factor transfer of the Hurwitz chain). **The one analytic step of Theorem T; Rule R target** |
| **Lemma T.B** | the α_n-layers: R_2 = ΣR_2^{(m)}(μ_n)n^{−m} + O(η_n) with R_2^{(m)} = Σ_eRes_e(zF_m), and n^pα_n/(2c) = Σ_{\|β\|≤B}μ_n^β𝔄_{β,K}(n) + O(n^{−K−1} + n^{−1−(B+1)p} + n^{−1−(J+1)p}), 𝔄_{0} = 1 + O(1/n) | **PROVED-mod-cite** (as Prop N.6c, + Paper 2 F8, E_pgt1 §7.1; §3.2); exact engine `toda_engine` (cross-checked against m4_rh4, NUMERICAL) |
| **Lemma T.2** | from exact flows with pointwise (non-uniform) polynomial expansions to formal identities: Baire ball, integrated identity, coefficient extraction | **PROVED** (elementary, §4.1) |
| **Theorem T** | (i) = Lemma T.A + T.B; (ii) **formal Toda hierarchy** in the ring ℛ of series Σu^γn^{−p\|γ\|_w}F_γ(1/n): ∂_{u_j}b̂ = ½c^jn^{−jp}b̂[(𝒥^j)_{00} − (𝒥^j)_{−1,−1}], ∂_{u_j}(2â) = c^jn^{−jp}[𝒷_1(𝒥^j)_{10} − 𝒷_0(𝒥^j)_{0,−1}]; (iii) ∂_{μ_j} = −n^{jp}∂_{u_j}, hence JZC_M4's (T1)–(T3) and every layer identity at μ = 0; (iv) the layers are determined by the integer layers (B, A) | **PROVED-mod-cite** (Lemma T.A [transfer, NOT REVIEWED], Lemma T.B, Theorem N.6 [REVIEWED], Lemmas T.1, T.2); p > 0, p ≠ 1, s ∈ (1, 1 + 2p) (\|α\| < 1), every finite set of integer exponents |
| **Theorem T_H** | the same for the Hurwitz lattices σ^δ (−1 < δ ≤ 0; δ < 0 if p < 1) with the layers of M(α + 2δ, α) | **PROVED-mod-cite** (as Theorem T, with Theorem H (i) [PROVED-mod-cite, links REVIEWED] in place of N.6 (i)) |
| **Cor T.3** | (ii)–(iv) hold for the layers of M(β, ν) identically in (p, β, ν) (rational identities) — JZC_SHIFT's hypothesis (T_H) in the form Cor SH.3 uses | **PROVED-mod-cite** (Theorem T_H + rationality, §5.2) |
| Prop T.4 | the diagonal integer layer: 𝔄_0 = 1 − p(β+2)/(2n) + …; in M := n + β/2 + 1 it has no M⁻¹, M⁻³ term and M⁻² coefficient **a₂ = −(p+1)/24 + (p+1)(p+2)ν²/8**, β-free to M⁻⁴ | exact computer algebra for the model (Lemma T.B's engine), identically in (p, ν, β), to order 4 (`toda_layers`); as a coefficient of α_n: PROVED-mod-cite for the lattice (Lemma T.B) |
| Checks | `toda_measures.out` (736 identities, 864 controls fail), `toda_layers.out` (75 identities, 91 controls fail) (§7) | exact computer algebra; X2 NUMERICAL |

## 0. Answer

**Theorem T is proved (PROVED-mod-cite, NOT REVIEWED), with one analytic transfer (Lemma T.A) as the only step not already reviewed.**
The proof has three parts.
1. *Exact Toda at fixed n* (Lemma T.1, elementary). For every compactly supported positive measure and every real tilt
   e^{Σt_jx^j}, differentiating the orthogonality relations gives the Toda hierarchy for (a_n, b_n) at every n. No citation is needed.
2. *The tilted lattice has the same layers* (Lemma T.A, + Lemma T.B for α_n). The tilted lattice σ_τ = e^{Στ_jx^j}σ_{p,s} is Paper 2's
   σ_{p,s,ℓ₁} with ℓ₁(k) = exp(Στ_jk^{−jp}), which satisfies Paper 2's hypothesis (A_ϑ) for every ϑ. In the Q-frame its band weight is
   the lattice's times r_n(z) = exp(Στ_jn^{−jp}(z^j − 1)), an entire polynomial tilt: by E3 Lemma E3.4 it shifts the band-factor
   parameters μ_n ↦ μ_n − τn^{−p·} **exactly** and changes nothing else. So the double expansion of Theorem N.6 (i) holds for σ_τ with
   the same layers 𝔇_β, evaluated at the shifted μ. In unscaled variables the total time is u = t + τ, t_j = −2ζ(−jp)/j, and u ranges
   over all of ℝ^J: the times are free.
3. *From exact flows to formal identities* (Lemma T.2). The exact Toda equation (part 1) relates exact numbers; the expansions (part 2)
   hold pointwise in τ, with constants depending on τ. A Baire-category argument gives an open ball of times on which the expansions
   hold uniformly; on it the **integrated** Toda identity, with all terms replaced by their expansions, is a family of polynomial
   identities in (u, h) up to O(n^{−L}); polynomial norm equivalence and the analyticity in 1/n of each coefficient turn it into an
   identity of formal series; differentiating that formal identity in h at h = 0 gives Theorem T (ii). **No asymptotic expansion is
   differentiated term by term**, and no uniformity of the Riemann–Hilbert analysis in the tilt is needed.

The relation ∂_{μ_j} = −n^{jp}∂_{u_j} is not an analytic statement: it is the chain rule for the substitution μ_j = −u_jn^{−jp} in a
ring of formal series (§1.2). Its content is that the shift n ↦ n + i acts at **fixed unscaled time u**, i.e. μ_j(n + i) =
μ_j(n)(1 + i/n)^{−jp}. Treating μ as n-independent gives the right first-order layers but the wrong second-order ones; that is the
"scaled-time" control of `toda_layers`.

**T_H.** The Hurwitz lattices σ^δ are tilted the same way, and Theorem H (i) replaces Theorem N.6 (i). This gives the formal Toda
hierarchy for the layers of M(α + 2δ, α). That family is open in the (β, ν)-plane and the identities are rational, so they hold for
M(β, ν) identically (Cor T.3). This discharges JZC_SHIFT's hypothesis (T_H) at the label PROVED-mod-cite, NOT REVIEWED.

**Exact checks.** Lemma T.1 holds exactly on finite truncations of the actual measures: 736 identities, and all 864 controls fail
(§7.1). The formal hierarchy holds on the exact engine's layers identically in (p, α) (lattice line), and in (p, α, β) (decoupled model).
It covers first and second order in the times, j ∈ {1, 2, 3}, both the b_n-equation and the α_n-equation, and α_n's layers come from a
new exact extraction (Lemma T.B) that is independent of the b-layers. Every control fails (§7.2).

## 1. Statement

### 1.1 Setting

- p > 0, p ≠ 1; s ∈ (1, 1 + 2p), so α := (s − 1)/p − 1 ∈ (−1, 1) (Paper 2's standing assumption, papers/paper2 sec_5.tex §"Standing
  assumptions"; other s by rationality, §5.2); c = c(p). Recurrence and Jacobi matrix as Paper 2 (sec_2.tex): xP_n = P_{n+1} + a_nP_n
  + b_n²P_{n−1}, b_n > 0, b_n² = h_n/h_{n−1}; orthonormal J with J_{nn} = a_n, J_{n,n−1} = J_{n−1,n} = b_n. We write α_n := a_n as in
  JZC_M4 (α without index is the exponent).
- σ := σ_{p,s} = Σ_{k≥1}k^{−s}δ_{k^{−p}}; σ^δ := Σ_{k≥1}(k + δ)^{−s}δ_{(k+δ)^{−p}} (JZC_M3a_H §1), −1 < δ ≤ 0.
- Tilts: J ∈ ℕ, τ ∈ ℝ^J, P_τ(x) := Σ_{j≤J}τ_jx^j, σ_τ := e^{P_τ}σ, σ^δ_τ := e^{P_τ}σ^δ.
- Band-factor parameters (Theorem N.6, E3 Lemma F.1′, E_plt1 Lemma F.1): μ_{n,j} = 2ζ(−jp)/(jn^{jp}) =: −t_jn^{−jp}, t_j := −2ζ(−jp)/j;
  Hurwitz: μ^δ_{n,j} = −t^δ_jn^{−jp} with t^δ_j := −2ζ(−jp, 1 + δ)/j (or the Fourier-sum form, JZC_M3a_H §3.2). For the tilt:
  **μ^τ_{n,j} := μ_{n,j} − τ_jn^{−jp} = −(t_j + τ_j)n^{−jp}** (τ_j := 0 for j > J).
- Layers. 𝔇_K(n; μ) is JZC_M4_proof §1's polynomial in 1/n (entire in μ ∈ ℂ^{J′}, n-free coefficients); 𝔇_{β,K} its μ-Taylor
  coefficients. Since R_1^{(m)}(μ) does not depend on K, the coefficient of n^{−k} in 𝔇_{β,K} does not depend on K ≥ k, and **𝔇_β(n) :=
  Σ_kd_{k,β}n^{−k}** is a well-defined formal series (𝔇_{β,K} is its truncation). It does not depend on J′ ≥ max supp β (the gauge with
  μ_j = 0 is the gauge without the j-th parameter). 𝔄_β is defined the same way from the α-extraction (Lemma T.B). For M(β′, ν):
  𝔇_β(n; β′, ν), 𝔄_β(n; β′, ν) (JZC_M3a_H §3.3; the engine with DECOUPLE). 𝔇_0 = B (integer layer), 𝔄_0 = A.

### 1.2 The formal ring, the shift, and ∂_μ = −n^{jp}∂_u

Let ℛ_J be the set of formal series F = Σ_{γ∈ℕ^J}u^γn^{−p|γ|_w}F_γ(1/n), F_γ ∈ ℂ[[1/n]], |γ|_w := Σ_jjγ_j, with the product induced
by n^{−pa}n^{−pb} = n^{−p(a+b)}. The map x := 1/n, s_j := u_jn^{−jp} identifies ℛ_J with ℂ[[x, s_1, …, s_J]] as rings, so ℛ_J is a
ring and the symbols n^{−pw} need no meaning beyond this. On ℛ_J:
- **Shift** (i ∈ ℤ): S_i(u^γn^{−pw}F(1/n)) := u^γn^{−pw}(1 + i/n)^{−pw}F(1/(n + i)), re-expanded in 1/n (binomial series; x/(1 + ix) ∈
  xℂ[[x]]). S_i is a ring endomorphism, and **it does not act on u** (the unscaled times are n-free). In the s-coordinates,
  S_i: x ↦ x/(1 + ix), s_j ↦ s_j(1 + ix)^{−jp}.
- **Derivations** ∂_{u_j}; in s-coordinates, ∂_{u_j} = n^{−jp}∂_{s_j}, i.e. u^γ ↦ γ_ju^{γ−e_j} with the weight n^{−pjγ_j} kept.
- **The substitution.** Θ: ℂ[[1/n]][[μ]] → ℛ_J, Θ(Σ_βμ^β𝔉_β(n)) := Σ_β(−u)^βn^{−p|β|_w}𝔉_β(n), i.e. μ_j = −u_jn^{−jp}. On monomials
  ∂_{u_j}Θ(μ^β𝔉) = −β_j(−u)^{β−e_j}n^{−p|β|_w}𝔉 = −n^{−jp}Θ(∂_{μ_j}(μ^β𝔉)). Hence

  **∂_{u_j}∘Θ = −n^{−jp}·Θ∘∂_{μ_j},  i.e. ∂_{μ_j} = −n^{jp}∂_{u_j},**  and Θ(𝔉)|_{u=0} = 𝔉|_{μ=0}.   (1.1)

  This is JZC_M4 §8's "∂_{μ_j} = −n^{jp}∂_{t_j} (z^j = n^{jp}x^j)", made exact: it is the chain rule for an algebraic substitution, and it
  needs no analytic input. The analytic content of Theorem T is (ii) below, which says which element of ℛ_J the lattice produces.

Define **b̂ := Θ(𝔇(n; μ)) = Σ_β(−u)^βn^{−p|β|_w}𝔇_β(n)** and **â := Θ(Σ_βμ^β𝔄_β(n))** (the formal n^pb_n/c and n^pα_n/(2c) at
total time u), the scaled shifted entries **𝒷_i := (1 + i/n)^{−p}S_ib̂, 𝒶_i := 2(1 + i/n)^{−p}S_iâ** ("n^pb_{n+i}/c", "n^pα_{n+i}/c"),
and the tridiagonal matrix 𝒥 indexed by i ∈ ℤ with 𝒥_{ii} = 𝒶_i, 𝒥_{i,i−1} = 𝒥_{i−1,i} = 𝒷_i. (𝒥^j)_{rs} is a finite sum of products of
entries with indices in [min(r, s) − j, max(r, s) + j].

### 1.3 Theorem T

**Theorem T (PROVED-mod-cite; NOT REVIEWED).** Let p > 0, p ≠ 1, s ∈ (1, 1 + 2p), J ∈ ℕ.

(i) *Tilted expansions.* For every τ ∈ ℝ^J, all K, B ∈ ℕ and J′ ≥ J, as n → ∞ (constants depending on τ, K, B, J′):

  n^pb_n(σ_τ)/c = Σ_{|β|≤B}(μ^τ_n)^β𝔇_{β,K}(n) + O(n^{−K−1} + n^{−2−(B+1)p} + n^{−1−(J′+1)p}),
  n^pα_n(σ_τ)/(2c) = Σ_{|β|≤B}(μ^τ_n)^β𝔄_{β,K}(n) + O(n^{−K−1} + n^{−1−(B+1)p} + n^{−1−(J′+1)p}),

  β ∈ ℕ^{J′}. At τ = 0 the first line is Theorem N.6 (i).

(ii) *Formal Toda hierarchy.* In ℛ_J, for j = 1, …, J:

  **∂_{u_j}b̂ = ½c^jn^{−jp}·b̂·[(𝒥^j)_{00} − (𝒥^j)_{−1,−1}]**,   (T-b)
  **∂_{u_j}(2â) = c^jn^{−jp}·[𝒷_1(𝒥^j)_{10} − 𝒷_0(𝒥^j)_{0,−1}]**.   (T-a)

  Equivalently, in s-coordinates (ℂ[[x, s]], s_j = −μ_j): ∂_{s_j}b̂ = ½c^jb̂[(𝒥^j)_{00} − (𝒥^j)_{−1,−1}], and likewise for (T-a).

(iii) *μ-form.* By (1.1), ∂_{μ_j}b̂ = −½c^jb̂[(𝒥^j)_{00} − (𝒥^j)_{−1,−1}], and the μ^β-coefficient of every iterate is an identity
  between the layers at μ = 0. Instances (JZC_M4 §8; n^pb_n abbreviates the formal b̂, scaled entries as above, "n^p(α_n − α_{n−1})"
  = c(𝒶_0 − 𝒶_{−1})):
  - (T1) 𝔇_{e₁} = −½c(𝒶_0 − 𝒶_{−1})B, i.e. ∂_{μ₁}(n^pb_n) = −½n^p(α_n − α_{n−1})·n^pb_n at μ = 0;
  - (T2) 2𝔇_{2e₁} = ∂²_{μ₁}b̂|₀ = n^{2p}∂²_{u₁}b̂|₀, with ∂²_{u₁}log b_n² = b²_{n+1} − 2b_n² + b²_{n−1} (Toda lattice);
  - (T3) 𝔇_{e₂} = −½c²[(𝒥²)_{00} − (𝒥²)_{−1,−1}]B, (𝒥²)_{00} = 𝒶_0² + 𝒷_0² + 𝒷_1².

(iv) *Determination.* Given (𝔇_0, 𝔄_0) = (B, A), the system (T-b), (T-a) determines every 𝔇_β, 𝔄_β. (The u^{γ+e_j}-coefficient of the
  left side is (γ_j + 1) times the new layer; the right side's u^γ-coefficient involves only layers of order ≤ |γ|, since S_i preserves
  the u-degree.) So **the layers are the Toda flow of the two integer layers**, and the lattice expansion is that flow evaluated at the
  total time u = t = (−2ζ(−jp)/j)_j, in the sense of Theorem N.6 (i) with u = t (Θ⁻¹ at u = t is Σ_βμ_n^β𝔇_β).

**Theorem T_H (PROVED-mod-cite; NOT REVIEWED).** Let p ≠ 1, s ∈ (1, 1 + 2p), −1 < δ ≤ 0 (δ < 0 if p < 1; δ = 0 is Theorem T). Then
(i)–(iv) hold for σ^δ_τ, with the layers 𝔇_β(n; α + 2δ, α), 𝔄_β(n; α + 2δ, α) of M(α + 2δ, α), and with μ^δ_n − τn^{−p·} in (i).

**Corollary T.3 (PROVED-mod-cite; NOT REVIEWED).** For every finite set of integer exponents, every coefficient identity contained in
(T-b), (T-a) for the layers of M(β, ν) holds identically in (p, β, ν), as an identity of rational functions. In particular JZC_SHIFT
§2.1 (b) holds on β′ ≠ ν, which is its hypothesis (T_H) (Cor SH.3).

*What kind of statement each part is.* Lemma T.1 is an **exact identity at fixed n** for the family of measures e^{Σt_kx^k}w (the
classical Toda flow of orthogonal polynomials). Theorem T (ii) is an **identity of formal series** (the coefficients of the asymptotic
expansions). Lemma T.2 is the bridge between them. Theorem T (i) is a statement about the actual tilted measures.

## 2. Lemma T.1: the Toda hierarchy for exponential tilts (PROVED; self-contained)

**Lemma T.1.** Let μ be a positive Borel measure on ℝ with compact support, either with infinitely many support points (set M := ∞)
or with exactly M support points. For t ∈ ℝ^J let μ_t := e^{P_t(x)}μ, P_t(x) := Σ_jt_jx^j. Let π_n(·; t) (0 ≤ n < M) be the monic
orthogonal polynomials of μ_t, h_n := ∫π_n²dμ_t, a_n, b_n as in §1.1, p_n := π_n/√h_n, J the orthonormal Jacobi matrix (M × M if M is
finite), and L the monic Jacobi matrix L_{nn} = a_n, L_{n,n+1} = 1, L_{n+1,n} = b²_{n+1}. Then a_n, b_n, h_n and the
coefficients of π_n are real-analytic in t, and for every j and 0 ≤ n < M:
1. ∂_{t_j}π_n = −Σ_{m<n}(∫x^jπ_nπ_mdμ_t/h_m)·π_m = −Σ_{m<n}(L^j)_{nm}π_m;
2. ∂_{t_j}log h_n = (J^j)_{nn};
3. ∂_{t_j}b_n = ½b_n[(J^j)_{nn} − (J^j)_{n−1,n−1}] (n ≥ 1);
4. ∂_{t_j}a_n = F_j(n) − F_j(n − 1), F_j(n) := b_{n+1}(J^j)_{n+1,n}, with F_j(−1) := 0 and, if M < ∞, F_j(M − 1) := 0 (b_M := 0).
In terms of L: (J^j)_{nn} = (L^j)_{nn}, F_j(n) = (L^j)_{n+1,n}.

*Proof.*
- *Regularity.* The moments m_k(t) = ∫x^ke^{P_t}dμ are entire in t: the integrand and all its t-derivatives are bounded on
  supp μ × (compact sets of t), so differentiation under the integral sign is allowed. The Hankel determinants D_n(t) are positive for
  n ≤ M (n < M + 1 support points). The coefficients of π_n are ratios of polynomials in the moments with denominator D_n (Cramer's rule
  for the orthogonality conditions ∫π_nx^idμ_t = 0, i < n), and h_n = D_{n+1}/D_n. So everything is real-analytic in t, and every
  ∫f(x)g(x)dμ_t with polynomials f, g depending smoothly on t may be differentiated under the integral, the derivative of the weight
  being x^je^{P_t}.
- *Multiplication by x.* xp_n = b_{n+1}p_{n+1} + a_np_n + b_np_{n−1} (the recurrence divided by √h_n, using b_{n+1} = √(h_{n+1}/h_n)).
  So the span of p_0, …, p_{N} is mapped into the span of p_0, …, p_{N+1} with matrix J, and by induction x^jp_n = Σ_m(J^j)_{mn}p_m (a
  finite sum). Since the p_m are orthonormal, ∫x^jp_np_mdμ_t = (J^j)_{mn} = (J^j)_{nm} (J symmetric). If M < ∞, L²(μ_t) has dimension M,
  p_0, …, p_{M−1} is a basis, and multiplication by x is exactly the M × M matrix J (the vector b_Mp_M is 0 in L²(μ_t)); the formula
  holds for all n, m < M.
- *1.* ∂π_n has degree < n (π_n is monic). For m < n differentiate ∫π_nπ_mdμ_t = 0:
  ∫∂π_n·π_m + ∫π_n·∂π_m + ∫x^jπ_nπ_m = 0. The middle term vanishes (deg ∂π_m < m < n). Expanding ∂π_n in the orthogonal basis
  π_0, …, π_{n−1} gives the first formula. Then ∫x^jπ_nπ_mdμ_t/h_m = √(h_n/h_m)(J^j)_{nm}. With D := diag(√h_n), J = D^{−1}LD
  (check: (D^{−1}LD)_{n+1,n} = b²_{n+1}√(h_n/h_{n+1}) = b_{n+1}, (D^{−1}LD)_{n,n+1} = √(h_{n+1}/h_n) = b_{n+1}), so
  (J^j)_{nm} = √(h_m/h_n)(L^j)_{nm}, which gives the second formula.
- *2.* ∂h_n = 2∫π_n∂π_n + ∫x^jπ_n²; the first term is 0 by orthogonality (deg ∂π_n < n), and ∫x^jπ_n² = h_n(J^j)_{nn}.
- *3.* From b_n² = h_n/h_{n−1}: ∂log b_n² = (J^j)_{nn} − (J^j)_{n−1,n−1}.
- *4.* Write π_n = x^n + c_nx^{n−1} + …, c_0 = 0. Comparing the x^n coefficients in xπ_n = π_{n+1} + a_nπ_n + b_n²π_{n−1} gives
  a_n = c_n − c_{n+1}. By 1, the x^{n−1} coefficient of ∂π_n comes only from m = n − 1: ∂c_n = −√(h_n/h_{n−1})(J^j)_{n,n−1} =
  −b_n(J^j)_{n,n−1} = −F_j(n − 1). Hence ∂a_n = F_j(n) − F_j(n − 1). For M < ∞ and n = M − 1: the monic polynomial
  π_M := xπ_{M−1} − a_{M−1}π_{M−1} − b²_{M−1}π_{M−2} is orthogonal to π_0, …, π_{M−1}, which span L²(μ_t), so it vanishes at every
  support point; it is Π(x − x_k), which does not depend on t. So ∂c_M = 0, which is the convention F_j(M − 1) = 0.
- *L-form.* (J^j)_{nn} = (L^j)_{nn} by similarity; F_j(n) = b_{n+1}√(h_n/h_{n+1})(L^j)_{n+1,n} = (L^j)_{n+1,n}. ∎

*Remarks.* (a) j = 1: ∂log b_n² = a_n − a_{n−1}, ∂a_n = b²_{n+1} − b_n² (the Toda lattice). This is the convention of JZC_SHIFT §2.1 (a)
and JZC_M4 §8. In matrix form, 1 reads ∂p = −((J^j)_− + ½(J^j)_0)p, where (·)_− is the strictly lower triangle and (·)_0 the diagonal.
(b) The proof uses only compact support (for the moments and the differentiation) and positivity. Each partial derivative is taken
at an arbitrary base point t, since μ_{t+he_j} = e^{hx^j}μ_t, so the multi-time version is automatic.

*Hypotheses in the applications.* σ_{p,s} and σ^δ are positive, have infinitely many atoms, and are supported in [0, 1] resp.
[0, (1 + δ)^{−p}] (δ > −1). Their total masses ζ(s), ζ(s, 1 + δ) are finite (s > 1). The tilt e^{P_τ} is continuous and positive on the
support, so σ_τ, σ^δ_τ are again such measures. Every moment is finite and entire in τ. The formal model M(β, ν) is not a measure, and
Lemma T.1 is never applied to it: its Toda identities are Theorem T (ii) / Cor T.3, obtained from the measures.

*Exact check* (`toda_measures.out`). 1–4 (in the L-form) hold as power series in τ, for every n = 0, …, M − 1 (including the boundary
convention at n = M − 1), on the M = 6 atom truncations of σ_{2,3}, σ_{3,2}, σ^{−1/2} (p = 2, s = 3) and a random rational measure, for
the times x, x², x³ (τ-degree ≤ 4, 4, 3) and (x, x²), (x, x², x³) jointly: 736 identities. Every control fails (864): the opposite
sign in 4; L^{j+1} in 2; (L^j)_{n+1,n+1} in 3; the transposed entry (L^j)_{n,n+1} in 4; the opposite sign in 1.

## 3. The tilted lattice (Lemma T.A) and the α-layers (Lemma T.B)

### 3.1 Lemma T.A (PROVED-mod-cite by transfer; NOT REVIEWED)

**Lemma T.A.** Let p > 0, p ≠ 1, s ∈ (1, 1 + 2p), J ∈ ℕ and τ ∈ ℝ^J be fixed. Then the conclusions of JZC_M4_proof Lemma N.6a, Lemma
N.6b, Prop N.6c and Theorem N.6 (i) hold for σ_τ, with μ_n replaced by μ^τ_n and the **same** functions Δ_k^μ, R^{(m)}(μ), 𝔇_K(n; μ)
(constants depending on τ). The same holds for σ^δ_τ (−1 < δ ≤ 0; δ < 0 if p < 1), with Theorem H (i) and μ^δ_n − τn^{−p·}.

*The mechanism.* σ_τ = Σ_kk^{−s}ℓ₁^τ(k)δ_{k^{−p}} with **ℓ₁^τ(t) := exp(Σ_jτ_jt^{−jp}) = e^{Λ_τ(log t)}, Λ_τ(ξ) := Σ_jτ_je^{−jpξ}**.
- **(A_ϑ) holds for every ϑ > 0** (Paper 2 Definition A, sec_front.tex: "Λ is analytic on S_ϑ, real on S_ϑ ∩ ℝ, bounded on
  S_ϑ ∩ {Re ξ ≤ 0}, and ε_Λ(T) := sup{|Λ′(ξ)|: ξ ∈ S_ϑ, Re ξ ≥ T} → 0", S_ϑ = {Re ξ ≥ −c₀, |Im ξ| ≤ ϑ}). Λ_τ is entire and real on ℝ;
  on S_ϑ ∩ {Re ξ ≤ 0}, |Λ_τ| ≤ Σ_j|τ_j|e^{jpc₀}; and ε_{Λ_τ}(T) ≤ pΣ_jj|τ_j|e^{−jpT} → 0.
- So Paper 2's standing assumptions hold for σ_τ (sec_5.tex §"Standing assumptions": p > 0, 1 < s < 1 + 2p, ℓ₁ with (A_ϑ)), and **Paper 2
  Proposition frame (F1)–(F8)** (sec_6.tex) applies to σ_τ. By (F2) and Lemma bandweight its band weight is
  W₀^τ = 𝗐_n^τz^α(4c − z)H_n(z)r_n(z), with **r_n(z) = ℓ₁^τ(nz^{−1/p})/ℓ₁^τ(n) = exp(Σ_jτ_jn^{−jp}(z^j − 1))** (t(z)^{−jp} = n^{−jp}z^j).
  H_n is the same function as for σ: the outer scalar F (Lemma outer, (O1)–(O5)) is built from θ = πnz^{−1/p} alone, and the weight is
  not used in it. So
  **r_n = e^{−Σ_jτ_jn^{−jp}}·q_{μ′_n}, q_μ := e^{−Σμ_kz^k}, μ′_{n,j} := −τ_jn^{−jp}**,
  an entire, zero-free polynomial tilt, real and positive on (0, ∞).
- The REVIEWED chain behind Theorem N.6 (i) (E_pgt1, E2, E3, E_plt1, RH_px, RH_plt1b, JZC_M4_proof) is "the frame of Paper 2
  specialised to ℓ₁ ≡ 1" (E_pgt1 §0, E_plt1 §0). In it the weight enters only through W₀ = 𝗐_nz^α(4c − z)H_n (r_n ≡ 1). The transfer
  is therefore **H_n ↦ H_n^τ := H_n·r_n**, row by row:

| input (REVIEWED chain) | how the weight enters | why it holds for σ_τ |
|---|---|---|
| Frame: Paper 2 Prop frame F1–F8 (contour, jumps, Cauchy bound, F4 super-small lip entries, F5 arcs away from the edges, F6 hard-edge map, F7 a-priori bound, F8 extraction) | for general ℓ₁ with (A_ϑ) | **direct**: Paper 2's own hypothesis, verified above. No transfer is needed. |
| Szegő data: ω = D_W²/W₀, ρ, (−ω)^{1/2} (Paper 2 (eq. omega), multiplicativity D_{q₁q₂} = D_{q₁}D_{q₂}) | E_pgt1 Lemma E.3 "n-dependence"; E3 Lemma E3.4 (i) | E3.4 (i) (PROVED, for every real μ): ω^τ = ω·e^{𝓡M_{μ′_n}}, (ρ^τ)² = ρ²e^{−𝓡M_{μ′_n}}, (−ω^τ)^{1/2} = (−ω)^{1/2}e^{𝓡M_{μ′_n}/2}; the constant e^{−Στ_jn^{−jp}} cancels in ω (F2). Exact algebra. |
| Band-factor law: E3 Lemma F.1′ (p > 1), E_plt1 Lemma F.1 (p < 1); Hurwitz Hc.2/Hc.3 (p > 1), Hc.5 (p < 1) | log H_n(z) − log H_n(1) = −Σ_{k≤K}μ_{n,k}(z^k − 1) + O(n^{−(K+1)p}) with derivative bounds, on \|z\| ≤ R₁ (boundary values on (−R₁, 0)) | log H_n^τ(z) − log H_n^τ(1) = −Σ_{k≤K}(μ_{n,k} + μ′_{n,k})(z^k − 1) + O(n^{−(K+1)p}) for K ≥ J, with the **same** remainder: the tilt part is exact and has no jump. |
| Circle jumps, Lemma N.6a / E3 Lemma E3.5 (and E2 Lemma E2.3, E_plt1 Lemma E′.3) | the DLMF sector expansions (weight-free); then "the band weight is 𝗐′z^α(4c − z)q_{μ_n}e^{−2E}; Δ_k depends analytically on (ρ²)^{±1}, (−ω)^{±1/2}, which are bounded above and below" | band weight 𝗐″z^α(4c − z)q_{μ_n+μ′_n}e^{−2E}; the bounds of Paper 2 Lemma szego (vi) hold for ℓ₁^τ (F-frame), and on the circles \|𝓡M_{μ′_n}\| ≤ C\|τ\|n^{−p}. So Δ_k = G_{μ^τ_n}Δ_k^{mod}G_{μ^τ_n}^{−1} + O(n^{−(J′+1)p}) with μ^τ_n = μ_n + μ′_n. |
| Meromorphy, Lemma N.6b | through the gauge E3.4 (iii), entire in μ ∈ ℂ^{J′} | unchanged: Δ_k^μ is the same function of μ; only the value μ^τ_n changes. |
| Hard-edge parametrix: RH_px §4.1 (p > 1; KMVV construction with W̃ = (C_N(−z)^α(4c − z)h_N)^{1/2}); RH_plt1b (p < 1, glued); Hurwitz G1u, G1u_plt1 L P3 | W̃ must be analytic in U(0, δ) apart from the super-small (h2) jump on (−δ, 0), inherited from h_N | W̃^τ = W̃·r_n^{1/2} with r_n^{1/2} := exp(½Σ_jτ_jn^{−jp}(z^j − 1)), **entire**: same jumps, and every bound changes by a factor ≤ sup_{U(0,δ)}\|r_n^{±1/2}\| ≤ e^{Σ\|τ_j\|}. Paper 2 needs its Conway–Deift comparison (sec_7.tex) only because a general r_n "is neither analytic at 0 nor of Fisher–Hartwig type"; a polynomial tilt is analytic at 0, so the direct construction of the ℓ₁ ≡ 1 chain applies. |
| Hard-edge mismatch (RH_px Lemma 4.3: \|J_H − I\| ≤ C_KN^{−K}min(1, \|z\|^K)) | super-small (h1), (h2) entries times the amplification by P₀ | (h1), (h2) unchanged up to the factor above; amplification unchanged. |
| Off-circle jumps (RH_px Gate 3, §4.3 top end; E_pgt1 Prop E.5′; E_plt1 Prop E′.5′ lips, seams; Ha F5 moved arcs) | bounds \|W₀^{±1}\|, \|D_W^{±1}\| ≤ poly(n) times e^{−n/C} or n^{−pn/4}, on pieces with \|z\| ≤ e^{pc₀}n^p | on \|z\| ≤ e^{pc₀}n^p: \|log r_n\| ≤ Σ_j\|τ_j\|(e^{jpc₀} + 1) and \|𝓡M_{μ′_n}\| ≤ C\|τ\| (degree-j polynomial times n^{−jp}). The bounds change by a constant factor. (F4, F5 also hold for ℓ₁^τ directly.) |
| Small norm, residue recursion (Prop N.6c), extraction (Paper 2 F8; E_pgt1 §7.1), μ-Taylor bound (N.6 proof (i)) | none beyond the above | verbatim; \|μ^τ_n\| ≤ C(τ)n^{−p}, so the Taylor remainder is O(n^{−2−(B+1)p}) (E3.7 is a statement about the model layers, unchanged). |

  For the Hurwitz lattice the same table runs through the chain of Theorem H (i) (JZC_M3a_H §2, steps H-a – H-f):
  - H-a (interpolation) uses the weights only through the residue condition. The tilt multiplies the node masses by e^{P_τ(x_k)},
    i.e. the interpolating weight by the entire factor e^{P_τ(z/n^p)}.
  - H-b and the index transfer H-d are weight-free (outer scalar, gauge).
  - H-b′ (a-priori bound) is a fixed-n statement; its weight dependence is through factors bounded above and below.
  - H-c becomes H_n^δ ↦ H_n^δr_n as in row 3.
  - H-e is N.6a–c for M(β′, α); G1u's hard-edge data change as in row 6.

  Paper 2's frame for general ℓ₁ does not cover Hurwitz nodes. So for σ^δ_τ the first row is the Hurwitz chain's own frame (H-a, H-b,
  H-b′, G12, G3, G23plt1), with W₀ multiplied by r_n: the same bounded-factor argument as in the off-circle row.

*Label.* PROVED-mod-cite by transfer, with the citation base of Theorem N.6 (i) / Theorem H (i). The transfer table is an argument, at
the same granularity as JZC_SIGMA Lemma F (ii). **It is the one step of Theorem T that is neither elementary nor already REVIEWED, and is
the target for Rule R.** The p < 1 rows were checked against the statements as quoted in E_plt1 / JZC_M4_proof / JZC_M3a_H. The seam
outer scalar of RH_plt1b (§1 there) is weight-free, which was checked. The rest of RH_plt1b was not re-read line by line.

### 3.2 Lemma T.B: the α_n-layers (PROVED-mod-cite; NOT REVIEWED)

JZC_M4_proof states Theorem N.6 for b_n only. Theorem T needs α_n.

**Lemma T.B.** In the setting of Theorem N.6 (and, by Lemma T.A, of σ_τ, σ^δ, σ^δ_τ), let F_m(μ) be the residue-recursion integrands of
JZC_M4_proof §1 and R_2^{(m)}(μ) := Σ_{e∈{0,4c}}Res_{z=e}(zF_m(μ; z)). Then:
1. R_2 = Σ_{m≤K}R_2^{(m)}(μ_n)n^{−m} + O(n^{−K−1} + n^{−1−(J+1)p}), where R = I + R_1/z + R_2/z² + O(z^{−3}).
2. With Q_1 = P_1 + R_1, Q_2 = P_2 + R_1P_1 + R_2, P_1 = [[0, ic], [−ic, 0]], P_2 = [[c²/2, 2ic²], [−2ic², c²/2]] (E_pgt1 §0), let
   𝔄_K(n; μ) be ((Q_2)_{12}/(Q_1)_{12} − (Q_1)_{22})/(2c) with R_k replaced by Σ_{m≤K}R_k^{(m)}(μ)n^{−m}, expanded to order n^{−K}.
   Then n^pα_n/(2c) = 𝔄_K(n; μ_n) + O(n^{−K−1} + n^{−1−(J+1)p}).
3. 𝔄_K(n; μ) is entire in μ with n-free coefficients, and its n⁰ coefficient is 1 for all μ. Hence
   n^pα_n/(2c) = Σ_{|β|≤B}μ_n^β𝔄_{β,K}(n) + O(n^{−K−1} + n^{−1−(B+1)p} + n^{−1−(J+1)p}), with 𝔄_β = O(n^{−1}) for β ≠ 0.

*Proof.* 1. This is the "Moment" bullet of Prop N.6c with s^{k−1}, k = 2, exactly as E_pgt1 Prop E.5′ does at first order:
R_2 = −(1/2πi)∫_{Σ_R}R₋(J − I)s ds. Split as in N.6c.
- On the clockwise circles, −(1/2πi)∮F_m(s)s ds = Σ_eRes_e(sF_m), with |s| bounded there.
- On the far pieces, |s| ≤ Cn^p is absorbed by the super-small bounds e^{−n/C}, n^{−pn/4} (as in E.5′).
- Inside U_0 the hard-edge mismatch is used with |s| ≤ δ.
- The induction error O(n^{−m−1} + n^{−1−(J+1)p}) of N.6c is paired with s in L² on the circles and super-small pieces.

At a pole e, Res_e(sF) = e·Res_eF + [(s − e)^{−2}]F, which is the formula used in `toda_engine.py` (as in m4_rh4.py, which computes
the same quantity numerically).

2. Paper 2 (F8): 𝖺(Q) = (Q_2)_{12}/(Q_1)_{12} − (Q_1)_{22} = n^pa_n. Outside the discs Q = RP_0^∞, so Q_1 = R_1 + P_1 and Q_2 = R_2 + R_1P_1 + P_2.
(Q_1)_{12} = ic + O(1/n) ≠ 0, so 𝖺 is an analytic function of the entries of (R_1, R_2) near (0, 0). Insert 1 and N.6c.

3. R_1^{(m)}(μ), R_2^{(m)}(μ) are entire in μ (Lemma N.6b and the algebraic recursion). 𝔄_K is a rational function of them whose
denominator has the constant term ic. The n⁰ term is 𝖺(P_0^∞)/(2c) = 1 (E_pgt1 §0: "the a-functional of P₀^∞ is 2c"). Taylor's
theorem in μ on |μ| ≤ 1, coefficientwise, gives the remainder O(|μ|^{B+1}n^{−1}) = O(n^{−1−(B+1)p}). ∎

(No α-analogue of E3.7 (exact linearity of the n^{−1} coefficient in μ) is claimed: E3 §9 lists it as open. It is not needed, since the
weaker remainder n^{−1−(B+1)p} suffices: B is free.)

*Exact engine.* `toda_engine.py` adds 1–2 to w2_engine.py (in exact arithmetic over ℚ(p, α, β)[i]).
- Its b-part is string-identical to w2_engine's (`toda_layers` X1).
- Its α-layers agree with the independent numerical engine m4_rh4.run(…, want_a=True) to 3·10⁻³⁹ (μ = 0) and 7·10⁻²³ (first order,
  central difference) at (p, α) = (3/2, 3/10) (X2, NUMERICAL).
- It reproduces E_pgt1 Thm E.1, n^pα_n/(2c) = 1 − p(α + 2)/(2n) + …, identically.

## 4. Proof of Theorem T

### 4.1 Lemma T.2 (from pointwise expansions of an exact flow to formal identities; PROVED)

We write the argument for (T-b) along a time u_j; (T-a) is identical with Lemma T.1.4 in place of T.1.3.

*Step 0: total time.* Put u := τ + t^{(J)}, t^{(J)} := (t_1, …, t_J), and σ^{[u]} := σ_{u−t^{(J)}}. As τ runs over ℝ^J, so does u, and
μ^τ_{n,j} = −u_jn^{−jp} (j ≤ J), −t_jn^{−jp} (j > J). Fix a target order L > 0 and take J′ = J in Theorem T (i) (Lemma T.A + T.B),
with K + 1 ≥ L, 1 + (B + 1)p ≥ L and 1 + (J + 1)p ≥ L, so that every remainder in (i) is O(n^{−L}). (A large J only adds times. An
identity among layers supported in {1, …, J₀} is the restriction u_{J₀+1} = … = u_J = 0 of the identity in ℛ_J, and the layers do not
depend on J, §1.1.) Then for every u ∈ ℝ^J:

  b_m(σ^{[u]}) = β̃_m(u) + O_u(m^{−p−L}),  α_m(σ^{[u]}) = α̃_m(u) + O_u(m^{−p−L}),   (4.1)

where β̃_m(u) := c m^{−p}Σ_{|γ|≤B}(−u)^γm^{−p|γ|_w}𝔇_{γ,K}(m) and α̃_m(u) := 2c m^{−p}Σ_{|γ|≤B}(−u)^γm^{−p|γ|_w}𝔄_{γ,K}(m)
(supp γ ⊂ {1, …, J}). These are **polynomials in u** of degree ≤ B, and the band-factor parameters for j > J sit in the remainder. The
constants in O_u depend on u.

*Step 1: a ball of uniformity (Baire).* Let I := {−J − 1, …, J + 1} and, for integers n > J + 1,
Φ_n(u) := n^{p+L}max_{i∈I}(|b_{n+i}(σ^{[u]}) − β̃_{n+i}(u)| + |α_{n+i}(σ^{[u]}) − α̃_{n+i}(u)|).
- Each Φ_n is continuous in u: b_m, α_m are real-analytic in u (Lemma T.1, regularity), and β̃_m, α̃_m are polynomials.
- By (4.1), sup_nΦ_n(u) < ∞ for every u. Only finitely many n lie below the threshold n₀(u), and (n + i)^{−p−L} ≍ n^{−p−L}.
- The sets F_M := {u: Φ_n(u) ≤ M for all n} are closed (intersections of closed sets) and cover ℝ^J.
- *Baire (proved here for ℝ^J).* If every F_M had empty interior, choose closed balls B̄_1 ⊃ B̄_2 ⊃ … with radii → 0 and B̄_M ∩ F_M = ∅:
  given B̄_{M−1}, its interior is not contained in the closed set F_M, so it contains a point outside F_M, and a small closed ball
  around that point misses F_M. The centres converge (Cauchy) to a point lying in every B̄_M, hence in no F_M — a contradiction.
- So some F_M contains an open ball U: **on U the expansions (4.1) hold with one constant M, for all n > J + 1 and all i ∈ I.**

*Step 2: the integrated identity.* Fix a closed ball U′ ⊂ U and h₀ > 0 with U′ + [−h₀, h₀]e_j ⊂ U. By Lemma T.1.3, for u ∈ U′,
|h| ≤ h₀:

  b_n(σ^{[u+he_j]}) − b_n(σ^{[u]}) = ∫_0^h ½b_n[(J^j)_{nn} − (J^j)_{n−1,n−1}](σ^{[u+ηe_j]})dη.   (4.2)

The integrand is a fixed polynomial Ψ_j in the entries b_{n+i}, α_{n+i}, i ∈ I. Each entry is O(n^{−p}) on U, so Ψ_j = O(n^{−(j+1)p}).
Replacing each entry by its approximant changes Ψ_j by O(n^{−(j+1)p−L}), uniformly on U. Hence

  Π_n(u, h) := β̃_n(u + he_j) − β̃_n(u) − ∫_0^hΨ_j(β̃_{n+i}, α̃_{n+i})(u + ηe_j)dη = O(n^{−p−L})   uniformly on U′ × [−h₀, h₀].   (4.3)

*Step 3: coefficients.* For each n, Π_n is a polynomial in (u, h) ∈ ℝ^{J+1} of degree ≤ D (D depends on B, j only). On the space
𝒫_D of such polynomials, the coefficient functionals are fixed linear combinations of point values on a (D + 1)^{J+1}-point tensor grid
in U′ × [−h₀, h₀] (Lagrange interpolation in each variable). So **each coefficient of Π_n is O(n^{−p−L})**.

Now compute the coefficient of u^γh^m. In β̃_{n+i}(u) the coefficient of u^γ is c(−1)^{|γ|}n^{−p(1+|γ|_w)}·[(1 + i/n)^{−p(1+|γ|_w)}
𝔇_{γ,K}(n + i)], and the bracket is an analytic function of x = 1/n for |x| < 1/(J + 2). Products add weights, and ∫_0^h(u + ηe_j)^δdη
produces u^γh^m with δ = γ + (m − 1)e_j. So the u^γh^m-coefficient of Π_n equals n^{−p(1+|γ|_w+mj)}ψ_{γ,m}(1/n), with ψ_{γ,m} analytic at
0. If ψ is analytic at 0 and ψ(1/n) = O(n^{−L′}) along the integers, then its Taylor coefficients of order < L′ vanish (the first nonzero
one would dominate). With L′ := L + p(|γ|_w + mj), the Taylor coefficients of ψ_{γ,m} of order < L′ vanish.

The Taylor coefficients of ψ_{γ,m} of order ≤ K and with |γ| + m ≤ B are the corresponding coefficients of the **formal** element
Π := b̂(u + he_j) − b̂(u) − ∫_0^hΨ_j(formal entries)(u + ηe_j)dη of ℛ_J[h]. The truncations K (in 1/n) and B (in the times) only affect
higher orders: S_i preserves the u-degree and maps n^{−k} into n^{−k}ℂ[[1/n]]. Since L, K, B are arbitrary, **Π = 0 in ℛ_J[h]**: the
formal integrated identity holds coefficientwise.

*Step 4: differentiate formally.* The h-linear coefficient of Π is ∂_{u_j}b̂ − Ψ_j(formal entries), and Ψ_j(formal entries) =
½c^jn^{−jp}b̂[(𝒥^j)_{00} − (𝒥^j)_{−1,−1}]: substitute b_{n+i} = cn^{−p}𝒷_i and α_{n+i} = cn^{−p}𝒶_i, and (J^j) = (c/n^p)^j(𝒥^j). This is
(T-b). (T-a) follows in the same way from Lemma T.1.4: α_n = cn^{−p}𝒶_0 and F_j(n) = (c/n^p)^{j+1}𝒷_1(𝒥^j)_{10}. ∎

*Why not differentiate the asymptotic expansion directly.* A uniform bound does not control derivatives: f_n(τ) = n^{−L}sin(n^{L+1}τ)
is O(n^{−L}) uniformly, while f_n′ is not. The integrated form (4.2) needs only bounds on values, and the polynomial structure of the
approximants in u (Step 3) recovers the derivative identity at the level of formal series. Analyticity in τ of the Riemann–Hilbert
solution, uniform in n, is not needed. The analyticity that is used is elementary: the exact b_n, α_n are real-analytic in τ (moments),
and each layer is a Taylor coefficient of an entire function of μ (Theorem N.6 proof (i), Lemma T.B.3).

### 4.2 Proof of Theorem T
(i) is Lemma T.A with Lemma T.B (for σ_τ). (ii) is Lemma T.2, applied for each j ≤ J. (iii) is (1.1) applied to (ii). The instances
(T1)–(T3) are the u-degree-0 coefficients (j = 1, 2) and the u₁-degree-1 coefficient (j = 1) of (ii), with (𝒥)_{00} − (𝒥)_{−1,−1} =
𝒶_0 − 𝒶_{−1} and (𝒥²)_{00} = 𝒶_0² + 𝒷_0² + 𝒷_1². For (T2): (ii) for j = 1 differentiated once more in u₁ at u = 0, together with (T-a)
for j = 1, which gives ∂_{u₁}𝒶_0 = c n^{−p}(𝒷_1² − 𝒷_0²) — this is JZC_M4's "∂_t²log b_n² = b²_{n+1} − 2b_n² + b²_{n−1}". (iv) is the
recursion stated there. ∎

### 4.3 Theorem T_H
Repeat §4.1–4.2 with σ^δ_τ. Lemma T.A gives (4.1) with the layers of M(α + 2δ, α) and μ^δ_n − τn^{−p·}; the total time is
u = τ + t^{δ,(J)}; Lemma T.1 applies to σ^δ_τ (hypotheses checked in §2). ∎

## 5. Consequences

### 5.1 JZC_M4 §8, JZC_SHIFT, Paper IV
- JZC_M4 §8's sketch is replaced by §4. The sketch's "uniformly for τ in a compact set" is not needed (Baire, Step 1). Its "(E3 Lemma
  E3.4 holds for any polynomial tilt)" is row 2 of the transfer table.
- JZC_SHIFT §2.1 (b) is Theorem T (ii)–(iv) on the lattice line, for every finite set of integer exponents and every p ≠ 1, |α| < 1. Its
  §2.1 (c) "A₀ = 1" is now direct: Lemma T.B.3 (n⁰ coefficient of 𝔄_0 is 𝖺(P_0^∞)/(2c) = 1). Its Cor SH.3 hypothesis (T_H) is
  Theorem T_H with Cor T.3. Labels: Thm SH on β′ ≠ ν becomes PROVED-mod-cite (Theorem T_H), with T_H's NOT REVIEWED inherited.
  JZC_SHIFT itself is not edited here.
- JZC_SHIFT §5.1's derivation of A₁, A₂ from (T1) is now confirmed by direct extraction (Prop T.4). m4_diag's closed form a₂
  (NUMERICAL there) is exact for the model (Prop T.4).
- Paper IV may state Theorem T as a Proposition at the label PROVED-mod-cite, with Lemma T.A (transfer) as the step to review.
  papers/ is not edited here.

### 5.2 Rationality (Cor T.3)
Each coefficient identity in (T-b), (T-a) has the form R(p, β′, ν) = 0. Here R is a polynomial in finitely many layer coefficients
d_{k,γ}, 𝔞_{k,γ} and in binomial coefficients binom(−p(1 + w) − m, l) (polynomial in p). The layer coefficients are rational in
(p, β′, ν):
- the residue recursion and both extractions are field operations on the Laurent data (JZC_SIGMA §1, which also covers β′; the gauge
  Taylor data are rational for integer exponents, m4_zeta_exact2 (A));
- the α-extraction divides only by (Q_1)_{12}, whose leading term is ic.

By Theorem T_H, R vanishes on {(p, α + 2δ, α): p ∈ (0, ∞) ∖ {1}, α ∈ (−1, 1), δ ∈ (−1, 0)}, and for each p the set of
(β′, ν) = (α + 2δ, α) is a non-empty open subset of the plane. (No irrationality of p is needed, unlike JZC_SIGMA §3.1: the tilts
separate the layers.) The argument of JZC_SIGMA §3.2 (numerator polynomial vanishing on an open set,
then in p) gives R ≡ 0. Note that s ∈ (1, 1 + 2p) is used only through |α| < 1 in the analytic inputs. The formal identities then hold
for all (β′, ν), including |α| ≥ 1, as identities of the formal model. ∎

### 5.3 Prop T.4 (the diagonal integer layer)
From the engine (Lemma T.B), identically in (p, ν, β) to order 4 (`toda_layers`, L1, L3, Q1, Q2):
- 𝔄_0 = 1 − p(β + 2)/(2n) + …;
- with M := n + β/2 + 1, the natural form (M/n)^p𝔄_0 = 1 + a₂M^{−2} + a₄M^{−4} + O(M^{−5}), with no M⁻¹, M⁻³ terms;
- **a₂ = −(p + 1)/24 + (p + 1)(p + 2)ν²/8**; a₄ as in §7.2 (the 3p + 2 hard-edge denominator again); the coefficients are β-free
  to M⁻⁴.

This is m4_diag's NUMERICAL closed form and JZC_SHIFT §5.1's (T1)-derived value, now by direct extraction. As coefficients of α_n of
the lattice this is PROVED-mod-cite (Lemma T.B). The evenness and β-independence **to all orders** (JZC_SIGMA §7 item 3) are not proved
here; the check is to order 4.

## 6. Rule A (adversarial pass) — log

1. *Circularity.* Theorem T is proved from the exact measures (Lemma T.1) and the frame (Lemma T.A). Neither uses any Toda structure of
   the model. The layer checks (`toda_layers`) compare the engine's higher layers with the Toda flow of the engine's integer layers.
   The α-layers come from a new extraction (R_2, never fitted, independent of the b-extraction), so the α-equation (T-a) at first order
   and both equations at second order are non-trivial tests. They are not consequences of how the engine was built: the engine knows
   nothing about Toda.
2. *Term-by-term differentiation.* Avoided (§4.1, last paragraph). Counterexample f_n(τ) = n^{−L}sin(n^{L+1}τ) recorded.
3. *Uniformity.* Baire gives uniformity only on some ball U, possibly far from τ = 0 (e.g. not containing u = t). This suffices because
   Step 3's identities are polynomial in (u, h): valid on an open set ⇒ valid as formal identities, in particular at u = 0 and u = t.
   Checked: the coefficient-extraction step needs only U′ × [−h₀, h₀] to have non-empty interior.
4. *Scaled vs unscaled times* (the one place where "∂_μ = −n^{jp}∂_t" can go wrong). Under n ↦ n + i, μ_j must shift by (1 + i/n)^{−jp}.
   The "scaled-time" control in `toda_layers`: that shift (μ treated as n-independent) agrees at first order (asserted, as it must:
   first-order layers use only μ = 0 data) and **fails at second order**, for both equations, j = 1, 2, 3 and mixed.
5. *Finite truncation conventions.* Lemma T.1 for M < ∞ at n = M − 1 needs F_j(M − 1) = 0. It is proved (π_M = Π(x − x_k) is
   t-free) and checked (`toda_measures`, all n).
6. *Does Lemma T.A prove too much?* It claims that a polynomial tilt changes only μ. Two-point and degenerate tests of the claim:
   - at p = 2 the lattice band factor vanishes (ζ(−2k) = 0), so σ_τ's expansion is the model at μ = −τn^{−2·} alone;
   - at τ = −t^{(J)} the tilted lattice's layers up to weight J are the integer layer alone (μ^τ_{n,j} = 0 for j ≤ J).

   Neither is contradicted by any data in the repo. A non-polynomial tilt (e.g. ℓ₁ = log-type) is **not** covered: then r_n is not
   analytic at 0 (Paper 2 sec_7 intro), and the transfer table's hard-edge row fails. The proof uses exactly this distinction.
7. *Lemma T.A for p < 1.* The rows rely on E_plt1 / RH_plt1b / G23plt1 statements as quoted in the REVIEWED memos. The seam
   construction (RH_plt1b §1) is weight-free, which was checked; the rest was not re-read. Flagged for Rule R.
8. *Normalisations (Rule N 5).* Engine units e_a = C(2j_a, j_a)c^{j_a}μ_a, c = 1; A := n^pα_n/(2c), so 𝒶 = 2A. The factors
   −1/(2C_a), −1/C_a in `toda_layers` follow from (1.1) and (T-b), (T-a). Controls without 1/C_a, with opposite signs, with (𝒥^j)_{11}
   in place of (𝒥^j)_{−1,−1}, and with 𝒷_0 in place of 𝒷_1 in F_j all fail.
9. *Engine copy.* toda_engine = w2_engine + R_2 + α-extraction; the b-part is string-identical to w2_engine's output (X1). The
   α-extraction matches the independent numerical engine m4_rh4 (X2).
10. *Weight of the shift in T.1 vs ℛ.* T.1's entries are unscaled; ℛ's entries are scaled by n^p/c. The factor (1 + i/n)^{−p} in 𝒷_i,
    𝒶_i is the shift of n^{−p}. Getting this wrong breaks the first-order identity, which holds.
11. *Process.*
    - A detached first launch of the engine runs was stopped by pid after ~2 min, before any output existed, and restarted as a
      tracked job. A `pkill -f` pattern matched its own shell (cf. JZC_SHIFT Rule A 10); no data were affected.
    - The symbolic runs with the default Laurent depth SHI = 30 had produced no output after ~35 CPU-min each, and were stopped.
    - They were rerun with SHI = 16 (the depth used for KORD 4 in JZC_SHIFT's registered runs), which finishes in 100–442 s.
    - The engine itself refuses an insufficient depth, since every principal part is asserted determined. X3 confirms independence
      of the depth at a rational point.

## 7. Checks

### 7.1 `toda_measures.py` → `toda_measures.out` (exact)
736 identities hold, and all 864 controls fail (§2). This is the exact verification, on finite truncations of the actual discrete
measures (lattice, Hurwitz), of the Toda identities: moments → Jacobi coefficients → derivatives in t vs (J^j)_{nn}, F_j.

### 7.2 `toda_layers.py` → `toda_layers.out` (exact computer algebra)
Engine configurations (toda_engine.py, KORD = 4, c = 1):

| cfg | model | exponents | orders in the times | field | engine (SHI) |
|---|---|---|---|---|---|
| L1 | lattice line M(α, α) | j = 1 | 1, 2 (E = (2, 0)) | ℚ(p, α) | 100 s (16) |
| L2 | lattice line | j = 2, k = 3 | 1, 2 (incl. mixed e₂e₃) | ℚ(p, α) | 138 s (16) |
| L3 | decoupled M(β, ν = α) | j = 1, k = 2 | 1, 2 (incl. mixed) | ℚ(p, α, β) | 442 s (16) |
| Q1 | lattice, p = 3/2, α = 3/10 | j = 1, 2 | 1, 2, 3 (E = (2, 1)) | ℚ | 36 s (30) |
| Q2 | decoupled, p = 3/5, ν = −2/7, β = 1/3 | j = 1, 3 | 1, 2 | ℚ | 23 s (30) |
| Q3 | lattice, p = 7/3, α = −1/2 | j = 3, 2 | 1, 2, 3 (E = (1, 2)) | ℚ | 20 s (30) |
| Q4 | lattice, p = 2/5, α = 5/8 | j = 1 | 1, 2, 3 (E = (3, 0)) | ℚ | 16 s (30) |

"Orders" counts the total degree in the times of the layer on the left side of (T-b), (T-a). KORD = 4 (n⁻⁴) throughout; SHI is the
engine's Laurent truncation depth, which the engine checks itself (a principal part that is not fully determined stops the run).

For each configuration and each time direction, the script checks:
- (T-b) and (T-a) on every computed monomial, to order n⁻⁴;
- the integer-layer assertions of Prop T.4;
- the controls: opposite sign (both equations), (𝒥^j)_{11}, F_j with 𝒷_0, no 1/C_a, and the scaled-time shift at second order (both
  equations), all of which must fail; and the first-order agreement of the scaled-time shift, which must hold.

Results (`toda_layers.out`): **ALL 75 IDENTITIES HOLD; ALL 91 CONTROLS FAIL.**
- (T-b) and (T-a) hold for every flow direction of every configuration, on all computed monomials and orders:
  - identically in (p, α) for j = 1, 2, 3 on the lattice line (L1, L2), including the mixed second-order layer e₂e₃;
  - identically in (p, α, β) for the decoupled model (L3), which is Cor T.3's content checked directly;
  - at third order in the times at rational points (Q1, Q3, Q4; Q4 has p < 1).
- The scaled-time control fails at second order in every case, while agreeing at first order, as it must.
- Cross-checks:
  - X1: the b-part of toda_engine is string-identical to w2_engine's;
  - X2 (NUMERICAL): α-layers against m4_rh4, 3·10⁻³⁹ and 7·10⁻²³;
  - X3: the symbolic L1 layers (SHI = 16) at (3/2, 3/10) equal the Q1 layers (SHI = 30).
- Prop T.4 (L1–L3, Q1–Q4): 𝔄_0's n⁻¹ coefficient is −p(β + 2)/2. Its natural form in M has M⁻¹ = M⁻³ = 0,
  M⁻² = (p + 1)(3(p + 2)ν² − 1)/24 = a₂, and
  **M⁻⁴ = a₄ = (p + 1)(p + 3)[45p²(p + 2)²ν⁴ + 30p(p² + 6p + 8)ν² − 21p² − 38p + 4]/(5760p(3p + 2))**, identical in L1, L2, L3
  (β-free in L3). Check at the Bessel point (p, ν) = (2, −½): a₂ = 1/4, a₄ = 1/16, the coefficients of the Lommel diagonal
  (1 − 1/(4M²))⁻¹ (JZC_M4 §8).

## 8. What remains
1. **Rule R** for this note. The priority is Lemma T.A (the transfer table, especially the hard-edge row and the p < 1 rows). Lemma T.B
   is a short extension of N.6c. Lemmas T.1, T.2 are elementary.
2. A direct numerical test of Lemma T.A: Jacobi coefficients of a tilted lattice (e.g. p = 2, where μ_n = 0) against the layers at
   μ = −τn^{−2·}. Not done here; it needs a tail-corrected high-precision lattice computation (Plan 62 style).
3. All-order evenness of the diagonal layer A in M = N + ½ and its β-independence (JZC_SIGMA §7 item 3): exact here only to order 4
   (Prop T.4). Route: run JZC_SIGMA's frame identity for α_n (Lemma T.B in the m-frame).
4. JZC_SIGMA §3.3 (Cor Σ.2 for weight ≥ 3) can now avoid the linear independence of zeta monomials. Use Lemma F of JZC_SIGMA for the
   tilted measures σ_τ: by Lemma T.A the times are free, so each μ^β layer separates. Not done here: it needs Lemma F (ii)'s transfer
   for σ_τ, which is the combination of the two transfer tables.
5. Propagation (other notes not edited): JZC_M4 §8 (label of Theorem T, point to this note); JZC_SHIFT header and Cor SH.3 ((T_H)
   supplied, label); JZC_M3a_H §4 (route for weight ≥ 3); Paper IV's Proposition; m4_diag / JZC_M4 §8 a₂ label (Prop T.4).
6. Rule L (§9).

## 9. Literature (Rule L) — partial
- The Toda hierarchy for exponential tilts of orthogonal-polynomial measures is classical, and Lemma T.1 is KNOWN. W. Van Assche,
  "Orthogonal polynomials, Toda lattices and Painlevé equations", arXiv:2202.11017 (KU Leuven): §2.1 Lemma 2.1 (measure e^{xt}dμ(x), μ
  positive on ℝ with all moments of μ_t finite; dP_n/dt = −a_n²P_{n−1}; in the proof db_n/dt = a²_{n+1} − a_n², da_n²/dt =
  a_n²(b_n − b_{n−1}), his a_n² = our b_n², his b_n = our a_n), §2.3 Lemma 2.3 and Theorem 2.4 (e^{x^kt}dμ: J′ = [J, ½((J^k)_− − (J^k)_+)]).
  These were read only through a summarising fetch tool, which returned paraphrases and fragments of at most 125 characters. That
  does not meet Rule C's "quoted verbatim with every hypothesis", so **nothing in this note rests on it**: Lemma T.1 is proved in full
  in §2. The paraphrased statements agree with Lemma T.1 (j = 1 and general j).
- Deift's book (Courant Lecture Notes 3) was not accessible; it is not used.
- The statements about the lattice layers (Theorem T (ii), T_H) were not searched for. Novelty UNCHECKED.
