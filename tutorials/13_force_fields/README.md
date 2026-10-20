# 13. Force fields and interaction potentials

Molecular simulation · Bonded terms · Lennard–Jones · Coulomb · limitations

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Separate bonded and non-bonded terms in a molecular force field.
- Compare harmonic, Lennard–Jones, and Coulomb potentials and identify the limits of a chosen model.

## Planned short videos

1. What is an interaction potential?
2. Building a molecular force field from energy terms

## Planned exercise

Plot a Lennard–Jones pair potential, locate its minimum, and obtain the force from its derivative with consistent units.

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

### 1. I do not understand what a force field adds together.

**Starting question:** “Is a force field just a Lennard–Jones potential?”

**A more useful question to ask:**

> Describe a typical molecular force field using bond, angle, torsion, Lennard–Jones, and Coulomb terms. Explain why the topology and non-bonded exclusions or scaling rules must match the parameter set.

**Why this helps:** It asks for the whole model and the conventions connecting its parts.

**Example answer:** A molecular force field commonly combines bonded and non-bonded terms, with parameters and conventions designed to work together. Topology determines which interactions apply. Some nearby bonded pairs are excluded or scaled in non-bonded calculations. A Lennard–Jones term alone does not represent this entire molecular model.

**Follow-up to ask:**

> What would happen if I counted an interaction twice by ignoring the exclusions?

**Check your understanding:** Does a Lennard–Jones pair term include every bonded and electrostatic interaction?

<details>
<summary>Reveal the check answer</summary>

No. Those require their own specified terms and conventions.

</details>

### 2. I confuse sigma with the equilibrium separation.

**Starting question:** “Why is the Lennard–Jones minimum not at sigma?”

**A more useful question to ask:**

> For U(r) = 4*epsilon*((sigma/r)^12 - (sigma/r)^6), show briefly where the energy crosses zero and where its minimum occurs. Distinguish sigma from the minimum position and epsilon from a distance.

**Why this helps:** It specifies the convention, making the parameter meanings checkable.

**Example answer:** At r = sigma the two powers cancel, so U = 0. Setting the derivative to zero gives r_min = 2^(1/6)*sigma, approximately 1.122*sigma. At that separation U = -epsilon. Sigma is a length parameter, while epsilon sets the well depth in energy units.

**Follow-up to ask:**

> Which parameter would I change to deepen the well without moving its minimum?

**Check your understanding:** Is the energy at r = sigma equal to -epsilon?

<details>
<summary>Reveal the check answer</summary>

No. It is zero for the stated convention.

</details>

### 3. My force curve has the wrong sign or units.

**Starting question:** “Can I use the potential energy as the force?”

**A more useful question to ask:**

> For a pair potential U(r), explain the radial force convention F_r = -dU/dr. State the force units when energy is in kJ/mol and distance in nm, and relate the sign to attraction and repulsion.

**Why this helps:** It fixes the coordinate and units before discussing the derivative.

**Example answer:** The radial force is the negative derivative of energy with respect to separation. Its units are kJ/mol/nm for the stated quantities. With increasing r as the positive radial direction, a negative radial force is attractive and a positive one repulsive. At a potential minimum the derivative and radial force vanish.

**Follow-up to ask:**

> How could I check an analytic force against a small finite difference in energy?

**Check your understanding:** What is the radial force at a smooth potential minimum?

<details>
<summary>Reveal the check answer</summary>

Zero.

</details>

## References

- [GROMACS bonded interaction potentials](https://manual.gromacs.org/documentation/current/reference-manual/functions/bonded-interactions.html)
- [GROMACS non-bonded interactions](https://manual.gromacs.org/documentation/current/reference-manual/functions/nonbonded-interactions.html)

## Learning path

[All topics](../README.md) · [Previous: Transition states and reaction paths](../12_reaction_paths/README.md) · [Next: Molecular dynamics (MD)](../14_molecular_dynamics/README.md)

