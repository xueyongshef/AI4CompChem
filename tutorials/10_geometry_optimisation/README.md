# 10. Geometry optimisation

Potential energy and reactions · Gradients · convergence · local minima

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Distinguish a single-point energy calculation from geometry optimisation.
- Read convergence criteria and explain why an optimised structure needs further checks.

## Planned short videos

1. How a molecule finds a local minimum
2. Reading an optimisation log

## Planned exercise

Plan a water optimisation starting from a distorted geometry; record the initial and final bond lengths and convergence information.

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

### 1. I cannot tell an energy calculation from an optimisation.

**Starting question:** “Why did the program not improve my geometry?”

**A more useful question to ask:**

> Explain the difference between a single-point calculation and geometry optimisation. Describe whether the nuclear coordinates change and what evidence in an output distinguishes the two jobs.

**Why this helps:** It asks what operation the program was instructed to perform.

**Example answer:** A single-point calculation evaluates a chosen electronic model at the supplied geometry. Geometry optimisation changes nuclear coordinates to approach a stationary structure according to an algorithm and convergence criteria. A successful single point says nothing about whether the starting geometry is a minimum.

**Follow-up to ask:**

> Can I evaluate several methods at the same optimised geometry?

**Check your understanding:** Does a converged single-point energy imply that the molecular geometry was optimised?

<details>
<summary>Reveal the check answer</summary>

No. The coordinates may never have been varied.

</details>

### 2. The energy stopped changing, but the optimiser continues.

**Starting question:** “Why is a small energy change not enough?”

**A more useful question to ask:**

> My optimisation has a small energy change but a gradient criterion is unmet. Explain energy, gradient, and displacement criteria conceptually. Ask for the relevant convergence table before suggesting changes.

**Why this helps:** It identifies the actual unmet criterion and requests the evidence needed to interpret it.

**Example answer:** Near a shallow region, successive energies can differ little while forces or geometry steps remain significant. Optimisation programs therefore check more than energy changes. Read all required criteria and the step history. First establish whether progress is normal, oscillatory, or limited by numerical noise before changing thresholds.

**Follow-up to ask:**

> What would a persistent large gradient tell us?

**Check your understanding:** Can an almost unchanged energy coexist with an unmet force criterion?

<details>
<summary>Reveal the check answer</summary>

Yes. They measure different aspects of progress.

</details>

### 3. Different starting geometries reach different structures.

**Starting question:** “Which optimised structure is the answer?”

**A more useful question to ask:**

> Two initial conformers converge to different geometries at the same method and basis. Explain local and global minima, propose checks of stationary-point character, and describe what a fair energy comparison requires.

**Why this helps:** It treats the starting geometry and search problem as part of the scientific question.

**Example answer:** An optimiser commonly finds a nearby local stationary structure. Multiple valid minima may exist, and one optimisation does not establish a global minimum. Check convergence and vibrational character, compare compatible energies, and explore additional conformers where relevant. The appropriate ranking may require thermal and environmental contributions.

**Follow-up to ask:**

> How would conformational sampling change my search strategy?

**Check your understanding:** Does reaching a local minimum prove there is no lower minimum elsewhere?

<details>
<summary>Reveal the check answer</summary>

No. A local search does not establish the global landscape.

</details>

## References

- [Psi4 geometry optimisation](https://psi4.github.io/psi4docs/master/optking.html)

## Learning path

[All topics](../README.md) · [Previous: Potential energy surfaces (PES)](../09_potential_energy_surfaces/README.md) · [Next: Vibrations and thermochemistry](../11_vibrations_thermochemistry/README.md)

