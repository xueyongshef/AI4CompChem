# 14. Molecular dynamics (MD)

Molecular simulation · Integration · time steps · ensembles · trajectories

**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.

## Learning goals

- Describe how forces and a numerical integrator generate a trajectory.
- Compare NVE, NVT, and NPT simulations and examine time-step choice and equilibration.

## Planned short videos

1. From forces to molecular motion
2. Choosing an ensemble and time step

## Planned exercise

Plan a small Lennard–Jones simulation and compare energy drift for two time steps under NVE conditions.

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

### 1. My NVE total energy drifts.

**Starting question:** “Should I just add a thermostat?”

**A more useful question to ask:**

> My intended NVE simulation shows total-energy drift. Help me design checks of time step, integration settings, constraints, force evaluation, and initial equilibration. Explain why adding a thermostat changes the diagnostic problem.

**Why this helps:** It preserves the intended ensemble and requests a controlled investigation.

**Example answer:** In an ideal isolated conservative system, total energy is conserved. Numerical integration and force approximations can cause deviations. Compare appropriately equilibrated runs at smaller time steps and inspect relevant settings and energy traces. A thermostat exchanges energy with a bath and changes the ensemble; it can hide a symptom without identifying its cause.

**Follow-up to ask:**

> What would a systematic reduction of drift with time step suggest, and what would it not prove?

**Check your understanding:** Does stable temperature after adding a thermostat prove that the original NVE integration was accurate?

<details>
<summary>Reveal the check answer</summary>

No. The thermostat can exchange energy.

</details>

### 2. The thermostat does not keep every temperature value identical.

**Starting question:** “Why is the temperature fluctuating in NVT?”

**A more useful question to ask:**

> Explain instantaneous kinetic temperature and canonical fluctuations. Distinguish a target temperature from a value that must be identical at every frame, and explain what diagnostics depend on the thermostat used.

**Why this helps:** It distinguishes a statistical target from an instantaneous constraint.

**Example answer:** An NVT simulation aims to sample a distribution at a specified temperature. Instantaneous kinetic energy, and therefore a kinetic-temperature estimate, generally fluctuates. The expected behaviour depends on system size, degrees of freedom, and thermostat algorithm. Judge averages, fluctuations, and sampling rather than requiring every frame to equal the target.

**Follow-up to ask:**

> How would changing the number of degrees of freedom affect my interpretation?

**Check your understanding:** Does NVT require the instantaneous kinetic temperature to be exactly constant?

<details>
<summary>Reveal the check answer</summary>

No. Canonical sampling includes fluctuations.

</details>

### 3. I do not know whether a trajectory is equilibrated.

**Starting question:** “My trajectory is long. Is it enough?”

**A more useful question to ask:**

> Help me assess equilibration and sampling for [observable] in [system]. Ask for time traces, initial conditions, run length, and independent runs. Explain why one apparently stable trace cannot prove global equilibrium.

**Why this helps:** It names the observable and asks for evidence of both relaxation and exploration.

**Example answer:** Inspect relevant observables for initial relaxation and compare production estimates across blocks and independent starts. A system may remain trapped in one region while a trace appears stationary. Adequate sampling is property-dependent; elapsed simulation time alone does not establish it.

**Follow-up to ask:**

> Which slow process could affect my observable without being obvious in the total-energy trace?

**Check your understanding:** Can a flat-looking energy trace prove that all important conformations were sampled?

<details>
<summary>Reveal the check answer</summary>

No. Other slow degrees of freedom may remain unexplored.

</details>

## References

- [GROMACS molecular dynamics](https://manual.gromacs.org/documentation/current/reference-manual/algorithms/molecular-dynamics.html)

## Learning path

[All topics](../README.md) · [Previous: Force fields and interaction potentials](../13_force_fields/README.md) · [Next: Statistical mechanics and sampling](../15_statistical_mechanics/README.md)

