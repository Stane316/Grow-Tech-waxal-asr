# Grow Tech AI Research Lab

# AI Documentation Hub

> **Document ID :** AI-README-001  
> **Category :** AI Onboarding & Navigation  
> **Version :** 1.0.0  
> **Project :** Google WAXAL ASR Challenge  
> **Organization :** Grow Tech AI  
> **Status :** Living Document

---

# Welcome

Welcome to the AI Documentation Hub of the **Grow Tech AI Research Lab**.

This directory is designed for AI development assistants (Codex, Claude Code, Cursor, Gemini CLI, Windsurf, etc.) joining the project.

Its purpose is to provide every AI agent with all the information required to understand the project, respect its engineering standards, and contribute effectively from the first task.

This documentation complements the human-oriented documentation available in:

```
docs/setup/
docs/research/
Developer-Pack/
```

while focusing specifically on **AI-assisted software engineering**.

---

# Mission

Every AI agent must be able to answer the following questions before writing any code:

- What is this project?
- Why does it exist?
- What problem does it solve?
- What is the current state?
- How is the repository organized?
- Which coding standards must be followed?
- Which tasks remain?
- Which files may be modified?
- Which decisions have already been made?
- How should improvements be proposed?

If one of these questions cannot be answered, the AI should consult the relevant document before proceeding.

---

# Documentation Structure

```
docs/
└── ai/
    ├── README.md
    ├── PROJECT_CONTEXT.md
    ├── ARCHITECTURE.md
    ├── DEVELOPMENT_GUIDE.md
    ├── TASKS.md
    ├── ROADMAP.md
    ├── TEAM_WORKFLOW.md
    ├── AI_RULES.md
    ├── PROMPTING_GUIDE.md
    ├── CONTEXT_MEMORY.md
    ├── TOOL_USAGE.md
    ├── QUALITY_ASSURANCE.md
    ├── REVIEW_PROCESS.md
    ├── AGENT_ROLES.md
    └── CHANGELOG.md
```

---

# Reading Order

Every AI should follow this reading order.

## Step 1 — Understand the project

Read:

- PROJECT_CONTEXT.md

Goal:

Understand the hackathon, the research objectives and the expected deliverables.

---

## Step 2 — Understand the architecture

Read:

- ARCHITECTURE.md

Goal:

Understand how the repository is organized and where each component belongs.

---

## Step 3 — Learn the development workflow

Read:

- DEVELOPMENT_GUIDE.md
- TEAM_WORKFLOW.md

Goal:

Understand how to implement new features and collaborate with the team.

---

## Step 4 — Learn the project rules

Read:

- AI_RULES.md
- QUALITY_ASSURANCE.md

Goal:

Respect the coding standards and validation requirements.

---

## Step 5 — Understand the current work

Read:

- TASKS.md
- ROADMAP.md
- CONTEXT_MEMORY.md

Goal:

Know what has already been completed and what remains to be done.

---

## Step 6 — Before submitting work

Read:

- REVIEW_PROCESS.md

Goal:

Ensure the contribution satisfies the project's review process.

---

# AI Mission

Every AI joining this project acts as a **Senior Research Software Engineer**.

The objective is not only to produce working code.

The objective is to build:

- reusable software;
- reproducible experiments;
- maintainable architectures;
- production-quality documentation;
- reusable AI research assets.

---

# Engineering Philosophy

The project follows the following principles:

1. Modularity.
2. Reproducibility.
3. Readability.
4. Documentation-first.
5. Specification-driven development.
6. Research before implementation.
7. Continuous improvement.

Every contribution should strengthen these principles.

---

# Development Workflow

The expected workflow is:

```
Understand
        ↓
Analyse
        ↓
Read Documentation
        ↓
Plan
        ↓
Implement
        ↓
Test
        ↓
Document
        ↓
Review
        ↓
Merge
```

No implementation should skip these steps.

---

# Repository Overview

Main directories:

```
config/
data/
docs/
experiments/
notebooks/
output/
scripts/
src/
tests/
Developer-Pack/
```

Each directory has a clearly defined responsibility.

The architecture is documented in:

```
ARCHITECTURE.md
```

---

# Documentation Ecosystem

The repository documentation is divided into three layers.

## Layer 1 — Setup

```
docs/setup/
```

Purpose:

Environment installation and project configuration.

---

## Layer 2 — Research

```
docs/research/
```

Purpose:

Scientific documentation.

Experiments.

Ideas.

Literature.

Decisions.

Dataset analysis.

---

## Layer 3 — AI

```
docs/ai/
```

Purpose:

Documentation dedicated to AI development assistants.

---

# Before Writing Code

Every AI must verify that:

- the requested task is clearly understood;
- the appropriate module exists;
- no duplicated implementation already exists;
- the architecture remains consistent;
- documentation has been reviewed.

---

# Communication Principles

When proposing a modification:

The AI must:

- explain the rationale;
- describe advantages;
- describe limitations;
- identify risks;
- justify architectural choices.

The AI should never make significant architectural decisions without explanation.

---

# Branch Strategy

Development follows the Git workflow defined in:

```
07_GIT_WORKFLOW.md
```

General rules:

- one feature per branch;
- one Pull Request per logical feature;
- no direct commits to `main`;
- documentation updated alongside the code.

---

# Quality Expectations

Every contribution should satisfy:

- PEP 8;
- static typing;
- Google-style docstrings;
- logging instead of print;
- reproducibility;
- deterministic behavior whenever possible;
- clear documentation;
- automated validation when applicable.

---

# Related Documentation

Developer-Pack/

- PROJECT_CONTEXT
- ROADMAP
- TASKS
- DELIVERABLES
- VALIDATION_CHECKLIST

Research Documentation

- Dataset Audit
- Baseline Analysis
- Experiment Log
- Decision Log
- Related Work

Setup Documentation

- Environment Setup
- Hugging Face Setup
- GPU Setup
- Troubleshooting

---

# Long-Term Vision

This documentation is designed to outlive the Google WAXAL ASR Challenge.

It serves as the operational foundation for future:

- hackathons;
- research projects;
- AI agents;
- reusable software components;
- Grow Tech AI initiatives;
- GrowTech projects;
- FacturaPro AI integrations.

Every improvement made here should benefit future projects.

---

# Living Document

This document evolves throughout the project.

Whenever the project architecture, workflow or AI collaboration strategy changes, this document must be updated accordingly.

---

# Version History

| Version | Date            | Author       | Description                                 |
| ------- | --------------- | ------------ | ------------------------------------------- |
| 1.0.0   | To be completed | Grow Tech AI | Initial version of the AI Documentation Hub |
