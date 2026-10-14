# Theorem RH₁(r): pointwise Law P for σ_r = Σ k^{−r} δ_{1/k}, every r > 1 (p = 1)

Status: **REVIEWED** 2026-10-13 (Rule R, review/REVIEW_RH1r.md: ACCEPT WITH FIXES. F1–F11 applied; the re-check
CONFIRMED subject to R1–R5, which are applied.) Label: **PROVED-mod-cite** (WLXZ v1 §§2–6; KV §5; Vanlessen
math/0212014 §4, incl. (4.26)–(4.34); DLMF 5.11). The reliance on WLXZ is the same as RH₁'s. This extends Theorem RH₁ (RH_p1.md, REVIEWED; r = 3/2) to all r > 1.

Notation is RH_p1.md's:
- WLXZ = Wu–Lin–Xu–Zhao, arXiv:1410.3948v1, run at their α = 1 (written α_W below);
- t = n/z² is the rescaled index variable;
- H(t) = Γ(t+1)e^t/(√(2π)t^{t+1/2});
- H_n(z) := H(n/z²).

Fisher–Hartwig exponent. Throughout,

  **a := r − 3/2 > −1/2.**

RH.md writes this as α_FH = (2r − 2 − p)/(2p) at p = 1. Here it is a, to keep it apart from WLXZ's α_W = 1.

## 0. Statement

**Theorem RH₁(r).** Let r > 1 and σ_r := Σ_{k≥1} k^{−r} δ_{1/k}. Let β_N be the squared recurrence coefficients of
σ_r's symmetrization, so that a_m = β_{2m−2} + β_{2m−1} and b_m² = β_{2m−1}β_{2m}, as in RH_p1.md §3. Then

  N β_N = 1 + O(1/N),

and consequently

  n b_n = ½(1 + O(1/n)) = c(1)(1 + O(1/n))  and  a_n/(2b_n) = 1 + O(1/n).

This is the **pointwise Law P for σ_r, with a rate, for every r > 1.** ~~By G1-T and A4 it discharges (T3) and (CL) for
this family.~~ *(Corrected — Plan 37 note, 2026-10-14: the theorem gives the pointwise b- and a-laws for this family
directly, so (T3) holds for it. (CL) and A2/A4 are p > 1 statements: for p = 1, J is not trace class and (CL)/A2 "do
not apply as stated" (G1 PROOF.md §3, "Status of (CL)" after A4; §3.1, CL4). Nothing is claimed about (CL) at p = 1.)* At r = 3/2
(a = 0) it reduces to RH₁.

**Numerics** (`checks/check_p1_general_r.out`, NUMERICAL). The fit Nβ_N − 1 = (k₀ + k₁(−1)^N)/N + O(N⁻²) gives:

| r    | a     | k₀      | k₁      |
|------|-------|---------|---------|
| 1.25 | −0.25 | −0.7500 | +0.7407 |
| 1.5  | 0     | −1.0000 | −0.0001 |
| 2    | 0.5   | −1.4998 | −1.4997 |
| 2.5  | 1     | −1.9992 | −2.9988 |
| 3    | 1.5   | −2.4980 | −4.4972 |

The fits agree under K-doubling, but that is weak evidence: with the Euler–Maclaurin tail to 1e16 they agree by
construction (Rule R F10). A different tail cut-off or fit window would be a real test. Still, k₀ ≠ 0, so the rate
O(1/N) cannot be improved in general.
- **k₀ = ½ − r** (to fit accuracy; conjecture).
- **k₁ ≈ −3a.** This is a conjecture. It agrees to < 0.1% except at r = 1.25, where +0.7407 vs +0.75 is 1.2% off. The earlier p = 2 fits gave ≈ −4a, which suggests k₁ = −(p+2)a.
- The (−1)^N term is the expected signature of a Fisher–Hartwig point at the band centre (compare Vanlessen
  Theorem 1.1, A₁(n) ∝ λ cos(2n arccos 0)). Vanlessen's fixed-weight constant does not transfer directly, because here
  the weight is n-dependent after rescaling.

The theorem asserts only the O(1/N) rate, not the constants.

## 1. Identification (exact)

- k^{−r} = k^{−3/2}·k^{−a}, and σ_{3/2} = √(2π)H(k)·TC(α_W = 1) (RH_p1.md §1).
- In WLXZ's rescaled symmetric variable the node index is t = n/z². So σ_r's analytic weight is

    w(z)·H_n(z)·(n/z²)^{−a} = n^{−a}·w(z)·H_n(z)·(z²)^{a},

  with (z²)^a principal. This is analytic on ℂ ∖ iℝ and positive on ℝ ∖ {0}.
- The constant n^{−a} multiplies every mass. Monic OPs and β_N are unchanged, and in the RHP it acts by a constant
  diagonal conjugation of Y. **We drop it.**
- Write F(z) := H_n(z)(z²)^a. So σ_r is TC(α_W = 1) with masses multiplied by √(2π)F(node).

## 2. Running WLXZ with weight wF (outside the special discs)

**Lemma W1(r).** Run WLXZ §§3–5 verbatim with weight w·F, exactly as Lemma W1 does with w·H_n:
- R, T, Q, V and the D-functions D, D̃, D̂, E are unchanged (they depend only on n/z² and α_W);
- the residual weights acquire F^{±1};
- the sign structure is unchanged.

*Proof.* This is RH_p1.md §2, steps 1–2, with H_n replaced by F. The extra factor (z²)^a is analytic and nonvanishing
on the same domain ℂ ∖ iℝ, so pole removal (3.13)–(3.18) is unchanged.

On the long saturated pieces, 2 − ε ≤ |z| ≤ k_n ≍ √n. There |(z²)^a| ≤ C n^{|a|}, a polynomial factor. So entries
that are O(e^{−cn}) for σ_{3/2} remain O(e^{−cn}) for σ_r. ∎

**Weight bookkeeping.** By RH_p1.md §2 (iii), the band jump of V on (−2,0) ∪ (0,2) is

  [[0, −m_σ(x)], [1/m_σ(x), 0]],  with m_σ(x) = e^L(4 − x²)·H_n(x)²·|x|^{2a}.

The lens and saturated jumps carry the same factor:
- upper-right entries × F;
- lower-left entries × F^{−1};
- diagonal entries D/D̂ unchanged.

This is (5.3) with w₀, ŵ ↦ w₀F, ŵF. The rule "multiplying the weight by an analytic f ⇔ V ↦ V f^{−σ₃/2} locally" is
used below.

## 3. Global parametrix with the Fisher–Hartwig factor

- **Stirling truncation.** Fix the integer m := ⌈|a|/2⌉, so that δ := 4m + 2 − 2|a| ≥ 2. (F2 needs δ > 0; §6 needs δ > 1/2. Any larger m also works.) Define the entire, nonvanishing function

    Q_m(z) := exp( 2 Σ_{k=1}^{m} B_{2k}/(2k(2k−1)) · (z²/n)^{2k−1} ),

  with Q_0 ≡ 1.
- **Lemma S (DLMF 5.11.1 and §5.11(ii); read, CITATIONS (DLMF)).** Uniformly for |arg(±z)| ≤ π/3,

    κ_n(z) := H_n(z)²/Q_m(z) = 1 + O((|z|²/n)^{2m+1}).

  - *Proof.* log H(t) = Σ_{k=1}^{m} B_{2k}/(2k(2k−1)t^{2k−1}) + R_m(t). This is lnΓ(t+1) = ln t + lnΓ(t) together
    with DLMF 5.11.1, where the leading terms cancel identically.
  - |arg(±z)| ≤ π/3 gives |ph t| ≤ 2π/3. There |R_m(t)| ≤ sec^{2m+2}(π/3)·|B_{2m+2}|/((2m+2)(2m+1)|t|^{2m+1}). ∎
  - Numerically (`checks/check_general_r_parametrix.out` [2]), sup |κ_n − 1|/(|z|²/n)^{2m+1} = 1/6, 1/180, 1/630
    for m = 0, 1, 2, independent of n. These are the leading Stirling coefficients.
- **Szegő functions.** Let Φ(z) := (z + √(z² − 4))/2 (the branch ~ z at ∞) and
  - D_a(z) := (z/Φ(z))^a, with log(z/Φ) → 0 at ∞;
  - D_Q(z) := exp( (√(z²−4)/2π) ∫_{−2}^{2} log Q_m(x) dx / (√(4−x²)(z − x)) ).
- **Lemma G.**
  - (i) D_a and D_Q are analytic and nonvanishing on ℂ ∖ [−2,2], and D_a(∞) = 1.
  - (ii) On (−2,2) ∖ {0}: D_{a,+}D_{a,−} = |x|^{2a} and D_{Q,+}D_{Q,−} = Q_m(x).
  - (iii) D_Q = 1 + O(1/n) uniformly on ℂ, and D_{Q,∞} = 1 + O(1/n).
  - (iv) |D_a(z)|/|z|^a is bounded above and below near 0.
  - (v) D_a is smooth and nonvanishing up to the band near ±2 from each side.
  - *Proof.*
    - (i) z/Φ(z) has no zeros or poles off [−2,2]. Its winding around [−2,2] is 0, since both z and Φ wind once. So
      the log is single-valued.
    - (ii) Φ₊Φ₋ = 1 on the band, so (z/Φ₊)(z/Φ₋) = x². log(z/Φ) is real on ℝ ∖ [−2,2], and z/Φ(±2) = 2 > 0, so the
      sum of boundary logs is continuous and equals log x² at ±2, hence everywhere. D_Q is the standard Szegő
      function. log Q_m = O(x²/n) on the band, which gives (iii).
    - (iv) Φ₊(0) = i, so D_a(z) ∼ (∓iz)^a near 0 in ℂ±.
  - Numerically ([1]): |D₊D₋/|x|^{2a} − 1| ≤ 1e−16 and |D_a|/|z|^a ∈ [0.987, 1.002] for a ∈ {−0.4, 0.5, 1.5, 2.5}.
- **Global parametrix.** Let N be WLXZ's (§5; band weight e^L(4 − x²), i.e. α_W = 1). Put D := D_aD_Q and

    N_r(z) := D_{Q,∞}^{σ₃} N(z) D(z)^{−σ₃}.

  N_r is analytic off [−2,2], N_r → I at ∞, and N_r has the band jump [[0, −m_r], [1/m_r, 0]] with

    m_r(x) := e^L(4 − x²)|x|^{2a}Q_m(x).

  (The jump follows from D₋^{σ₃}[[0,A],[B,0]]D₊^{−σ₃} = [[0, AD₊D₋],[B/(D₊D₋), 0]].)
- **The model mismatch** on the band is m_σ/m_r = κ_n. Outside the discs it is 1 + O(n^{−2m−1}), uniformly on
  [−2+ε, −ε] ∪ [ε, 2−ε], where N_r is bounded. So J_S = N_{r,−}·diag(κ_n^{−1}, κ_n)·N_{r,−}^{−1} = I + O(1/n) there,
  as in RH₁ step 3.
- **Extraction value.** Write D(z) = D_∞(1 + d₁/z + O(z⁻²)). Then

    N_{r,1} = D_{Q,∞}^{σ₃}(N₁ − d₁σ₃)D_{Q,∞}^{−σ₃},

  so (N_{r,1})₁₂(N_{r,1})₂₁ = (N₁)₁₂(N₁)₂₁ = 1 (RH_p1.md §3).

## 4. Airy discs U(±2, ε)

Let P^{(3/2)} be RH₁'s local parametrix at ±2 (RH_p1.md §2, step 4). It has exactly the jumps of V_{σ_{3/2}} in
U(±2, ε), and P^{(3/2)}N^{−1} = I + O(1/n) on ∂U(±2, ε).
- In U(±2, ε), q(z) := (z²)^a is analytic and nonvanishing, since |z| ≈ 2. V_{σ_r} has the jumps of
  V_{σ_{3/2}}·q^{−σ₃/2} (§2 bookkeeping).
- Put g := (qQ_m)^{1/2}/D. Then g₊g₋ = 1 on the band, so N g^{σ₃} has the same band jump as N (an off-diagonal J
  satisfies g₋^{−σ₃}Jg₊^{σ₃} = J when g₊g₋ = 1). Hence A := N g^{σ₃}N^{−1} has no jump in U(±2, ε).
- At ±2, |A| = O(|z∓2|^{−1/2}). By WLXZ (5.11) at α_W = 1, N's first column is O(|z∓2|^{−3/4}) and its second
  O(|z∓2|^{1/4}). Each term of A = N g^{σ₃}N^{−1} pairs a column of N with the matching row of N^{−1} = adj N, so the
  exponents add to −3/4 + 1/4 = −1/2. g is bounded by Lemma G(v). So the singularity is
  removable. A is analytic, with A and A^{−1} bounded uniformly in n.
- Define P_r := D_{Q,∞}^{σ₃}·A·P^{(3/2)}·q^{−σ₃/2}. It has V_{σ_r}'s jumps exactly. On ∂U(±2, ε),

    P_rN_r^{−1} = D_{Q,∞}^{σ₃}·A(I + O(1/n))·N(q^{−1/2}D)^{σ₃}N^{−1}·D_{Q,∞}^{−σ₃}.

  Since q^{−1/2}D = Q_m^{1/2}/g, the middle factor is A^{−1}·N Q_m^{σ₃/2}N^{−1} = A^{−1}(I + O(1/n)). So

    P_rN_r^{−1} = I + O(1/n). ∎

## 5. The origin U(0, ε): a Bessel (Fisher–Hartwig) parametrix

**Contours.**
- Let ψ be WLXZ's equilibrium density (TC, α_W = 1). It is even, with ψ(0) > 0.
- WLXZ's φ satisfies φ = l/2 − g in ℂ± (from (4.29) and (4.34)–(4.35)). So φ₊ + φ₋ = 0 on the band and φ₊ is
  imaginary there.
- With KV's convention φ_KV := −φ (see the dictionary below), set f(z) := iφ_KV(z) − iφ_KV,₊(0) in ℂ₊ and −iφ_KV(z) − iφ_KV,₊(0)
  in ℂ₋ (KV (5.6)). Then f(x) = π∫₀^x ψ and f′(0) = πψ(0) > 0 (KV (5.7)–(5.8)).
- **Parity (cosmetic, F8).** ψ is even, so f is odd and real on ℝ, hence f(iℝ) ⊂ iℝ. So KV's Σ₃ ∪ Σ₇ = iℝ ∩ U(0, ε),
  and KV's Σ₁ ∪ Σ₅ is the band. This is not load-bearing: KV's W (5.9) is defined by sectors of arg f wherever
  f^{−1}(iℝ) lies, and V has no jump near iℝ (iℝ lies in Ω_∞, where D has no cut).
- Inside U(0, ε), deform WLXZ's lips Σ_{l,±}, Σ_{r,±} to KV's Σ₂, Σ₄, Σ₆, Σ₈ = f^{−1}(arg ζ = ±π/4, ±3π/4). For
  small ε these lie in |arg(±z)| ∈ [π/4 − η, π/4 + η]. That is inside WLXZ's admissible sectors (away from both ℝ and
  iℝ), and there Re φ < 0 (WLXZ (4.33); exactly, Re φ = −Im f in ℂ₊ and Re φ = Im f in ℂ₋).

**Dictionary WLXZ → KV.**
- WLXZ (6.24)/(5.3) on the band reads [[0, −m], [1/m, 0]], and on the lips [[1, 0], [−e^{2nφ}/m, 1]] plus terms that
  are discarded below. Conjugation by σ₃ gives [[0, m], [−1/m, 0]] and [[1, 0], [m^{−1}e^{−2nφ_KV}, 1]].
- With m = h|x|^{2a}, this is KV (5.1)–(5.2) with weight |x|^{2a} times the analytic factor h. So V ↦ σ₃Vσ₃ (a
  constant conjugation, harmless) puts us in KV's frame.

**Local model jumps.**
- h₀(z) := e^L(4 − z²)Q_m(z) is analytic and nonvanishing in U(0, ε). (F9: Vanlessen assumes h has positive real
  part; h₀ need not, since e^L is not real here. That hypothesis is used only to choose h^{1/2}. Here we use only an
  analytic, nonvanishing branch of h₀^{1/2} on the simply connected disc U(0, ε), which exists.)
- The model jumps are those with m = m_r = h₀|x|^{2a} on the band, and lower-triangular lip jumps with h₀(z²)^{a}.
- The true jumps of V_{σ_r} differ from these in two ways:
  - (J1) multiplicatively, by κ_n on the band (in the off-diagonal entries) and by κ_n^{−1} in the lip lower-left
    entries;
  - (J2) by the discarded diagonal D/D̂ − 1 and upper-right −(ŵF/D̂²)e^{−2nφ̂} lip entries.

**Construction** (KV §5 with Vanlessen's absorption of h; CITATIONS (KV), (Van)):

  P₀(z) := E_n(z)·Ψ_a(n f(z))·W_h(z)^{−σ₃}·e^{−nφ_KV(z)σ₃},  W_h := W·h₀^{1/2},

where:
- W = (−z)^a or z^a by sector (KV (5.9));
- Ψ_a is KV's Bessel model (5.17)–(5.23), which exists for every a > −1/2;
- E_n := E·e^{nφ_KV,₊(0)σ₃}e^{−πiσ₃/4}(1/√2)[[1, i], [i, 1]], with E := P^{(∞)}W_h^{σ₃}e^{±aπiσ₃/2} (and the
  anti-diagonal factor in sectors V–VIII). This is KV (5.26)–(5.30) and Vanlessen (4.47), with P^{(∞)} := σ₃N_rσ₃.

**Lemma B.**
- (i) P₀ has exactly the model jumps in U(0, ε).
- (ii) det P₀ ≡ 1.
- (iii) E_n is analytic in U(0, ε). E_n and E_n^{−1} are bounded uniformly in n.
- (iv) P₀(σ₃N_rσ₃)^{−1} = I + O(1/n) uniformly on ∂U(0, ε). (P₀ lives in KV's frame. Undoing V ↦ σ₃Vσ₃, the WLXZ-frame parametrix is σ₃P₀σ₃, and it matches N_r.)

*Proof.*
- (i) This is KV (5.10)–(5.24). The analytic h₀ enters only through W_h, exactly as in Vanlessen's W_{x_ν} (his p. 18:
  "W_{xν}(z) = (1−z)^{α/2}(1+z)^{β/2}h^{1/2}(z) …").
- (ii) This is Vanlessen (4.53).
- (iii) E_n's analyticity is KV p. 19 ("E is analytic in a full neighborhood of U_δ. Here we need the fact that
  D(z)/W(z) and W(z)/D(z) remain bounded as z → 0"). This holds by Lemma G(iv): D/W_h = (D_a/W)(D_Q/h₀^{1/2}), and
  both factors are bounded above and below.
  - Boundedness in n: N_r is uniformly bounded near ∂U(0, ε). |e^{nφ_KV,₊(0)σ₃}| = 1 because φ₊(0) ∈ iℝ. The
    remaining factors are constant.
  - E_n is analytic, so the maximum principle bounds it inside the disc.
- (iv) This uses Vanlessen (4.43)–(4.46) (Ψ = B(I + O(1/ζ))e^{−iζσ₃}C with constant B, C) and KV (5.26). ∎

**Lemma M (mismatch).** Let H := V P₀^{−1} in U(0, ε). On Σ ∩ U(0, ε),

  |J_H − I| ≤ C n^{−1}  (uniformly, including at 0),  and  ‖J_H − I‖_{L¹∩L²∩L^∞} = O(1/n).

*Proof.* Everything below is in KV's frame (V means σ₃Vσ₃). J_H = P₀₋ (J_V J_{P₀}^{−1}) P₀₋^{−1}. Write P₀ = E_n Ψ_a(nf) Λ, with Λ := W_h^{−σ₃}e^{−nφ_KVσ₃}, which is
analytic across the lips and the band. Let ζ = nf(z) and ρ = |ζ| ≍ n|z|.

- **(J1), band.** J_V J_P^{−1} = diag(κ_n, κ_n^{−1}) (in WLXZ's frame; after the σ₃ conjugation it is the same), which
  commutes with Λ₋. So

    J_H − I = E_nΨ₋ M Ψ₋^{−1}E_n^{−1},  M = diag(κ_n − 1, κ_n^{−1} − 1).

  M is a combination of I and σ₃ with coefficients O(|κ_n − 1|).
- **(J1), lips.** J_V J_P^{−1} − I is lower-triangular. After conjugation by Λ₋ it is (κ_n^{−1} − 1)(J_Ψ − I), where
  J_Ψ is Ψ_a's constant lip jump. (Λ conjugates the model lip jump into J_Ψ: that is how Ψ_a was built.) So

    J_H − I = (κ_n^{−1} − 1)·E_n(Ψ₊Ψ₋^{−1} − I)E_n^{−1}.

- **Amplification bound** (from KV (5.21)–(5.22) for ρ ≤ 1, Vanlessen (4.43)–(4.46) for ρ ≥ 1, and det Ψ = 1):

    |Ψσ₃Ψ^{−1}| + |Ψ₊Ψ₋^{−1} − I| ≤ C·(1 + ρ^{−2|a|}(1 + |log ρ|)²).

  (The log² padding is needed only at a = 0. For a ≠ 0 the growth is the pure power ρ^{−2|a|}.)

  - For ρ ≥ R₀: Ψ = B(I + O(1/ζ))e^{−iζσ₃}C, where C is diagonal or anti-diagonal, so Cσ₃C^{−1} = ±σ₃ commutes with
    e^{−iζσ₃}. Also Ψ₊Ψ₋^{−1} − I = O(1/ζ). (4.43)–(4.46) are "as ζ → ∞" statements; for 1 ≤ ρ ≤ R₀ the bound follows
    from continuity.
  - For ρ ≤ 1: the entries are O(ρ^{−|a|}) (log at a = 0) and det = 1.
  - Numerically ([3], a ∈ {−0.4, 0, 0.5, 1.5, 2.5}, ρ ∈ [1e−6, 1e2]; sector I only, i.e. the band ray arg 0⁺ and
    the lip ray arg π/4⁻; the other sectors follow by KV's symmetries):
    - the band amplification is C_a·ρ^{−2|a|}, with a constant C_a up to ≈ 40 (4.07e31 at a = 2.5, ρ = 1e−6, against
      ρ^{−5} = 1e30);
    - the printed ratios (≤ 1.3 for ρ ≤ 1e−2, ≤ 68 at ρ = 1) are against ρ^{−2|a|}(1 + |log ρ|)², not ρ^{−2|a|};
    - the lip amplification is ≤ C for ρ ≥ 1 and decays like e^{−2ρ sin(π/4)}.
- **Combining with Lemma S.**
  - For ρ ≥ 1: |J_H − I| ≤ C(|z|²/n)^{2m+1} ≤ Cn^{−2m−1}.
  - For ρ ≤ 1, i.e. |z| ≲ 1/n: |J_H − I| ≤ C(|z|²/n)^{2m+1}(n|z|)^{−2|a|}log² ≤ C n^{−2m−1−2|a|}|z|^{4m+2−2|a|}log².
    This is ≤ Cn^{−1}, and → 0 at z = 0, because δ = 4m + 2 − 2|a| > 0 (the choice of m). Explicitly,
    |J_H(z) − I| ≤ C n^{−1}·min(1, (n|z|)^δ) near 0, which is used in §6.
- **(J2).** The discarded lip terms are O(e^{−cn/|z|²}). By (4.29)–(4.30), φ̂ = φ ∓ (1/z² − 1)πi, and D̃ = D(1 − e^{∓2iθ})
  (4.16) with θ = πn/z² + O(1). On rays with |arg(±z)| ∈ [π/4 − η, π/4 + η], |e^{∓2πin/z²}| = e^{−2πn|sin 2arg z|/|z|²}
  in the relevant half-plane: this is WLXZ's "exponentially small … so long as arg z keeps a distance to ±π/2" made
  explicit.
  - The crude bound |P₀₋||M||P₀₋^{−1}| ≤ poly(n, 1/|z|)·e^{2n|Re φ|}·e^{−cn/|z|²} applies, with |Re φ| ≤ C|z|. It is
    O(n^{−K}) for every K once ε³ < c/(4C).
- **L¹ and L².** Σ ∩ U(0, ε) has length O(1), so these follow from the uniform bound. ∎

**Remark (the role of m).** Lemma M alone needs only δ > 0, and §6 needs δ > 1/2. So m = 0 (Q ≡ 1, κ_n = H_n²)
suffices for |a| < 3/4, i.e. 1 < r < 9/4. (The choice m = ⌈|a|/2⌉ above is a uniform safe choice.) For larger |a| the
truncation Q_m is needed: the bare H_n² − 1 = O(|z|²/n) is not small enough against the (n|z|)^{−2a} growth of
Ψ_a near 0. Q_m cannot be replaced by H_n² itself, since H_n has poles on iℝ accumulating at 0 (Γ(t+1) at t = −1, −2, …).

## 6. Behaviour at 0 and identification (Lemma O; rewritten per F1, F3, F4)

**(Y4)_r.** Fix δ₀ ∈ (0, π/4). As z → 0:
- (a) for δ₀ ≤ |arg(±z)| ≤ π/2,

    Y(z) = O([[1, 1 + |z|^{2a}ℓ(z)], [1, 1 + |z|^{2a}ℓ(z)]]),  ℓ := 1 + |log|z|| (only needed at a = 0);

- (b) the same bound holds for R (WLXZ (3.11), the pole-free transform) in the lens sectors |arg(±z)| < δ₀, up to
  the boundary values on the band.

The constants may depend on n; only fixed-n bounds are needed here.

*Proof.*
- **(a) Sectors away from ℝ.** Y₁₂(z) = Σ_k μ_k π_n(x_k)/(z − x_k), with μ_k ≍ k^{−r} (nodes of both signs), and π_n
  is bounded near 0. For such z, |z − x_k| ≥ c max(|x_k|, |z|), with x_k ≍ k^{−1/2}. For k ≤ |z|^{−2} the max is
  ≍ k^{−1/2}; for k > |z|^{−2} it is |z|. So (F4)

    |Y₁₂| ≤ C( Σ_{k≤|z|^{−2}} k^{1/2−r} + |z|^{−1} Σ_{k>|z|^{−2}} k^{−r} ) = O(1 + |z|^{2r−3}ℓ) = O(1 + |z|^{2a}ℓ).

  Row 2 is the same with π_{n−1}. Y₁₁ and Y₂₁ are polynomials.
- **(b) Lens sectors** (F3). Take z ∈ Ω_{r,+} ∩ U(0, ε); the other three lens sectors are symmetric. Here R₁₂ =
  U₁₂ − K₋(z), with K_±(s) := U₁₁(s)(wF/Π)(s)e^{±iθ(s)} (WLXZ (3.11)–(3.12)).
  - **Residues.** By (3.13), K_± has a simple pole at each node X_k > 0 with residue μ_kU₁₁(X_k).
  - **Size.** θ = πn/s² + O(1) gives Im θ < 0 in the upper right quadrant. So |e^{−iθ}/sin θ| ≍ e^{2Im θ} =
    O(e^{−cn/|s|²}) there, and symmetrically K₊ is O(|θ′||wF|e^{−cn/|s|²}) in the lower right quadrant.
  - **Difference.** K₋ − K₊ = U₁₁(wF/Π)(e^{−iθ} − e^{iθ}) = −2iU₁₁wFθ′ is pole-free. Its size is
    |wF| ≍ |s|^{3+2a} times |θ′| ≍ n|s|^{−3}, i.e. O(|s|^{2a}).
  - Let G := {0 < |s| < b, |arg s| < φ₀}, with φ₀ larger than the lens angle and b between two nodes. Let Γ_± be its
    boundary rays arg s = ±φ₀ and C_b its arc. The residue theorem gives

      Σ_{0<X_k<b} μ_kU₁₁(X_k)/(z − X_k) − K₋(z) = −(1/2πi)∮_{∂G} K₋(s) ds/(s − z).

    (R3) Read this with the poles near 0 cut off: replace the tip of G by an arc |s| = η_j through a midpoint between
    consecutive nodes, η_j → 0. The arc contributes O(η_j^{1+2a}) → 0, since |K_±| = O(|s|^{2a}) on such midpoint arcs.
    On the lower part of ∂G write K₋ = K₊ + (K₋ − K₊). The contributions are:
    - Γ₊ with K₋, and Γ₋ with K₊: O(e^{−cn/|s|²}), so negligible;
    - Γ₋ with −2iU₁₁wFθ′: since |s − z| ≥ c max(|s|, |z|) on Γ₋, ∫_{Γ₋}|s|^{2a}|ds|/max(|s|,|z|) = O(1 + |z|^{2a}ℓ);
    - C_b: bounded.
  - **Remaining part of U₁₂.** The nodes X_k < 0 accumulate at 0, but z lies in the right sector, so
    |z − X_k| ≥ c max(|z|, |X_k|) and the estimate of (a) applies. The nodes in [b, k_n] are finitely many for fixed n,
    so they contribute a bounded amount.
  - The part of the lens with δ₀ ≤ |arg z| < lens angle is covered both by (a), for U = Y there, and by this
    representation. The two agree because R = U there up to a factor that is O(e^{−cn/|z|²}).
  - So R₁₂ = O(1 + |z|^{2a}ℓ), and the same for R₂₂ with π_{n−1}. R₁₁ = U₁₁ and R₂₁ are polynomials. ∎

**Bounds on V and P₀ near 0.** For fixed n, all explicit factors between R and V (WLXZ (5.1)) are bounded with bounded
inverses in U(0, ε):
- e^{ngσ₃} and the e^{nlσ₃/2} normalisations;
- E, which is analytic at 0;
- D, D̃, D̂ in their regions. In Ω_∞ (which contains iℝ near 0), D ≈ 1 by Stirling, since there −n/z² lies in
  |ph| < π − δ. In the lens regions, D̃ = 1/H_n and D̂ are bounded in |arg(±z)| < π/2 − δ.
- the lens factors I − (e^{2nφ}/m_σ)e₂₁, with |e^{2nφ}| ≤ 1. These are bounded except through 1/m_σ ≍ |z|^{−2a}, which is
  treated below.

Write V = V^u·L_V inside the lens and V = V^u outside, where V^u is R times the bounded factors, and
L_V := I + (e^{2nφ}/m_σ)e₂₁ in WLXZ's convention. Similarly write P₀ = P^u·L_P with L_P := I + (e^{2nφ}/m_r)e₂₁, where
P^u is the analytic continuation of P₀ from outside the lens.

**Lemma O1 (H on small circles).** Let H := VP₀^{−1} (KV frame). As z → 0, uniformly in arg z,
- (i) for a ≥ 0, H = O(ℓ(z)²);
- (ii) for −1/2 < a < 0, H = O(|z|^{2a}).

*Proof.*
- **(i) Un-lensing, a ≥ 0.**
  - Outside the lens, V = O(ℓ) by (Y4)_r(a): the second column O(1 + |z|^{2a}ℓ) is O(ℓ) since a ≥ 0. P₀ = O(1), with
    P₀^{−1} = adj P₀ = O(1), by KV (5.5) "outside the lens".
  - Inside the lens,

      H = V^u (L_V L_P^{−1})(P^u)^{−1},  L_V L_P^{−1} = I + (e^{2nφ}/m_r)(κ_n^{−1} − 1)e₂₁ = I + O(|z|^{δ}).

    Here |1/m_r| ≍ |z|^{−2a}, κ_n^{−1} − 1 = O(|z|^{4m+2}) by Lemma S, and δ > 0 by F2.
  - V^u = O(ℓ) by (Y4)_r(b).
  - P^u = O(1) with O(1) inverse. P^u = E_nΨ^u(nf)Λ, where Ψ^u is the continuation of Ψ_a across the lip rays Γ₂, Γ₄,
    Γ₆, Γ₈ into the lens sectors I, IV, V, VIII from the neighbouring sectors II, III, VI, VII.
    - Source (R4). Vanlessen (4.27)–(4.28) and (4.31)–(4.32) write Ψ in II, III, VI, VII through
      ζ^{1/2}I_{a±½}(ζe^{∓πi/2}) and ζ^{1/2}K_{a±½}(ζe^{∓πi/2}). By his proof of Theorem 4.2 ("defined and analytic in
      the complex plane with a branch cut along the negative real axis"), these formulas continue analytically across
      Γ₂, Γ₄, Γ₆, Γ₈ into the adjacent lens sectors; (4.34) gives the continuation across Γ₂ explicitly.
    - The small-argument expansions (A&S 9.6.7, 9.6.9, which Vanlessen cites for condition (c)) give columns O(|ζ|^{a})
      and O(|ζ|^{−a}) for a > 0.
    - Λ = W_h^{−σ₃}e^{−nφσ₃} contributes |z|^{∓a}, so the column exponents cancel.
- **(ii) a < 0.** By KV (5.4), P₀ = O([[1, |z|^{2a}], [1, |z|^{2a}]]) in all directions. By (Y4)_r, together with the
  bounded factors and lens factors (now 1/m_σ ≍ |z|^{2|a|} → 0), V has the same column structure. So

    H = V·adj(P₀) = V_{·1}(P₀₂₂, −P₀₁₂) + V_{·2}(−P₀₂₁, P₀₁₁) = O(|z|^{2a}). ∎

**Lemma X (a local solution of the inverse jump).** Fix a small ε₁ ∈ (0, ε) and let Γ := Σ ∩ U(0, ε₁): six analytic
arcs (two band half-rays and four lips) meeting at 0. For n large there is X̃, analytic in U(0, ε₁) ∖ Γ, with

  X̃₊ = J_H^{−1}X̃₋ on Γ  (so HX̃ has no jump on Γ),

such that:
- (i) |X̃(z) − I| ≤ C n^{−1}(1 + dist(z, Γ)^{−1/2}), and near 0, |X̃(z)| ≤ C_n(1 + |z|^{δ}dist(z, Γ)^{−1/2}). (R1: X̃(0) is generically a nonzero constant ≠ I, contributed by the far part of Γ.)
- (ii) det X̃ is analytic in U(0, ε₁/2) and det X̃ = 1 + O(1/n) there;
- (iii) X̃₋ − I ∈ L²(Γ ∩ U(0, ε₁/2)).

*Proof.*
- **Existence.** X̃ᵀ solves the right-multiplicative problem with jump J_H^{−T}. By Lemma M (|J_H − I| ≤ Cn^{−1}
  everywhere, and ≤ C_n|s|^δ near 0, with δ ≥ 2), ‖J_H^{−T} − I‖_{L²∩L^∞(Γ)} = O(1/n). The Cauchy operator is bounded
  on L²(Γ), since Γ is a finite union of analytic arcs meeting transversally (the same fact the global small-norm step
  uses). So μ = I + C₋(μ(J_H^{−T} − I)) has a unique solution with μ − I ∈ L²(Γ) and ‖μ‖ = O(1). Set
  X̃ᵀ := I + C(μ(J_H^{−T} − I)). This gives (iii).
- **(i)** follows from Cauchy–Schwarz, |X̃ − I| ≤ ‖μ‖_{L²}(∫_Γ|J − I|²|s − z|^{−2}|ds|)^{1/2}. For the second bound,
  split Γ into |s| ≤ 2|z|, where |J − I| ≤ C_n|s|^δ gives C_n|z|^δ dist^{−1/2}, and |s| > 2|z|, where |s − z| ≍ |s|
  gives O(1).
- **(ii).** det J_H = 1, so det X̃ has no jump on Γ. It is analytic in U(0, ε₁/2) ∖ {0}.
  - Sub-mean-value bound (R2). |det X̃ − 1|^{1/2} is subharmonic, and pointwise
    |det X̃ − 1| ≤ C|X̃ − I|(1 + |X̃ − I|). By (i), |det X̃ − 1|^{1/2} is bounded by C_n(1 + |z|^{δ}dist^{−1/2}), and
    by Cn^{−1/2}(1 + dist^{−1/2}). dist(·, Γ)^{−1/2} is area-integrable near Γ (dist^{−1} is not).
    - Averaging |det X̃ − 1|^{1/2} over discs of radius |z|/4, which avoid 0, gives |det X̃(z) − 1| ≤ C_n(1 + |z|^{2δ−1}).
      This is bounded since δ ≥ 2 > 1/2, so the singularity of det X̃ at 0 is removable.
    - Averaging over discs of fixed radius with the n^{−1} bound gives det X̃ = 1 + O(1/n) on U(0, ε₁/4). ∎

**Identification.**
- G := HX̃ has no jump in U(0, ε₁/4) ∖ {0}, so it has an isolated singularity at 0.
- Its Laurent coefficients satisfy |c_{−k}| ≤ (1/2π) r^{k−1}∫_{|z|=r}|G||dz|. By Lemma O1 and Lemma X(i), using
  ∫_{|z|=r}dist(z, Γ)^{−1/2}|dz| = O(r^{1/2}) (the arcs leave 0 at fixed angles),

    ∫_{|z|=r}|G||dz| ≤ sup_{|z|=r}|H|·∫_{|z|=r}|X̃||dz| ≤ C_n r^{min(0,2a)}ℓ(r)²·(r + r^{δ+1/2}).

  This tends to 0 as r → 0, because 1 + 2a > 0 and δ ≥ 2.
- So every c_{−k} = 0, G is analytic and bounded near 0, and

    H = G·X̃^{−1} = G·adj(X̃)/det X̃.

  det X̃ = 1 + O(1/n) is nonvanishing near 0 (Lemma X(ii)), and adj X̃₋ ∈ I + L² (Lemma X(iii)). So H₋ ∈ L² near 0. More precisely, H lies locally in E², since X̃ − I is a Cauchy integral of an L² density. That is what the uniqueness step uses.
- Consequently the global S := V·(parametrices)^{−1} has L² boundary values near 0, and it satisfies the small-norm
  RHP of §7. By uniqueness in the L² class (S·S_sn^{−1} has no jumps, lies locally in E¹, and → I at ∞, hence ≡ I),
  it equals the small-norm solution.
- Away from 0, S's special points (±2 and the disc boundaries) are handled exactly as in RH₁.

*Rigour level.* At the origin this is now standard RHP rigour:
- (Y4)_r is proved by elementary sums and one residue identity;
- removability is by circle integrals, with a local inverse-jump solution X̃;
- the remaining dependence on WLXZ is the same as RH₁'s (their transformations and the uniform O(e^{−cn}) up to k_n).

The one step argued only by a structural continuation, rather than quoted, is "Ψ^u keeps the outside-lens column
exponents" in O1(i). It follows from the Bessel-function formulas behind KV (5.23) ([38] (4.26)–(4.33), via KV).

## 7. Small norm and extraction

- **Final contour.** Σ_S = (Σ ∖ discs) ∪ ∂U(0, ε) ∪ ∂U(±2, ε) ∪ (Σ ∩ U(0, ε)). Inside the Airy discs the residual jump
  is exactly I (§4). Inside U(0, ε) the residual is J_H (Lemma M).
- **Jump sizes:**
  - J_S − I = O(1/n) on the circles (Lemmas B(iv) and §4), on the band pieces (§3), and on Σ ∩ U(0, ε) (Lemma M);
  - J_S − I = O(e^{−cn}) on the lips and saturated pieces outside the discs (Lemma W1(r)).
- The long pieces have length ≍ √n, so ‖J_S − I‖_{L¹∩L²∩L^∞} = O(1/n). Hence S = I + O(1/n) and S₁ = O(1/n), as in
  RH_p1.md W1, step 6.
- **Extraction** (RH_p1.md §3 verbatim, with N_r):

    Nβ_N = (N_{r,1})₁₂(N_{r,1})₂₁ + O(1/N) = 1 + O(1/N).

  The fold gives n b_n = ½(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n). ∎

## 8. What is cited, what is new

- **Cited** (read):
  - WLXZ v1 §§2–6 (via RH₁);
  - KV §5: the Bessel model RHP (5.17)–(5.23), the parametrix form (5.10)/(5.25) and E_n (5.26)–(5.30);
  - Vanlessen math/0212014 §4: the absorption of analytic h into W, E_n (4.47), det = 1 (4.53) and the Ψ asymptotics
    (4.43)–(4.46);
  - DLMF 5.11.
- **New:**
  - the identification F = H_n(z²)^a;
  - Lemma S (Stirling truncation Q_m);
  - Lemma G and N_r;
  - the reduction of the Airy discs to RH₁ via A = Ng^{σ₃}N^{−1};
  - the parity observation Σ₃ ∪ Σ₇ = iℝ;
  - Lemma M (the structured mismatch: diagonal on the band, proportional to J_Ψ − I on the lips, with amplification
    ≤ ρ^{−2|a|});
  - (Y4)_r.
- **Reliance.**
  - As RH₁: WLXZ's O(e^{−cn}) uniformly up to k_n, and their identification step (§6, flagged).
  - KV's Ψ_a needs a > −1/2 ⇔ r > 1, which is exactly the theorem's range (r ≤ 1 gives an infinite measure).
