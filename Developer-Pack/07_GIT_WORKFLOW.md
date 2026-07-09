# Grow Tech AI Research Lab

# 07_GIT_WORKFLOW

> **Document ID:** BFADP-07
>
> **Version:** 1.0.0
>
> **Status:** Active
>
> **Category:** Git Workflow
>
> **Project:** Google WAXAL ASR Challenge
>
> **Organization:** Grow Tech AI

---

# 1. Purpose of this Document

This document defines the official Git workflow of the Grow Tech AI Research Lab.

Its objectives are to:

- standardize collaborative development;
- ensure repository stability;
- facilitate AI-assisted development;
- preserve code quality;
- guarantee traceability of every modification.

Every contributor must follow this workflow.

---

# 2. Development Philosophy

The repository follows a **Git Flow inspired workflow**, adapted for AI-assisted software engineering.

Main principles:

- no direct development on `main`;
- every feature is isolated;
- every modification is reviewed;
- every merge is documented;
- every change remains traceable.

---

# 3. Branch Strategy

The repository is organized around three categories of branches.

```
main

│

develop

│

feature/*
```

---

# 4. Main Branch

Purpose:

Production-ready code.

Characteristics:

- always stable;
- always deployable;
- protected branch;
- reviewed code only.

Direct commits are prohibited.

---

# 5. Develop Branch

Purpose:

Integration branch.

Characteristics:

- receives validated features;
- integration testing;
- preparation for release.

This branch reflects the current development state.

---

# 6. Feature Branches

Every new feature is developed in its own branch.

Naming convention:

```
feature/<short-description>
```

Examples:

```
feature/dataset-loader

feature/gemma-baseline

feature/whisper-model

feature/hubert-model

feature/preprocessing

feature/eda

feature/inference

feature/evaluation
```

Each branch must implement one clearly defined objective.

---

# 7. Branch Lifecycle

```
develop

↓

Create feature branch

↓

Implementation

↓

Local testing

↓

Documentation update

↓

Pull Request

↓

Technical review

↓

Merge into develop

↓

Release validation

↓

Merge develop → main
```

---

# 8. Feature Development Process

Each feature follows six stages.

### Stage 1 — Planning

Before coding:

- objective defined;
- specification written;
- dependencies identified.

---

### Stage 2 — Development

Implementation occurs only inside:

```
feature/*
```

No unrelated modifications are allowed.

---

### Stage 3 — Validation

Verify:

- code execution;
- tests;
- documentation;
- formatting;
- logging.

---

### Stage 4 — Pull Request

A Pull Request is created targeting:

```
develop
```

The description must explain:

- objective;
- implementation;
- testing;
- limitations.

---

### Stage 5 — Review

The Pull Request is reviewed.

Possible outcomes:

- Approved
- Changes Requested
- Rejected

---

### Stage 6 — Merge

Once approved:

```
feature/*

↓

develop
```

Only reviewed code may reach `develop`.

---

# 9. Release Workflow

When a milestone is completed:

```
develop

↓

Validation

↓

Documentation Review

↓

Experiment Validation

↓

Merge

↓

main
```

The `main` branch always reflects a stable project state.

---

# 10. Commit Message Convention

Commit messages follow the Conventional Commits specification.

Examples:

```
feat: implement dataset loader

fix: correct metadata parsing

docs: update setup guide

refactor: simplify preprocessing pipeline

test: add dataset validation tests

chore: update dependencies
```

This improves project history readability.

---

# 11. Pull Request Template

Every Pull Request should contain:

## Summary

Brief description.

## Motivation

Why the change is necessary.

## Technical Changes

Implemented modifications.

## Testing

Executed tests.

## Documentation

Updated documents.

## Risks

Potential side effects.

---

# 12. Merge Policy

A Pull Request may be merged only if:

- specification exists;
- code review completed;
- documentation updated;
- tests successful;
- no conflicts remain.

---

# 13. Branch Protection

The following branches should be protected:

```
main

develop
```

Recommended GitHub settings:

- Require Pull Request.
- Require review.
- Prevent force push.
- Prevent branch deletion.
- Require successful checks.

---

# 14. AI Development Workflow

AI assistants always work inside:

```
feature/*
```

They must never:

- commit directly to main;
- modify unrelated modules;
- bypass Pull Requests.

Every AI-generated change must remain reviewable.

---

# 15. Documentation Workflow

Documentation evolves alongside code.

Whenever implementation changes:

```
Code

↓

Documentation

↓

Experiment Log

↓

Decision Log

↓

Changelog
```

Documentation must never lag behind implementation.

---

# 16. Conflict Resolution

Merge conflicts should be resolved by:

1. understanding both modifications;
2. preserving repository consistency;
3. avoiding duplicate logic;
4. updating documentation if necessary.

Conflict resolution must never introduce undocumented behavior.

---

# 17. Release Management

Major milestones should correspond to Git tags.

Example:

```
v0.1.0

Baseline reproduced

v0.2.0

Dataset pipeline completed

v0.3.0

First training framework

v0.4.0

Model benchmarking

v1.0.0

Competition submission
```

---

# 18. Repository Maintenance

Regular maintenance tasks include:

- removing obsolete branches;
- updating documentation;
- cleaning stale experiments;
- archiving completed milestones.

---

# 19. Relationship with Other Documents

This document complements:

- 05_DEVELOPMENT_RULES.md
- 06_CODING_STANDARDS.md
- 10_TASKS.md
- 12_VALIDATION_CHECKLIST.md
- docs/ai/TEAM_WORKFLOW.md
- docs/ai/REVIEW_PROCESS.md

---

# 20. Compliance Checklist

Before merging:

✓ Feature isolated

✓ Specification available

✓ Documentation updated

✓ Tests executed

✓ Review completed

✓ No merge conflicts

✓ Commit messages compliant

✓ Repository remains stable

---

# 21. Maintenance Policy

Update this document whenever:

- branching strategy changes;
- review process evolves;
- automation is introduced;
- release management changes.

---

# 22. Conclusion

The Git workflow defined in this document establishes a disciplined and reproducible development process for the Grow Tech AI Research Lab.

By isolating features, enforcing reviews and synchronizing documentation with implementation, the workflow enables efficient collaboration between human developers and AI assistants while preserving the stability and long-term maintainability of the repository.
