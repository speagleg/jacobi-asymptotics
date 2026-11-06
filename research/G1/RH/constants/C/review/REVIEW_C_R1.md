# Rule R review of C/C.md (Conjecture C, the constant 2π/p in h_n): reader R1

Reviewer: independent second agent (Rule R), 2026-11-05, branch `g1-constants`. I read the note and then the Paper II
sources (sec2_prelim §tool-wlxz(a), §tool-dlmf; sec4_frame in full; sec5_outer: lem:outer, Szegő functions,
lem:szego, lem:normalisation, prop:frame; sec6 prop:moments; sec7 thm:window; appA lem:binetcut; appB
prop:apriori(ii)) and Paper III sec6 (lem:telescope, thm:UFlim, eq:Sp). I re-derived every step below myself.
Independent numerics: `review/checks/hn_independent.py` (no code shared with `C/checks/`).

## Verdicts

| Step | Verdict |
|---|---|
| Theorem 1, Steps 1–6 and (1.2) → (1.1) | OK |
| Lemma 2 (a), (b), (d), (e) | OK |
| Lemma 2 (c) | OK for p > 1 and p < 1; FIXABLE GAP for p = 1 (F1) |
| Lemma 2, node at 4c (parenthetical in (a)) | OK, wording could be fuller (F3) |
| Lemma 3 | OK |
| Lemma 4 | OK |
| §5 (Stirling, R_n → 1, extension to all s > 1 through lem:telescope) | OK |
| Node at 4c in Paper II's frame (§8 item 4) | not a gap; a remark in Paper II would help (F4) |
| Rule C bookkeeping | FIXABLE (F2) |

## Re-derivations

**Theorem 1.** Step 1: (Y₁)₁₂ = h_n is proved in Paper II §tool-wlxz(a) (expand Y₁₂ = Σ w_k P_n(x_k)/(z − x_k), then
right-multiply by z^{−nσ₃}). Step 2: U_j = n^{jp} n^{pnσ₃} Y_j n^{−pnσ₃} (proof of lem:interp), so
(U₁)₁₂ = n^{p(2n+1)} h_n. Step 3: from eq:Q-at-infinity, Q₁₂ = k_∞^{−1}(Uz^{−nσ₃})₁₂ k^{−1}, so
(Q₁)₁₂ = k_∞^{−2}(U₁)₁₂. Step 4: k_∞ = e^{nγ_p}D_∞/𝗁_∞(∞), with F(∞) := 1/𝗁_∞(∞) (by lem:gfunction(ii)).
Step 5: from eq:szego, |D_∞|² = exp⟨Re log W₀⟩ = exp⟨log|W₀|⟩ whatever branch of log ŵ_n is taken, and
⟨log x⟩ = ⟨log(4c − x)⟩ = log c. Step 6: prop:moments gives Q₁ = P₁ + O(1/n) entrywise, with constants depending
on (p, s, ℓ). Its hypotheses are those of thm:window (p > 0, |α| < 1, ℓ analytic of angle ϑ > 0), which are the
note's, and (P₁)₁₂ = ic is computed in sec7. An absolute O(1/n) on (Q₁)₁₂ is all that is needed, since c is fixed.
h_n > 0, so taking moduli throughout is legitimate and loses nothing. I redid the algebra (1.2) → (1.1) → (C):
e^{2nγ_p} = c^{2n}e^{2np}, Γ(n+1)^{2p} = n^{2pn}e^{−2pn}(2πn)^p(1 + O(1/n)), and c^{α+1}n^{1−s} = (c^{1/p}/n)^{s−1}. All
the exponents match.

**Lemma 2.**
- (a) The jumps of F e^{−ng} cancel on (−∞,0) (n ∈ ℕ) and on (4c,∞) off the nodes. At a saturated node, |υ_±| ≍ |z − X_k|^{−1}
  and F̃ is bounded and bounded away from 0, so F has a pole of exact order 1 (from both sides). Π cancels it, and A(X_k) ≠ 0.
  The behaviour at ∞ follows from lem:normalisation. Ω = Ĉ∖[0,4c] is simply connected, so L = log A exists.
- (b) The map J(w) = c(w + 2 + 1/w) is correct. I checked the Parseval constant π Σ|a_k|² r^{−2k} and that the
  substitution x = 4c cos²(ψ/2) gives dx/√(x(4c−x)) = dψ.
- (c) I checked each logarithm separately. Im g ∈ (0,π). |e^{−2iθ}| < 1 on all of ℂ₊ for p ≥ 1 (eq:imtheta), and on
  S_in ∩ ℂ₊ for p < 1, so |arg(1 − e^{−2iθ})| < π/2. For p > 1, |arg t| ≤ π/p < π and j is bounded for large |t|
  (eq:binet-bound). log B is bounded up to the cut near 0 for fixed n (lem:binetcut(iii)). For p < 1 the outer sector uses
  B_out K e^χ, and no υ appears there. **F1** concerns p = 1 (below).
- (d) The truncation argument is a correct Vitali argument: ∫_{|u_r|>K}|u_r| ≤ 𝔐²/K, and T_K u_r → T_K u a.e. and
  boundedly. I tried to break it. Pointwise domination indeed fails, because the radial curves pass close to the band nodes,
  but the proof does not use it. The exceptional set (preimages of 0, 4c and the band nodes) is countable. The poles of F_±
  at the band nodes become the log-singularities of log|2 sin θ| and are in L². I found no gap.
- (e) For X > 4c, ⟨log|x − X|⟩ = log(Υ(X)/4) (proof of lem:gfunction(iii)), and 2 log(Υ/(4c)) = 4 arccosh√(X/4c).
  Redoing the arithmetic gives (2.1).

**Lemma 3.** I checked every step:
- ∫f = 2p, via (κ₀/2)B(1/p,½) = p/2 with I(p) = (√π/2)Γ(1/p+½)/Γ(1/p+1) (Paper II sec1) and κ₀ = 2I/π.
- f_r(0⁺) = 4 log 2 + 2p log κ₀, and f_r′ ∈ L¹.
- The Euler–Maclaurin form Σ_{k=1}^N G(k) = ∫₀^N G + ½(G(N) − G(0)) + ∫P₁G′, and Riemann–Lebesgue on [0,κ₀] minus a
  vanishing piece.
- n∫_{N/n}^{κ₀}f_r = ρ f_r(κ₀) + o(1), uniformly in ρ ∈ (0,1].
- Stirling for N!, and the cancellation of the ρ terms.

The factor (2πn)^{−p} comes from −2p·½ log(2πN) with N ≈ κ₀n; the κ₀^{−p} = 4c that comes with it combines with
−2 log 2 to give log c. The o(1) is pointwise in n, which is all (C) needs.

**Lemma 4.** The density ρ(τ) checks out. λ ∈ L⁴, ρ ∈ L^{4/3}_loc, and the tail series Σ m^{−1−p/2} converges. Whole periods
of λ integrate to 0. The proof takes separate limits S_n − (2np + log c − p log 2πn) → 0 and M_n → 0. It does **not** use the
O(n^{−1/2}) cancellation, which appears only as a numerical remark. Correct.

**Extension to all s > 1.** lem:telescope (Paper III sec6) is stated pointwise for all s₀, s₁ > 1 for σ_{p,s} (ℓ ≡ 1), all
p > 0. Its proof uses thm:UFlim on {t₀,t₁} ⊂ (1,1+p] ⊂ S_p (eq:Sp: S_p ⊇ (1,1+2p) for every p) and the product identity.
The ratio it gives, c^{(s₁−s₀)/p}n^{−(s₁−s₀)}, is that of (C). (C_ℓ) is correctly claimed only on the window. R_n → 1
follows from lem:pottersector(iii).

## Findings

**F1 (FIXABLE, Lemma 2(c), p = 1).** The note says that "−j(t) is continuous and bounded on {|arg t| ≤ π/p, |t| ≥ …}
(… for p = 1 … j → 0)". For p = 1 this set reaches arg t = ±π. Approaching the negative t-axis, LnΓ has its poles at
t = −k, that is at z = −n/k, and these points accumulate at 0 inside the image region. So j is not bounded there. The
conclusion still holds:
- near the band, use F = υ₊D̃K with |arg t| ≤ π − η;
- near the negative axis, use F = DK = e^{j(−n/z)}K (eq:reflection), with |arg(−n/z)| ≤ π − η;
- Im log υ₊ is bounded on all of ℂ₊.

Two overlapping sectors cover the region, and the logarithms differ by constants. The fix is one sentence.

**F2 (FIXABLE, Rule C).** There is no CITATIONS entry for C. DLMF 5.11.1 + §5.11(ii) is used for log N! and log Γ(n+1)
(Lemma 3(iv), §5); DLMF 5.12.1/5.5.1 (Beta–Gamma) is used in Lemma 3(i). All three are already quoted in
research/G1/RH/CITATIONS.md, entries (DLMF) and (DLMF-2). Add "Also used in: C/C.md" lines there, and list 5.12.1/5.5.1
among the note's inputs.

**F3 (wording).** For a node at 4c, A ~ (z − 4c)^{−3/2} near the boundary point 4c. The note should say that Im L stays
bounded there and that log|A| has only a logarithmic singularity, so (c)–(d) are unaffected. This is true; it is just
not written.

**F4 (§8 item 4: node at 4c in Paper II).** This is not a gap.
- The pole removal (Step 1 of §frame-transf) is local and meromorphic. U L_± and U A^△_±υ_±^{σ₃} are each regular at X_k
  in a full disc, so they are regular at a node on the vertex 4c too.
- Since ε < 𝖧₀, 𝔻(4c,ε) contains no part of Ω_∞. V there involves only R and F̃, and the jumps of V on the band, on the
  saturated segment and on Σ_v (lem:jumpsV(a),(c),(d)) contain no υ.
- prop:apriori(ii) (appB) covers the cancellation in the same words.

So the Airy analysis is unaffected. Severity: cosmetic. Recommend a one-line remark in Paper II Step 1 or lem:jumpsV
("a node may coincide with the vertex 4c; nothing changes"). The note's own argument is fine.

## Independent numerics (Rule N: NUMERICAL)

h_n is computed as the pivots of Gaussian elimination on the Hankel matrix of the exact moments ζ(s + pj), at two
precisions. The runs at the larger precision agree with dps1 to all 30 printed digits.

- (p,s) = (2.5, 6) (outside the window, so it also tests telescope): log(h_n/h_n^C) = −0.532, −0.272, −0.138, −0.0693
  at n = 8, 16, 32, 64. n·log → −4.43, so the error is O(1/n).
- (p,s) = (0.7, 1.6): log(h_n/h_n^C) = −0.0233, −0.0052, +0.0016, +0.00345, +0.00337 at n = 8, 16, 32, 64, 128. This
  is consistent with A n^{−0.7} + B/n, A ≈ 0.26, B ≈ −0.69 (fitted at n = 64, 128). That fit predicts 0.0027 at n = 256. The
  extended run gives 0.00318, 0.00300, 0.00270 at n = 160, 192, 256: past its maximum the ratio is decreasing, as the fit
  predicts. The rate is ≈ n^{−p} for p < 1, as the note reports.

Outputs: `review/checks/hn_p2.5_s6.out`, `hn_p0.7_s1.6.out`, `hn_p0.7_s1.6_N256.out`.

## Recommendation

Apply F1–F3, which are a few sentences and citation bookkeeping, and optionally F4 in Paper II. Then the label is
**PROVED-mod-cite (Paper II thm:window/prop:moments/prop:frame/lem:outer/lem:binetcut/lem:seam/lem:corner/
lem:pottersector; Paper III lem:telescope; DLMF 5.11.1, 5.12.1, 5.5.1) + REVIEWED**. Novelty stays UNCHECKED, since
Rule L has not been done.
