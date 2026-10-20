# AI4CompChem

Learn computational chemistry and how to ask AI useful questions: identify confusion, provide evidence, explore an explanation, and check your understanding.

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

**Available now:** 15 chapter pages and 45 worked Ask AI examples, with improved questions, example answers, follow-ups, and self-checks. Videos, full lessons, and runnable exercises remain in preparation. See the [full learning path](tutorials/README.md).

Each chapter has a dedicated **Ask AI when you get stuck** section. Students learn to turn a vague question into a specific, evidence-based question and assess the response. The answers are course-authored examples, not recorded outputs from a named model. Students can use ChatGPT or another AI tutor and record the tool, displayed model, and date.

The website chapters are linked from the course homepage; matching question-and-answer material is also included in the tutorial READMEs.

## Repository Structure

```text
AI4CompChem/
├── README.md
├── LICENSE
├── requirements.txt
├── content/
│   └── ai_questions.json
├── scripts/
│   └── build_chapters.py
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
    └── chapters/
```

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Updating the Ask AI material

Edit `content/ai_questions.json` for the worked questions and `tutorials/*/README.md` for the chapter outlines, then run:

```bash
python3 scripts/build_chapters.py
```

This rebuilds the static pages in `docs/chapters/` and the matching Ask AI sections in the tutorial READMEs. Commit the content, builder, tutorial, and generated website changes together.
