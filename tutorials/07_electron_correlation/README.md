# 07. Electron correlation and post-HF

Electronic structure · Correlation energy · MP2 · coupled cluster

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Distinguish exchange from electron correlation beyond HF.
- Recognise MP2 and coupled-cluster methods and discuss accuracy, cost, and single-reference limitations.

## Planned short videos

1. What is missing from Hartree–Fock?
2. From MP2 to coupled cluster

## Planned exercise

Design a comparison of HF and MP2 energies for water at the same geometry and basis; identify which variables must remain fixed.

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

### 1. I think a complete basis makes HF exact.

**Starting question:** “What remains after fixing the basis?”

**A more useful question to ask:**

> Explain basis incompleteness and electron correlation as two separate issues. Compare converging an HF calculation with increasing basis size against changing from HF to a post-HF method at a fixed basis.

**Why this helps:** It varies one modelling choice at a time.

**Example answer:** A more complete basis improves the representation available to a chosen method. HF still restricts the wavefunction to its single-determinant form. Post-HF methods add descriptions of correlation beyond that reference, but retain their own approximations and basis dependence. Both choices must be considered when judging a result.

**Follow-up to ask:**

> What would a two-dimensional comparison across methods and basis sizes tell me?

**Check your understanding:** Is the HF basis-set limit generally the exact many-electron energy?

<details>
<summary>Reveal the check answer</summary>

No. Correlation beyond HF remains.

</details>

### 2. The MP2 energy is lower, but I do not know what that proves.

**Starting question:** “Is the lowest computed energy always best?”

**A more useful question to ask:**

> Explain why a lower MP2 total energy than HF does not by itself establish greater accuracy. State whether MP2 is variational and discuss what comparison would be relevant for my target property.

**Why this helps:** It tests a claimed conclusion instead of accepting a numerical ranking.

**Example answer:** MP2 adds a perturbative correlation correction to an HF reference and is not a variational upper-bound method. A lower value alone cannot certify proximity to the exact energy. Check the reference's suitability and compare the property of interest with trustworthy benchmarks or convergence evidence.

**Follow-up to ask:**

> What problems can appear when the HF reference has small orbital-energy gaps?

**Check your understanding:** Does MP2 guarantee an energy above the exact ground-state energy?

<details>
<summary>Reveal the check answer</summary>

No. MP2 is not variational.

</details>

### 3. I am unsure why stretching a bond causes trouble.

**Starting question:** “Why not use the same single-reference method everywhere?”

**A more useful question to ask:**

> Use stretched H2 to explain why one closed-shell determinant can become a poor reference. Describe the role of nearly degenerate configurations and explain why an apparently converged result is not sufficient evidence of reliability.

**Why this helps:** It asks for a failure mechanism in a concrete system.

**Example answer:** As the bond stretches, configurations that are well separated near equilibrium can become comparably important. A single closed-shell determinant then struggles to describe the electronic structure. A method built on that reference may also struggle. Numerical convergence is a separate question from whether the electronic description is appropriate.

**Follow-up to ask:**

> Why is allowing spin-symmetry breaking not automatically a complete validation of the result?

**Check your understanding:** Does successful SCF convergence prove a stretched-bond reference is adequate?

<details>
<summary>Reveal the check answer</summary>

No. The quality of the reference needs separate assessment.

</details>

## References

- [Psi4 methods and capabilities](https://psicode.org/psi4manual/master/introduction)
- [Psi4 MP2 theory](https://psi4.github.io/psi4docs/master/dfmp2.html)

## Learning path

[All topics](../README.md) · [Previous: Hartree–Fock (HF)](../06_hartree_fock/README.md) · [Next: Density functional theory (DFT)](../08_dft/README.md)

