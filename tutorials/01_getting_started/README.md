# 01. Getting started

Foundations · Environments · notebooks · reproducible workflows

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Set up a Python environment and use a notebook.
- Keep inputs, units, software versions, and outputs together.

## Planned short videos

1. Your first computational chemistry workspace
2. How to keep a calculation reproducible

## Planned exercise

Create a notebook that records your environment, a molecular question, and the inputs needed to investigate it.

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

### 1. My package is installed, but my notebook cannot import it.

**Starting question:** “Why does Python not work?”

**A more useful question to ask:**

> I am using a Jupyter notebook and get ModuleNotFoundError after installing a package in my terminal. Explain how the notebook kernel and terminal Python can differ. Ask for my operating system, the exact error, and the interpreter paths before suggesting a fix.

**Why this helps:** It describes the symptom and asks for evidence that can separate several possible causes.

**Example answer:** A notebook kernel may use a different Python environment from the terminal. First compare the notebook's sys.executable with the interpreter used for installation. Check the package name and installation message. Then select the intended kernel or install into that environment. The error alone does not identify which of these is responsible.

**Follow-up to ask:**

> How can I verify that the notebook now uses the intended environment?

**Check your understanding:** Does a successful terminal installation prove the notebook can import the package?

<details>
<summary>Reveal the check answer</summary>

No. The installation and notebook must use the same intended environment.

</details>

### 2. I do not know what information to include in a question.

**Starting question:** “My calculation failed. Fix it.”

**A more useful question to ask:**

> Help me write a useful troubleshooting question for a failed water calculation. Ask me for the software and version, input, charge, multiplicity, method, basis, relevant error text, and what I expected. Explain why each item matters.

**Why this helps:** It turns a broad request into a reproducible description of the problem.

**Example answer:** Start with the smallest input that reproduces the failure and the relevant error lines. State the intended calculation and what happened instead. Geometry, charge, multiplicity, method, basis, software, and version constrain the diagnosis. A useful first answer may ask for missing evidence rather than prescribe a change.

**Follow-up to ask:**

> Which information should I collect first if I only have the error message?

**Check your understanding:** Can an AI diagnose every calculation failure from 'SCF failed'?

<details>
<summary>Reveal the check answer</summary>

No. That symptom has several possible causes and needs context.

</details>

### 3. My result differs from someone else's.

**Starting question:** “Which result is right?”

**A more useful question to ask:**

> Two water calculations give different energies. Help me make a comparison table before deciding which is correct. Include geometry, charge, spin, method, basis, units, numerical settings, and software version. Do not invent either result.

**Why this helps:** It asks whether the calculations are comparable before judging their outputs.

**Example answer:** Different inputs can produce different legitimate results. Compare like quantities with matching units and definitions, then check the geometry, electronic state, method, basis, and numerical settings. A discrepancy becomes evidence of an error only after differences in the calculation setup are understood.

**Follow-up to ask:**

> Which differences would change the physical model, and which concern numerical convergence?

**Check your understanding:** Is matching the molecule's name enough to compare two energies?

<details>
<summary>Reveal the check answer</summary>

No. The geometry, electronic state, model, units, and settings also matter.

</details>

## References

- [Python virtual environments](https://docs.python.org/3/tutorial/venv.html)

## Learning path

[All topics](../README.md) · [Next: Python essentials](../02_python/README.md)

