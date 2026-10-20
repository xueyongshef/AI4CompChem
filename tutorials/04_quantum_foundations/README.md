# 04. Quantum chemistry foundations

Foundations · Wavefunctions · Hamiltonians · Born–Oppenheimer

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Identify the electronic and nuclear contributions in a molecular Hamiltonian.
- Explain the purpose of the Born–Oppenheimer approximation and molecular orbitals.

## Planned short videos

1. What does a wavefunction describe?
2. Separating electronic and nuclear motion

## Planned exercise

Annotate the terms in a molecular Hamiltonian and sketch how a molecule changes when its nuclei move.

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

### 1. I cannot tell a wavefunction from an electron density.

**Starting question:** “Are orbitals and electron density the same?”

**A more useful question to ask:**

> Explain the difference between a many-electron wavefunction, a molecular orbital, and electron density at an introductory level. Use their variables and normalisation to distinguish them, then ask me one check question.

**Why this helps:** It asks for explicit distinctions instead of an analogy that could hide them.

**Example answer:** A many-electron wavefunction depends on all electronic coordinates and spin variables. An orbital is a one-electron function used to build approximate descriptions. Electron density describes the expected number of electrons per volume at a position; integrating it over space gives the electron count. A single orbital's squared magnitude is not generally the total density.

**Follow-up to ask:**

> How is the density assembled from occupied orbitals in a closed-shell independent-particle picture?

**Check your understanding:** For a ten-electron system, what does the spatial integral of the electron density give?

<details>
<summary>Reveal the check answer</summary>

Ten electrons.

</details>

### 2. I do not understand why the nuclei are held fixed.

**Starting question:** “Why can we ignore nuclear motion?”

**A more useful question to ask:**

> Explain the Born–Oppenheimer approximation using a bond-length scan. Describe what is solved at each fixed geometry, how the nuclei can move later, and when separating electronic and nuclear motion becomes less reliable.

**Why this helps:** It asks about the approximation's role and limits, rather than treating nuclei as permanently frozen.

**Example answer:** At each chosen nuclear geometry, solve an electronic problem parametrised by those nuclear positions. Electronic energy together with nuclear repulsion defines an energy surface for nuclear motion. Nuclear motion is then treated on that surface in the usual single-surface picture. Electronic-state coupling can matter near degeneracies or other nonadiabatic situations.

**Follow-up to ask:**

> What quantity changes between the points of a bond-length scan?

**Check your understanding:** Does the approximation mean real nuclei never move?

<details>
<summary>Reveal the check answer</summary>

No. It separates parts of the description of their motion.

</details>

### 3. Negative energies seem to mean that something is wrong.

**Starting question:** “Why is the total energy negative?”

**A more useful question to ask:**

> Explain why an isolated molecule can have a negative total energy relative to the chosen zero. Then explain why comparing raw total energies of different molecular compositions does not establish which is more stable.

**Why this helps:** It asks about both the reference and the validity of a comparison.

**Example answer:** An energy's sign depends on its zero. For a typical isolated electronic-structure calculation, attractive binding can give a negative total energy relative to separated free charges. A larger molecule often has a more negative total energy simply because it contains more particles. Chemical stability requires a defined comparison, such as a balanced reaction with consistently computed energies.

**Follow-up to ask:**

> How would you define an energy change for a balanced dissociation reaction?

**Check your understanding:** Does the most negative total energy among molecules with different compositions identify the most stable substance?

<details>
<summary>Reveal the check answer</summary>

No. The comparison needs a chemically defined reference.

</details>

## References

- [Hartree–Fock theory and the electronic Hamiltonian](https://psi4.github.io/psi4docs/master/scf.html)

## Learning path

[All topics](../README.md) · [Previous: Working with molecules](../03_molecules/README.md) · [Next: Basis sets](../05_basis_sets/README.md)

