# 15. Statistical mechanics and sampling

Molecular simulation · Boltzmann weights · averages · uncertainty · free energy

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Connect Boltzmann weights and ensembles to observable averages.
- Recognise correlated samples, sampling uncertainty, and the distinction between potential energy and free energy.

## Planned short videos

1. From one structure to an ensemble
2. Why a long trajectory may still sample poorly

## Planned exercise

Calculate populations for a simple two-state model, then discuss how correlated simulation samples affect uncertainty.

## Ask AI when you get stuck

Practise asking a precise question, examining the explanation, and checking your understanding.

**Example-answer provenance:** The example answers are course-authored teaching examples, not recorded responses from a named external model.

Use ChatGPT or another AI tutor, and record the tool, model name shown in the app, and date when you try a question.

### Build a useful question

1. **What I know:** State your level and the part you already understand.
2. **Where I am stuck:** Identify one confusing term, step, result, or contradiction.
3. **My evidence:** Include the relevant molecule, method, basis, units, code, or output.
4. **Help I need:** Request an explanation, comparison, diagnostic question, or hint.
5. **How I will check:** Ask for assumptions and a check against a reference, calculation, or self-test.

### 1. I expect the lowest-energy state to have the largest population.

**Starting question:** “Can a higher-energy group of states be more populated?”

**A more useful question to ask:**

> Consider a toy model with two groups: energy 0 and degeneracy 1, and energy 2*k_B*T and degeneracy 10. Calculate their canonical population ratio and explain the role of degeneracy.

**Why this helps:** It states the statistical model and includes the missing count of accessible states.

**Example answer:** The higher-to-lower group population ratio is (10/1)*exp(-2), about 1.35. The higher-energy group therefore has about 57.5% of the total population in this two-group model. Its greater degeneracy outweighs its energy penalty. This is a toy calculation, not a simulated molecular population.

**Follow-up to ask:**

> What happens to the ratio if the higher group's degeneracy is reduced to 1?

**Check your understanding:** Is a lower energy alone sufficient to rank group populations?

<details>
<summary>Reveal the check answer</summary>

No. Statistical weights include the number of accessible states.

</details>

### 2. I assume every saved frame is an independent sample.

**Starting question:** “Why does a huge trajectory still have uncertainty?”

**A more useful question to ask:**

> Explain time correlation and effective sample size for an observable in an MD trajectory. Suggest how block analysis and independent runs can help, and avoid inventing a correlation time without data.

**Why this helps:** It asks for a property-specific uncertainty estimate supported by measurements.

**Example answer:** Nearby frames often retain memory of each other. Consequently, the number of independent observations can be much smaller than the number saved. Correlation analysis and suitably chosen blocks can help estimate uncertainty, with sufficient data and attention to stationarity. Saving more frequent frames does not by itself generate more independent information.

**Follow-up to ask:**

> How would I check that increasing a block length has reached a useful uncertainty plateau?

**Check your understanding:** Does doubling the number of saved frames by halving the save interval necessarily double independent information?

<details>
<summary>Reveal the check answer</summary>

No. Closely spaced frames may be strongly correlated.

</details>

### 3. I want to turn a histogram into free energy.

**Starting question:** “Can I always take minus log of my histogram?”

**A more useful question to ask:**

> Explain F(s) = -k_B*T*ln P(s) + C for a specified coordinate and probability measure. Discuss sampling, zero-count bins, and why radial distributions may require a geometric measure correction.

**Why this helps:** It supplies the coordinate issue and asks about the assumptions behind a transformation.

**Example answer:** A free-energy profile is related to the equilibrium probability density under a defined measure. Finite sampling, bin choice, and correlations affect its estimate. A zero-count bin indicates missing observed samples, not a measured infinite barrier. Radial coordinates include geometric volume factors, so a radial histogram and a radial distribution function must be distinguished.

**Follow-up to ask:**

> Which probability density does my histogram estimate, and does it include a radial volume factor?

**Check your understanding:** Does an empty histogram bin establish an infinite physical free-energy barrier?

<details>
<summary>Reveal the check answer</summary>

No. It may simply be unsampled.

</details>

## References

- [GROMACS ensembles and simulation algorithms](https://manual.gromacs.org/documentation/current/reference-manual/algorithms/molecular-dynamics.html)

## Learning path

[All topics](../README.md) · [Previous: Molecular dynamics (MD)](../14_molecular_dynamics/README.md)

