# 06. Hartree–Fock (HF)

Electronic structure · Mean field · exchange · SCF · RHF and UHF

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Describe the single-determinant approximation, exchange, and the mean-field picture.
- Follow an SCF cycle, distinguish RHF and UHF, and identify the limitations of HF.

## Planned short videos

1. Hartree–Fock in pictures
2. What happens during an SCF cycle?

## Planned exercise

Plan an RHF calculation on water with a fixed basis, then identify the convergence history and orbital energies in its output.

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

### 1. I cannot see why SCF needs repeated calculations.

**Starting question:** “Why does Hartree–Fock repeat itself?”

**A more useful question to ask:**

> For closed-shell water in a fixed basis, explain an SCF cycle using orbitals, density, and the Fock operator. Identify what is updated and why the starting orbitals are not usually the final solution. Keep it conceptual before introducing equations.

**Why this helps:** It fixes the system and asks which quantities depend on each other.

**Example answer:** The orbitals determine an electron density, and that density determines the mean-field operator used to obtain new orbitals. SCF iterates this dependency until selected changes or residuals satisfy thresholds. These iterations are a numerical solution procedure, not a movie of electrons moving through time.

**Follow-up to ask:**

> What would it mean for the input and output densities of an iteration to agree?

**Check your understanding:** Is an SCF iteration a molecular-dynamics time step?

<details>
<summary>Reveal the check answer</summary>

No. It updates an approximate electronic solution.

</details>

### 2. I think HF ignores electron–electron interaction.

**Starting question:** “Does HF leave out all electron repulsion?”

**A more useful question to ask:**

> Distinguish Coulomb interaction, exchange, and electron correlation in Hartree–Fock. Explain which effects arise in a single-determinant description and which remain missing relative to an exact solution of the same electronic Hamiltonian.

**Why this helps:** It identifies a specific misconception and asks for separate definitions.

**Example answer:** HF includes electron–electron Coulomb interaction in a mean-field description and exchange associated with an antisymmetric determinant. It does not supply all the remaining electron correlation of an exact many-electron solution. 'HF neglects electron interaction' is therefore misleading; the issue is the approximation used to describe that interaction.

**Follow-up to ask:**

> Why would increasing the orbital basis not automatically recover the missing correlation?

**Check your understanding:** Does HF include exchange?

<details>
<summary>Reveal the check answer</summary>

Yes. Exchange is present in its antisymmetric single-determinant description.

</details>

### 3. The output says converged, so I assume the result is correct.

**Starting question:** “Is a converged HF calculation accurate?”

**A more useful question to ask:**

> My water RHF calculation converged. Help me separate numerical convergence from physical and chemical accuracy. Ask about the geometry, charge, multiplicity, basis, SCF solution, and property I want to predict before judging the result.

**Why this helps:** It asks what was actually established by the success message.

**Example answer:** Convergence establishes that the selected numerical criteria were met for a particular model and solution. It does not validate the electronic state, establish the appropriate SCF solution, or eliminate basis and method errors. Check the input and the target property, then use suitable convergence studies and comparisons.

**Follow-up to ask:**

> What evidence would support a claim that a predicted bond length is reliable?

**Check your understanding:** Can tightening SCF thresholds alone make HF exact?

<details>
<summary>Reveal the check answer</summary>

No. It changes numerical tolerance, not the underlying approximation.

</details>

## References

- [Psi4 Hartree–Fock theory](https://psi4.github.io/psi4docs/master/scf.html)

## Learning path

[All topics](../README.md) · [Previous: Basis sets](../05_basis_sets/README.md) · [Next: Electron correlation and post-HF](../07_electron_correlation/README.md)

