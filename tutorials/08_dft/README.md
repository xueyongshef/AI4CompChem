# 08. Density functional theory (DFT)

Electronic structure · Electron density · functionals · grids · dispersion

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Explain the role of density and approximate exchange-correlation functionals in Kohn–Sham DFT.
- Distinguish functional, basis-set, integration-grid, and dispersion choices.

## Planned short videos

1. DFT explained: from wavefunctions to density
2. Choosing and checking a DFT calculation

## Planned exercise

Plan a comparison of two DFT functionals on the same water geometry and basis, recording all numerical settings.

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

### 1. I heard DFT does not use orbitals.

**Starting question:** “Why does my DFT output contain orbitals?”

**A more useful question to ask:**

> Explain the distinction between electron density and the auxiliary orbitals of Kohn–Sham DFT. Compare this with HF at an introductory level without treating the two energy expressions as identical.

**Why this helps:** It names the formulation and resolves an apparent contradiction in the output.

**Example answer:** Kohn–Sham DFT commonly uses auxiliary orbitals to construct the density and part of the energy. Its exchange-correlation contribution is described through a functional, approximated in practical calculations. Thus, 'DFT uses density' does not mean a Kohn–Sham program never solves orbital equations.

**Follow-up to ask:**

> Which parts of a practical Kohn–Sham calculation depend on the chosen functional?

**Check your understanding:** Is seeing orbitals in a DFT output inconsistent with Kohn–Sham DFT?

<details>
<summary>Reveal the check answer</summary>

No. Orbitals are part of that formulation.

</details>

### 2. I do not know which settings are being compared.

**Starting question:** “Why do two DFT calculations disagree?”

**A more useful question to ask:**

> Help me compare two DFT calculations on the same molecule. Separate geometry and electronic state, functional, basis, grid, dispersion treatment, and convergence settings before interpreting the energy difference.

**Why this helps:** It prevents several changed settings being mistaken for a single effect.

**Example answer:** A difference can reflect the physical setup, model, or numerical approximation. Make a table of these settings and identify which vary. To isolate a functional change, keep the other relevant choices controlled and document any functional-dependent conventions. No particular cause can be diagnosed without the actual inputs and outputs.

**Follow-up to ask:**

> Which settings would you vary first to check numerical convergence?

**Check your understanding:** Is the integration grid the same thing as the orbital basis?

<details>
<summary>Reveal the check answer</summary>

No. They serve different roles.

</details>

### 3. An AI recommends one functional for everything.

**Starting question:** “Which functional is the best?”

**A more useful question to ask:**

> I want to predict [property] for [system]. Ask me about bonding, charge, spin, environment, and available benchmarks before discussing functional choices. Explain the evidence and limits behind any recommendation.

**Why this helps:** It supplies a target and requests evidence instead of a universal ranking.

**Example answer:** A useful recommendation depends on the chemical problem and property. Performance on one benchmark does not establish performance on every bonding regime or observable. First define the task, then examine relevant validation and practical settings. A functional's name or popularity is not sufficient evidence.

**Follow-up to ask:**

> What benchmark would resemble my intended application closely enough to be useful?

**Check your understanding:** Can one benchmark score guarantee the best functional for every molecule and property?

<details>
<summary>Reveal the check answer</summary>

No. The evidence must be relevant to the intended task.

</details>

## References

- [Psi4 SCF and Kohn–Sham DFT](https://psi4.github.io/psi4docs/master/scf.html)
- [Psi4 DFT](https://psi4.github.io/psi4docs/master/dft.html)

## Learning path

[All topics](../README.md) · [Previous: Electron correlation and post-HF](../07_electron_correlation/README.md) · [Next: Potential energy surfaces (PES)](../09_potential_energy_surfaces/README.md)

