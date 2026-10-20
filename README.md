# AI4CompChem

Learn computational chemistry with AI-assisted explanations, short videos, and reproducible exercises.

## Website

Course website: [xueyongshef.github.io/AI4CompChem](https://xueyongshef.github.io/AI4CompChem/).

## Curriculum

The learning path contains **15 topics in four stages**. Start with the foundations or open the topic you need.

| Stage | Topics |
| --- | --- |
| Foundations | [Getting started](tutorials/01_getting_started/README.md) · [Python essentials](tutorials/02_python/README.md) · [Working with molecules](tutorials/03_molecules/README.md) · [Quantum chemistry foundations](tutorials/04_quantum_foundations/README.md) |
| Electronic structure | [Basis sets](tutorials/05_basis_sets/README.md) · [Hartree–Fock (HF)](tutorials/06_hartree_fock/README.md) · [Electron correlation and post-HF](tutorials/07_electron_correlation/README.md) · [Density functional theory (DFT)](tutorials/08_dft/README.md) |
| Potential energy and reactions | [Potential energy surfaces (PES)](tutorials/09_potential_energy_surfaces/README.md) · [Geometry optimisation](tutorials/10_geometry_optimisation/README.md) · [Vibrations and thermochemistry](tutorials/11_vibrations_thermochemistry/README.md) · [Transition states and reaction paths](tutorials/12_reaction_paths/README.md) |
| Molecular simulation | [Force fields and interaction potentials](tutorials/13_force_fields/README.md) · [Molecular dynamics (MD)](tutorials/14_molecular_dynamics/README.md) · [Statistical mechanics and sampling](tutorials/15_statistical_mechanics/README.md) |

**Status:** topic outlines are available; videos, detailed lessons, and runnable exercises are in preparation. See the [full learning path](tutorials/README.md) for the proposed sequence and each topic's learning goals.

Each topic is organised around a short video, a concept explanation, a worked calculation, an exercise, and an AI study prompt.

## Repository Structure

```text
AI4CompChem/
├── README.md
├── LICENSE
├── requirements.txt
├── tutorials/
│   ├── README.md
│   ├── 01_getting_started/
│   ├── 02_python/
│   ├── 03_molecules/
│   ├── 04_quantum_foundations/
│   ├── 05_basis_sets/
│   ├── 06_hartree_fock/
│   ├── 07_electron_correlation/
│   ├── 08_dft/
│   ├── 09_potential_energy_surfaces/
│   ├── 10_geometry_optimisation/
│   ├── 11_vibrations_thermochemistry/
│   ├── 12_reaction_paths/
│   ├── 13_force_fields/
│   ├── 14_molecular_dynamics/
│   └── 15_statistical_mechanics/
├── notebooks/
├── examples/
└── docs/
```

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
