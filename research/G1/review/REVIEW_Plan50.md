# Rule R review: Plan 50 (Route II for p = 1, WP5a): Theorem RII₁, Corollaries B_{p=1}, B_{p=1}⁺, B_{p>1}⁺, Lemmas CT, D

Reviewer: independent second reader (Rule R). Branch `plan-50-r2p1`, commit c513363 (`git diff master...HEAD`).
Targets: `research/G1/RH/route2/ROUTE2_p1.md`; PROOF.md §3.19 and §0 row "RII₁ / B_{p=1} / CT"; LOG.md Plan 50 entry;
RH/CITATIONS.md (KV and Van additions, DLMF-5); `RH/route2/checks/check_r2p1_{lw1,coeff,ct}.py/.out`; plan doc
`docs/superpowers/plans/2026-10-14-plan-50-r2p1.md`.
Compared against: RH/RH_p1_general.md (RH₁(r), REVIEWED), RH/route2/ROUTE2.md and review/REVIEW_Plan48.md (UR′(b′)),
RH/zeta/RH_zeta_close.md §1 (Lemma W, Lemma UR), and **master's PROOF.md §3.21 and §0 row "SH / B_all" (Plan 52, REVIEWED)**.
This branch was cut before Plan 52 was merged.

## Verdicts

| Claim | Verdict | Recommended label |
|---|---|---|
| §1 RedA at p = 1 (open strip \|Im u\| < π) | **ACCEPT** | PROVED (ROUTE2 §1, REVIEWED); p = 1 check correct |
| Lemma H1₁ (W̃ := W·D_ϱ; Ẽ_n = const·E^{KV}) | **ACCEPT WITH FIXES** (F4, a constant in the Airy discs of §3.4) | PROVED-mod-cite |
| Lemma LF₁ (Ψ_a = Ψ̂ζ^{aσ₃}S_j, det Ψ̂ = 1) | **ACCEPT** | PROVED-mod-cite |
| Lemma LW1₁ (even pairing) | **ACCEPT** | PROVED-mod-cite (DLMF 5.11 for H_n); NEW |
| UR₁ (incl. (b′)), Q ∈ I + ∂C(L²), C₁, D₁ | **ACCEPT** | PROVED-mod-cite |
| **Theorem RII₁** (p = 1, 1 < r < 2, O(1/n)) | **ACCEPT WITH FIXES** (F4, F7) | PROVED-mod-cite; REVIEWED after the fixes |
| **Corollary B_{p=1}** | **ACCEPT** | PROVED-mod-cite; REVIEWED |
| **Lemma CT** (i) and (ii) "⟺" | **ACCEPT WITH FIXES** (F1 merge, F5 hypothesis) | PROVED (self-contained). "⟹" coincides with master's Theorem SH. "⟸" is correct and is new relative to SH |
| Lemma D (a), (b) | **ACCEPT WITH FIXES** (F3: a constant in (b)) | PROVED |
| **Corollary B_{p=1}⁺** (every non-integer r > 1) | **ACCEPT**; strengthen on merge (F2) | PROVED-mod-cite. With master's SH-r it holds **with rate** |
| **Corollary B_{p>1}⁺** (every s > 1, p > 1) | **ACCEPT as correct, but REDUNDANT** (F1) | it is master's Corollary B_all without the rate; replace by a cross-reference |
| GAP-int | **ACCEPT** (genuine within present tools); add the reduction of F6 | GAP |
| GAP-rate₁ | **PARTLY OBSOLETE after merge** (F2) | GAP for the tilt law only |
| OBSTRUCTION-a | **ACCEPT** (scoped to this frame) | OBSTRUCTION (scoped); HEURISTIC remedies as stated |
| Numerics | **ACCEPT** (F7, F8 wording) | NUMERICAL |
| Stop (i) RESOLVED-mod-cite at p = 1 for 1 < r < 2; (ii) MOOT | ACCEPT | as stated |

No counterexample was found. No step is wrong in a way that affects a conclusion. The two MEDIUM findings (F1, F2) concern
consistency with master after Plan 52. Two LOW findings (F3, F4) are slips in constants that need a one-line fix.

## Checks done

### Citations (Rule C), re-verified against the sources

- **KV**, arXiv:math-ph/0305044 (the arXiv PDF, fetched now and run through pdftotext). These match the source verbatim:
  - (3.6), including KV's typo "contination";
  - (5.1)–(5.3), (5.6) and the sentence "Since φ₊ = −φ₋ …";
  - (5.9), with W = z^α for π/2 < |arg f| < π and (−z)^α for 0 < |arg f| < π/2;
  - (5.13) e^{πiασ₃} on Σo3 ∪ Σo7, (5.17)–(5.20), and "Γj = {arg ζ = (j − 1)π/4}";
  - the sentence after (5.25) ("for every matrix valued function En analytic in a neighborhood of Uδ … conditions (a), (b)
    and (d)");
  - (5.26)–(5.30), and p. 19 "E is analytic in a full neighborhood of Uδ. Here we need the fact that D(z)/W(z) and W(z)/D(z)
    remain bounded as z → 0".
  - (5.21)–(5.22) are consistent with LF₁'s |ζ|^{−|a|}.
- **Vanlessen**, arXiv:math/0212014 (the arXiv PDF). These match:
  - (4.20)–(4.23): the same jumps as KV, with λ for α;
  - (4.26)–(4.28): the sector-II matrix quoted in LF₁ is exactly (4.27), including the right factor e^{−½λπiσ₃};
  - (4.43)–(4.46): the quadrant statements, with the factor [[0, −1], [1, 0]] in the lower half-plane;
  - (4.53), and the sketch "det Ψλν ≡ 1" via Liouville.
  - KV's (5.23) equals Vanlessen's (4.26) with λ = α, so the identification Ψ_a(KV) = Ψ_λ(Van) used throughout is right.
- **DLMF-5** (dlmf.nist.gov/10.25 and /10.27, live pages): (10.25.2), (10.27.3) and (10.27.4) are quoted verbatim.

### Lemma LF₁, re-derived

- Substituting 10.27.4 into the second column of (4.27):
  - sin((a ± ½)π) = ±cos aπ;
  - both rows give the same κ = 1/(2cos aπ);
  - the remainder c₂ is as stated.
- Branch of ζ^{1/2}I_ν(ζe^{−πi/2}) = ζ^{ν+½}e^{−iπν/2}(½)^νΣ(−ζ²/4)^k/(k!Γ(ν+k+1)). This is valid exactly when
  arg(ζe^{−πi/2}) ∈ (−π, π] with ζ^ν principal, i.e. arg ζ ∈ (−π/2, π]. That interval contains sector II.
- Ψ̂ is entire (1/Γ is entire) and det S_II = 1, so det Ψ̂ = 1.
- Continuation sector by sector: Ψ̂ζ^{aσ₃} is analytic off Γ₅ and Ψ has constant jumps, so S_j is constant in every sector.
- Rank-one conjugate bound: |ζ|^{−2|a|}. Correct.

### Lemma H1₁, re-derived

- **(i)** P̃^{(∞)}W̃^{σ₃} = 𝔇_∞^{σ₃}σ₃N₀σ₃(W/D_a)^{σ₃} = (𝔇_∞/D_{a,∞})^{σ₃}·P^{(∞)}_{KV}W^{σ₃}. D_ϱ cancels, so KV's
  analyticity argument for E needs only D_a/W bounded (RH₁(r) Lemma G(iv)). This is the key idea, and it is correct.
- **(ii)** Recomputed from the jump P₋^{−1}P₊.
  - Band (1,2) entry: W̃₊W̃₋ = |x|^{2a}·D_{ϱ,+}D_{ϱ,−} = m_σ.
  - Lip (2,1) entry: W̃^{−2}e^{∓2πia}e^{−2nφ} = ω^{−1}D_ϱ^{−2}e^{−2nφ}.
  - iℝ: D_ϱ is analytic across iℝ, so the cancellation of (5.19) against W's cut is unchanged.
  - q_n is never continued across iℝ. This is the real point of the construction.
- **(iii)** The algebra is correct as written.
- **Large-ζ form.**
  - From (5.6) in KV's frame: −nφ = iζ − nφ₊(0) in ℂ₊ and −iζ + nφ₊(0) in ℂ₋.
  - Je^{−iζσ₃} = e^{iζσ₃}J, so Φ = Ψ_ae^{±iζσ₃} = B(I + O(1/ζ))e^{πiσ₃/4}·(D_j or D_jJ). Φ is bounded with bounded inverse.

### LW1₁, re-derived

- The representation (R/π)∫dx/(√(4 − x²)(z − x)) = 1 holds.
- Pairing: 1/(z − x) + 1/(z + x) = 2z/(z² − x²).
- Path bound:
  - along the arc, Im u = −2θ ∈ [−(π/2 + π/12), 0] and Re u ≥ log n − 2 log 2;
  - with u′ = |z|·u, the substituted integral ∫(1 + |log u|)(1 + u)^{−2}du is finite;
  - the far part satisfies |z|log(2/|z|) ≤ C.
- The h_W part agrees with the closed form: D_{h_W}²/h_W = −1/Φ² → 1 at 0 in ℂ₊.
- The H_n part: |ph t| ≤ π/2 + π/12 < 2π/3, so Stirling applies.

### UR₁, C₁, D₁

- **UR₁ (a), (b′).** Checked against REVIEW_Plan48 F1 (re-check), with exponents ±a, |a| < ½ in place of ±α/2.
  - The three-range bound needs exactly |±a| < ½.
  - The far part is O(ε^{2−|a|}), the area estimate O(ε^{3/2−|a|}), and the K-term needs ∫|s|^{−2|a|}|ds| < ∞.
  - Branches in the factorization (nf/z)^a·z^a: both cuts lie on the negative band.
- **UR₁ (d).** Θ is a two-sided bounded multiplier. The large–large block needs no commutator, since Φ^{±1} is bounded. The
  K-term HS bound and the cross blocks were checked.
- **Q at 0.** The (Y4)_r Potter loss and the lens factor give Q = O(|z|^{−|a|−3η}), which is in L²_loc for small η.
- **D₁ main term, worked out by hand.**
  - (v − ṽ)ṽ^{−1} = δ_ne₂e₁ᵀ, because the first row of ṽ^{−1} is e₁ᵀ.
  - Θe₂e₁ᵀΘ^{−1} = θ^{−2}e₂e₁ᵀ with θ^{−2} = e^{±2nφ₊(0)}(W/D_a)².
  - δ_nθ^{−2} = (W²/ω)e^{±2iζ}(D_ϱ²/ϱ − 1), and W²/ω is a constant per sector.
  - Φe₂e₁ᵀΦ^{−1} = e^{∓2iζ}Ψ_ae₂e₁ᵀΨ_a^{−1}.
  - Hence the integrand is c_j(D_ϱ²/ϱ − 1)A₀Ψ_ae₂e₁ᵀΨ_a^{−1}A₀^{−1}, as stated.
  - The integral is (1/n)∫(ρ/n + ε)(1 + ρ^{−2|a|})(…)dρ = O(ε′_n/n).
- **D₁ correction term.** Both factors carry e^{−2|Im ζ|} in full, so the "splitting" is not even needed. It is O(ε′²/n).
- **Extraction.** The 𝔇 conjugation leaves the product of the off-diagonal 1/z-coefficients unchanged. Outside the discs
  Q̃ = 𝒵̃′N₀, so (Q̃₁)₁₂(Q̃₁)₂₁ = 1 + O(1/n). The fold preserves relative O(1/m) errors.
- **Comparison problem.** It has no jump inside U(0, δ): P̃₀ carries the band jump m_σ exactly and V has no jump on iℝ.
  Outside the discs Q̃ has exactly V's jumps. So v − ṽ is supported on the lips in U(0, δ), plus (J2).

### Lemma CT and Lemma D (focus item), re-derived line by line

- **CT(i).**
  - Matrix entries: (LLᵀ)_{nn} = l_n² + m_{n−1}², (LLᵀ)_{n+1,n} = l_nm_n, (LᵀL)_{nn} = l_n² + m_n², (LᵀL)_{n,n+1} = m_nl_{n+1}.
  - From xq = L^{−1}xP = LᵀP: ∫q_nq_m x dμ = δ_{nm}. For m = n the value is l_n·lc(q_n)/lc(p_n) = 1.
  - Positivity: the zeros of p_N lie in the open convex hull of supp μ.
  - Cross-check with master's monic form: g_n = −P_{n+1}(0)/P_n(0) = det J_{n+1}/det J_n = **l_n²**, and h_n = β_n/g_{n−1} =
    **m_{n−1}²**. So master's Lemma CT (§3.21) and this CT(i) are the same identity in different coordinates, and
    x_n = n^pl_n²/c = G_n/c.
- **CT(ii) "⟹".** The recursion x_{n+1} = A_{n+1} − B_n/x_n is checked, with A_{n+1} = (n+1)^pa_{n+1}/c and
  B_n = (n+1)^pn^pb_{n+1}²/c². This is exactly master's Lemma CS together with Theorem SH.
- **CT(ii) "⟸" (stronger than SH; checked carefully).**
  - Given J(xμ), the factorization LᵀL with L positive lower bidiagonal is **not unique**. The free parameter is u_0 = l_0².
    The proof does not need uniqueness: whatever positive factorization J(μ) supplies satisfies 0 < z_n < A′_n (v_n > 0), and
    Lemma D(b) says every such orbit tends to 1.
  - The recursion z_{n+1} = B′_n/(A′_n − z_n) is correct.
  - So are a_n(μ) = u_n + v_{n−1} and b_{n+1}(μ)² = u_nv_n.
  - **Verdict: correct.** The direction is genuinely stronger than SH, and SH's text explicitly does not claim it.
- **Lemma D(a).** Every inequality was checked with δ ≤ ⅕ and ε = δ³/16. Each one holds:
  - x_m ≥ (1 − ε)/(2 + ε) ≥ ⅓;
  - 4ε ≤ δ²/2;
  - x_n ≥ ⅘ ⇒ ε/x ≤ 4ε/3;
  - (x − 1)²/x ≥ δ²/(1 + δ) for x ≥ 1 + δ;
  - g(1 + δ) = 1 + δ/(1 + δ);
  - δ²/(1 + δ) > 3ε.
- **Lemma D(b).** The structure is correct (h(z) − z = (1 − z)²/(2 − z) ≥ 0; the fixed point attracts from below and repels
  from above; the escape above 1.7 contradicts z < A′). The constant 17ε is true, but its displayed justification is not
  (F3).
- **Is positivity enough with no rate?** Yes. In (a), every orbit that dips below 1 − δ decreases by at least δ²/2 per step
  and hits a negative value. Every orbit above 1 + δ is pulled down by at least δ²/4 per step. Neither argument uses a rate on
  A_n − 2 or B_n − 1. If (A, B) admits no positive orbit (e.g. A_n = 2 − 1/log n, B_n = 1), the hypothesis is vacuous.
  Such (A, B) never come from a measure.
- **Adversarial probe** (reviewer script, not committed):
  - Setup: μ = Σk^{−3/2}exp√log(k+e)δ_{1/k} + tail, plus an atom m·μ(ℝ)·δ_{10^{−60}} for m = 0, 1, 100.
  - Result: nb_n/c = 0.9998 and na_n/(2c) = 0.9992 at n = 800 for all three m. The Cholesky factor stays positive, and
    x_n → 1 like 1 − (2.1–2.2)/n for m > 0.
  - Conclusion: the law is insensitive to mass at 0, as CT(ii) "⟸" predicts once its hypothesis is relaxed (F5).

### B_{p=1}⁺ and B_{p>1}⁺ bookkeeping

- r₀ = r − ⌊r⌋ + 1 ∈ (1, 2) for r ∉ ℤ, and ⌊r⌋ − 1 steps reach r.
- For s ≥ 1 + 2p: j = ⌊(s − 1)/p⌋ − 1 ≥ 1 and s₀ ∈ [1 + p, 1 + 2p). Correct.
- The shift identity x_k·k^{−r′}Ψ(k) = k^{−r′−p}Ψ(k) is exact, with the same Ψ.

### GAP-int (focus item)

The gap is **genuine** for the tools available here:
- the shift (CT or SH, step p = 1) preserves r mod 1;
- the base interval (1, 2) is open, and its endpoints are excluded by OBSTRUCTION-a: a = ±½ gives a logarithmic divergence in
  UR₁(a), in Lemma W (A₂ fails at the endpoint) and in D₁;
- a Geronimus step (÷x) moves r down, not up;
- a base at r = 1 exists as a finite measure only when ΣΨ(k)/k < ∞ (e.g. Ψ = exp(−√log k), which has D(γ) = ∞). That is
  a = −½, which is equally obstructed;
- other polynomial Christoffel factors (x + c) do not change r.

See F6 for the reduction the converse gives.

### Numerics (re-run from the jacobi-asymptotics root)

- `check_r2p1_lw1.py` (13 s), `check_r2p1_ct.py` (1 m 20 s) and `check_r2p1_coeff.py` (2 m 22 s) were all re-run. The output
  is **byte-identical** to the committed `.out` files.
- Every number quoted in ROUTE2_p1 §§3.2, 3.3 and 6, PROOF.md §3.19 and LOG.md matches the output, apart from F7.

## Findings

**F1 (MEDIUM: merge consistency, duplicated results, name clash). Location: ROUTE2_p1 §5 (Lemma CT, Lemma D, Corollary
B_{p>1}⁺, "closes Plan 48's GAP-α"); PROOF.md §3.19 and §0 row; LOG.**
- **Issue.** Master now has Plan 52 (§3.21, REVIEWED):
  - master's Lemma CT is the same identity as this CT(i) (g_n = l_n², h_n = m_{n−1}²);
  - master's Lemma CS together with Theorem SH is exactly this CT(ii) "⟹" with Lemma D(a) (G_n = c·x_n);
  - master's Corollary B_all is this Corollary B_{p>1}⁺ **with** an O(1/n) / regular rate (Theorem SH-r).
- **Consequences.**
  - The claim "closes Plan 48's GAP-α for the law" is no longer Plan 50's result.
  - "Lemma CT" names two different statements on the merged master.
- **Fix (on merge).**
  - Rename this lemma (e.g. "Lemma CT⇔" or "Lemma CT₁").
  - Cite master §3.21 (CT, CS, SH) for (i) and "⟹", and keep Lemma D(a) only as an alternative proof, or drop it.
  - State the genuinely new content as **CT(ii) "⟸" with Lemma D(b)**.
  - Replace Corollary B_{p>1}⁺ by "= Corollary B_all (Plan 52, §3.21), proved there with rate". Remove "closes GAP-α" from
    §3.19, the §0 row and the LOG, or reword it as "independently of Plan 52".

**F2 (MEDIUM: GAP-rate₁ and the "no rate" remarks are superseded). Location: ROUTE2_p1 §5 Remarks ("transfers the law only,
not the rate"), Corollary B_{p=1}⁺ ("No rate is claimed for r > 2"), §7 GAP-rate₁; PROOF.md §3.19 "Remaining (GAP)"; §0 row.**
- **Issue.** Master's Theorem SH-r transfers any regular rate r_n under σ ↦ xσ, for any p > 0 (PROVED, REVIEWED). With
  Theorem RII₁ (O(1/n) under (H_an₁)) and Corollary B_{p=1} (O(1/n + ρ(⌈n/M₀⌉))), this gives B_{p=1}⁺ **with** rate:
  - O(1/n) for every non-integer r > 1 when Ψ satisfies (H_an₁);
  - the regular majorant of 1/n + ρ(⌈n/M₀⌉) in sequence form.
- **Fix (on merge).**
  - State B_{p=1}⁺ with that rate, citing SH-r.
  - Reduce GAP-rate₁ to the tilt law (the 1/n coefficient; CONJECTURE, NUMERICAL).
  - Keep "Lemma D gives no rate" only as a remark about this proof.

**F3 (LOW: constant in Lemma D(b)). Location: ROUTE2_p1 §5, proof of Lemma D(b), "> ⅓, so z_n < 1.7 and 2 − z_n > 0.3; then
|z_{n+1} − h(z_n)| ≤ 17ε".**
- **Issue.** |B/(A − z) − 1/(2 − z)| ≤ 3ε/((A − z)(2 − z)). With the displayed lower bounds ⅓ and 0.3, this gives 30ε, not
  17ε. With 30ε the no-dip step (30ε ≤ δ²/4) fails at δ = ⅕; it needs δ ≤ 0.133.
- **Why the conclusion survives.** The constant 17ε is true: z_{n+1} < A_{n+1} gives A_n − z_n > B_n/A_{n+1} ≥
  (1 − ε)/(2 + ε) ≥ 0.499, hence 2 − z_n ≥ 0.498, and the bound is ≤ 12.1ε.
- **Fix.** Replace "> ⅓ … > 0.3" by "A_n − z_n ≥ (1 − ε)/(2 + ε) ≥ 0.49, 2 − z_n ≥ 0.48, so |z_{n+1} − h(z_n)| ≤ 13ε".
  Alternatively take δ ≤ ⅛.

**F4 (LOW: constant diagonal factor in the Airy discs). Location: ROUTE2_p1 §3.4, first bullet, "P_± := 𝔇_∞^{σ₃}A_±P^{(3/2)}ϱ₁^{−σ₃/2}".**
- **Issue.** By §3.1, WLXZ's N = D_{h_W,∞}^{σ₃}N₀D_{h_W}^{−σ₃}, and D_{h_W,∞} = e^{L/2} ≠ 1. So N_σ = (𝔇_∞/D_{h_W,∞})^{σ₃}N(D_aD_HD_q)^{−σ₃},
  and with the stated prefactor P_±N_σ^{−1} = 𝔇_∞^{σ₃}A_±(I + O(1/n))A_±^{−1}(ND_H^{σ₃}N^{−1})·D_{h_W,∞}^{σ₃}𝔇_∞^{−σ₃}. That is not
  I + O(1/n) in the 𝔇_∞-frame.
- **Fix.** Use the prefactor (𝔇_∞/D_{h_W,∞})^{σ₃}, which plays the role of RH₁(r)'s D_{Q,∞}^{σ₃}. Then the displayed chain is
  correct. Nothing downstream changes, because the factor is an n-independent constant diagonal.

**F5 (LOW: hypothesis of Lemma CT; Rule A (f) statement). Location: ROUTE2_p1 §5 Lemma CT ("μ on (0, ∞)"); §7 Rule A (f)
("μ with an atom at 0: excluded (supp ⊂ (0, ∞) is needed for J_N > 0 …)").**
- **Issue.** J_N > 0 holds for every μ on [0, ∞) with infinite support, because the zeros of p_N lie in the *open* convex hull
  (0, max supp). So CT(i) and both directions of CT(ii) hold on [0, ∞), and the Rule A sentence is wrong.
- **Consequences.**
  - Through "⟸", Law P for xμ implies Law P for μ + mδ_0 for every m ≥ 0. The reviewer probe confirms this numerically for
    m = 1, 100.
  - Master's SH is already stated on [0, ∞).
- **Fix.** Either relax the hypothesis to supp μ ⊂ [0, ∞) and record the corollary "Law P is unchanged by adding a mass at 0",
  or keep (0, ∞) and correct the Rule A sentence. Either way, say that J(xμ) does not determine μ: the bidiagonal factorization
  is not unique, and "⟸" covers every positive factorization.

**F6 (LOW/INFO: GAP-int; make the reduction explicit). Location: ROUTE2_p1 §5 last paragraph, §7 GAP-int; PROOF.md §3.19.**
- **Issue.** The gap is genuine (see "Checks"). However, "⟸" together with "⟹" shows that the law at any single integer
  r₀ ≥ 2 is equivalent to the law at every integer r ≥ 2 (for the same Ψ). So GAP-int is equivalent to the law at r = 2
  (a = ½, α_x = 0).
- **Fix.** Add this reduction, and list the alternatives that were checked and fail:
  - the SH shift from (1, 2) never reaches ℤ;
  - a base at a = ½ is obstructed (logarithmic divergence);
  - a Geronimus step goes down;
  - an r = 1 base exists only for ΣΨ/k < ∞ and is equally obstructed (a = −½);
  - an unsymmetrized hard-edge analysis at α_x = 0, which ROUTE2 handles for p > 1 with Lemma W′, is not available at p = 1
    (HEURISTIC, as OBSTRUCTION-a already says).
- This is also the main contribution of the "⟸" direction and should be stated as such.

**F7 (LOW: numerics wording). Location: PROOF.md §3.19 NUMERICAL ("spreads ≤ 2·10⁻⁶"); LOG ("spread ≤ 2·10⁻⁶").**
- **Issue.** The spread of the R column over the five truncations is 2.0·10⁻⁵ (s = 1.5, n = 50). The 2·10⁻⁶ bound holds for
  nB, E and T only.
- **Fix.** Say "≤ 2·10⁻⁶ for nB, E, T; ≤ 2·10⁻⁵ for R".

**F8 (INFO: numerics independence). Location: ROUTE2_p1 §6, check_r2p1_ct [4].**
- **Issue.** "[4] p = 2, s = 6 computed directly" uses the same weights as the shifted measure of [1]/[2]. Its numbers
  coincide with [2]'s Cholesky image to every printed digit. This is fine as a check of law-boundedness, but it is not
  independent evidence.
- **Fix.** Say so in one line.

**F9 (INFO: Rule L pointer for "⟸"). Location: ROUTE2_p1 §5, LOG "Literature (Rule L)".**
- **Issue.** In master's chain-sequence form (REVIEW_Plan52 F1), "⟸" says the following: every parameter sequence of a chain
  sequence tending to ¼ tends to ½, not only the minimal one. This is very likely in the chain-sequence literature (Wall;
  Chihara 1978, Ch. III). Not read; pointer only.
- **Fix.** Label CT(ii) "very likely KNOWN (chain-sequence form), novelty UNCHECKED", as master does for CS.

**F10 (INFO: correct but worth stating). Location: ROUTE2_p1 §3.1.**
- **Observation.** In the Q-frame D_ϱ disappears from the local form: Q̃ = A₀ΦΘ with Θ = e^{∓nφ₊(0)σ₃}(D_a/W)^{σ₃}. So the
  possible |z|^{±O(ε₁)} behaviour of D_q at 0 never enters UR₁. It enters only Q itself, through the 3η margin of §4.2.
- **Fix.** A one-line remark would pre-empt the obvious objection.

## Recommended labels (after F1–F7)

- §1 RedA at p = 1: PROVED (ROUTE2, REVIEWED).
- H1₁, LF₁, LW1₁ (NEW), UR₁, C₁, D₁: PROVED-mod-cite.
- **Theorem RII₁, Corollary B_{p=1}: PROVED-mod-cite; Rule R ACCEPT WITH FIXES, REVIEWED once F4 and F7 are applied**
  (no re-check needed; F4 is a constant).
- **Lemma CT (renamed), CT(ii) "⟺", Lemma D: PROVED (self-contained)** once F3 is applied.
  - "⟹" is master's SH (cite §3.21).
  - "⟸" is new relative to master, and very likely KNOWN in chain-sequence form (novelty UNCHECKED).
- **Corollary B_{p=1}⁺: PROVED-mod-cite**, with rate O(1/n) under (H_an₁) via master's SH-r (F2). REVIEWED after the merge
  edit.
- **Corollary B_{p>1}⁺:** replace by a cross-reference to master's Corollary B_all (F1). No separate label.
- GAP-int: GAP. Equivalent to the law at r = 2 (F6).
- GAP-rate₁: GAP for the tilt law only (F2).
- OBSTRUCTION-a: OBSTRUCTION (scoped to the band-centre C–D frame).
- Numerics: NUMERICAL. Novelty: UNCHECKED.

## Numerics re-run log

- From `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics`:
  `.venv/bin/python ../ja-plan50/research/G1/RH/route2/checks/check_r2p1_{lw1,ct,coeff}.py`. All three are byte-identical to
  the committed `.out` files (13 s, 80 s, 142 s).
- Reviewer probe (scratch, not committed): Law P with an added atom at 0, for m ∈ {0, 1, 100}. The law holds, with x_n → 1.
- Sources fetched for Rule C: arXiv:math-ph/0305044 and arXiv:math/0212014 (PDF → pdftotext), dlmf.nist.gov/10.25 and /10.27.
