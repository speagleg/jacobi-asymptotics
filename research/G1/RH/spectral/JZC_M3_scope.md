# JZC M3 scope: Hypothesis G (Riemann–Hilbert for non-lattice nodes) — what it must deliver, prior art, first step, go/no-go

Status (2026-10-21): scoping memo for Plan JZC milestone M3 (local plan docs/superpowers/plans/PLAN_JZC.md). NOT REVIEWED.
Labels per VERIFICATION_POLICY.md. Almost everything here is a plan or HEURISTIC; nothing in it is used as a proof. Quotes
marked (WF) are second-hand: WebFetch tool extractions of the arXiv PDFs/abstract pages, not a reading under Rule C.
Convention: Z_Λ(w) = Σλ_m^{−w} (SPEC §0), so the lattice value is Z(−k) = ζ(−kp); "Z_Λ(−kp)" in the plan text means this.

## 1. What G must deliver (statement level; PLAN)

Class. λ_k = Λ(k), Λ(t) = t^p(1 + Σ_i c_i t^{−q_i} + O(t^{−Q})), p ∉ {1}, plus finite modifications. κ := Λ^{−1} (index function),
t_κ(z) := κ(n^p/z) (so the rescaled nodes z_k = n^p/λ_k are exactly t_κ = k), σ_Λ = Σλ^{−s/p}δ_{1/λ}, 1 < s < 1 + 2p (base
window; Paper 2 Theorem 3, x·σ_{Λ,s} = σ_{Λ,s+p}, transfers verbatim because it only multiplies masses by the node 1/λ).

Target (Theorem G, the M3 deliverable). The RH analysis of Paper 2 §§5–8 + E_pgt1/E_plt1/E2/E3/JZC_M4_proof runs for σ_Λ with:
- (G1) g-function of the constrained equilibrium (JZC_M1 Theorem Q) of the n-dependent constraint σ_n(y) := (1/n)|dt_κ/dy|;
  band [0, a_n], a_n the root of (Q) for σ_n; φ, φ̃, the hard-edge map f_n and soft-edge map f_{r,n} analytic in z and in the
  perturbation, with the sign conditions of Paper 2 Lemmas 5.3–5.4 globally (incl. the saturated region up to the top node).
- (G2) the band factor H_n^κ = e^{−2G_κ}, G_κ = −j(t_κ) + log B_κ, with log H_n^κ(z) − log H_n^κ(1) = −2Σ_{k≤K}m_k^κ(z^k − 1)
  + O(n^{−(K+1)p}) on |z| ≤ 4c + 2 (one derivative), m_k^κ = D_Λ(k)/(kn^{kp}), where D_Λ is the discrete (Abel–Plana) part of
  Z_Λ (§3.2); i.e. E3's gauge form with μ_{n,k} = 2D_Λ(k)/(kn^{kp}).
- (G3) the band weight is W₀ = C_n z^α(4c − z)H_n^κ(z)J_n(z), with the Jacobian tilt J_n := t_κ′/t′ (and the mass ratio, which is
  1 as a function of z because masses are (n^p/z)^{−s/p}); the parametrix corrections it causes are O(n^{−2−q₁}) (minimal G3),
  or explicitly −(mpq₁/2)W(q₁) per unit (full G3 = S1⁗; needs E3.7 for branched tilts z^{q₁}, q₁ ∉ ℕ).
Output under G (HEURISTIC, SPEC §3.14 Prop E): n^pb_n/c = a_n/(4c)·[1 + (1/n)(d₁ + Σ_j pW(j)D_Λ(j)n^{−jp}) + …]; a_n/(4c) carries
the pole terms pR_qW(q)π cot(πq)n^{−1−pq} (JZC_M1 Prop M1.2, PROVED as a statement about the root) and the continuum integer
values; the index offset carries pZ(0)/n.

What the lattice proof uses that is lattice-specific (with where; HEURISTIC classification):
| Lattice ingredient | Where | General replacement | Kind |
|---|---|---|---|
| t(z) = nz^{−1/p} explicit; arg t ∈ (−π/p, π/p) | Paper 2 L5.1, L5.5, Table 1 | t_κ(z); needs κ analytic on the sector image (hypothesis (A) below) | hypothesis + routine |
| interpolant sin πt; node product 1/Γ(1 − t) | Paper 2 L5.1, §6 | sin πt_κ(z), 1/Γ(1 − t_κ(z)) (composition: zeros exactly at the nodes for any κ) | routine |
| masses k^{−s} = t^{−s} ⇒ band weight a pure power z^α | Paper 2 L5.2 | z^α·J_n(z): Jacobian tilt | G3 (new if branched) |
| equilibrium μ* explicit (Paper 1 Thm 1.3), n-independent | Paper 2 L5.3–5.4, E_pgt1 L E.4 | Theorem Q for σ_n; n-dependent local data f′(0), κ, κ₂ | G1 (new: global signs) |
| Binet scalar D̃ = e^{−j(t)}, Binet-cut B with jump 𝔟 on (−∞, 0) | Paper 2 L6.1 = RH_px L3.1–3.3; E_pgt1 L E.2 | j(t_κ), B_κ; Liouville needs t_κ on all of (−∞, 0), i.e. κ near λ = 0⁻ (far region) | routine if κ nice at 0, else new |
| seam scalar χ (p < 1), seams at arg z = ±πp/2 | Paper 2 L6.4–6.5; E_plt1 L F.1 | same with t_κ; seams ↔ arg t = ∓π/2 | routine |
| band-factor moments ζ(−kp)/(kn^{kp}) via DLMF 5.9.1/5.2.1, 25.4.1 | E3 L F.1′(i), E_plt1 L F.1(iii) | D_Λ(k)/(kn^{kp}) via a rotated Abel–Plana formula | new (Lemma AP) |
| model data p-free, n-free (f′(0), κ, κ₂, A₀, A_r, B_r) | E_pgt1 L E.4–E.5; N.6d exact algebra | n-dependent analytic perturbations of the same data | routine bookkeeping, long |
| normalisation at ∞ (g − log z, F at ∞, z^{nσ₃}) | Paper 2 L6.7, (O1)–(O5) | index offset −Z(0) (the Hurwitz crossover, SPEC §3.1) | new |

Hypothesis (A) (PLAN; the analogue of BKMM's analytic node density, §2): κ is analytic on a neighbourhood of the closed sector
image needed by the frame (p > 1: λ ∈ ℂ∖(−∞, 0] incl. boundary values, i.e. Λ analytic on |arg t| ≤ π/p; p < 1: |arg t| ≤ π/2),
real on (0, ∞), with the sign condition Im t_κ(y + i0) < 0 for y < 0 (p > 1; on the seams for p < 1) and |e^{−2πit_κ₊}| ≤
exp(−c n|y|^{−1/p}); the asymptotic expansion of Λ holds uniformly in the sector.

## 2. Literature (Rule L first pass for M3; queries listed at the end)

- **BKMM** (Baik–Kriecherbauer–McLaughlin–Miller, arXiv:math/0310278 = Ann. Math. Stud. 164; announcement math/0212149).
  Exactly a non-lattice node set, but finite and in a bounded interval. Read in the repo (G1/CITATIONS.md "(BKMM)", abstract
  and §1 of math/0212149): "The density function ρ0(x) is real analytic in a complex neighborhood of the closed interval
  [a, b]"; "A saturated region Γ is an open subinterval of [a, b] of maximal length in which dμ^c_min/dx ≡ ρ0(x)/c".
  (WF, math/0310278 §1.1): quantisation (10) ∫_a^{x_{N,n}}ρ⁰(x)dx = (2n+1)/(2N), n = 0, …, N−1; ρ⁰ > 0 on [a, b], ∫ρ⁰ = 1;
  weights (11) w_{N,n} = e^{−NV_N(x_{N,n})}∏_{m≠n}|x_{N,n} − x_{N,m}|^{−1}, V_N = V + η/N; degree k = cN + κ, c ∈ (0, 1);
  constraint (61) 0 ≤ ∫_Bdμ ≤ (1/c)∫_Bρ⁰; "triangularity reversal" Q = P[∏_{n∈Δ}(z − x_{N,n})]^{−σ₃} (eq. 34) and duality
  (Δ = ℤ_N, k̄ = N − k, eqs. 40–45) to handle saturated regions. (WF, math/0212149 §4.3, eq. 79): the pole-removal phase
  β_±(z) := ±i exp(∓iπN∫_z^bρ⁰(s)ds), with "β₊(x_{N,j}) = β₋(x_{N,j}) = (−1)^{N−1−j}". "The paper gives no extension of its
  method to unbounded or infinite lattices" (WF summary, not a quote).
  *Transfer (HEURISTIC).* Their phase πN∫_z^bρ⁰ is our πt_κ(z) (integer instead of midpoint quantisation); their analyticity of
  ρ⁰ near [a, b] is our (A) away from 0; their ∏|x − x_m|^{−1} normalisation is, for infinitely many nodes, a regularised
  product — our 1/Γ(1 − t_κ) (Γ-normalisation) plus masses. Their saturated-region machinery (reversal on Δ) is the analogue of
  Paper 2's V^△ (WLXZ). What does not transfer: the accumulation point (ρ⁰ has a non-integrable singularity at 0, infinitely
  many nodes in every neighbourhood of the hard edge). There Paper 2's Γ/Binet structure is needed, and it is lattice-specific
  only through t(z); under (A) it should go through with t_κ.
- **WLXZ** (Wu–Lin–Xu–Zhao, arXiv:1410.3948, READ, RH/CITATIONS.md): "discrete orthogonal polynomials on infinite nodes with an
  accumulation point"; only Tricomi–Carlitz (nodes ±(k + α)^{−1/2}: a Hurwitz lattice at p = 1 in the squared variable). The
  repo frame is theirs. A Hurwitz offset α is therefore already inside an RH analysis there, at p = 1 (relevant to H-d, §3.1).
- **Bleher–Liechty**, arXiv:0909.1985 (WF): "We consider the large-N asymptotics of a system of discrete orthogonal
  polynomials"; proof "based on formulation of an interpolation problem"; infinite regular lattice of mesh 1/N, weight e^{−NV},
  V real-analytic with growth. Infinite but regular, no accumulation; nodes not general.
- **Ou–Wong**, Anal. Appl. 8 (2010) 247–286 (WF abstract): RH approach for Charlier (infinite nodes), "similar to BKMM";
  regular lattice.
- **Joshi–Lasic Latimer**, arXiv:2111.11663 (WF): q-RHP for q-orthogonal polynomials (geometric accumulation, a different
  analytic structure: q-difference jumps, not a discrete measure with an interpolating phase). Not a transfer candidate.
- **Constrained equilibrium**: Rakhmanov 1996, Dragnev–Saff 1997 (J. Anal. Math., link.springer.com BF02843160, not fetched),
  Kuijlaars–Rakhmanov 1998, Beckermann–Kuijlaars 2002: potential theory only; JZC_M1 §6 already records them.
- **Abel–Plana / Plana summation** (needed for Lemma AP, §3.2): DLMF §2.10(i) (2.10.2) and Saharian, "The generalized Abel–Plana
  formula with applications to Bessel functions and Casimir effect" (arXiv:0708.1187): NOT READ; to be quoted under Rule C.
- **Hurwitz's formula** (needed for H-c): DLMF 25.11.9 still NOT READ (both the DLMF page and the E9 permalink truncate before
  25.11.9 under WebFetch today; 25.11.1 and 25.11.3 were returned). Apostol, Thm 12.6, is the fallback.
- **Nothing found** on RH asymptotics of OPs for discrete measures on {1/λ_k} for a general (non-lattice) node set
  accumulating at a point, nor for spectra of operators. Verdict for an M3 result: POSSIBLY-NEW, pending Rule L (one search
  round is not a check).
Queries: "Bleher Liechty … regular infinite lattice"; "Riemann-Hilbert discrete orthogonal polynomials nodes accumulating at a
point asymptotics non-uniform lattice" (extended); "Dragnev Saff constrained energy problems … discrete variable".

## 3. The first step: concrete sub-theorems (PLAN; sketches HEURISTIC)

### 3.1 Sub-theorem M3a = Theorem H (Hurwitz lattices; rule H to the orders of Theorem N.6)
Statement (target). Λ(t) = (t + δ)^p, −1 < δ ≤ 0 (a := 1 + δ ∈ (0, 1]), p ≠ 1, s > 1. Then Theorem N.6 (i)–(iii) holds with
μ_{n,j} = 2ζ(−jp, a)/(jn^{jp}), ε_j(a) = C(2j, j)pc^jζ(−jp, a), and the integer layer in the index ν := n + δ:
n^pb_n/c = (n/ν)^p·Φ_{p,α}(ν; ζ(·, a)), Φ the lattice expansion of N.6(iii) (this is rule H, SPEC §3.11(a), and S1-N with
−Z(0) = ½ + δ). Here κ(λ) = λ^{1/p} − δ, so t_κ = t − δ: (A) holds on the whole slit plane, J_n ≡ 1, σ_n = σ (G1 trivial:
identical g, φ, f, f_r, μ*), and |e^{−2πi(t₊−δ)}| = |e^{−2πit₊}| (δ real): every lattice bound is unchanged.
Band factor in E3's gauge form (sketch; SPEC §3.1 "Reduction"): G_δ := −j_δ(t) + log B_δ with j_δ(t) = LnΓ(t − δ) −
(t − δ − ½)ln t + t − ½ln 2π; the j_δ parts of the jump cancel as in E_pgt1 L E.2(a), leaving 𝔢_δ = 2Im Log(1 − e^{−2πi(t₊−δ)});
(E.2.1) holds by the same Liouville argument (K_δ bounded at 0 since t → ∞; O(log|z|) at ∞); Lemma H (CONDITIONAL on
Hurwitz's formula; NUMERICAL to 10⁻²⁷) gives m_k(δ) = ζ(−kp, a)/(kn^{kp}); F.1′(ii)'s truncation is verbatim. Hence
H_n^δ ∝ e^{−P_n^δ}(1 + O(n^{−(K+1)p})), P_n^δ = Σμ_{n,k}(δ)x^k. E3.4 (pure algebra), E3.7 (exact, any μ), N.6b–c (k-free) apply
unchanged; p < 1 likewise (seam sum checked, spec_hurwitz_moments_plt1.out).
Lemmas and their status:
| # | Lemma | Model | New argument? |
|---|---|---|---|
| H-a | interpolation with sin π(t − δ), 1/Γ(1 − t + δ); band weight | Paper 2 L5.1–5.2 | no (routine) |
| H-b | outer scalar j_δ: sectors, bounds | Paper 2 L6.1, L6.4 (p < 1); DLMF 5.11.8 (Rule C) | no (routine + citation) |
| H-c | band factor (p > 1: B_δ; p < 1: χ_δ), moments ζ(−kp, a) | E_pgt1 L E.2, E3 L F.1′, E_plt1 L F.1 + Lemma H | citation only (Hurwitz) |
| H-d | normalisation at ∞ / index transfer: the δ-problem is the lattice problem at "degree ν" | Paper 2 L6.7, (O1)–(O5) | **yes** (see below) |
| H-e | circle jumps, small norm, residue recursion with μ(δ) | N.6a–c, E3.5–E3.6 | no |
| H-f | assembly: rule H to N.6(iii)'s orders; exact algebra in ν | N.6d | no (re-run m4_* scripts with ν) |
H-d (HEURISTIC). As t → 0 (z → ∞), j_δ ~ (δ + ½)ln t + LnΓ(−δ) against the lattice's pole of Γ at t = 0 (SPEC §3.1): the outer
scalar's power of z at ∞ changes by z^{O(δ)/p}, which is absorbed in the normalisation z^{nσ₃}. Conjectured mechanism: after
rescaling by ν^p, all jumps are the lattice's at the real parameter ν, and the only mismatch, z^{nσ₃} vs z^{νσ₃}, is cancelled
exactly by that power; then N.6 (whose proof is analytic in the parameter in the jumps) gives Φ(ν) and the (n/ν)^p prefactor
comes from the constraint mass (ν/n)σ (Theorem Q by scaling: a = 4c(n/ν)^p, PROVED by the scaling σ(λy)λ). Check before work:
δ → 0⁻ is a crossover (Γ's pole at t = δ approaches 0); WLXZ's Tricomi–Carlitz offset α is a worked p = 1 instance.

### 3.2 Sub-theorem M3b (analytically perturbed lattices; G1 + G2 + minimal G3)
Statement (target). Λ(t) = t^p(1 + εh(t)) (or (t + δ)^p(1 + εh)), h analytic and bounded on the closed sector |arg t| ≤ θ
(θ > π/p, p > 1; θ > π/2, p < 1) including t → 0, real on (0, ∞), h(t) = Σ_ih_it^{−q_i} + O(t^{−Q}) at ∞, |ε| ≤ ε₀(h, p);
non-resonant (pq ∉ ℕ for the poles q = q_i/p, and q_i/p ∉ ℕ); e.g. h(t) = (1 + t)^{−1}. Then n^pb_n/c has S1″'s first-order
series at the leading power of each pole: integer layer pW(j)Z_Λ(−j)n^{−1−jp}, pole terms pR_qW(q)π cot(πq)n^{−1−pq}, the
d₁ = −pα/2 + pZ_Λ(0) term, remainder O(n^{−2−min(q₁, p)} + n^{−2}). (A) holds by perturbation: the sign condition of the
lattice degrades by a factor 1 − Cε. Example check: §3.12's data use λ_k = (k + γk^{−m})^p, which is singular at t = 0, so
M3b needs new numerics on a nice h (cheap; reuse spec_pole.py).
Band factor with Z_Λ (sketch, HEURISTIC; the core of G2). In the lattice, y^{−k−1}dy = −d(Λ(t)^k)/(kn^{kp}) along the ray
y < 0 ↔ arg t = ∓π/p (p > 1), resp. the seams ↔ arg t = ∓π/2 (p < 1). Integrating by parts, ∫Log(1 − e^{−2πit})dΛ^k =
−∫Λ^k·2πi/(e^{2πit} − 1)dt: so m_k is the remainder term of a rotated Abel–Plana (Plana) formula for f = Λ^k, with rays at
±π/p (±π/2 for p < 1 is the classical one). Write Z_Λ(−w) = C_Λ(w) + D_Λ(w), C_Λ the Mellin-continued "integral" part
∫_0^∞τ^{pw}κ̂′(τ)dτ in τ := λ^{1/p} (κ̂ := κ∘(·)^p), D_Λ the Plana remainder (entire in w under (A)). Lemma AP (target):
m_k^κ = D_Λ(k)/(kn^{kp}). For pure-power corrections C_Λ(k) = 0 in Mellin regularisation (this is why Lemma H and Prop
3.14.4 see the full Z(−j)); for general h, C_Λ(k) ≠ 0 and must come out of G1 (the continuum soft-edge root, M1.2 "plus
integer terms"). Then H_n^κ ∝ e^{−P_n}·(1 + O(n^{−(K+1)p})), μ_{n,k} = 2D_Λ(k)/(kn^{kp}): E3's gauge form; E3.4, E3.7 verbatim.
Lemmas and their status:
| # | Lemma | Model | New? |
|---|---|---|---|
| P-a | interpolation with t_κ; band weight z^αJ_n; sector lemma | Paper 2 L5.1, 5.2, 5.5 | routine |
| P-b | G1: g, φ, φ̃ from Theorem Q for σ_n; local maps f_n, f_{r,n} analytic in (z, ε, n^{−q}); global signs (lenses, saturated region up to the top node) | Paper 2 L5.3–5.4, RH_px L2.1–2.2, JZC_M1 Thm Q(iii) | **yes** (signs off the axis for non-explicit μ) |
| P-c | outer scalar j(t_κ), B_κ / χ_κ; Liouville representation | E_pgt1 L E.2(a)–(c), E_plt1 L F.1(i)–(ii) | routine under (A) |
| P-d | Lemma AP: moments = D_Λ(k)/(kn^{kp}); truncation | E3 L F.1′, E_plt1 L F.1(iii)–(iv) | **yes** (rotated Plana formula + regularisation; Rule C) |
| P-e | n-dependent model data: E_pgt1 L E.4–E.5 and N.6a with f_n, f_{r,n}; uniformity of DLMF remainders | E_pgt1 L E.3–E.5, N.6a | routine, long (exact algebra now in a perturbation parameter) |
| P-f | minimal G3: the tilt J_n with sup|log J_n| ≤ Cεn^{−1−q₁} on the discs moves R_1 by O(n^{−2−q₁}) | Paper 2 L7.3/Prop 7.6 (C–D comparison) or a direct Lipschitz bound on the small-norm map | semi-routine |
| P-g | extraction: n^pb_n/c = a_n/(4c)[1 + (d₁ + e(μ_n))/n] + …, then M1.2 for a_n | Paper 2 F8; E3 §6; JZC_M1 Prop M1.2 | **yes** (C_Λ/D_Λ bookkeeping = Prop E proved for this class) |
| P-h | index offset −Z_Λ(0) | H-d | reuses M3a |

### 3.3 Deferred (NO-GO for now)
- Full G3 (S1⁗): E3.7 for branched tilts z^{q₁}: G_μ is no longer entire at 0, Δ₁^μ is not meromorphic at the hard edge, the
  residue recursion (N.6c) breaks; needs a new Bessel-edge local analysis (Puiseux corrections). Research-level; NUMERICAL only.
- Far region: Λ singular at t = 0 (every spectrum with t^{−m} corrections: §3.12's synthetic family, bouncer/Airy, Bessel
  zeros, quartic oscillator p = 4/3). Then Im t_κ₊ changes sign at |y| ≫ n^p and (E.2.1)'s Liouville step fails; the moments
  depend on Λ at t ≍ 1, so the cut-off is not negligible. Needs a seam-type construction at |z| ≍ n^p (modelled on RH_plt1b)
  and Plana with base point t* ∈ (0, 1). For the Airy/Bessel spectra the exact phases (DLMF 9.9.1; Bessel phase) are candidate
  κ's; for the quartic oscillator no analytic κ in the sector is known to us (exact WKB, Voros: UNCHECKED).
- p = 1 (drums), resonant poles (pq ∈ ℕ: log terms), logarithmic counting laws: excluded, as in the plan.

## 4. Recommendation (PLAN)

**GO for M3a, then M3b; NO-GO (defer) for full G3 and for the far region.**
- M3a (Theorem H): 6 lemmas; 5 routine adaptations + 1 new (H-d, the index transfer), plus one Rule C citation (Hurwitz's
  formula). Size: about one plan the size of E3. It proves rule H (S1-N with Hurwitz offset) to the orders of Theorem N.6, and
  isolates exactly one of the three new mechanisms (the index offset −Z(0)).
- M3b: 8 lemmas; 4 routine (P-a, P-c, P-e long, P-h reuse), 1 semi-routine (P-f), 3 new (P-b global signs, P-d Lemma AP, P-g
  extraction/bookkeeping). About 1.5–2 E3-sized plans; P-e is the volume. It would make Principle E / S1″ (leading power per
  pole) a theorem for an open class, i.e. the "Jacobi–zeta correspondence" at first order in 1/n.
- Full G + far region: Paper-2 scale (the plan's risk estimate stands), only after M3a/M3b.
Order of work: (1) Rule C: read DLMF 25.11.9 (or Apostol Thm 12.6), DLMF 5.11.8, DLMF 2.10.2 / a Plana reference; (2) H-d on
paper first (decides M3a; check against WLXZ's offset and against spec_shift_hi.out); (3) M3a remaining lemmas, N.6d re-run in
ν; Rule A, Rule R; (4) numerics for M3b on a nice h (both p > 1 and p < 1, assertions; Rule X: predictions before fits);
(5) P-d (Lemma AP) as a standalone analytic lemma with a 40-digit check; (6) P-b, P-g; (7) P-e, P-f; (8) Rule L for M3a/M3b.

Top risks.
1. **H-d (index offset) is not a re-run.** The normalisation at ∞ and the Γ crossover at δ → 0⁻ have never been done; if the
   z^{δ}-type mismatch does not cancel exactly, rule H needs a new term and M3a's statement changes (SPEC §3.1 "What is not done").
2. **P-b, global signs for a non-explicit equilibrium.** Paper 2 leans on Paper 1's explicit μ*; for σ_n the relative
   perturbation is O(1) near the top node (y ≍ n^p), (H2) can fail there for large perturbations (e.g. κ-shifts with κ > 1/(p−1)
   violate yσ decreasing near the top), and the off-axis signs (lenses) are not covered by Theorem Q(iii).
3. **Scope creep into the far region / branched tilts.** Every physically interesting spectrum (Airy, Bessel, quartic, §3.12's
   data) is singular at t = 0 and has branched tilts; M3a/M3b prove the mechanism on an artificial but open class only. The
   C_Λ/D_Λ split (P-d, P-g) is HEURISTIC and could hide a missing term; test numerically on h = (1 + t)^{−1} before investing.
