# 09. Potential energy surfaces (PES)

Potential energy and reactions · Energy landscapes · bond scans · minima · forces

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Describe energy as a function of nuclear geometry and distinguish a one-dimensional scan from the full PES.
- Relate forces to energy gradients and identify minima and saddle points.

## Planned short videos

1. Reading a potential energy landscape
2. Building a bond-distance scan

## Planned exercise

Sketch a diatomic bond-energy curve and label its equilibrium distance, repulsive region, and dissociation region.

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

### 1. I cannot tell a scan from a full surface.

**Starting question:** “Is a bond-length plot the entire PES?”

**A more useful question to ask:**

> Explain the difference between a potential energy surface and a one-dimensional bond-length scan for a polyatomic molecule. Then distinguish a fixed-coordinate scan from a relaxed scan, stating which variables can change.

**Why this helps:** It specifies the dimensionality and the constraints on the calculation.

**Example answer:** A PES assigns an energy to molecular geometries under a defined electronic description. A one-dimensional scan samples a selected coordinate. In a fixed-coordinate scan the remaining coordinates are held fixed; in a relaxed scan selected remaining coordinates are optimised under the scan constraint. The resulting curves need not coincide.

**Follow-up to ask:**

> Could a low point on a constrained scan still fail to be a full molecular minimum?

**Check your understanding:** Does a one-dimensional scan explore every internal degree of freedom?

<details>
<summary>Reveal the check answer</summary>

No. It follows a chosen slice or constrained path.

</details>

### 2. I confuse the sign of the force with the slope.

**Starting question:** “Does a positive energy mean a positive force?”

**A more useful question to ask:**

> For the toy potential U(x) = k*x^2/2 with k positive, explain F = -dU/dx. Determine the force direction at x greater than zero and distinguish the energy value from its gradient.

**Why this helps:** It gives an explicit potential and asks about direction instead of vague signs.

**Example answer:** Differentiating gives dU/dx = k*x, so F = -k*x. At positive x the force points toward decreasing x, back toward the minimum. Shifting all energies by a constant changes U but not its gradient or the force. The force is set by slope, not by the sign of the energy.

**Follow-up to ask:**

> What is the force at x = 0?

**Check your understanding:** If I add a constant to every energy, does the force change?

<details>
<summary>Reveal the check answer</summary>

No. The derivative of a constant is zero.

</details>

### 3. I use potential energy and free energy interchangeably.

**Starting question:** “Is the lowest-energy geometry always the most populated?”

**A more useful question to ask:**

> Explain the difference between a PES and a finite-temperature free-energy profile. Use the number of accessible configurations to explain why a potential-energy minimum alone does not determine a population.

**Why this helps:** It asks about what is averaged over and which thermodynamic information is missing.

**Example answer:** A PES describes energy at specified geometries. A free-energy profile incorporates statistical weighting over configurations compatible with a selected coordinate and conditions. A region can have favourable population because it contains many accessible configurations. Defining the ensemble, temperature, and coordinate is essential when interpreting that profile.

**Follow-up to ask:**

> What information would I need to turn a trajectory histogram into a free-energy estimate?

**Check your understanding:** Can a single geometry's potential energy alone establish its finite-temperature population?

<details>
<summary>Reveal the check answer</summary>

No. Accessible configurations and statistical conditions also matter.

</details>

## References

- [Psi4 geometry optimisation and reaction coordinates](https://psi4.github.io/psi4docs/master/optking.html)

## Learning path

[All topics](../README.md) · [Previous: Density functional theory (DFT)](../08_dft/README.md) · [Next: Geometry optimisation](../10_geometry_optimisation/README.md)

