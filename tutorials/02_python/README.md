# 02. Python essentials

Foundations · Arrays · plotting · scientific data

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Use arrays and plots to explore scientific data.
- Read molecular data and report quantities with explicit units.

## Planned short videos

1. Python arrays for molecular data
2. Plotting an energy curve

## Planned exercise

Plot a small supplied table of bond distances and energies, labelling both axes and units.

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

### 1. I do not understand an array-shape error.

**Starting question:** “Why does NumPy reject my calculation?”

**A more useful question to ask:**

> My coordinate array has shape (3, 3), and I subtract an array of shape (2,). Explain why broadcasting fails by comparing the dimensions. Give me a hint about the intended operation before rewriting the code.

**Why this helps:** It provides exact shapes and asks for an explanation tied to the operation.

**Example answer:** NumPy compares dimensions from the right. Dimensions must be equal or one must be 1. Here the final dimensions are 3 and 2, so they are incompatible. Ask whether you intended to subtract a three-component displacement vector, select two coordinates, or do something else; the correct fix depends on that intention.

**Follow-up to ask:**

> If I subtract one vector of shape (3,), what will the output shape be?

**Check your understanding:** Can an array of shape (3,) be subtracted from coordinates of shape (3, 3)?

<details>
<summary>Reveal the check answer</summary>

Yes. It is broadcast across the rows, giving a result of shape (3, 3).

</details>

### 2. I am mixing units and numerical values.

**Starting question:** “Is this energy difference large?”

**A more useful question to ask:**

> My toy energies are -75.000 and -74.990 hartree. Help me calculate the difference first, state the sign convention, and explain what I must know before calling it chemically important. Keep any unit conversion explicit.

**Why this helps:** It separates arithmetic, units, and chemical interpretation.

**Example answer:** Taking the second value minus the first gives +0.010 hartree. To interpret it, check whether the energies describe comparable states, geometries, and methods, and whether you need an electronic-energy or free-energy difference. Convert both the number and its unit using a documented factor. These toy values are not calculation results.

**Follow-up to ask:**

> How would the sign change if I reversed the order of subtraction?

**Check your understanding:** Does subtracting two energies remove the need to report units?

<details>
<summary>Reveal the check answer</summary>

No. Their difference still has an energy unit.

</details>

### 3. I want help debugging without losing the chance to learn.

**Starting question:** “Write the correct code for me.”

**A more useful question to ask:**

> A three-atom coordinate array gives IndexError when I request atom 3. Explain Python indexing and ask me to predict the valid indices. Give one hint before showing a corrected expression.

**Why this helps:** It requests a limited hint and makes the learner practise the missing concept.

**Example answer:** Python uses zero-based indexing. An array with three rows has row indices 0, 1, and 2. Index 3 requests a fourth row. First decide which atom you meant, then choose its corresponding row. Confirm the array shape and atom ordering rather than changing an index at random.

**Follow-up to ask:**

> How can I select the final row without assuming the number of atoms?

**Check your understanding:** Which row is selected by index 0?

<details>
<summary>Reveal the check answer</summary>

The first row.

</details>

## References

- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## Learning path

[All topics](../README.md) · [Previous: Getting started](../01_getting_started/README.md) · [Next: Working with molecules](../03_molecules/README.md)

