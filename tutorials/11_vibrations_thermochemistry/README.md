# 11. Vibrations and thermochemistry

Potential energy and reactions · Hessians · normal modes · ZPE · thermal corrections

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Connect a Hessian and normal modes to vibrational frequencies and stationary-point character.
- Distinguish electronic energy, zero-point energy, enthalpy, and Gibbs free energy, including temperature and standard-state assumptions.

## Planned short videos

1. What does a vibrational frequency tell us?
2. From electronic energy to thermochemistry

## Planned exercise

Use a supplied frequency report to identify normal modes and list the corrections needed for a free-energy comparison.

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

### 1. I do not understand how many vibrations a molecule has.

**Starting question:** “Why is the mode count different for water and CO2?”

**A more useful question to ask:**

> Count vibrational modes for isolated nonlinear H2O and linear CO2. Explain the translational and rotational degrees of freedom and distinguish the number of modes from the number of distinct frequencies.

**Why this helps:** It supplies molecular geometry and separates two ways of counting.

**Example answer:** A nonlinear N-atom molecule has 3N - 6 vibrational modes, giving three for water. A linear molecule has 3N - 5, giving four for CO2. Two CO2 bending modes are degenerate in the ideal linear molecule, so four modes need not mean four distinct frequencies.

**Follow-up to ask:**

> How would you classify the two degenerate bending motions?

**Check your understanding:** How many vibrational modes does linear CO2 have?

<details>
<summary>Reveal the check answer</summary>

Four, including two degenerate bending modes.

</details>

### 2. A small imaginary frequency worries me.

**Starting question:** “Should I delete the imaginary frequency?”

**A more useful question to ask:**

> My intended minimum has a small imaginary frequency. Explain how the mode, geometry convergence, numerical settings, and possible constraints affect interpretation. Ask me to inspect the mode before deciding what action to take.

**Why this helps:** It requests a diagnosis rather than discarding inconvenient evidence.

**Example answer:** An imaginary harmonic frequency corresponds to negative curvature in the analysed vibrational direction. A small value can require checks of numerical accuracy or geometry convergence; it must not simply be deleted. Inspect the motion, any constraints, and relevant settings, then determine whether a genuine unstable direction remains.

**Follow-up to ask:**

> What would a large imaginary mode involving a substantial structural change suggest?

**Check your understanding:** Does a small imaginary frequency alone prove that the intended minimum is acceptable?

<details>
<summary>Reveal the check answer</summary>

No. Its origin and mode need investigation.

</details>

### 3. I confuse electronic energy with Gibbs free energy.

**Starting question:** “Can I call my electronic-energy difference a free energy?”

**A more useful question to ask:**

> Explain the contributions required to compare molecular Gibbs free energies from electronic-structure calculations. State temperature, pressure or standard state, and the treatment of low-frequency modes, and separate these from the electronic energy.

**Why this helps:** It asks for the definition and assumptions of the quantity being reported.

**Example answer:** A molecular thermochemistry model combines electronic energy with zero-point and thermal contributions and entropy. Temperature, standard state, and approximations for translation, rotation, and vibration matter. Low-frequency modes can make the harmonic treatment sensitive. An electronic-energy difference alone is not a Gibbs free-energy difference.

**Follow-up to ask:**

> Which corrections cancel, and which must be computed, for my specific reaction?

**Check your understanding:** Can I report a bare electronic-energy barrier as a Gibbs free-energy barrier?

<details>
<summary>Reveal the check answer</summary>

No. It must be labelled as an electronic-energy barrier.

</details>

## References

- [Psi4 computational capabilities](https://psicode.org/psi4manual/master/introduction)
- [Psi4 harmonic vibrational analysis](https://psi4.github.io/psi4docs/master/freq.html)
- [Psi4 thermochemistry](https://psi4.github.io/psi4docs/master/thermo.html)

## Learning path

[All topics](../README.md) · [Previous: Geometry optimisation](../10_geometry_optimisation/README.md) · [Next: Transition states and reaction paths](../12_reaction_paths/README.md)

