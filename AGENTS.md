# Grow Tech AI Research Lab

# AGENTS.md

> Repository Entry Point for AI Development Agents
>
> Project: Google WAXAL ASR Challenge
>
> Organization: Grow Tech AI
>
> Version: 2.0.0

---

# Welcome

Welcome to the Grow Tech AI Research Lab.

This repository is not a traditional software project.

It is a documentation-first, specification-driven, AI-assisted engineering laboratory built to develop high-quality, reusable Artificial Intelligence systems.

Every AI assistant joining this repository is considered a senior engineering collaborator.

Your objective is not only to write code, but to preserve architecture, documentation quality, reproducibility and long-term maintainability.

---

# Primary Mission

The current repository develops the official multilingual Automatic Speech
Recognition (ASR) system for the Google WAXAL ASR Challenge.

The project officially adopts:

- one multilingual production model;
- one official training pipeline;
- one preprocessing pipeline;
- one evaluation pipeline;
- one inference pipeline.

Alternative architectures are developed only for benchmarking and research.

The long-term objective is to transform every reusable component into a
permanent asset of the Grow Tech AI Research Lab.

---

# Engineering Philosophy

Always follow these principles.

1. Documentation First

2. Specification First

3. Modular Development

4. Incremental Validation

5. Reproducibility

6. Explain Decisions

7. Preserve Maintainability

Never prioritize short-term speed over long-term quality.

---

# Official Architecture Decisions

Before implementing any feature, every AI agent must understand the project's
Architecture Decision Records (ADR).

Currently accepted decisions are:

ADR-001

Dataset downloads are filtered exclusively using the official Zindi metadata.

Downloading the complete Hugging Face dataset is prohibited.

ADR-002

The project uses one official multilingual ASR model covering Luganda,
Lingala and Shona.

Monolingual models remain research artefacts only.

Future ADRs must be treated as mandatory engineering constraints.

---

# Repository Structure

Main directories

```text
config/
data/
Developer-Pack/
docs/
experiments/
notebooks/
outputs/
scripts/
src/
tests/
```

Business logic belongs inside **src/**.

Notebooks are only used for exploration.

Generated files belong inside **outputs/**.

Documentation belongs inside **docs/**.

---

# Mandatory Reading Order

Before modifying any code, read the following documents in this order

0. docs/ai/...

1. README.md

2. SETUP.md

3. AGENTS.md

4. Developer-Pack/README.md

5. Developer-Pack/00_PROJECT_CONTEXT.md

6. Developer-Pack/01_HACKATHON_SPECIFICATION.md

7. Developer-Pack/02_TECHNICAL_ARCHITECTURE.md

8. Developer-Pack/03_DATASET_DOCUMENTATION.md

9. Developer-Pack/04_RESEARCH_OBJECTIVES.md

10. Developer-Pack/05_DEVELOPMENT_RULES.md

11. Developer-Pack/06_CODING_STANDARDS.md

12. Developer-Pack/07_GIT_WORKFLOW.md

13. Developer-Pack/08_PROJECT_ROADMAP.md

14. Developer-Pack/09_CURRENT_STATUS.md

15. Developer-Pack/10_TASKS.md

16. Developer-Pack/11_DELIVERABLES.md

17. Developer-Pack/12_VALIDATION_CHECKLIST.md

18. Developer-Pack/13_AI_INSTRUCTIONS.md

19. Developer-Pack/14_EXPERIMENT_TRACKING.md

20. Developer-Pack/15_REFERENCES.md


Only after reading these documents may implementation begin.

---

# Official Development Constraints

The following constraints are mandatory.

✓ Documentation First

✓ Specification First

✓ Configuration-driven development

✓ One multilingual production pipeline

✓ Dataset validation before training

✓ Deterministic experiments

✓ Modular architecture

✓ Full traceability

These constraints override implementation preferences.

---

# Development Rules

Always:

- follow Python 3.11;
- respect PEP 8;
- use type hints;
- write Google-style docstrings;
- use logging instead of print();
- update documentation when modifying code;
- keep modules focused on a single responsibility.
- import configuration from configs/
- reuse existing modules
- validate the dataset before training
- respect accepted ADRs
- keep experiments reproducible
- explain architectural impacts

Never:

- hardcode secrets;
- bypass architecture;
- duplicate business logic;
- place production logic inside notebooks;
- commit generated datasets.

---

# Git Workflow

Development always follows:

```text
main
    │
develop
    │
feature/*
```

Every implementation must occur inside a dedicated feature branch.

Merge sequence:

Feature

↓

Develop

↓

Main

Pull Requests are mandatory.

---

# Model Development Policy

The repository distinguishes two categories of models.

Official Model

The multilingual production model.

Research Models

Temporary benchmark models used only for scientific comparison.

Only the official multilingual model may generate competition submissions.

---

# AI Behaviour

You are expected to:

Understand the objective before coding.

Explain technical decisions.

Identify risks.

Suggest alternatives when appropriate.

Produce maintainable code.

Keep documentation synchronized.

Reject unsafe or inconsistent implementations.

Never modify unrelated components.

---

# Documentation Policy

Code and documentation evolve together.

Whenever implementation changes:

Update:

- documentation;
- changelog;
- related specifications;
- task status.

Documentation is considered part of the deliverable.

---

# Experiment Policy

Every experiment must be reproducible.

Record:

- objective;
- hypothesis;
- configuration;
- metrics;
- conclusions.

Experiments without documentation are incomplete.

---

# Experiment Classification

Experiments belong to one of three categories.

Benchmark

Architecture comparison.

Research

Scientific investigation.

Production

Official multilingual pipeline.

Production experiments have the highest priority.

---

# Quality Requirements

Before considering any task complete, verify:

- implementation works;
- tests pass;
- documentation updated;
- architecture respected;
- reproducibility ensured;
- quality checklist completed.

Minimum quality target:

85/100

---

# AI Decision-Making Policy

When multiple implementation options exist, AI agents shall prioritize:

1. architectural consistency;

2. reproducibility;

3. maintainability;

4. modularity;

5. computational efficiency.

Never optimize local performance at the expense of project consistency.

---

# Current Status

Current phase:

Architecture Consolidation

Documentation completed

Dataset engineering in progress

Official baseline pending

Implementation phase starting

Current priorities:

- finalize engineering framework;
- validate environment;
- implement dataset loader;
- reproduce official baseline;
- begin controlled experimentation.

---

# Communication Style

When proposing changes:

Explain:

- why;
- expected benefits;
- trade-offs;
- risks;
- impact on architecture.

Avoid unexplained modifications.

---

# Available Documentation

Developer-Pack/

Contains the complete engineering specifications.

docs/setup/

Environment installation.

docs/research/

Research reports.

docs/ai/

AI operational documentation.

---

# Definition of Success

A successful contribution:

improves the project;

preserves architecture;

remains reusable;

is documented;

is reproducible;

passes review.

---

# Collaboration Principles

AI agents are expected to collaborate through documentation.

Every implementation must:

- preserve repository consistency;
- leave clear documentation;
- update task status;
- remain understandable by another AI agent.

A future AI agent should be able to continue development without additional explanations.

---

# Final Instruction

If information appears missing:

Do not invent.

Search the repository.

Consult documentation.

Review previous decisions.

Then ask for clarification only if absolutely necessary.

Always prioritize:

Architecture

↓

Documentation

↓

Correctness

↓

Reproducibility

↓

Performance

↓

Speed

Engineering quality always prevails over implementation speed.

Welcome to Grow Tech AI.
