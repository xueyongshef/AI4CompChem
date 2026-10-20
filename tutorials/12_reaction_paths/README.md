# 12. Transition states and reaction paths

Potential energy and reactions · Saddle points · barriers · imaginary modes · IRC

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Distinguish a reaction coordinate, a transition-state search, and an intrinsic reaction coordinate (IRC).
- Assess a candidate transition state using its relevant imaginary mode and connection to reactants and products.

## Planned short videos

1. Finding a transition state
2. Checking where a reaction path leads

## Planned exercise

Annotate a model reaction-energy diagram and describe how to check the saddle point and report an electronic or free-energy barrier.

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

### 1. I found one imaginary mode and assume the reaction is solved.

**Starting question:** “Does one imaginary frequency prove the intended transition state?”

**A more useful question to ask:**

> Explain how to assess a candidate first-order saddle point. Include stationarity, the relevant imaginary mode, and checking its connection to the intended reactant and product, for example using IRC calculations and endpoint optimisation.

**Why this helps:** It asks whether mathematical character and chemical connectivity both match the intended reaction.

**Example answer:** One relevant unstable vibrational direction supports first-order saddle character when stationarity and numerical quality are established. It does not identify the connected species by itself. Inspect the mode and follow suitable paths in both directions, then characterise their endpoints. The resulting connection must match the reaction being proposed.

**Follow-up to ask:**

> What would I conclude if the two endpoints belonged to an unintended rearrangement?

**Check your understanding:** Does counting imaginary frequencies determine the identities of the reactant and product?

<details>
<summary>Reveal the check answer</summary>

No. Connectivity requires separate checks.

</details>

### 2. I mix up forward and reverse barriers.

**Starting question:** “Which barrier should I subtract?”

**A more useful question to ask:**

> Use a toy electronic-energy diagram with reactant 0, transition state 40, and product -10 kJ/mol. Calculate forward and reverse electronic barriers with explicit reference states, and explain why these values are not automatically free-energy barriers.

**Why this helps:** It supplies a complete sign convention and labels the energy type.

**Example answer:** The forward electronic barrier is 40 - 0 = 40 kJ/mol. The reverse barrier is 40 - (-10) = 50 kJ/mol. The reaction electronic energy is -10 kJ/mol in the forward direction. These arithmetic examples describe the supplied toy diagram; thermal and entropy contributions would be needed for free-energy barriers.

**Follow-up to ask:**

> How would the two barriers change if every energy were shifted by the same constant?

**Check your understanding:** What is the reverse barrier in the toy diagram?

<details>
<summary>Reveal the check answer</summary>

50 kJ/mol, measured from product to transition state.

</details>

### 3. I think an IRC is a molecular movie.

**Starting question:** “Does an IRC predict the actual time evolution?”

**A more useful question to ask:**

> Compare an intrinsic reaction coordinate with a bond scan and a molecular-dynamics trajectory. Explain what each path represents, whether it has physical time, and how it helps test a reaction hypothesis.

**Why this helps:** It distinguishes different meanings of a path through molecular configurations.

**Example answer:** An IRC follows a particular steepest-descent path from a saddle point in mass-weighted coordinates. A bond scan follows a chosen constraint. A dynamics trajectory follows equations of motion with a time parameter. An IRC can help establish connectivity, but is not a finite-temperature movie or a full kinetic prediction.

**Follow-up to ask:**

> What additional ingredients would a finite-temperature rate calculation require?

**Check your understanding:** Does an IRC step correspond to a fixed amount of physical time?

<details>
<summary>Reveal the check answer</summary>

No. IRC progress is not a dynamics time coordinate.

</details>

## References

- [Psi4 optimisation, transition states, and IRC](https://psi4.github.io/psi4docs/master/optking.html)

## Learning path

[All topics](../README.md) · [Previous: Vibrations and thermochemistry](../11_vibrations_thermochemistry/README.md) · [Next: Force fields and interaction potentials](../13_force_fields/README.md)

