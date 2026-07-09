# Grow Tech AI Research Lab

# AGENTS.md

> Repository Entry Point for AI Development Agents
>
> Project: Google WAXAL ASR Challenge
>
> Organization: Grow Tech AI
>
> Version: 1.0.0

---

# Welcome

Welcome to the Grow Tech AI Research Lab.

This repository is not a traditional software project.

It is a documentation-first, specification-driven, AI-assisted engineering laboratory built to develop high-quality, reusable Artificial Intelligence systems.

Every AI assistant joining this repository is considered a senior engineering collaborator.

Your objective is not only to write code, but to preserve architecture, documentation quality, reproducibility and long-term maintainability.

---

# Primary Mission

The current repository supports the development of a multilingual Automatic Speech Recognition (ASR) system for the Google WAXAL ASR Challenge.

The long-term objective is larger.

Every component developed here must become reusable for future AI competitions and research projects.

Think beyond the current competition.

Build reusable engineering assets.

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

Before modifying any code, read the following documents in this order.

## Step 1

docs/ai/

README.md

---

## Step 2

PROJECT_CONTEXT.md

---

## Step 3

ARCHITECTURE.md

---

## Step 4

DEVELOPMENT_GUIDE.md

---

## Step 5

AI_RULES.md

---

## Step 6

TEAM_WORKFLOW.md

---

## Step 7

QUALITY_ASSURANCE.md

---

## Step 8

REVIEW_PROCESS.md

---

## Step 9

TASKS.md

---

## Step 10

ROADMAP.md

---

## Step 11

CONTEXT_MEMORY.md

---

Only after reading these documents may implementation begin.

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

# Current Status

Current phase:

Research Laboratory Setup

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

# Final Instruction

If information appears missing:

Do not invent.

Search the repository.

Consult documentation.

Review previous decisions.

Then ask for clarification only if absolutely necessary.

Always prioritize consistency over speed.

Welcome to Grow Tech AI.
