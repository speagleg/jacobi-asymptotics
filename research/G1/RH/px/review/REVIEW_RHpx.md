# REVIEW_RHpx: Rule R second reading of RH_px.md (Theorem RH_p, p > 1), 2026-10-13

- **Reviewer.** An independent second-reader agent (opus), on branch plan-12-RH-general-p (HEAD 3982e4d). It edited
  no repo file except this one.
- **Read:** RH_px.md in full; REVIEW_RH.md; REVIEW_RH1r.md; CITATIONS.md ((WLXZ-v1), (KMVV)); checks/*.py and *.out.
  From the sources: WLXZ v1 (1410.3948.txt) §3 (3.1)–(3.24), §4 (4.1)–(4.40), §5 (5.1)–(5.12), §6.1 (6.1)–(6.2);
  KMVV (kmvv.txt) §6, lines 1340–2190: (6.1)–(6.53), Proposition 6.5, Lemma 6.4, Lemma 6.6.
- **Probes** (session scratchpad `rhpx_review/`; not committed, because this review may edit only its own file):
  - `probe_e2e.py`: the end-to-end test, true U → V versus the global parametrix N;
  - `probe_bessel.py`: the hard-edge parametrix as written versus the KMVV left-endpoint form.

  Both are described precisely below, so they can be re-created.

**Verdict: ACCEPT WITH FIXES.**
- The architecture is right. The x-variable, the one-sided D on the slit plane, the scalar S, F = DS(4c − z)^{−1/2},
  the Jacobi-type N, and l = 2(log c + p) are all **confirmed end to end**: V N^{−1} − I = O(1/N) at points outside the
  discs, for three (p, s) pairs including α_x < 0 and p ∉ 2ℤ. This is the test that exposed the old p = 2 error, and
  it now passes cleanly.
- Two formula-level errors must be fixed and re-checked before any PROVED label:
  - **F1:** the hard-edge parametrix as written has the wrong jumps and fails to match;
  - **F2:** the saturated-region D/D̃ bookkeeping.
- Neither affects the strategy. Each has a verified or standard repair.

| Item | Verdict | Findings |
|---|---|---|
| §1 IP, transformations, Lemma 1.1 | ACCEPT | — (R on the band and the saturated side agrees with WLXZ (3.9)–(3.15); residues re-derived) |
| Lemma 1.2 (α_x) | ACCEPT | — (|W| re-derived; α_x > −1 ⇔ s > 1; a − ½ = α_x) |
| Lemma 2.1, incl. strictness | ACCEPT | — |
| Lemma 2.2 (lip signs) | ACCEPT | — (∂_y Re φ̃ = π(ρ − ψ) re-derived) |
| g = log z + O(z^{−1/p}) | ACCEPT WITH FIX | **F3** (T ≠ I + O(1/z); V needs F_∞^{−σ3} and an analyticity-at-∞ lemma) |
| Lemma 3.1 | ACCEPT | — |
| Lemma 3.2 (S) | ACCEPT WITH FIX | exponent ½ − 1/(2p) **correct**; F4(b) (state Hölder-1/p, not just continuity) |
| Lemma 3.3 and V = QF^{σ3} | **FIX REQUIRED** | **F2** (D versus D̃ in Ω^△; Lemma 3.3(ii) misattributed) |
| w₀, global parametrix N | ACCEPT | confirmed by the end-to-end probe |
| Lemma 4.1 (f) | ACCEPT WITH FIX | F1(d) (the "reflection absorbed in f" claim is false) |
| Lemma 4.2 (Bessel parametrix) | **REJECT as written** | **F1** (blocking), **F4** |
| Lemma 4.3 (mismatch) | ACCEPT | exponents and angles correct; the amplification bound holds for the corrected P₀ |
| §4.2 Airy at 4c | ACCEPT (mod-cite) | F5 (quotes) |
| §4.3 top end | ACCEPT WITH FIX | **F6** (segment entries not written; false cross-reference; mislabelled WLXZ (3.22)) |
| §5 (Y4)_x | ACCEPT WITH FIX | F9 (the lens representation must be rewritten for one-sided nodes) |
| §5 identification transfer | ACCEPT (structure) | conditional on F1 and F4 (it needs KMVV (6.4)–(6.6) for the *corrected* P₀) |
| §5 small norm | ACCEPT WITH FIX | F3 (state D_∞-conjugated smallness); F8 (S clash) |
| §5 extraction | ACCEPT WITH FIX | F7 (invariance of the a-functional; index convention) |
| Citations (Rule C) | FIX | **F5** |

## What was verified (and holds)

- **§1.**
  - t(X_k) = k, and Res U₁₂ = wU₁₁ with w = N^p t^{−s} (re-derived from U = N^{pNσ₃}Y(·/N^p)).
  - In ℂ₊, arg t = −arg z/p < 0, so Im θ < 0 and |e^{−iθ}| < 1.
  - With R = U[[1, −we^{−iθ}/Π], [0, 1]] above and U[[1, −we^{+iθ}/Π], [0, 1]] below (WLXZ (3.11), Ω_{r,±}), the band
    jump is [[1, 2iθ′w], [0, 1]], i.e. W = 2iθ′w (WLXZ (3.19) "2iγw").
  - The saturated form R = UΠ^{−σ₃}[[1, 0], [−e^{∓iθ}/(Πw), 1]] gives the real-axis jump [[1, 0], [2iθ′/w, 1]]
    (WLXZ (3.19), (2, k_n)). Both are pole-free (WLXZ (3.13), (3.16)).
  - Lemma 1.1 is correct, including the failure at p < 1.
- **Lemma 1.2.** |W| = (2π/p)N^{1+p−s}x^{(s−1−p)/p} and arg W = −π/2 were re-derived.
- **§2.**
  - g₊ − g₋ = 2πiμ*((x, ∞)) = 2iθ/N on (4c, ∞), so φ̃ = φ ± iθ/N is jump-free there (the corrected sign).
  - Re g′ = ∫_{t_x}^1 dτ/√(x(x − β_τ)) > 0 settles strictness.
  - ∂_y Re φ = −πψ and ∂_y Re φ̃ = π(ρ − ψ), from θ′/N = −πρ.
  - Near 0, Re φ < 0 everywhere off the band, because U*(z) > U*(0) for z ∉ [0, ∞) near 0. This fact matters for F1.
- **Lemma 3.1 / 3.2.**
  - S₊/S₋ = exp(−iℓ̂) = D₋/D₊, by Plemelj on (−∞, 0) oriented left to right.
  - At ∞, ∫ℓ̂(y)[1/(y − z) − 1/(y − 1)]dy ~ ℓ̂(−∞)log(−z). So S ~ (−z)^{−ℓ̂(−∞)/(2π)} = (−z)^{½ − 1/(2p)}. **The sign
    is right.**
  - (D̃S)₊/(D̃S)₋ = (1 − e^{−2iθ₊})/(1 − e^{2iθ₋}). Since θ₋ = conj θ₊ on (−∞, 0), this has modulus 1 and phase
    O(e^{−2πN sin(π/p)|x|^{−1/p}}). So Lemma 3.2(v) holds on (−δ, 0). (Far out it is O(1), as check 3a shows for
    p = 1.5 and 3; the text restricts to (−δ, 0), correctly.)
  - S/S(1) = 1 + O(1/N): ℓ̂(y) = Λ(y/N^p) with Λ(u) = O(|u|^{1/p}). Substituting gives O(N^{−p}·N^{p−1}) = O(1/N).
- **w₀ and N.**
  - w₀ = W/F̃² = W(4c − x)/(D̃S)², with constant phase −i, since D̃ and S are positive on (0, ∞). This matches WLXZ
    (5.4) on (0, 2), [[0, w₀/D̃²], [−D̃²/w₀, 0]] with w₀^{WLXZ} = 2iγw/E².
  - N₀ with a = ((z − 4c)/z)^{1/4} gives (N₁)₁₂(N₁)₂₁ = c² and a(N₀) = (N₂)₁₂/(N₁)₁₂ − (N₁)₂₂ = 2c (expanded by
    hand: (a − a^{−1})/(2i) = ic/z + 2ic²/z² + …).
- **Lemma 4.1.** f = (φ ± iπ)²/4 is analytic at 0, negative on the band and positive on (−δ, 0); f/z → −1/π² (check
  [1]).
- **Lemma 4.3.**
  - The lips are the preimages of arg ζ = ∓2π/3 under ζ ≈ −N²κz, i.e. arg z = ±π/3.
  - |e^{−2iθ}| = exp(−2πN|z|^{−1/p}sin(arg z/p)), and Re(iθ/N) = π|z|^{−1/p}sin(arg z/p) > 0 for arg z ∈ (0, π].
  - On (−δ, 0) the amplification is e^{2N|Re φ|} ≤ e^{CN|x|^{1/2}}, beaten by e^{−cN|x|^{−1/p}}.
  - The exponents are right. They apply verbatim to the corrected P₀ of F1, whose growth bounds are the same
    (σ₃-conjugation preserves entry sizes).
- **Top end.** Re φ̃ = log c + p − U*(x) ≤ −½log x for x ≥ x₀ (U* = log x + o(1)). At the closing segment
  Re z = N^p + δ′, t ≈ 1 − δ′/(pN^p), so 1 − e^{−2iθ} ≍ δ′N^{−p} and D = O(N^p). Everything is poly(N)·N^{−pN}.
- **Extraction indices.**
  - (U₁)₁₂(U₁)₂₁ = N^{2p}(Y₁)₁₂(Y₁)₂₁ = N^{2p}h_N/h_{N−1}, and the formula a(Y) = (Y₂)₁₂/(Y₁)₁₂ − (Y₁)₂₂ returns the
    diagonal coefficient a_N of xπ_N = π_{N+1} + a_Nπ_N + b_N²π_{N−1}. Both were re-derived from the moment expansion:
    (Y₂)₁₂/(Y₁)₁₂ = a_N + Σ_{k<N}a_k and (Y₁)₂₂ = Σ_{k<N}a_k.
  - This is the toolkit convention: `reference._fold` returns b² 1-indexed, b_j² = h_j/h_{j−1}.
  - The probe gives N^p√(h_N/h_{N−1})/c = 0.9091, 0.9524, 0.9756 at N = 10, 20, 40 (p = 2, s = 3), i.e. 1 − (s−1)/(2N)
    as in Phase 0's d₁.

## Probe results

### P1. End-to-end: the true V against the global parametrix (`probe_e2e.py`)

**Construction.**
- U is built from the OPs of σ_{p,s}. The atoms k ≤ K = 4N are exact. The tail k > K is replaced by an (N + 12)-point
  Gauss rule, built by the Chebyshev algorithm from the exact tail moments ζ(s + pj, K + 1) at ≥ 200 digits. This
  reproduces the OPs exactly through degree N + 11, and the Cauchy transforms at |z| ≥ 0.5 to spectral accuracy, since
  the tail sits in [0, 1/16] in z-units. A plain K-truncation is **not** adequate at N = 40: the relative perturbation
  is ≈ N^4/(4cK²) ≈ 0.1 at K = 3000.
- Then

    V := F_∞^{−σ₃} e^{−Nlσ₃/2} U e^{Nφσ₃} F^{σ₃},

  with:
  - F = D·S·(4c − z)^{−1/2}, D = D̃/(1 − e^{∓2iθ}) and S as in Lemma 3.2;
  - φ = l/2 − g, g by the τ-integral, l = 2(log c + p);
  - F_∞ := lim F e^{−N(g − log z)}, which agrees in two directions to 10^{−9} at |z| = 10⁹. That confirms the 1/z
    rate of F3. F alone converges only like |z|^{−1/p}.
- N = D_∞^{σ₃}N₀D_w^{−σ₃}, with D_w the Szegő function of w₀ = W(4c − x)/(D̃S)².
- Reported: max-entry |D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}|. All points are in Ω_∞ outside the discs, including one on the
  negative axis (−1.5 + i0), where V's lack of a jump depends on S.
- |det V − 1| ≤ 4e−31 everywhere.

| (p, s), α_x | z | N=10 | N=20 | N=40 | N·err at 40 |
|---|---|---|---|---|---|
| (2, 3), 0 | 1.2+1.0i | 0.0682 | 0.0340 | 0.0170 | 0.68 |
| | −1.5+i0 | 0.0443 | 0.0234 | 0.0120 | 0.48 |
| | 0+2.5i | 0.0354 | 0.0186 | 0.0096 | 0.38 |
| | 4.5+1.5i (above saturated) | 0.0466 | 0.0258 | 0.0137 | 0.55 |
| | 3.0−1.2i | 0.0885 | 0.0494 | 0.0261 | 1.04 |
| | 15+8i | 0.0082 | 0.0044 | 0.0023 | 0.09 |
| (1.5, 3), 1/3 | 1.2+1.0i | 0.0720 | — | 0.0185 | 0.74 |
| | −1.5+i0 | 0.0384 | — | 0.0104 | 0.42 |
| | 3.0−1.2i | 0.0749 | — | 0.0219 | 0.88 |
| (3, 2.5), −1/2 | 1.2+1.0i | 0.0554 | 0.0271 | 0.0134 | 0.53 |
| | −1.5+i0 | 0.0322 | 0.0165 | 0.0083 | 0.33 |
| | 3.0−1.2i | 0.0955 | 0.0536 | 0.0281 | 1.12 |

(Each run covers 9 points; all scale the same way.)

**Conclusion.**
- N·err is stable across N = 10, 20, 40 at every point, for even p, non-even p, α_x > 0, α_x = 0 and α_x = −½.
- This verifies, as a package:
  - l = 2(log c + p) (an error in l would show as e^{NΔ} growth of the off-diagonal entries);
  - the one-sided D;
  - S, including the absence of a jump on (−∞, 0);
  - E = (4c − z)^{−1/2};
  - w₀;
  - the Jacobi-type N with Szegő conjugation.
- The old p = 2 failure mode (an O(1) or N^{−1/2} mismatch) is absent.
- Not tested: points inside the discs and the lens. Those are F1's job.

### P2. Hard-edge parametrix (`probe_bessel.py`, p = 2, s = 3, α_x = 0, δ = 0.4)

**[A] Band jump of E_N.** Using N₊ = N₋[[0, w₀], [−1/w₀, 0]] and W² = w₀, we get
E₋^{−1}E₊ = f₋^{−σ₃/4}M^{−1}[[0, 1], [−1, 0]]M f₊^{σ₃/4}, with f± computed from g at x = 0.05 and 0.2:
- the doc's M = [[1, −i], [−i, 1]]/√2 (KMVV (6.31)) gives **E₋^{−1}E₊ = −I**;
- KMVV (6.53)'s M = [[1, i], [i, 1]]/√2 gives E₋^{−1}E₊ = I.

**[B] Matching** on |z| = 0.4, outside the lens. Entries are max |D_∞^{−σ₃}(P N^{−1} − I)D_∞^{σ₃}|.

| N | arg z | doc: E_N(M₋)Ψ W^{−σ₃}e^{−Nφσ₃} | corrected: (−1)^N Ẽ_N(M₊)·σ₃Ψσ₃·W^{−σ₃}e^{+Nφσ₃} |
|---|---|---|---|
| 20 | ±π/2 | 1.1e5 | 0.049 |
| 20 | ±0.8π | 4.8e6 | 0.065 |
| 40 | ±π/2 | 1.1e10 | 0.025 |
| 40 | ±0.8π | 1.9e13 | 0.034 |

## Findings

**F1 (blocking for the label): the hard-edge parametrix of §4.1 / Lemma 4.2 is KMVV's right-endpoint construction. Our
geometry is KMVV's left endpoint.**

- Here the band (0, δ) lies to the right of the hard edge. Under ζ = N²f ≈ −N²κz the band's orientation is reversed,
  and ℂ₊ maps to the lower ζ-half-plane.
- That is exactly KMVV's endpoint −1. There they write: "the ordering is reversed … f̃(Σ₁ ∩ Ũδ) is part of the ray γ₃",
  and "The reversal of the directions is taken care of by conjugating with the Pauli matrix σ₃. Thus we take
  Ψ̃(ζ) = σ₃Ψ(ζ; α → β)σ₃ (6.51)", together with Ẽ_n(z) = N(z)W̃(z)^{σ₃}(1/√2)[[1, i], [i, 1]]f̃(z)^{σ₃/4}(2πn)^{σ₃/2}
  (6.53).
- The doc uses (6.23)–(6.25) and (6.31) unchanged. It has four concrete defects:
  - **(a)** M = [[1, −i], [−i, 1]]/√2 makes **E_N jump by −I across the band** (P2[A]). Since f₊^{1/4} = −if₋^{1/4}
    here, not +i as in KMVV (6.36), E_N is not analytic, and Lemma 4.2(i) and (iii) are false.
  - **(b)** The exponential factor has the wrong sign.
    - (6.23) and (6.28) use the principal ζ^{1/2}. Since Re φ < 0 on U(0, δ) off the band, the principal root is
      f^{1/2} = −(φ ± iπ)/2, not (φ ± iπ)/2 as in the doc's "e^{2Nf^{1/2}} = ±e^{Nφ} (from f^{1/2} = (φ ± iπ)/2)".
    - So Ψ(N²f) ≈ (…)e^{−Nφσ₃}(−1)^N, and P₀ = …e^{−Nφσ₃} gives P₀N^{−1} ≈ N e^{−2Nφσ₃}N^{−1}. That is exponentially
      large on ∂U(0, δ) (P2[B]: 10⁵ → 10¹³).
    - The analogue of KMVV's ϕ̃^{−nσ₃} is e^{+Nφσ₃}(−1)^{Nσ₃}, because ϕ̃^{−2n} = e^{−4Nf^{1/2}} = e^{2Nφ} matches
      the lip entry e^{2Nφ}.
  - **(c)** The W branch.
    - "z^{α_x} cut along the band [0, δ)" with arg z ∈ (0, 2π) gives W₊W₋ = e^{iπα_x}w₀.
    - KMVV (6.44)–(6.46) use the principal (−1 − z)^β, which gives W̃₊W̃₋ = w. Use (−z)^{α_x} (principal).
  - **(d)** Lemma 4.1 says ζ ↦ "KMVV's orientation after reflection", and CITATIONS says "The reflection z ↦ −z is
    absorbed in f (f′(0) < 0)". Both are false: the reflection is absorbed only by the σ₃-conjugation (6.51) and the
    changed constant matrix (6.53).
- **Fix** (verified by P2: matching 0.049 → 0.025 as N doubles, and the band jump is I):

    P₀ := (−1)^N Ẽ_N(z) σ₃Ψ(N²f(z))σ₃ W̃(z)^{−σ₃} e^{+Nφ(z)σ₃},
    Ẽ_N := N W̃^{σ₃}(1/√2)[[1, i], [i, 1]] f^{σ₃/4}(2πN)^{σ₃/2},
    W̃ := (C_N(−z)^{α_x}(4c − z)h_N)^{1/2},

  with f^{1/4} principal and Bessel order α_x.
  - Cite KMVV (6.42)–(6.53) and Lemma 6.6, not (6.27) and (6.31).
  - Re-derive Lemma 4.2(i), the analogue of (6.35)–(6.36) with f₊^{1/4} = −if₋^{1/4}, in writing.
  - Re-run P2 (or add it as checks/check_px_bessel.py, including a check of the lens-sector formulas (6.24)–(6.25)
    after σ₃-conjugation, which P2 did not sample).
- Lemma 4.3 and the identification are unaffected in substance: σ₃-conjugation preserves KMVV (6.4)–(6.6) entry by
  entry.

**F2 (important): the saturated-region bookkeeping (Ω^△) is wrong as stated, and §3 contradicts §4.2.**

- §3 sets F = DSE "in Ω_∞ and the saturated regions". Lemma 3.3(ii) says F₊/F₋ = e^{2iθ} "removes T's jump
  diag(e^{−2iθ}, e^{2iθ}) on the saturated region".
- With R = UΠ^{−σ₃}L in Ω^△ (WLXZ (3.10)/(3.15), as in §1), this fails under both readings:
  - **Q = T.** The factor Π^{−1}D = θ′D̃/(sin θ(1 − e^{∓2iθ})) has double poles at the saturated nodes, so V is not
    bounded there.
  - **Q with WLXZ (4.12)–(4.13)'s V^△.** Using D (not D̃) leaves a diagonal jump −diag(e^{2iθ}, e^{−2iθ}) on (4c, N^p).
- What WLXZ actually do: (5.1) uses D̃^{σ₃} (with E) in Ω^△_{r,±}. V^△₊ = diag(e^{iθ}/(2iγ), 2iγe^{−iθ}) removes
  e^{∓2iθ}, and E's −1 matches the sign of −V^△₋. The identity Π^{−σ₃}V^△₊ = (1 − e^{−2iθ})^{−σ₃} = (D/D̃)^{σ₃} is why
  "relative to U" the effective factor looks like DSE. The text conflates these two.
- §4.2 already uses D̃²e^{2Nφ̃}/w̃ on (4c, 4c + ε), i.e. D̃.
- **Fix:**
  - Q := T × (WLXZ (4.12)–(4.13) with γ ↦ θ′).
  - V := F_∞^{−σ₃}Q·{F^{σ₃} in Ω_∞; F̃^{σ₃} = (D̃SE)^{σ₃} in Ω_{r,±} ∪ Ω^△_{±}}.
  - Lemma 3.3(ii): F's jump e^{2iθ} cancels T's diagonal jump only on (N^p + δ′, ∞). On (4c, N^p) the diagonal is
    removed by V^△.
  - State the resulting real-axis jump [[1, 0], [(2iθ′/w)D̃²S²e^{2Nφ̃}/(x − 4c), 1]] explicitly.
- The probe used F only in Ω_∞, which is unaffected.

**F3 (important): normalization at ∞ with unbounded supp μ*.**

- g − log z ≍ z^{−1/p}, so T = I + O(N|z|^{−1/p}) and not I + O(1/z). Also V → F_∞^{σ₃} unless it is normalized: the
  doc's V := QF^{σ₃} omits F_∞^{−σ₃}, the analogue of WLXZ's n^{(α−1/2)σ₃}.
- The correct statement, which needs a one-line proof:
  - h := F^{−1}e^{N(g − log z)} has no jump on (N^p + δ′, ∞): both factors jump by e^{2iθ}.
  - It has no jump on (−∞, 0): g and log z both jump by 2πi, and F is jump-free.
  - It is bounded, so it is analytic at ∞ with an integer expansion.
  - Hence V = I + O(1/z). P1 confirms this: F e^{−N(g − log z)} agrees in two directions to 10^{−9} at |z| = 10⁹,
    whereas F alone converges at rate |z|^{−1/2} (check 3b).
- The same lemma is what makes the extraction work, because U z^{−Nσ₃} = const·V·(const·h)^{σ₃}.
- Also state the smallness in the D_∞-conjugated frame: R = D_∞^{σ₃}(I + O(1/N))D_∞^{−σ₃}, with
  D_∞ ∝ N^{(1+p−s)/2}. Otherwise "(R₁)₁₂ = O(1/N)" is not relative to (N₁)₁₂ ∝ D_∞².
- Answer to the brief's question: the unbounded support does **not** affect T → I qualitatively, the jump structure,
  or the extraction, once this lemma is stated.

**F4 (important): Lemma 4.2(iii) misdescribes KMVV's removability, and continuity of h_N is not enough.**

- **(a)** KMVV Prop. 6.5 concludes "Since we already know that E_n is analytic in a punctured neighborhood of 1, the
  isolated singularity at 1 is removable". Removability needs analyticity in the punctured disc plus the
  O(|z|^{−1/2}) bound, not only "W/D bounded". Here E_N has the (h2) jump on (−δ, 0).
- Fix: write E_N = E^a + Φ, where Φ := (1/2πi)∫_{−δ}^0 (E_{N+} − E_{N−})(y)dy/(y − z). Then:
  - the density is E_{N−}(J_E − I) = O(|y|^{−1/2}e^{−cN|y|^{−1/p}}), so Φ is bounded, continuous and O(e^{−c′N});
  - E^a is analytic in the punctured disc and O(|z|^{−1/2}), hence analytic.
  - So E_N is bounded with bounded inverse. P₀ then carries the (h2) jump, which Lemma 4.3 already bounds. Restate
    Lemma 4.2(i) as "the model jumps, up to (h2)".
- **(b)** "W/D_w bounded because h_N is continuous and nonzero at 0" is false in general: Szegő or Cauchy integrals of
  merely continuous densities can be unbounded.
  - h_N is **Hölder-1/p** at 0: ℓ̂ = O(|y|^{1/p}/N), and on the band μ(t) = x^{1/p}/(12N) + …. With a Hölder density,
    the endpoint behaviour of the Cauchy integral (Muskhelishvili, Ch. 4) gives log D_w(z) − ½log h_N(0) − (power
    part) = o(1).
  - State this, cite it (with a Rule C quote), and change "continuous" to "Hölder" in Lemma 3.2(ii) and in CITATIONS
    (KMVV, hypothesis gap).
- KMVV's sharper Lemma 6.4/6.6 is not needed.

**F5 (citation gate, Rule C): verbatim quotes are missing for what RH_px actually uses.**

- **WLXZ.** CITATIONS has only (2.15), (4.16)–(4.17), (5.8), §6.1's opening, and (6.27)–(6.37). RH_px relies on:
  - (3.9)–(3.11) and (3.15) (R in Ω_r and Ω^△);
  - (3.19)–(3.22) (the R jumps);
  - (4.7), (4.10)–(4.13) (T's jumps, the factorization, V^△);
  - (5.1)–(5.4), (5.7), (5.9)–(5.11) (V, its jumps, the global N at α = 1);
  - the §6.1 content (6.4)–(6.21) used in §4.2.

  I read these in 1410.3948.txt and they say what F2 and the doc need. Add them.
- **KMVV.**
  - Add (6.42)–(6.53) (required by the F1 fix), including the two sentences quoted in F1.
  - Add Prop. 6.5's removability sentence verbatim. The current CITATIONS quote is spliced with "…" and omits "Since
    we already know that E_n is analytic in a punctured neighborhood of 1".
  - The paraphrase "This uses only that W/D is bounded" is an interpretation, not a quote. Mark it as such or delete it.
- **Muskhelishvili** (or Gakhov) for F4(b).
- **G2 PROOF.md.** μ*, B*(ii), and dμ*/dρ = I_{x/4c}(1/p + ½, ½) are cited as REVIEWED. Fine; check 2 confirms them
  numerically.

**F6 (important, local): §4.3 top end.**

- (i) "The precise entry list of the segment jumps, the WLXZ (3.22) analogue, is in §1." §1 contains no such list.
- (ii) WLXZ (3.22) is the jump on the vertical segments ±2 ± i(0, δ) at the **band–saturated junction**, i.e. at 4c
  here (relevant to §4.2), not at the top. The top closing piece belongs to Σ^△, with J_R = U^△^{±1} by WLXZ
  (3.20)–(3.21). After Q and V it is the lower-triangular Σ^△ entry of WLXZ (5.4).
- **Fix:** write J_V on Σ^△ and on the segment N^p + δ′ + i(0, ±δ) as I + (F F̃/W)e^{2Nφ}e₂₁ (or as derived), with
  - |D| ≤ C N^p/δ′, from 1 − e^{−2iθ} ≍ δ′/(pN^p);
  - |e^{2Nφ}| = |e^{2Nφ̃}||e^{∓2iθ}| ≤ e^{2N Re φ̃}e^{2|Im θ|}.

  This yields poly(N)·N^{−pN}. Also list the 4c ± i(0, δ) segments (upper-triangular, w̃e^{−2Nφ̃}/D̃²), with
  Re φ̃ > 0 on them (φ̃ ≈ −κ̃(iy)^{3/2}).
- Reliance (c) is then closed.

**F7 (minor): extraction.**

- State the invariance lemma. For constant diagonal C and scalar k(z) = k_∞(1 + k₁/z + …) analytic at ∞, the
  functionals (Y₁)₁₂(Y₁)₂₁ and (Y₂)₁₂/(Y₁)₁₂ − (Y₁)₂₂ are unchanged under Y ↦ C Y k^{σ₃}. (Check: the 12-entries
  pick up −k₁(Y₁)₁₂ and (Y₁)₂₂ picks up −k₁; these cancel.)
- Then a(U) = a(V) = a(RN) = a(N₀) + O(1/N) = 2c + O(1/N), using R₂ = O(1/N) in the D_∞-frame (the top-end pieces have
  |s| ≍ N^p but carry N^{−pN}).
- Write the convention: b_N² = h_N/h_{N−1}, and a_N is the coefficient in xπ_N = π_{N+1} + a_Nπ_N + b_N²π_{N−1} (the
  toolkit `_fold` convention). The O(1/N) claim is insensitive to N ↔ N − 1.

**F8 (minor): notation.**
- S denotes both the Binet-cut scalar (§3) and the small-norm matrix (§5, "So S = I + O(1/N)").
- E denotes both (4c − z)^{−1/2} and E_N.
- Rename one of each.
- The status line repeats "Not reviewed. No PROVED labels" twice.

**F9 (minor): (Y4)_x lens sectors.**
- "Use the K± representation of RH₁(r) §6(b)": that representation had nodes on both sides and a negative-node sum.
- Here nodes accumulate at 0 from the right only, the left half-plane is node-free, and the oscillatory factors are
  e^{∓iθ} with θ = πNz^{−1/p}.
- Rewrite the representation with:
  - the switch on the lower ray;
  - the η_j-arc residue bookkeeping (REVIEW_RH1r R3(i)), with arcs contributing O(η_j^{1+α_x}) → 0 since α_x > −1;
  - the strip δ₀ ≤ |arg z| < π/3 (R3(ii)).
- The sum estimate itself is correct: O(1 + |z|^{α_x}), with a log at α_x = 0.

**F10 (minor): Lemma 4.3 and §5 wording.**
- "Lips leave 0 at the angles ±π/3, by Lemma 4.1" holds to leading order. With the F1 convention the upper lip maps to
  γ₃ (KMVV: "f̃(Σ₁ ∩ Ũδ) is part of the ray γ₃"). Say so.
- In the identification, the bounds O1 and X must be quoted for the corrected P₀ via KMVV's P̃ behaviour ("For β > 0 …
  O(1, 1) outside the lens, O(|z + 1|^{−β}, 1) inside").

## Status of REVIEW_RH.md's missing steps 1–9

| # | Status |
|---|---|
| 1 behaviour at 0 / uniqueness | addressed by (Y4)_x and the transfer of O1/X; complete after F1, F4, F9 |
| 2 two-sided D/E, test A's N^{−1} | **resolved** by the one-sided x-variable; P1 confirms O(1/N) with the predicted normalization |
| 3 θ branch | **resolved** (principal t on ℂ ∖ (−∞, 0]) |
| 4 Re φ̃ > 0 on band lips | **resolved** (Lemma 2.2, check 2) |
| 5 origin perturbation | Lemma 4.3 is correct in substance; it needs the corrected P₀ (F1) |
| 6 Airy discs | §4.2 is acceptable mod-cite (F5); E's singularity matches WLXZ (5.7) at α = 1 |
| 7 top end | partially; F6 |
| 8 extraction | **resolved** up to F7; the values c² and 2c were re-derived |
| 9 p = 1 runs | not applicable |

## Recommended label

- **Now:** PROOF SKETCH (strong), NUMERICALLY VALIDATED END TO END (P1) — not PROVED. Lemma 4.2 as written is false
  (F1, demonstrated).
- **After F1–F6 are fixed and re-checked:** PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6 incl. (6.42)–(6.53);
  Muskhelishvili for the Hölder endpoint Szegő bound; G2 PROOF.md μ*, B*), REVIEWED.
  - F1 and F2 need a re-check by a second reader. I recommend committing P2 as a check, with lens-sector points added.
  - F3–F7 can be verified by the coordinator against the text above.
- The theorem statement (n^p b_n = c(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n), for all p > 1 and s > 1) is supported
  by P1 at three (p, s) pairs spanning α_x ∈ {−½, 0, ⅓}.

## Fixes applied (author, 2026-10-13) — re-check of F1 and F2 pending

- **F1:** §4.1 is rewritten as KMVV's left-endpoint construction (6.42)–(6.53):
  - P₀ = (−1)^N Ẽ_N σ₃Ψσ₃ W̃^{−σ₃}e^{+Nφσ₃}, with Ẽ_N built on [[1, i], [i, 1]];
  - W̃ uses the principal (−z)^{α_x}, and f^{1/2} = −(φ ± iπ)/2;
  - the band jump of Ẽ_N is written out (M^{−1}J₀M = diag(i, −i) and f₊^{σ₃/4} = diag(−i, i)f₋^{σ₃/4});
  - the reflection claim is removed from Lemma 4.1 and from CITATIONS;
  - P2 is committed as `checks/check_px_bessel.py`, with Hankel-sector lens points added. Inside the lens the matching
    is 0.0290 → 0.0142 for N = 20 → 40.
- **F2:** F̃ = D̃BK is used in the band lens and in Ω^△. Q carries WLXZ's V^△. F's jump is used only beyond N^p + δ′.
  The (4c, N^p) jump entry is stated explicitly.
- **F3:** Lemma 3.5 (κ = F^{−1}e^{N(g − log z)} is analytic at ∞), with C_∞ normalization; smallness is stated in the
  D_{w,∞} frame.
- **F4:** (a) Lemma 4.2(iii) splits off a Cauchy integral of the super-small jump. (b) Lemma 3.4 is a self-contained
  Hölder endpoint bound, used in place of a Muskhelishvili citation; B and h_N are Hölder-ν at 0.
- **F5:** CITATIONS adds the WLXZ quotes ((3.10)–(3.15), (4.1), (4.4), (4.10), (4.12)–(4.13), (5.1), (5.7), (5.9),
  (6.4), (6.5), (6.10)–(6.12)), KMVV (6.42)–(6.53), and Prop. 6.5's sentence verbatim. The paraphrase is marked as ours.
- **F6:** §4.3 writes out the top-end entries and bounds, and corrects the cross-reference about (3.22).
- **F7:** the invariance lemma and the index convention.
- **F8:** renames S → B, E → K, small-norm → 𝒵.
- **F9:** the one-sided (Y4)_x lens representation, with η_j-arcs.
- **F10:** the upper lip maps to γ₃; P̃'s behaviour is quoted.
- **Probe P1** is committed as `checks/check_px_e2e.py` with its three outputs.
