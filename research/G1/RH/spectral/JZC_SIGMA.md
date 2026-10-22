# JZC Σ: the shift lemma (Conjecture Σ of JZC_M4 §7) from a second steepest-descent frame of the same lattice problem

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_SIGMA_A.md); fixes S1–S8 applied 2026-10-22.
Status (2026-10-22): **REVIEWED** for Lemma F (i)–(ii), Prop FI, Theorem Σ, Cor Σ.1 and Cor Σ.2 (Rule R: independent second reader A
re-derived the key steps (gauge, residues, (−∞, 0) cancellation, lip phase, band limit, transfer rows 2–5 against Paper 2 / the memos,
uniqueness, rationality, FI ⇔ Σ, evenness, the ζ(−2p)/ζ(−p)² separation), re-ran sigma_frame_exact.py (with and without the d_k cache:
identical outputs, byte-identical cache) and sigma_frame_num.py (byte-identical), plus independent spot checks: general base β ≠ ν at
order 8, the 2e₁ layer, order 10; fixes S1 (major, scope γ ≥ 0) and S2–S8 applied). Weight ≥ 3 zeta layers remain open (§3.3, §7).
Labels per VERIFICATION_POLICY.md. Novelty: UNCHECKED (Rule L not
done; §8). Scope: the integer layer of the decoupled model M(β, ν) of JZC_M4 §7 (Conjecture Σ as stated there), its first- and
second-weight zeta layers, and what this gives for Theorem R's evenness. Nothing here concerns RH or zeros; the lattice is
σ_{p,s} = Σ_k k^{−s}δ_{k^{−p}} (Paper 2 with ℓ₁ ≡ 1). Checks: `checks/sigma_frame_exact.py/.out` (+ `sigma_frame_exact_fresh.out`, the engine run), `checks/sigma_frame_num.py/.out`.
Read-only inputs (not edited): papers/paper2/{sec_3,sec_5,sec_6,sec_7,app_outer}.tex, JZC_M4.md, JZC_M4_proof.md, JZC_M3a_Hd.md,
JZC_M3a_H.md, JZC_M3a_H_G1u.md, checks/m4_shift_exact.py, checks/m4_rh4.py (imported, not modified).

| # | Statement | Label |
|---|---|---|
| Lemma F (i) | *Frame algebra.* For real γ and m := n + γ, the degree-n lattice problem in the frame of index m (scaling m^p, phase e^{mφ}) after the gauge U_m ↦ U_mz^{γσ₃} has exactly Paper 2's jumps for the weight exponent α̃ := α − 2γ, no jump on (−∞, 0), and on the lips in the hard-edge disc the Q-frame entry ω♮e^{−4ζ^{1/2}}, ω♮ := ω^{(α̃)}e^{∓2πiγ}, ζ = m²f, whose band limits are e^{∓iπα}: Bessel order α, Szegő exponent α̃ | PROVED (algebra, §2.2) + REVIEWED (Rule R reviewer A) |
| Lemma F (ii) | *Analytic transfer.* For p > 1, \|α\| < 1, 0 ≤ γ < (1 − \|α\|)/2 (γ = −δ with −1 < δ ≤ 0, the range of the cited H-d/G12/G1u statements; γ < 0 is expected to work — the H-a obstruction (phantom node) does not occur in the m-frame — but is not covered by any reviewed statement and is not used) (fixed per Rule R review A, S1): the m-frame analysis goes through and gives m^pb_n/c = Σ_{\|β\|≤B}μ_m^β𝔇_β(m; α − 2γ, α) + O(m^{−K−1} + m^{−2−(B+1)p} + m^{−1−(J+1)p}), μ_{m,j} = 2ζ(−jp)/(jm^{jp}) | PROVED-mod-cite by transfer (§2.3: each step is a REVIEWED step of Paper 2 / the Hurwitz chain H-a, H-d, G12, G1u, Hc, N.6 under the dictionary (n, δ, β′) ↦ (m, −γ, α − 2γ)); range 0 ≤ γ < (1 − \|α\|)/2 + REVIEWED (Rule R reviewer A) |
| Prop FI | *Frame identity.* For the integer layer B(n; β, ν) := Σ_kd_k(p, β, ν)n^{−k}: B(n + γ; β − 2γ, ν) = (1 + γ/n)^pB(n; β, ν) as formal series in 1/n, identically in (p, β, ν, γ) | PROVED-mod-cite (Lemma F + Theorem N.6 + uniqueness of asymptotic expansions + identity theorem; §3) + REVIEWED (Rule R reviewer A) |
| **Theorem Σ** | Conjecture Σ: b(n; β, ν)n^p/c = (n/N)^pF_p(N; ν²), N = n + (β + 1)/2, F_p β-free, as formal series, all orders, identically in (p, β, ν) | **PROVED-mod-cite (Lemma F (ii)) + REVIEWED** (Rule R reviewer A) |
| Cor Σ.1 | With Theorem R: the integer layer is even in N to all orders (f_odd = 0 for every odd order, in particular f₇ = 0) | PROVED-mod-cite (Theorem Σ, Theorem R) + REVIEWED (Rule R reviewer A) |
| Cor Σ.2 | The shift also holds for the zeta layers of weight 1 and 2 (μ₁, μ₂, μ₁²): 𝔇_β(n + γ; ν − 2γ, ν) = (1 + γ/n)^{(1+\|β\|_w)p}𝔇_β(n; ν, ν) for β ∈ {e₁, e₂, 2e₁} | PROVED-mod-cite (as Theorem Σ; separation argument §3.3) + REVIEWED (Rule R reviewer A; the 2e₁ layer also checked numerically by the reviewer). Weight ≥ 3: open (§3.3) |
| Checks | FI exact (orders ≤ 4, identically in (p, α, β, γ); 5 identities, 6 controls) and numerical (order 8, 32 points; zeta layer j = 1, 2 to order 6; 176 checks), with controls that fail; re-run by Rule R reviewer A (identical) | exact computer algebra / NUMERICAL (§5) |
| Remark C | Paper 2's Christoffel shift (sec_3) moves the Bessel order with the Szegő exponent (s ↦ s + p, i.e. (β, ν) ↦ (β + 1, ν + 1)); it is not the transformation Σ needs | PROVED (algebra) / OBSTRUCTION for that tool (§4) |

## 0. Answer

**Σ is proved (PROVED-mod-cite + REVIEWED, Rule R reviewer A), not by an exact transformation of the formal model, but by analysing the same
exact object twice.** The degree-n lattice problem Y can be steepest-descended in the frame of *any* real index m = n + γ: rescale by
m^p, normalise with e^{mg}, and absorb the mismatch z^{(n−m)σ₃} at infinity by the gauge z^{γσ₃} (principal power, cut (−∞, 0]). The
gauge's cut cancels the non-integer monodromy e^{−2πimσ₃} of e^{mφσ₃} on (−∞, 0) exactly (because n is an integer), multiplies the
band weight by x^{−2γ} (Szegő exponent α ↦ α − 2γ), and leaves on the hard-edge lips the constant phase e^{∓2πiγ} (because
e^{2mφ} = e^{∓2πim}e^{−4mf^{1/2}} there), which resets the Bessel order to α. So the m-frame produces the decoupled model
M(α − 2γ, α) at index m — the structure of Lemma H-d of JZC_M3a_Hd.md, with the phase coming from the non-integer index instead of the
Hurwitz offset. Both frames give asymptotic expansions of the same number b_n. Uniqueness of asymptotic expansions (p irrational
separates the integer layer from the zeta layers) gives the frame identity FI on an open set of (p, α, γ), and FI is an identity of
rational functions, so it holds identically. FI is Σ.

This removes the obstruction recorded in JZC_M4 §7 (caveat (c)) and JZC_M3a_Hd §5: there the m-frame problem was compared with the
n-frame problem *as models*, and their phases differ by ∫_n^{m}log φ(z(t/n)^p)dt, which is not a φ-power. Here the two models are never
compared directly; they are both expansions of b_n, and the finite-γ "absorption of the Bessel/Airy corrections" is automatic.

**The exact transformation asked for in task (1)** is the tautological gauge Ỹ = Yz^{γσ₃} (Ỹ₁ = Y₁, so b_n is unchanged) together with
the change of frame; at the level of the formal model alone we found no transformation relating M(β + 2, ν) at index n to M(β, ν) at
index n + 1 (§4.2), and Paper 2's Christoffel shift is not one (Remark C). **The step that carries the analysis** is Lemma F (ii), a
transfer of reviewed analytic estimates to a non-integer index; it is written step by step (§2.3) and was checked line by line by
Rule R reviewer A (REVIEW_JZC_SIGMA_A.md §B5–B8), for 0 ≤ γ < (1 − |α|)/2 (S1).

## 1. Setting and the statements

Notation of JZC_M4 §7 and JZC_M4_proof §1. For the lattice, α := (s − 1)/p − 1. The decoupled model M(β, ν): Bessel order ν in the
coefficients a_k(ν), b_k(ν) (DLMF 10.17.1, 10.17.8 as quoted in JZC_M4_proof §2), Szegő exponent β in ρ² = φ^{2(β+1)} at the hard edge
and φ^{−2(β+1)} at the soft edge. Its integer layer is B(n; β, ν) = Σ_{k≥0}d_k(p, β, ν)n^{−k}, d₀ = 1, each d_k is a rational function of (p, β, ν), for every k: the residue recursion of N.6b–c and
the extraction are field operations on the Laurent data of the circle jumps; these data are rational in p once c = 1 (JZC_M4_proof N.6d),
polynomial in ν (the DLMF a_k(ν), b_k(ν), polynomials in ν²), and polynomial in β, because β enters only through
ρ² = (w/2 + (1 + w²/4)^{1/2})^{2(β+1)} and its soft-edge analogue, binomial series of 1 + (series with zero constant term) raised to
the power 2(β+1) (m4_rh_exact2 l. 218; m4_shift_exact.py computes the same over ℚ(p, α, β) to order 4) (fixed per Rule R review A, S6). Its μ^β layers are 𝔇_β(n; β′, ν) (JZC_M4_proof §1; JZC_M3a_H §3.3 for
β′ ≠ ν). Weight |β|_w := Σ_j jβ_j. Theorem N.6(i) for the lattice: n^pb_n/c = Σ_{|β|≤B}μ_n^β𝔇_β(n; α, α) + O(n^{−K−1} + n^{−2−(B+1)p}
+ n^{−1−(J+1)p}) with μ_{n,j} = 2ζ(−jp)/(jn^{jp}).

**Conjecture Σ (JZC_M4 §7).** B(n; β, ν) = (n/N)^pF_p(N; ν), N := n + (β + 1)/2, with F_p independent of β (as formal series: the
re-expansion of B in 1/N, after multiplying by (N/n)^p, has β-free coefficients).

**Prop FI (frame identity).** For every γ: B(n + γ; β − 2γ, ν) = (1 + γ/n)^pB(n; β, ν), where the left side is re-expanded in 1/n.

*FI ⇔ Σ.* (⇐) With N′ := (n + γ) + (β − 2γ + 1)/2 = N: B(n + γ; β − 2γ, ν) = ((n + γ)/N)^pF(N) = (1 + γ/n)^p(n/N)^pF(N). (⇒) Fix a reference β₀ and, for a given β,
put γ := (β₀ − β)/2. FI at base β₀ and index n − γ gives B(n; β, ν) = (n/(n − γ))^pB(n − γ; β₀, ν). So (N/n)^pB(n; β, ν) =
(N/(n − γ))^pB(n − γ; β₀, ν), and n − γ = N − (β₀ + 1)/2 does not involve β: the right side is a fixed series in 1/N. ∎ (algebra; FI
is checked exactly to order 4 in sigma_frame_exact.out, Σ in m4_shift_exact.out.)

*Infinitesimal form.* d/dγ of FI at γ = 0: ∂_nB − 2∂_βB = (p/n)B, the flow identity of JZC_M4 §7 ("Mechanism"); it is FI's
generator (FI is its integrated form, by the Taylor expansion in γ coefficientwise in 1/n, all terms being polynomial in γ).

## 2. Lemma F: the m-frame of the degree-n lattice problem

### 2.1 Set-up
Fix p > 1, s ∈ (1, 1 + 2p) (|α| < 1), an integer n ≥ n₀ and a real γ with 0 ≤ γ < (1 − |α|)/2 (γ = −δ with −1 < δ ≤ 0, the range of the cited H-d/G12/G1u statements; γ < 0 is expected to work — the H-a obstruction (phantom node) does not occur in the m-frame — but is not covered by any reviewed statement and is not used) (fixed per Rule R review A, S1); put m := n + γ > 0 and α̃ := α − 2γ (so
|α̃| < 1 as well; this is a convenience, see Rule A item 7). All Paper 2 objects with the subscript m are Paper 2's objects with the
parameter n replaced by the real number m, **except the degree, which stays n**:
- U_m(z) := m^{pnσ₃}Y(zm^{−p}) (Paper 2 (eq:U) with the scale m^p). Lemma interp's proof is a substitution: U_m is analytic off
  {X_k} ∪ {0} with X_k := (m/k)^p, Res_{X_k}(U_m)_{j2} = m^pw_k(U_m)_{j1}(X_k), U_mz^{−nσ₃} = I + U₁/z + … for |z| > m^p, and
  𝖻(U_mz^{−nσ₃}) = m^{2p}b_n² (Lemma invariance with the constant m^{pnσ₃}; the factor m^{jp} from the substitution).
- t_m(z) := mz^{−1/p}, θ := πt_m (t_m(X_k) = k: the nodes are the lattice nodes, labelled by the same integers), g the lattice
  g-function (Paper 2 (eq:g)) in the variable z, φ := γ_p − g, φ̃ := φ ± iθ/m. Since θ/m = πz^{−1/p}, φ̃ does not depend on m
  (Paper 2's remark after (eq:g)), and Lemma gfunction holds verbatim with m: g₊ − g₋ = 2iθ/m on (4c, ∞) because
  μ*((x, ∞)) = x^{−1/p} = t_m(x)/m.
- The gauge: **Ũ := C·U_mz^{γσ₃}·C^{−1}, C := m^{pγσ₃}** (principal z^γ, cut (−∞, 0]). Since C is constant and diagonal and commutes
  with z^{γσ₃}, Ũz^{−mσ₃} = C(U_mz^{−nσ₃})C^{−1} → I, and 𝖻(Ũz^{−mσ₃}) = 𝖻(U_mz^{−nσ₃}) = m^{2p}b_n² (Lemma invariance).
- Residues: Ũ_{j1} = (c_j/c₁)(U_m)_{j1}z^{γ}, Ũ_{j2} = (c_j/c₂)(U_m)_{j2}z^{−γ} (C = diag(c₁, c₂), c₁/c₂ = m^{2pγ}), so
  Res_{X_k}Ũ_{j2} = (c₁/c₂)X_k^{−2γ}m^pw_kŨ_{j1}(X_k). With X_k^{−2γ} = m^{−2pγ}k^{2pγ} and w_k = k^{−s} this is
  **Res_{X_k}Ũ_{j2} = m^pk^{−s̃}Ũ_{j1}(X_k), s̃ := s − 2pγ**: the residue condition of the lattice σ_{p,s̃} in the m-frame. Paper 2
  Lemma bandweight then gives W̃ := 2iθ′w̃ = 𝗐̃_mz^{α̃}, w̃ := m^pt_m^{−s̃}, 𝗐̃_m := −(2πi/p)m^{1+p−s̃}, α̃ = (s̃ − 1)/p − 1 = α − 2γ.
- Ũ has one jump that U_m does not have: Ũ₊ = Ũ₋e^{2πiγσ₃} on (−∞, 0) (z₊^γ/z₋^γ = e^{2πiγ}).

Run Paper 2 §5 Steps 1–4 on Ũ with W̃, κ_±, L_±, A_±, A^△_± built from θ (= πt_m) and W̃, Step 2 as T := e^{−mγ_pσ₃}Re^{mφσ₃}, and in
Step 4 the outer scalar F_m := Paper 2's F (Lemma outer, p > 1: F = DBK) built with t_m: D = κ_±e^{−j(t_m)}, B the Binet-cut scalar
(eq:B) with t_m, K = (4c − z)^{−1/2}. Call the result V_m, and Q_m := D_∞^{−σ₃}V_mD_{W̃}^{σ₃} with D_{W̃} the Szegő function of
W̃₀ := W̃/F̃_m² = 𝗐̃_mz^{α̃}(4c − z)H_m (Paper 2 (eq:W0); H_m := (e^{−j(t_m)}B)^{−2}).

### 2.2 Lemma F (i): the jumps (PROVED)
Paper 2's proof of Lemma jumpsV computes M₋^{−1}M₊ from (eq:VM) and uses only: (eq:identities), Lemma gfunction (i), (O1)–(O2), and
in (g) the integrality of the degree. With m in place of n, every identity in (a)–(f) is the same algebra (none of them uses n ∈ ℤ:
(a) uses φ₊ = −φ₋ on the band; (b), (c), (e), (f) use κ_± − 1 = e^{∓2iθ}κ_± and e^{∓2iθ}e^{−2mφ} = e^{−2mφ̃}; (d) uses
e^{m(φ₊−φ₋)}F₊/F₋ = e^{−2iθ}e^{2iθ}, i.e. m(g₊ − g₋) = 2iθ on (4c, ∞), true for real m by §2.1). So V_m has the jumps (a)–(f) of
Lemma jumpsV with n ↦ m and W₀ ↦ W̃₀. The only change is (g):
- **(g′) On (−∞, 0):** the jump of V_m is (e^{mφσ₃})₋^{−1}e^{2πiγσ₃}(e^{mφσ₃})₊ (F_m has no jump there, (O1); app_outer L binetcut (iv), (O1): F = DBK is analytic
  and zero-free off [0, ∞); D's jump e^{i𝔟} on (−∞, 0) is cancelled by B, and the proof uses n only as the real scale in t (fixed per
  Rule R review A, S2)), and φ₊ − φ₋ = −(g₊ − g₋) =
  −2πi (Lemma gfunction (i)), so it equals e^{2πiγσ₃}e^{−2πimσ₃} = e^{−2πinσ₃} = **I**, because n is an integer. On
  (m^p + δ′, ∞) there is no jump, as in Paper 2 (g).
- **Normalisation** (Paper 2 Lemma normalisation with m): near ∞, V_m = C_∞e^{−mγ_pσ₃}(Ũz^{−mσ₃})(z^me^{mφ}F_m)^{σ₃}, and
  z^me^{mφ}F_m = e^{mγ_p}·(F_m^{−1}e^{m(g − Log z)})^{−1}. Paper 2's proof that ϰ_∞ := F^{−1}e^{m(g − Log z)} is analytic at ∞ with
  ϰ_∞(∞) ≠ 0 uses: g − Log z → 0 (Lemma gfunction (ii)), g − Log z has no jump on (−∞, 0) (for *every* real m the factor e^{m(g − Log z)}
  has none, since g and Log z jump by the same 2πi), and F₊/F₋ = e^{2iθ} = e^{m(g₊−g₋)} beyond the top node (§2.1). All hold.
- **Hard-edge lips.** Paper 2 Lemma signs (iii): φ = ∓iπ − 2f^{1/2} in U(0, 2δ₀) ∩ ℂ_±, f independent of the parameter. Hence
  **e^{2mφ} = e^{∓2πim}e^{−4mf^{1/2}} = e^{∓2πiγ}e^{−4ζ^{1/2}}**, ζ := m²f, n ∈ ℤ. (Paper 2 (eq:he-ephi) is the case γ = 0.) In the
  Q-frame the lip jump [[1, 0], [(D_{W̃}²/W̃₀)e^{2mφ}, 1]] + super-small (Lemma jumpsV (b) conjugated by D_{W̃}^{σ₃}) is therefore
  [[1, 0], [ω♮e^{−4ζ^{1/2}}, 1]] + E with **ω♮ := ω^{(α̃)}e^{∓2πiγ}**, ω^{(α̃)} := D_{W̃}²/W̃₀.
- **Band limits.** ω^{(α̃)} → c_± = e^{∓iπα̃} at 0 along the lips (Paper 2 Notation, c_± = e^{∓iπ(exponent)}; JZC_M3a_H_G1u L1 (ii)
  for every real exponent). So ω♮ → e^{∓iπα̃}e^{∓2πiγ} = e^{∓iπ(α̃ + 2γ)} = **e^{∓iπα}**: the lip data of the order-α Bessel model
  (Paper 2 (eq:he-Phi-jumps)), glued to the Szegő function of x^{α̃}.
- **Soft edge.** In U(4c, ε) every jump is written with φ̃ (Lemma signs (iv); the lips avoid U(4c, h₀), Lemma lips (c)), and φ̃ is
  m-free; there is no phase. The soft-edge data are those of the α̃-lattice: φ^{−2(α̃+1)} (as in JZC_M3a_Hd (iii)).

**Dictionary.** These are exactly the jumps of JZC_M3a_Hd Lemma H-d (ii)–(iii) (frame 1, REVIEWED) with
(n, δ, β′) ↦ (m, −γ, α − 2γ) (there ω♮ = ω^{(β′)}e^{±2πiδ} with β′ = α + 2δ; here ω^{(α̃)}e^{∓2πiγ} with α̃ = α − 2γ), except that the
Hurwitz-specific phases on Σ_v, the saturated segment and Σ^△ (θ_δ ≠ θ) are absent here: θ is the lattice's. On Σ^△ and the top segment
(away from U(0, δ)) only |e^{2mφ}| enters the bounds, as in H-d (ii). ∎

### 2.3 Lemma F (ii): the analytic inputs (PROVED-mod-cite by transfer, 0 ≤ γ < (1 − |α|)/2; REVIEWED, Rule R reviewer A)
The Hurwitz chain proves Theorem H (i) (JZC_M3a_H.md §4: PROVED-mod-cite + REVIEWED for p > 1) from the jump structure of H-d plus
fixed-n analytic inputs. Each input is listed with the reason it transfers to (Ũ, m).

| input (Hurwitz chain) | what it uses | transfer to the m-frame |
|---|---|---|
| H-a (JZC_M3a_H_Ha): interpolation, node masses, top node | Paper 2 L interp, t ↦ t − δ | Not needed in modified form: our nodes are the lattice nodes, top node X₁ = m^p (Paper 2 with n ↦ m; t_m(X₁) = 1). Lemma interp: §2.1. |
| G12 §1 / H-b: outer scalar (O1)–(O5) | j(t), Binet cut B, K = (4c − z)^{−1/2}; the parameter n only through t = nz^{−1/p} and the top node n^p | F_m is Paper 2's F with t_m: (O1)–(O4) are statements about t ↦ j(t), κ(θ) and the Cauchy integral (eq:B), whose density 𝔟 is a function of t on (−∞, 0); with y ↦ (m/n)^py the integral is the n-frame one up to the additive normalisation constant, so B_m(z) = B_n((n/m)^pz)·exp(c_{n,m}), c_{n,m} independent of z (substitute y′ = (n/m)^py in (eq:B); 𝔟_m(y) = 𝔟_n((n/m)^py)) (fixed per Rule R review A, S4), and H_m(z) = const·H_n((n/m)^pz). (O5) is a fixed-index statement with the top node at m^p. No integrality of n is used (Lemma outer's proof, app_outer.tex §p > 1). |
| G12 §2 / H-b′: a-priori bound \|Q\| ≤ C\|z\|^{−\|α\|/2−η} (column factorisation) | Paper 2 App C from the Cauchy-sum form of U; G := (−z)^{−δ}D_{x^{2δ}} bounded above and below (G12 L2.3) | U_m is U rescaled (fixed n), so App C's bound for U_m is Paper 2's. The columns of Q_m are those of U_m times z^{±γ}(F_mD_{W̃})^{±1}, and z^γD_{x^{−2γ}} = (Υ/4c)^{γ} up to a unimodular constant in ℂ_± (Paper 2 L szego (i)), bounded above and below near 0 (Υ(0) = −4c): G12 L2.3 with δ = −γ. The exponent stays \|α\|/2. In the lens, the m-frame lens factor is built with W̃ = const·z^{−2γ}W, and R̃_{j2} = Ũ_{j2} − Ũ_{j1}W̃e^{−2iθ}κ₊ = (c_j/c₂)z^{−γ}R_{j2}, where R is the lens transform of U_m with W, to which Paper 2 L lenssector applies at fixed n (nodes at t_m ∈ ℕ, arcs at t_m ∈ ℕ + ½). Hence the lens columns of Q_m are Paper 2's lens columns (U_{·1} ∓ R_{·2}/W)e^{mφ}F̃_mD_W and R_{·2}e^{−mφ}(F̃_mD_W)^{−1} times (z^γD_{x^{−2γ}})^{±1}, and Prop apriori (i) holds with exponent \|α\|/2 (fixed per Rule R review A, S3). |
| G1u L1–L4, Prop G1u (A), (B): hard-edge comparison, Bessel order α with Szegő exponent β′, order-K small norm | the Q-frame jumps near 0: band J, lips ω♮e^{−4ζ^{1/2}}, ζ = n²f; ρ♮ = ρ^{(α)}/G; L4 from the a-priori bound | Identical Q-frame data with (n, δ, β′) ↦ (m, −γ, α̃) (§2.2). G1u never uses n ∈ ℤ in the Q-frame: n enters only through ζ = n²f and (2πn)^{σ₃/2} (L2), and G1u L2 states the V-frame form with (−1)^ne^{nφσ₃}, which in our frame is replaced by the identity of §2.2, e^{2mφ} = e^{∓2πiγ}e^{−4ζ^{1/2}}. "For every real β′" covers α̃. |
| Hc (JZC_M3a_H_Hc), E3 Lemmas F.1′, E3.4–E3.5: band factor H = exp(−Σμ_kz^k)(1 + O(n^{−(K+1)p})), gauge on the circles | Binet-cut moments, t = nz^{−1/p} | H_m(z) = const·H_n((n/m)^pz) (row 2), and the moments are homogeneous: μ_{n,k}(n/m)^{kp}z^k = μ_{m,k}z^k with μ_{m,k} = 2ζ(−kp)/(km^{kp}) — the unscaled times t_k = −2ζ(−kp)/k of JZC_M4 §8 are frame-free. E3 F.1′'s proof uses n only through t₊ = nr^{−1/p}e^{−iπ/p} and the Γ-integral with a_n = 2πin e^{−iπ/p}, both valid for real m > 0 (fixed per Rule R review A, S4). |
| JZC_M4_proof N.6a–c, Theorem N.6 (i) for M(β, ν) (JZC_M3a_H §3.3, G5; E3.7 for M(β, ν): m3a_e37_decoupled, REVIEWED) | circle jumps Δ_k(β, ν), small norm, residue recursion, extraction | Verbatim with n ↦ m: the expansion parameter of N.6a is the Bessel/Airy scale ζ^{1/2} = mf^{1/2}, ξ = −mφ̃, and all inputs above. |

**Conclusion of Lemma F.** For p > 1, |α| < 1, 0 ≤ γ < (1 − |α|)/2 (fixed per Rule R review A, S1) and every K, B, J:

  m^pb_n/c = Σ_{|β|≤B}μ_m^β𝔇_β(m; α − 2γ, α) + O(m^{−K−1} + m^{−2−(B+1)p} + m^{−1−(J+1)p}),   m = n + γ.   (F)

(This is Theorem H (i)'s statement with (n, δ) ↦ (m, −γ) and the lattice band factor. At γ = 0 it is Theorem N.6 (i).)

*Label.* (F) is PROVED-mod-cite with the same citation base as Theorem H (i) (Paper 2 as quoted in those memos; DLMF as quoted in
JZC_M4_proof §2; the REVIEWED memos). The transfer table is an argument, not a re-proof; Rule R reviewer A checked rows 2–5 against
app_outer.tex, app_c.tex, sec_5–7 and JZC_M3a_H_G1u.md / E3 line by line (REVIEW_JZC_SIGMA_A.md §B5–B8) and accepted it with fixes
S1–S4 (applied): **PROVED-mod-cite + REVIEWED** for 0 ≤ γ < (1 − |α|)/2.

## 3. Proof of Prop FI and Theorem Σ

### 3.1 Two expansions of one number
Fix p ∈ (1, 2) ∖ ℚ, α ∈ (−½, ½), γ ∈ (0, ¼) (fixed per Rule R review A, S1). For integer n → ∞, Theorem N.6 (i) (n-frame) and (F) (m-frame, multiplied by (n/m)^p)
both give n^pb_n/c as a finite sum of terms c·n^{−e} plus a remainder:
- n-frame: exponents e = k + |β|_wp, coefficients from 𝔇_β(n; α, α)μ̂^β (μ̂_j := 2ζ(−jp)/j, so μ_{n,j} = μ̂_jn^{−jp});
- m-frame: (n/m)^pμ_m^β𝔇_β(m; α − 2γ, α) = μ̂^βn^{−|β|_wp}·(n/m)^{(1+|β|_w)p}𝔇_β(m; α − 2γ, α), and (n/m)^{(1+|β|_w)p} and m^{−k} are
  convergent series in 1/n for n > |γ|; so again exponents k + |β|_wp.

Given E > 0, choose K > E, B and J with 2 + (B + 1)p > E, 1 + (J + 1)p > E. Both remainders are then o(n^{−E}) (for fixed γ; the constants in (F) may depend on γ, which is
harmless since the coefficient identity is extracted separately for each γ) (fixed per Rule R review A, S5). Since p is irrational, the
exponents k + jp (k, j ∈ ℕ₀) are pairwise distinct, finitely many lie below E, and {n^{−e}} is an asymptotic scale along integers; two
finite sums Σc_en^{−e}, Σc′_en^{−e} that agree up to o(n^{−E}) have c_e = c′_e for e < E (induction on the smallest exponent). For e = k
∈ ℕ₀ (j = 0) only β = 0 contributes on both sides. Hence, coefficientwise in 1/n up to every order:

  (1 + γ/n)^{−p}B(n + γ; α − 2γ, α) = B(n; α, α)   i.e.   B(n + γ; α − 2γ, α) = (1 + γ/n)^pB(n; α, α).   (FI₀)

### 3.2 From an open set to an identity
The coefficient of n^{−k} in B(n + γ; α − 2γ, α) − (1 + γ/n)^pB(n; α, α) is Σ_{i≤k}d_i(p, α − 2γ, α)C(−i, k − i)γ^{k−i} −
Σ_{j≤k}C(p, j)γ^jd_{k−j}(p, α, α), a rational function R_k(p, α, γ) (d_i rational, §1). By §3.1 it vanishes on
((1, 2)∖ℚ) × (−½, ½) × (0, ¼) (still an open set in (α, γ); fixed per Rule R review A, S1). Write R_k = N_k/D_k with
N_k, D_k ∈ ℚ[p, α, γ], D_k ≢ 0. For all but finitely many p ∈ (1, 2)∖ℚ, D_k(p, ·, ·) ≢ 0, so N_k(p, ·, ·) vanishes on a non-empty open
subset of (α, γ) and is the zero polynomial; each coefficient of N_k as a polynomial in (α, γ) is then a polynomial in p with infinitely
many zeros, so N_k ≡ 0 and R_k ≡ 0 (fixed per Rule R review A, S7). So (FI₀) holds identically in (p, α, γ).

Rename α ↦ ν and write γ = (ν − β)/2: (FI₀) reads B(n₀ + (ν − β)/2; β, ν) = ((n₀ + (ν − β)/2)/n₀)^pB(n₀; ν, ν) for every β.
Define F_p(N; ν) := (N/n₀)^pB(n₀; ν, ν) with n₀ := N − (ν + 1)/2, re-expanded in 1/N (β does not occur). For any β put
m := n₀ + (ν − β)/2 = N − (β + 1)/2; then B(m; β, ν) = (m/n₀)^pB(n₀; ν, ν) = (m/N)^pF_p(N; ν), which is Σ with F_p independent of β
(all re-expansions are between formal series in 1/m, 1/n₀, 1/N, which differ by constants, so they are invertible). ν enters F only through ν² because
a_k, b_k are polynomials in ν² (DLMF 10.17.1, 10.17.8) and β is now gone (JZC_M4 §7). This proves **Theorem Σ**, and FI for general base
β follows by the "(⇐)" computation of §1. ∎

**Cor Σ.1 (evenness).** JZC_M4 §7 Corollary, now unconditional on Σ: Theorem R (d_k(−β − 2, ν) = (−1)^kd_k(β, ν), PROVED) with Theorem Σ
gives F_p(N′) = F_p(−N′). So f_{2k+1} = 0 for all k, the integer layer is a function of (p, ν², N²), f_{2k} is a polynomial in ν² (degree k
is the observed pattern, not proved here), and the lattice's −Z(0) = ½ is the Szegő part of N.

### 3.3 The zeta layers (Cor Σ.2)
§3.1 also identifies, for each weight J ≥ 1, the coefficient of n^{−k−Jp}:
Σ_{|β|_w=J}μ̂^β[X_β]_k = 0, X_β := (n/m)^{(1+J)p}𝔇_β(m; α − 2γ, α) − 𝔇_β(n; α, α) (re-expanded), [·]_k its n^{−k} coefficient.
- J = 1: only β = e₁; μ̂₁ = 2ζ(−p) ≠ 0 for p ∈ (1, 2) (the real zeros of ζ are −2, −4, …, and −p ∈ (−2, −1)), so X_{e₁} = 0. The engine's μ_j enters as c^jμ_j (JZC_M4_proof §5), a common factor of all β of weight J.
- J = 2: β ∈ {e₂, 2e₁}: μ̂₂[X_{e₂}]_k + μ̂₁²[X_{2e₁}]_k = ζ(−2p)[X_{e₂}]_k + 4ζ(−p)²[X_{2e₁}]_k = 0 on (1, 2)∖ℚ, hence, both sides being real-analytic in p on (1, 2) off the finitely many poles of the rational factors
  [X]_k (rational in p after removing the common factor c(p)²), on all of (1, 2) minus those poles (fixed per Rule R review A, S8). If [X_{e₂}]_k ≢ 0, then ζ(−2p)/ζ(−p)² would equal a rational function of p on (1, 2), hence on
  ℂ minus poles (both sides meromorphic in p); but ζ(−2p)/ζ(−p)² vanishes at every odd integer p ≥ 1 (ζ(−2p) = 0 there, ζ(−p) =
  −B_{p+1}/(p+1) ≠ 0), infinitely many zeros. So [X_{e₂}]_k ≡ 0, and then [X_{2e₁}]_k ≡ 0.
- Then §3.2's argument in (α, γ) (on ((1, 2)∖ℚ) × (−½, ½) × (0, ¼); fixed per Rule R review A, S1) gives 𝔇_β(n + γ; ν − 2γ, ν) = (1 + γ/n)^{(1+|β|_w)p}𝔇_β(n; ν, ν) for β ∈ {e₁, e₂, 2e₁}.

For J ≥ 3 the separation needs the monomials Πζ(−jp)^{β_j} (|β|_w = J) to be linearly independent over ℚ(p); we do not prove this
(§7). (A route that avoids it: run Lemma F for the Toda-tilted measures of JZC_M4 §8 Theorem T, which make the μ's free parameters.)

## 4. What the requested tools give

### 4.1 Remark C: Paper 2's Christoffel shift (sec_3, Theorem shift)
Paper 2 (eq:shift-identity): x·σ_{p,s,ℓ} = σ_{p,s+p,ℓ}, and Lemma transfer: J(σ) = LU, J(xσ) = UL with u_n = −P_{n+1}(0)/P_n(0). The
exponent α = (s − 1)/p − 1 moves to α + 1, and by Lemma bandweight (W = 𝗐_nz^αr_n) this is the *local* exponent at the hard edge:
the Bessel order moves with the Szegő exponent, (β, ν) ↦ (β + 1, ν + 1), at the same degree. It relates M(α, α) and M(α + 1, α + 1)
through the unknown chain sequence u_n, not M(β, ν) and M(β + 2, ν). Any polynomial (Christoffel/Geronimus/Uvarov) modification of the
measure that is regular and non-zero at 0 leaves both exponents unchanged, and one that changes the local power at 0 changes ν. So no
modification of the measure alone moves β with ν fixed; the decoupling needs the lip phase of §2.2 (or of H-d). (OBSTRUCTION for that
tool; heuristic in the last sentence, which is not used.)

### 4.2 An exact transformation of the formal model?
The formal model M(β, ν) at index n is the residue recursion with jumps Δ_k(β, ν)n^{−k} on fixed circles. A transformation taking
(n, β) to (n + γ, β − 2γ) would have to act on the *frames*: in the genuine problem the two frames are related by z ↦ (m/n)^pz and by the
phase difference (n + γ)Φ(((n + γ)/n)^pz) − nΦ(z) = −2∫_n^{n+γ}log φ(z(t/n)^p)dt (Lemma BR integrated, JZC_M3a_Hd §5), which is not a
φ-power and has a nontrivial 1/n expansion (the "δ² defect" of JZC_M4 §7). We did not find a formal (model-level) transformation,
and none is needed: §3 uses only that both frames are valid for the same exact problem. (OBSTRUCTION for a model-level proof: recorded,
not a claim that none exists.) The exact statement at the level of the genuine problem is the tautology Ỹ = Yz^{γσ₃}: Ỹz^{−(n+γ)σ₃} =
Yz^{−nσ₃}, so Ỹ₁ = Y₁; for γ = 1 this is, formally (x^{−2}σ need not be finite), the Geronimus-type statement that zπ_n(z) is orthogonal to x, …, x^n
in L²(x^{−2}σ). The content
of Lemma F is that the steepest descent of Ỹ at index n + γ is legitimate.

## 5. Checks

**sigma_frame_exact.py / .out** (exact computer algebra; the engine of m4_shift_exact.py imported unchanged, field ℚ(p, α, β, γ), c = 1;
sha256 lines in the output). Coefficientwise in 1/n, orders 0..4 (KORD = 4, series cap SHI = 18; the engine's guard asserts that every
principal part is determined at that cap, and [5] confirms agreement with the reviewed SHI = 30 run):
- [1] FI₀, identically in (p, α, γ); [2] FI with general base β, identically in (p, α, β, γ); [3] the flow identity
  ∂_nB − 2∂_βB = (p/n)B, identically; [4] at the Bessel point (p, α, β) = (2, −½, −½): B(n) = (n/N)²(1 − 1/(4N²))^{−1/2}, N = n + ¼
  (JZC_M4 Prop N.2), d₀..d₄ = 1, −½, 5/16, −3/16, 31/256; [5] the natural form at general β has f₁ = f₃ = 0 and f₂, f₄ equal to the closed
  forms of m4_shift_exact.out.
- Controls (each must fail at some order ≤ 4, asserted), with the first failing order and residual: C1 half Szegő shift β = α − γ
  (order 1, −pγ/2); C2 wrong sign β = α + 2γ (order 1, −2pγ); C3 no frame factor (order 1, pγ); C4 no index shift, i.e. the gauge alone
  at fixed degree (order 1, pγ); C5 Bessel order moved with β, ν = β = α − 2γ (order 2, γ(α − γ)(p + 2)/2 — the f₂ term (p + 2)ν²/8);
  C6 frame factor (1 + γ/n)^{2p} (order 1, −pγ).
- Result: **ALL IDENTITIES HOLD, ALL CONTROLS FAIL** (5 identities, 6 controls). The engine run itself is logged in
  sigma_frame_exact_fresh.out (588 s on a loaded machine, by the previous version of the script, which lacked [5]; it wrote the d_k cache
  <repo>/tmp/sigma_cache/d_K4_SHI18_c5bf8bb1a9743a07.txt that the final run, sigma_frame_exact.out, reads; delete it to recompute).

**sigma_frame_num.py / .out** (NUMERICAL, mpmath 40–50 digits, engine m4_rh4.py imported unchanged, KORD = 8, SHI = 56):
- FI₀ to order 8 at p ∈ {1.7, 0.6, 3.2, √2}, ν ∈ {0.3, −0.45}, γ ∈ {0.37, −0.21, 1, 2.5} (32 points; γ = 1 is the integer case with no
  lip phase, γ = 2.5 is outside Lemma F's range — FI is an algebraic identity and holds there too): residuals 2·10⁻³⁹–2·10⁻³³ relative
  (largest at γ = 2.5, where the coefficients grow like γ^k).
- Controls at every point (half shift, no index shift, no frame factor, ν moved): relative residuals 0.049–4.0·10³ (must exceed 10⁻⁶).
- First-order zeta layer j = 1, 2 (central differences in μ_j, h = 10⁻¹⁵, KORD = 6, dps 50) at p ∈ {1.7, 0.6}, ν = 0.3,
  γ ∈ {0.37, −0.21}: 𝔇_{e_j}(n + γ; ν − 2γ, ν) = (1 + γ/n)^{(j+1)p}𝔇_{e_j}(n; ν, ν), residuals 10⁻²⁷–10⁻³⁰ (the central-difference
  error); the control "frame factor (1 + γ/n)^p" fails (0.07–0.46).
- Count: **ALL 176 CHECKS PASSED** (32 points × (1 identity + 4 controls) + 8 zeta points × (1 identity + 1 control)).
  At p = 1.7 and √2 (p > 1, inside Lemma F's range for γ = 0.37 (γ = −0.21 tests the algebraic identity only; fixed per Rule R review A, S1)) the check is a check of FI where Lemma F applies; the other
  points test the algebraic identity, which by §3.2 holds for every p.
- The 2e₁ layer (second order in μ₁) is checked numerically by Rule R reviewer A (REVIEW_JZC_SIGMA_A.md §D), not by this note's
  scripts (fixed per Rule R review A, S8).

What the checks do and do not show (Rule X). FI at finite order is algebraically equivalent to Prop S at that order (§1), so the checks
re-confirm Prop S in the frame-identity form (with independent controls for the frame bookkeeping: C3, C4, C6 test the (1 + γ/n)^p factor
and the index shift that Lemma F predicts). They do not test Lemma F (ii); that is analysis, and its numerical support is the existing
Hurwitz-chain evidence for the same jump structure (m3a_g1u_hardedge.out: the Q-frame hard-edge problem with lip phase and Szegő exponent
β′ ≠ ν, 110 checks; m3a_hd_model.out) plus the lattice fits of N.6 (m4_f4_lattice.out), which FI then transports.

## 6. Rule A (adversarial pass) — log

1. *Does the argument prove too much?* Applied with the Bessel order also moving, it would give C5, which fails exactly (§5) and is
   excluded by the Hurwitz data (H2 of JZC_M3a_Hd §4). Lemma F does not move ν: the lip phase e^{∓2πiγ} restores it. Checked the sign:
   with e^{±2πiγ} instead, the band limit would be e^{∓iπ(α−4γ)}, i.e. the model M(α − 2γ, α − 4γ), which cannot satisfy FI as well
   (FI with ν = α holds identically, and d₂ depends on ν through (p + 2)ν²/8); the sign follows from
   φ = ∓iπ − 2f^{1/2} in ℂ_± (Paper 2 L signs (iii), quoted proof: "φ = −iπ − 2f^{1/2} in U(0, 2δ₀) ∩ ℂ₊").
2. *(−∞, 0) cancellation.* z₊^γ/z₋^γ = e^{2πiγ} (arg z = ±π); e^{mφ} jumps by e^{−2πim} (φ₊ − φ₋ = −2πi). Product e^{−2πin} = 1. If n were
   not an integer this would fail: the argument uses that the *degree* is an integer and only the frame index is real. ✓.
3. *Integer γ.* γ = 1: m = n + 1, lip phase 1, Szegő exponent α − 2, Bessel α; the band limit e^{∓iπ(α−2)} = e^{∓iπα}: consistent. The
   numerical FI holds at γ = 1 (§5).
4. *Is the m-frame equilibrium the right one?* Yes: the lattice equilibrium is self-similar; in the variable z of the m-frame it is the
   same μ* (Paper 2 (eq:g) does not depend on n), and the constraint μ* ≤ λ_p with saturation on (4c, ∞) is a statement about the node
   density in z, which is m-free (t_m/m = z^{−1/p}). The n-frame and m-frame differ only in which z the nodes X_k = (m/k)^p sit at.
5. *Uniqueness step.* Needs the two expansions along the same sequence (integer n) with remainders o(n^{−E}) after finitely many terms:
   both (N.6 (i), (F)) have that form; (n/m)^{(1+J)p} is a convergent series for n > |γ|. Distinct exponents need p ∉ ℚ; rational p is
   recovered by §3.2 (rationality in p). Tried p = 3/2 directly: exponents collide (n^{−4} from d₄ and n^{−1−2p} from the μ₂ layer), so the restriction
   is necessary for the direct argument, not for the result.
6. *Rationality of d_k.* Each d_k is rational in (p, β, ν) for every k: the residue recursion and extraction are field operations
   on circle-jump data that are rational in p (c = 1), polynomial in ν and in β (binomial series in 2(β + 1)) (§1); the exact engine
   confirms it to order 4 (m4_shift_exact.py, field("p,alpha,beta")). The substitution β = α − 2γ keeps it rational (fixed per Rule R
   review A, S6). The identity theorem for rational functions on open sets is elementary.
7. *Range of γ.* 0 ≤ γ < (1 − |α|)/2 keeps |α̃| < 1 and δ = −γ ∈ (−1, 0], the range of the cited H-d/G12/G1u statements. Only an
   open set is needed (fixed per Rule R review A, S1).
8. *Constants.* The constants m^{pnσ₃}, C = m^{pγσ₃}, 𝗐̃_m, C_∞ are diagonal (or scalar) and constant; 𝖻 is invariant (Paper 2 L invariance). The
   extraction in the m-frame gives m^{2p}b_n², hence the factor (n/m)^p in (F).
9. *Hidden use of n ∈ ℤ elsewhere.* Searched Paper 2 sec_5–7, app_outer, app_c and the Hurwitz memos for (−1)^n, e^{2πin}, "integer":
   the only uses are jumpsV (g) and (eq:he-ephi)/(eq:he-P0) (the (−1)^n of P̃₀), both handled in §2.2; G1u L2 inherits (−1)^n only
   in the V-frame form of P₀♮, and its Q-frame statement (the one used) is phase-explicit.
10. *Circularity (Rule X).* Lemma F uses no output of the model engine; the checks use the engine only to confirm the algebraic
   consequence. Prop S was not used in §3.

## 7. What remains

1. ~~Rule R review of Lemma F (ii)~~ Done 2026-10-22: REVIEW_JZC_SIGMA_A.md, ACCEPT WITH FIXES, S1–S8 applied; Theorem Σ is
   PROVED-mod-cite + REVIEWED. Optional: γ < 0 in Lemma F (not needed; not covered by a reviewed statement, S1).
2. Zeta layers of weight J ≥ 3 (and mixed second-order layers beyond 2e₁, e₂): need either linear independence of Πζ(−jp)^{β_j} over ℚ(p)
   or Lemma F for Toda-tilted measures (Theorem T's frame).
3. The diagonal coefficient: the same argument applies to n^pa_n via the 𝖺-functional (also invariant, Paper 2 L invariance), giving the
   shift of JZC_M4 §8 (A β-free in M = N + ½) once the order-K expansion of n^pa_n is written for M(β, ν) (Theorem N.6 is stated for b_n
   only). Not done here.
4. Consequences (propagated 2026-10-22 to JZC_M4.md, JZC_M4_proof.md, JZC_M3a_H.md; Paper 2/IV texts under papers/ not edited): JZC_M4 §7 (Conjecture Σ → Theorem Σ, label as above), JZC_M4 §4 Open
   ("Proofs of evenness"), JZC_M3a_H Theorem H (ii) (the natural form beyond the exact orders: integer layer and J ≤ 2 zeta layers now
   PROVED-mod-cite + REVIEWED), JZC_M4 Prop N.3 (f₇ = 0: from NUMERICAL to PROVED-mod-cite via Cor Σ.1).
5. KORD ≥ 5 exact runs of sigma_frame_exact.py (not attempted: the engine needed 588 s for KORD = 4 on the shared machine, and order 6
   did not finish in earlier runs). They would only re-confirm Prop S; Theorem Σ does not depend on them.

## 8. Literature (Rule L) — not done
Novelty UNCHECKED. The mechanism (an exact gauge z^{γσ₃} at the hard edge plus a second, non-integer steepest-descent frame) was not
searched for. NOVELTY_JZC item N records Bleher–Its 2005 Thm 5.2 (evenness via string equations for varying weights) as the nearest
known phenomenon; it was not re-read for this note.
