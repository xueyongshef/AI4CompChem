# 05. Basis sets

Electronic structure · Gaussian functions · polarisation · diffuse functions

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Explain how basis functions represent molecular orbitals.
- Compare minimal and split-valence bases, polarisation and diffuse functions, and basis-set convergence.

## Planned short videos

1. What is a basis set?
2. Why add polarisation and diffuse functions?

## Planned exercise

Plan a fixed-geometry water calculation with STO-3G, 6-31G, and 6-31G(d). Record the method, basis, energy, and computational cost separately.

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

### 1. I confuse the method with the basis set.

**Starting question:** “Is a basis set another method?”

**A more useful question to ask:**

> Using HF/6-31G, HF/cc-pVDZ, and B3LYP/6-31G, identify which part describes the electronic-structure approximation and which part describes the orbital expansion. Explain what is held fixed in each comparison.

**Why this helps:** It uses named examples to separate two independent choices.

**Example answer:** HF and B3LYP specify electronic-structure approximations. The basis supplies functions used to represent orbitals. Moving from HF/6-31G to HF/cc-pVDZ changes the basis; moving from HF/6-31G to B3LYP/6-31G changes the method while keeping that basis. A larger basis does not turn HF into a correlated wavefunction method.

**Follow-up to ask:**

> Which settings would you hold fixed in a basis-convergence study?

**Check your understanding:** What changes between HF/6-31G and HF/cc-pVDZ?

<details>
<summary>Reveal the check answer</summary>

The basis set.

</details>

### 2. Polarisation and diffuse functions sound similar.

**Starting question:** “Which extra functions do I need?”

**A more useful question to ask:**

> Explain polarisation and diffuse functions separately, using a bent neutral molecule and an anion as motivating examples. Describe what each adds to the orbital description and how I could check whether it matters for my target property.

**Why this helps:** It requests mechanisms and a property-specific check, rather than a universal recipe.

**Example answer:** Polarisation functions add angular flexibility so an orbital description can respond to molecular bonding. Diffuse functions extend spatial flexibility farther from nuclei, which can matter for anions and other spatially extended distributions. Their practical importance depends on the system and property. Compare suitable basis choices systematically rather than treating one addition as a substitute for the other.

**Follow-up to ask:**

> Why might a small change in total energy still accompany an important change in a property?

**Check your understanding:** Are diffuse functions simply another name for higher angular momentum functions?

<details>
<summary>Reveal the check answer</summary>

No. Radial extent and angular flexibility are different features.

</details>

### 3. A larger basis gave a different energy.

**Starting question:** “Does a lower energy always mean a better answer?”

**A more useful question to ask:**

> Explain when the variational principle predicts a non-increasing HF energy as a basis is enlarged. State the assumptions about nested spaces and comparable converged solutions, and explain why this does not prove chemical accuracy.

**Why this helps:** It asks for the conditions behind a familiar rule.

**Example answer:** For the same Hamiltonian and HF variational class, enlarging a nested orbital space cannot raise the globally minimised HF energy. Practical comparisons may use non-nested bases or different stationary SCF solutions. Even a converged basis expansion retains the method's approximations. Accuracy in a reaction energy or another property therefore needs its own assessment.

**Follow-up to ask:**

> How would you distinguish basis incompleteness from missing electron correlation?

**Check your understanding:** Does basis convergence remove HF's remaining electron-correlation error?

<details>
<summary>Reveal the check answer</summary>

No. Method and basis errors are distinct.

</details>

## References

- [Psi4 basis sets](https://psi4.github.io/psi4docs/master/basissets.html)

## Learning path

[All topics](../README.md) · [Previous: Quantum chemistry foundations](../04_quantum_foundations/README.md) · [Next: Hartree–Fock (HF)](../06_hartree_fock/README.md)

