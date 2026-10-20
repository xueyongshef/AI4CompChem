# 03. Working with molecules

Foundations · Coordinates · charge · spin · file formats

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Describe a molecule using coordinates, charge, and spin multiplicity.
- Inspect molecular structures and recognise common file formats.

## Planned short videos

1. From a molecular drawing to 3D coordinates
2. Why charge and spin matter

## Planned exercise

Inspect a water structure and document its coordinates, units, charge, and multiplicity.

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

### 1. I confuse charge with spin multiplicity.

**Starting question:** “What spin should I use?”

**A more useful question to ask:**

> For neutral H2O and neutral OH, explain electron count, charge, total spin, and multiplicity separately. Use their usual ground-state assignments and ask me to count the electrons before giving the answer.

**Why this helps:** It names the systems and distinguishes quantities that are easily confused.

**Example answer:** Neutral water has ten electrons and its usual ground state is a closed-shell singlet, with multiplicity 1. Neutral OH has nine electrons and its usual ground state is a doublet, with multiplicity 2. Charge measures net electric charge; multiplicity is 2S + 1. A neutral molecule can have unpaired electrons.

**Follow-up to ask:**

> What changes if I remove an electron from a neutral molecule?

**Check your understanding:** Does neutral always mean singlet?

<details>
<summary>Reveal the check answer</summary>

No. Neutral OH is a counterexample.

</details>

### 2. My molecule looks much too large or too small.

**Starting question:** “Are my coordinates wrong?”

**A more useful question to ask:**

> My XYZ structure has unexpected bond lengths after import. Help me check coordinate units, atom order, and file interpretation before changing the geometry. Explain what I can and cannot infer from a bare XYZ file.

**Why this helps:** It asks for checks of representation before changing the physical structure.

**Example answer:** Standard XYZ-style coordinates commonly use angstrom, but a bare coordinate list may not declare units or electronic state. Check the generating program, importer settings, and one known interatomic distance. A consistent scale error can suggest a unit mismatch; it is not proof that the molecule should be reoptimised.

**Follow-up to ask:**

> What additional information should accompany the XYZ file for a quantum calculation?

**Check your understanding:** Does a list of element symbols and coordinates uniquely specify charge and multiplicity?

<details>
<summary>Reveal the check answer</summary>

No. Those must be supplied separately.

</details>

### 3. I am unsure whether two geometries are different conformers.

**Starting question:** “These two structures look different. Which is better?”

**A more useful question to ask:**

> Two coordinate files describe an isolated water molecule. Explain how to distinguish a rigid rotation or translation from a change in internal geometry. Ask me to compare bond lengths and the bond angle before comparing energies.

**Why this helps:** It checks physical equivalence before treating a visual difference as chemistry.

**Example answer:** For an isolated molecule without an external field, a rigid rotation or translation preserves its internal geometry and physical energy. Compare interatomic distances and angles, or align the structures. A changed bond length or angle represents an internal change. Tiny computed differences can also reflect numerical settings.

**Follow-up to ask:**

> What other information would you need before comparing two molecular conformers?

**Check your understanding:** Does translating all atoms by the same vector change their bond lengths?

<details>
<summary>Reveal the check answer</summary>

No. Pairwise separations remain the same.

</details>

## References

- [Psi4 molecule specification](https://psi4.github.io/psi4docs/master/psithonmol.html)

## Learning path

[All topics](../README.md) · [Previous: Python essentials](../02_python/README.md) · [Next: Quantum chemistry foundations](../04_quantum_foundations/README.md)

