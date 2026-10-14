# Novelty search (Rule L): G3′ (Hankel / OP asymptotics of σ = Σ 2x_k δ_{x_k}, x_k = 1/(γ_k² + ¼))

Date: 2026-10-14. Searcher: subagent (read-only on jacobi-asymptotics).
Repo files read: AGENTS.md, THEOREMS.md (H5, §2.5, §3.3), research/G3prime/CITATIONS.md, PROOF.md §0, §1, §3, §4, §4.1,
§5.2–5.5, §8, §9 (header), and the headers of rhfree/{RHFREE, RHFREE2, RHPRIME, RH99}.md.

Framing (AGENTS.md rule 3): nothing below is a claim about RH. Where a source assumes RH, that is stated as the
source's hypothesis.

Rule C: a source is listed only if it was actually opened. "PDF" means the arXiv PDF was downloaded and its text
extracted and read at the place quoted. "abs" means only the arXiv abstract page was read. Quotes are verbatim from the
text extraction; math symbols are lossy where the extraction is lossy.

---

## 0. Headline findings

1. **The moment sequence of σ is a named object in the literature: Voros's superzeta function of the 2nd kind at
   t = ½.** Voros (arXiv:1403.4558, PDF) defines Z(σ | t) = Σ_k (τ_k² + t²)^{−σ}, with ρ = ½ ± iτ_k. It writes
   Z∗(σ) ≡ Z(σ | ½) and expresses the Keiper–Li coefficients as a finite triangular combination of Z∗(1), …, Z∗(n).
   - In the repo's convention, the ordinates γ_k are taken as real inputs. Then ∫x^j dσ = 2Σ_k x_k^{j+1} =
     2Σ_k(γ_k² + ¼)^{−(j+1)}. This equals 2Z∗(j+1) term by term whenever τ_k = γ_k (real τ_k).
   - So D_n(σ) = 2^n·det[Z∗(i+j+1)]_{0≤i,j<n}, i.e. the G3′ Hankel determinants are Hankel determinants of superzeta
     values (equivalently of a triangular transform of the Keiper–Li coefficients).
   - This connection is **not recorded in the repo** (grep for voros/superzeta/keiper: no hits). It should be cited
     as the standard name for the moments, and it identifies Voros (and Keiper–Li researchers) as natural readers.
   - **No source found computes Hankel determinants or orthogonal polynomials of these moments.**
2. **No paper found studies orthogonal polynomials, Jacobi matrices or Hankel determinants of a measure supported on
   (functions of) zeta zeros.** The closest templates:
   - the Lommel/Bessel case: the measure has atoms at reciprocals of Bessel zeros with weights ∝ j^{−2} (Van Assche,
     math/9510214, PDF; Clark, 2608.12588, abs; Chung–Lee–Park, 2406.09746, abs, with "Rayleigh-type sums" as
     moments and "a formula for the Hankel determinant");
   - the Coulomb-wave case (Štampach–Šťovíček, 1403.8083, abs).
   σ is the zeta analogue of these: its Stieltjes transform is a log-derivative of Ξ, and its Jacobi matrix is a
   compact (trace-class, since Σx_k < ∞) Jacobi matrix in Stieltjes' sense.
3. **Leading-order Hankel asymptotics of the pure-power measures are prior work** (relevant to Φ_n and to item 11 /
   Theorem H, not to G3′ itself):
   - Monien (0901.1883, PDF). Already recorded in THEOREMS.md:156.
   - **Haynes–Zudilin, SIGMA 11 (2015) 101, DOI 10.3842/SIGMA.2015.101** (1510.01901, PDF). **Not recorded in the
     repo.** It treats det ζ(a(i+j)+b), i.e. the measure Σ_k k^{−b}δ_{k^{−a}} with x_k = k^{−a}, the same family as
     σ_{p,s} with p = a. It proves only an upper bound with a non-sharp leading coefficient (−(a/2)n²log n) and states
     the expected −a n² log n + O(n²).
4. **Pair-correlation side.** The step "PCC ⇒ small gaps are rare" used in Theorem C is KNOWN and stated explicitly:
   - Goldston, math/0412313 (6.10)–(6.11);
   - Hejhal's spacing hypothesis, which is a quantitative (SG) and is called "a weak consequence of Montgomery's
     pair-correlation conjecture" (Hiary–Odlyzko, 1105.4312, PDF).
   The repo's hypothesis (SG) is a weakened form of Hejhal's hypothesis (1.1). It should cite it.
5. **No source found links any spacing or near-pair energy of zeta zeros to Hankel determinants or Jacobi
   coefficients.** The nearest conceptual neighbour of Theorem Ch's "capped near-pair log-energy" is the role of
   small gaps in the distribution of log|ζ′(ρ)|: Hejhal's CLT needs a spacing hypothesis (Hiary–Odlyzko quote below).
   No paper found uses the energy 𝒞(K) or P(K) = Σ_{close pairs} log(1/d), and none computes the GUE constant
   ∫_0^1 log(1/u)(1 − (sin πu/πu)²)du.

---

## 1. Per-result verdicts

### G3′-U (limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0, unconditional)
**Verdict: NOT FOUND.**
- **Closest prior work.**
  - Haynes–Zudilin Lemma 1 (PDF): for a Dirichlet series f(s) = Σ a_n n^{−s} with a_n ≪ n^{1−δ}, "log |Hn [f ]| ≤
    − (1/2) n² log n + O(n²)". Their proof is the same Heine/Vandermonde expansion the repo uses: "Using the linearity of
    determinant with respect to each row and the formula for the Vandermonde determinant we have that Hn [f ] = Σ … Π
    (k_i^{−1} − k_j^{−1})".
  - Monien (PDF): "log Hn(0) [ζ] ∼ log Hn(1) [ζ] ∼ −n² (log(2n) − 3/2)" (heuristic; "We do not know how to prove the
    full asymptotic expansions").
- **What differs.**
  - These treat equally spaced reciprocal integers (pure powers), and only at leading order or with a non-sharp
    constant.
  - G3′-U is a sharp O(n²)-constant upper bound for an irregular atom set (the zeta ordinates), obtained by
    comparison with a smooth model through the explicit Riemann–von Mangoldt formula.
  - No source found takes Hankel determinants of the superzeta moments Z∗(m).

### Theorem B (liminf ≥ −3 log C, i.e. log D_n = Φ_n + O(n²), no hypothesis on the zeros)
**Verdict: NOT FOUND as a Hankel/OP statement. The ingredients are KNOWN.**
- **Ingredients.**
  - GLSS (6.1), the unconditional averaged pair correlation. It is in CITATIONS (C5); abstract re-read: "the method
    of Gallagher and Mueller does not depend on RH".
  - Positive proportions of distinct zeros are known unconditionally. Lamzouri (2609.02882, abs): "at least 83.62% of
    the non-trivial zeros are distinct"; Wang (2609.24167, abs) slightly improves the constant.
  - The step "a positive-density set of ordinates pairwise separated by ≫ 1/log T exists unconditionally" (via
    Caro–Wei) was not found stated in this form. It is a routine consequence of (6.1); present it as a lemma, not as
    a novelty.
- **What differs.** The conclusion log D_n(σ) = Φ_n + O(n²) does not appear anywhere.

### Theorem Ch (G3′ ⟺ 𝒞(K) = o(K²), capped near-pair log-energy)
**Verdict: NOT FOUND.**
- **Closest prior work.**
  - (a) Hejhal's theorem on log|ζ′(½+iγ_n)| needs a spacing hypothesis (Hiary–Odlyzko, PDF): "Hejhal [He] assumed the
    RH and a weak consequence of Montgomery's [Mo] pair-correlation conjecture, namely that for some τ > 0, there is a
    constant B such that (1.1) lim sup_{N→∞} (1/N)|{n : N ≤ n ≤ 2N, (γ_{n+1} − γ_n) log γ_n < c}| ≤ Bc^τ, holds for
    all c ∈ (0, 1)." Reference: D.A. Hejhal, "On the distribution of log|ζ′(1/2+it)|", in Number Theory, Trace Formulas,
    and Discrete Groups (Proc. 1987 Selberg Symposium), Academic Press, 1989, 343–370 (not opened).
  - (b) Matiyasevich (0709.0028 and 0707.1983, PDF) reformulates RH through Hankel/Toeplitz determinants of Taylor
    coefficients of 1/ζ̃: "The Riemann Hypothesis can be reformulated as statements about the eigenvalues of certain
    matrices whose entries are defined in terms of the Taylor coefficients of the zeta function." These are
    Hadamard/Kronecker pole-detection Hankels with growth "det(M_{l,m}(ζ∗)) = W_l^m(R_l(ζ∗) + o(1))". They are not
    moment Hankels of a positive measure, and they are not about spacing.
  - (c) Montgomery-method papers on multiplicities, such as Chirre–Gonçalves–de Laat (1810.08843, PDF): "N∗(T) :=
    Σ_{0<γ≤T} m_ρ … Theorem 1. Assuming RH, we have N∗(T) ≤ (1.3208 + o(1))N(T)". They bound pair or multiplicity
    sums from above. They give no equivalence with any OP quantity.
- **What differs.** No source characterizes a Hankel/Jacobi asymptotic by a spacing functional of the zeros. The
  "pair-based, capped" energy 𝒞(K) appears to be new.

### N″ (d̄(E) > 0 ⇒ the law fails; G3′ ⇒ d(E) = 0) and N‴ (gaps ≤ e^{−βk} at positive density ⇒ the law fails)
**Verdict: NOT FOUND.**
- The repeated-ordinate density is studied in its own right:
  - N∗(T) bounds (CGdL above);
  - "100% simple and on the line" under PCC (GLSS abstract: "we use PCC to prove that asymptotically 100% of the
    zeros are not only simple but also on the critical line");
  - unconditional proportions (Lamzouri, Wang).
- No source turns multiplicity or tiny gaps into a failure of an OP/Hankel asymptotic. The "deletion cost"
  mechanism (Christoffel function / Lemma Sat) is standard OP technique, but it was not found applied to zeta ordinates.

### Conditional closures
| Result | Verdict | Prior work (opened) | What is new |
|---|---|---|---|
| **Theorem C** (PCC, GLSS form ⇒ (SG) ⇒ G3′) | **PARTIALLY KNOWN.** PCC ⇒ (SG) is KNOWN; (SG) ⇒ G3′ was NOT FOUND | Goldston math/0412313 (PDF): "Another related conjecture that follows immediately from the PCC is that (6.10) N(T, β) = o(1), as β → 0+"; "the PCC itself implies a stronger repulsion between zeros: as β → 0+, (6.11) N(T, β) ≪ β³." Hiary–Odlyzko: Hejhal's (1.1) is "a weak consequence of Montgomery's pair-correlation conjecture". GLSS (abs): PCC treated "as a conjecture only concerning the vertical distribution of zeros" | Only the Hankel conclusion (via G3′-L). The repo's (SG) step should cite Goldston (6.10)/(6.11), GLSS Thm 1 for repeats, and Hejhal (1.1) |
| **Corollary P** (RH + prime variance (V) ⇒ G3′) | **PARTIALLY KNOWN** (the chain RH + (V) ⇒ SPC ⇒ PCC is KNOWN, as the repo already says) | Goldston notes Thm 7 and Thm 4 (PDF): "Theorem 4. Assume the Riemann Hypothesis. SPC implies PCC and SZC." | Only the last link (G3′-L) |
| **Theorem S / S′** (SPC_ℂ⁺, RH-free; on RH, the upper half of SPC ⇒ 100% simple critical, small gaps ≪ δ³, G3′) | **PARTIALLY KNOWN** (on-RH qualitative part); the RH-free version was NOT FOUND | Goldston Thm 4 proof (PDF): "For SZC, we repeat the calculation in (5.5) but now assume λ ≥ 1 and use SPC for that range to find (6.13) Σ (sin(λ/2(γ−γ′)log T)/(λ/2(γ−γ′)log T))² w(γ−γ′) ∼ (1 + 1/(3λ²)) (T/2π) log T." *Searcher's observation, not a quoted claim:* that SZC derivation has nonnegative terms on RH, so it needs only an upper bound for F on [1, M]. "RH + upper half of SPC ⇒ SZC" is therefore implicit in Goldston's argument. The RH-free route through BGST's complex-weighted F and Lamzouri's Prop. 2.1 inequality was not found anywhere | RH-free Theorem S, the Hilbert–Schmidt "Lemma G", the δ³ small-gap rate from a one-sided hypothesis, and the Hankel conclusion. In S′, state that the on-RH qualitative "simple zeros" part is essentially Goldston Thm 4 |
| **Theorem V⁺** (RH + one-sided prime variance ⇒ (SG) ⇒ G3′) | **NOT FOUND** | Goldston–Montgomery equivalence (two-sided; Goldston Thm 7, read). A web search for a one-sided variance ⇒ simplicity/small-gap statement found nothing | One-sidedness and the Hankel conclusion. Do not overclaim: the mechanism (nonnegativity of the Fejér-weighted pair sum on RH) is standard Montgomery-method practice |

### Numerics (P(K)/K → 0.227 vs GUE 0.2410; 𝒞(K)/K² ≤ 1.1·10⁻⁷ at K = 2·10⁶)
**Verdict: NOT FOUND** (no source computes this log-pair energy).
- Odlyzko-type numerics of the related statistic log|ζ′(ρ)| exist. Hiary–Odlyzko (PDF): "the frequency of very small
  normalized values of log |ζ′(1/2 + iγn)| is higher than predicted by a standard normal distribution".
- Comparing with them would be natural: small gaps drive both statistics.

---

## 2. Key quotes for the bridge (Voros, arXiv:1403.4558v2, RIMS Kôkyûroku Bessatsu B52 (2014) 147–164; PDF)

- (14): "ρ = 1/2 ± iτk (Re τk > 0) (k = 1, 2, . . .)"; (15): "Re ρ = 1/2 ⇐⇒ τk is real".
- §2: "Over the set of Riemann zeros {ρ} (always counted with multiplicities, if any), several generalized zeta
  functions are conceivable"; (17): "Z (σ | t) = Σ_{k=1}^∞ (τk² + t²)^{−σ}, Re σ > 1/2 (2nd kind)".
- (34)–(35): "λn = −n Σ_{m=1}^n ((−1)^m/m) C(m+n−1, 2m−1) Z∗(m), n = 1, 2, . . ." and "This yields a representation
  by an integral over the superzeta function Z∗(σ) ≡ Z(σ | 1/2) (of the 2nd kind)". Here λ_n are the Keiper–Li
  coefficients.
- Table 2 lists pre-2000 work on the 2nd kind, including "Matiyasevich … σ=n" (1989) and "Kurokawa t = 1/2" (1988).
  Full treatment: Voros, *Zeta functions over zeros of zeta functions*, Lecture Notes of the UMI (ref. [31]; not
  opened).
- **Consequence for the repo** (a derivation, not a source claim): with t = ½, τ_k² + ¼ = ρ(1 − ρ) for ρ = ½ + iτ_k.
  The repo's x_k equals 1/(τ_k² + ¼) when τ_k = γ_k. In general the repo's x_k is defined from ordinates, so its
  moments are the ordinate version of Z∗ and coincide with Voros's Z∗ only for real τ_k. State it that way, with no
  RH framing.

Other quotes used above:
- Haynes–Zudilin (PDF), Introduction: "we expect that log det_{1≤i,j≤n} ζ(a(i + j) + b) = −an² log n + O(n²) as
  n → ∞"; Monien "rigorously justified the above asymptotics in the case r = 0, by explicitly constructing a family of
  orthogonal polynomials related to the corresponding Riemann–Hilbert problem". The latter is secondary: HZ cite it
  as "[5] Monien H., Personal communication, 2011".
- Van Assche (math/9510214, PDF), §3: "the Lommel polynomials are orthogonal with respect to an atomic measure with
  support a denumerable set with accumulation point at the origin … the spectrum consists of the closure of the set
  {1/jk,ν−1 : k ∈ Z}"; Stieltjes' Theorem 2: "lim bn = 0 is a necessary and sufficient condition in order that the
  continued fraction (1) converges to F(z) = ∫ dΦ(u)/(z+u) where F is meromorphic for z ∈ C \ {0}"; and
  "Σ(|an+1| + √λn) < ∞ … means that J is trace class".
- Chung–Lee–Park (2406.09746, abs): "We introduce a sequence of orthogonal polynomials whose associated moments are
  the Rayleigh-type sums, involving the zeros of the Bessel derivative J′_ν … we obtain a formula for the Hankel
  determinant, elements of which are chosen as the aforementioned Rayleigh-type sums."
- Štampach–Šťovíček (1403.8083, abs): "a Jacobi (tridiagonal) matrix J_L whose eigenvalues coincide with reciprocal
  values of the zeros of the regular Coulomb wave function … The spectral zeta function corresponding to … the
  respective tridiagonal matrix is studied as well."

---

## 3. Sources opened (IDs)

| Source | ID / DOI | How read |
|---|---|---|
| A. Voros, Zeta functions over zeros of Zeta functions and an exponential-asymptotic view of RH | arXiv:1403.4558v2; RIMS Kôkyûroku Bessatsu B52 (2014) | PDF §§1–3 |
| H. Monien, Hankel determinants of Dirichlet series | arXiv:0901.1883 | PDF §1 |
| A. Haynes, W. Zudilin, Hankel Determinants of Zeta Values | arXiv:1510.01901; SIGMA 11 (2015) 101; DOI 10.3842/SIGMA.2015.101 | PDF §§1–2 |
| Yu. Matiyasevich, Hidden Life of Riemann's Zeta Function 2 (and part 1, arXiv:0707.1983) | arXiv:0709.0028 | PDF §2 (abstract, defs); part 1 grep |
| W. Van Assche, Compact Jacobi matrices: from Stieltjes to Krein and M(a,b) | arXiv:math/9510214 | PDF §§1–3 |
| G.A. Hiary, A.M. Odlyzko, Numerical study of the derivative of the Riemann zeta function at zeros | arXiv:1105.4312 | PDF §1, refs |
| A. Chirre, F. Gonçalves, D. de Laat, Pair correlation estimates … via semidefinite programming | arXiv:1810.08843 | PDF §§1–2 |
| D.A. Goldston, Notes on pair correlation of zeros and prime numbers | arXiv:math/0412313 | PDF §§6–7 |
| Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, Pair correlation … I | arXiv:2501.14545v3 | PDF abstract, §1 |
| Goldston–Lee–Schettler–Suriajaya (GLSS) | arXiv:2503.15449 | abs |
| Y. Lamzouri, A new proof that more than 2/3 … | arXiv:2609.02882 | abs |
| B. Wang, Proportions of the non-trivial zeros … | arXiv:2609.24167 | abs |
| B. Wang, Simple critical zeros and distinct zeros … in short intervals | arXiv:2609.07918 | abs |
| X. Wu, Distinct zeros of the Riemann zeta-functions ("more than 66.036% … distinct") | arXiv:1206.3737 | abs |
| S. Inoue, Small gaps between consecutive zeros (μ < 0.50895 under RH) | arXiv:2604.05733 | abs |
| S.-Y. Chung, S. Lee, Y.W. Park, Complex zeros of Bessel function derivatives and associated OPs | arXiv:2406.09746 | abs |
| F. Štampach, P. Šťovíček, OPs associated with Coulomb wave functions | arXiv:1403.8083 | abs |
| S.P. Clark, Lommel polynomials and explicitly solvable prediction problems on the unit circle | arXiv:2608.12588 | abs |
| M.W. Coffey, On certain sums over the nontrivial zeta zeros | arXiv:0912.2390; DOI 10.1098/rspa.2010.0064 | abs |
| M. Suzuki, Aspects of the screw function corresponding to the Riemann zeta function | arXiv:2206.03682 | abs (paraphrase only; no Hankel/OP content) |

Withdrawn or unavailable: Goldston–Turnage-Butterbaugh arXiv:1904.06001v2 ("This version … has been withdrawn"). It was
not used.

## 4. Suggested references to add (CITATIONS / README "related work")
1. Voros 1403.4558 (and his UMI Lecture Notes book): name the moments s_j = 2Z∗(j+1) (ordinate version) and note the
   Keiper–Li link (34).
2. Haynes–Zudilin, SIGMA 2015: prior Hankel asymptotics for Σk^{−b}δ_{k^{−a}}, relevant to Φ_n and Theorem H; add
   next to Monien.
3. Van Assche math/9510214: Stieltjes' compact-Jacobi theorem. σ's Jacobi matrix is compact (trace class); the Lommel
   template.
4. Hejhal 1989 via Hiary–Odlyzko: (SG) as a weakened form of Hejhal's spacing hypothesis (1.1).
5. Goldston notes (6.10)–(6.11): PCC ⇒ N(T, β) = o(1), ≪ β³, for Theorem C's (SG) step.
6. CGdL 1810.08843 and Lamzouri 2609.02882: the multiplicity and distinctness state of the art, for N″'s "open"
   remark. Lamzouri's 83.62% distinct zeros updates the 0.4075 bound used in PROOF.md §5.5's (C3) remark.
   - Caveat: distinct *zeros* ≠ distinct *ordinates* (the repo already notes this in (C6)). So 83.62% does not
     directly bound d̄(E). The repo's (C3)-based bound |E ∩ [1, K]| ≤ 0.5925K could be improved to ≈ 0.3275K via
     "simple and on the line ≥ 67.25%".
   - *(Plan 43 note, 2026-10-14: proved as PROOF.md §5.6 Corollary Lz, d̄(E) ≤ 1 − C_Lz = 0.32749… from (C6) Thm 1.1.
     The update comes from the simple-and-critical proportion, not from 83.62% distinct zeros.)*

## 5. Search terms used
- Hankel determinants: "Hankel determinants sums over zeros zeta"; arXiv `abs:Hankel AND abs:"Riemann hypothesis"`;
  "Hankel" + "Riemann zeros" + superzeta; Keiper–Li + Hankel.
- Orthogonal polynomials and Jacobi matrices: "orthogonal polynomials measure supported on zeros of Riemann zeta
  Jacobi matrix"; `abs:"Jacobi matrix" AND abs:zeta AND abs:zeros`; "tridiagonal Jacobi matrix eigenvalues Riemann
  zeros inverse spectral"; Hilbert–Pólya + Jacobi; Lommel polynomials + reciprocal zeros + zeta.
- Moments: "positive definite Hankel … sums over zeros … moment sequence Stieltjes".
- Gaps and pair correlation: `abs:"small gaps" AND abs:"zeros of the Riemann zeta"`; pair correlation small gaps;
  `ti:"distinct zeros"`; "log energy pairs zeta zeros GUE"; "sum over pairs log|γ−γ′|"; Hejhal log|ζ′| spacing
  hypothesis; Alpöge–Furman; "one-sided variance primes simple zeros".
- Discrete measures: "discrete measure masses 1/k² Hankel n² log n"; Monien follow-ups.

## 6. Natural expert readers
- Superzeta and Keiper–Li moments: André Voros; Mark Coffey; Krzysztof Maślanka.
- Pair correlation, simple zeros and gaps: D.A. Goldston, A.I. Suriajaya, C.L. Turnage-Butterbaugh, S.A.C. Baluyot,
  Y. Lamzouri, M. Milinovich, S. Gonek, A. Chirre.
- Hankel asymptotics and discrete OPs: H. Monien, W. Zudilin, W. Van Assche, F. Štampach, D. Lubinsky.
- Log|ζ′| statistics and numerics: G. Hiary, A. Odlyzko (Odlyzko's zero tables are the repo's data source).
- RMT and Coulomb-gas viewpoint: J.P. Keating, B. Rodgers.

## 7. Caveats
- Paywalled originals were not opened: Hejhal 1989, Montgomery 1973, Gallagher–Mueller 1978, Goldston–Gonek–Özlük–
  Snyder 2000, Voros's book, and Bui–Goldston–Milinovich–Montgomery (seen only as a search snippet: "≫ε T^{1−ε} such
  small gaps between distinct zeros", RH; source not opened, do not cite). A specialist could know unpublished or
  book-only material on OPs of superzeta moments. The NOT FOUND verdicts mean only "not found by these searches".
- The arXiv API was rate-limited mid-search. Later searches used arXiv abstract pages and general web search.
