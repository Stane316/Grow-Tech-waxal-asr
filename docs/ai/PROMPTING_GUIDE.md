# Grow Tech AI Research Lab

# PROMPTING_GUIDE

> **Document ID :** AI-PROMPT-001  
> **Category :** AI Prompt Engineering Handbook  
> **Version :** 1.0.0  
> **Project :** Google WAXAL ASR Challenge  
> **Organization :** Grow Tech AI  
> **Status :** Living Document

---

# 1. Purpose

This document defines the official prompting methodology used throughout the Grow Tech AI Research Lab.

Its objective is to ensure that every interaction with an AI assistant is:

- clear;
- contextualized;
- reproducible;
- technically accurate;
- aligned with project standards.

Prompting is considered an engineering discipline, not an informal conversation.

---

# 2. Philosophy

Every prompt should provide the AI with enough information to act as a senior engineer joining the project.

A good prompt minimizes ambiguity and maximizes context.

The objective is not simply to obtain code, but to obtain **well-reasoned engineering contributions**.

---

# 3. The Grow Tech Prompt Formula

Every technical prompt should contain the following elements.

```
Context

↓

Objective

↓

Available Resources

↓

Constraints

↓

Expected Deliverables

↓

Quality Criteria

↓

Output Format
```

Missing one of these elements increases the risk of incomplete or inconsistent outputs.

---

# 4. Prompt Structure

## Step 1 — Context

Explain:

- project;
- current phase;
- repository;
- previous work;
- related documentation.

Example:

```
You are joining the Google WAXAL ASR Challenge repository.

The project already contains a modular architecture.

The current milestone is Dataset Loading.
```

---

## Step 2 — Objective

Clearly state the requested task.

Example:

```
Implement dataset_loader.py.
```

Avoid vague requests.

---

## Step 3 — Resources

List every available resource.

Examples:

- GitHub repository
- Hugging Face dataset
- Competition notebook
- Documentation
- Existing modules

---

## Step 4 — Constraints

Specify all technical constraints.

Examples:

- Python 3.11
- PEP8
- Google Docstrings
- Type hints
- Modular architecture
- No duplicated logic

---

## Step 5 — Deliverables

Specify expected outputs.

Examples:

- Python file
- Documentation
- Tests
- Examples
- Logging
- Validation

---

## Step 6 — Quality Criteria

Explain what defines success.

Example:

- reusable
- modular
- documented
- reproducible
- production-ready

---

## Step 7 — Output Format

Specify the expected response.

Examples:

- complete code
- markdown document
- implementation plan
- architecture proposal
- code review

---

# 5. Prompt Templates

## Template — New Module

```
Context

Current milestone

Objective

Architecture constraints

Expected file

Validation criteria

Required documentation
```

---

## Template — Bug Fix

```
Problem description

Observed behavior

Expected behavior

Files involved

Potential causes

Expected solution
```

---

## Template — Refactoring

```
Current implementation

Weaknesses

Objectives

Constraints

Expected improvements
```

---

## Template — Documentation

```
Document name

Purpose

Audience

Structure

Required sections

Expected output
```

---

## Template — Research

```
Research question

Current knowledge

Hypothesis

Expected analysis

References

Deliverables
```

---

# 6. Prompting Rules

Every prompt should:

- be explicit;
- define scope;
- specify constraints;
- avoid contradictions;
- include repository context.

---

# 7. Context Before Code

Before requesting code, always provide:

- current branch;
- affected modules;
- project phase;
- related documentation.

The AI should never work in isolation from the project context.

---

# 8. Multi-Step Prompting

Complex work should be divided into phases.

Example:

```
Planning

↓

Architecture

↓

Implementation

↓

Review

↓

Optimization
```

Avoid requesting large, unrelated changes in a single prompt.

---

# 9. Progressive Prompting

Prefer iterative development.

Instead of:

```
Build the entire project.
```

Use:

```
Implement dataset_loader.py.

↓

Review.

↓

Improve.

↓

Test.

↓

Document.
```

---

# 10. Prompt Review Checklist

Before sending a prompt, verify:

- Is the objective clear?
- Is enough context provided?
- Are constraints specified?
- Are deliverables listed?
- Is the expected output format defined?

---

# 11. AI Response Evaluation

A good AI response should:

- answer the objective;
- justify decisions;
- respect architecture;
- be reproducible;
- remain maintainable.

---

# 12. Common Mistakes

Avoid:

- vague prompts;
- missing context;
- contradictory instructions;
- unrealistic scope;
- undefined deliverables.

---

# 13. Recommended Prompting Workflow

```
Understand problem

↓

Gather context

↓

Write specification

↓

Generate prompt

↓

AI implementation

↓

Human review

↓

Merge
```

---

# 14. Prompt Library

Maintain a reusable library of prompts for:

- environment setup;
- dataset loading;
- preprocessing;
- training;
- evaluation;
- inference;
- documentation;
- research;
- code review;
- bug fixing.

---

# 15. Prompt Versioning

Important prompts should be version-controlled.

Document:

- purpose;
- modifications;
- related milestone.

This ensures reproducibility.

---

# 16. Prompt Quality Levels

## Level 1 — Basic

Simple requests with minimal context.

---

## Level 2 — Structured

Clear objectives and constraints.

---

## Level 3 — Engineering

Complete context, architecture, validation and deliverables.

This is the minimum level expected for Grow Tech AI.

---

## Level 4 — Research

Includes hypotheses, alternatives, risks and evaluation criteria.

---

## Level 5 — Autonomous Collaboration

The prompt enables the AI to act as a senior collaborator while respecting project governance.

This is the preferred standard.

---

# 17. Prompt Lifecycle

Every reusable prompt follows:

```
Draft

↓

Review

↓

Validation

↓

Reuse

↓

Continuous Improvement
```

---

# 18. Related Documentation

- PROJECT_CONTEXT.md
- ARCHITECTURE.md
- DEVELOPMENT_GUIDE.md
- AI_RULES.md
- TEAM_WORKFLOW.md
- Developer-Pack/

---

# 19. Long-Term Vision

Grow Tech AI aims to build a reusable Prompt Engineering framework applicable to future hackathons, research projects and AI-assisted software engineering.

Prompt quality is considered a strategic asset and a core component of the laboratory's engineering methodology.

---

# 20. Version History

| Version | Date            | Author       | Description                         |
| ------- | --------------- | ------------ | ----------------------------------- |
| 1.0.0   | To be completed | Grow Tech AI | Initial Prompt Engineering Handbook |
