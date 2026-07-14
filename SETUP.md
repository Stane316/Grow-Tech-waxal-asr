# SETUP.md

# 🚀 Grow Tech WAXAL ASR - Complete Setup Guide

> **Version:** 1.0.0
>
> **Project:** Grow Tech WAXAL ASR
>
> **Purpose:** Complete installation and configuration guide for all contributors.

---

# Table of Contents

1. Introduction
2. Prerequisites
3. Clone the Repository
4. Install Python
5. Create a Virtual Environment
6. Install Dependencies
7. Configure Environment Variables
8. Configure Hugging Face
9. Download the Dataset
10. Verify the Environment
11. First Run
12. Project Structure
13. Development Workflow
14. Common Commands
15. Troubleshooting
16. Updating the Environment

---

# 1. Introduction

Welcome to the Grow Tech WAXAL ASR project.

This guide explains how to configure a fully functional development environment.

When every step has been completed successfully, you will be able to:

- run every script;
- access the dataset;
- train models;
- launch experiments;
- contribute to the repository.

---

# 2. Prerequisites

Required:

- Git
- Python 3.12+
- pip
- Internet connection
- Hugging Face account

Recommended:

- VS Code
- NVIDIA GPU
- CUDA Toolkit
- GitHub account

Recommended RAM:

Minimum:

16 GB

Recommended:

32 GB

Disk space:

Minimum:

500 GB

Recommended:

1 TB+

---

# 3. Clone the Repository

```bash
git clone <repository-url>
```

Move inside the project.

```bash
cd Grow-Tech-WAXAL-ASR
```

---

# 4. Install Python

Verify Python.

```bash
python --version
```

or

```bash
python3 --version
```

Expected:

```text
Python 3.12.x
```

---

# 5. Create the Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

# 6. Upgrade pip

```bash
python -m pip install --upgrade pip
```

Verify.

```bash
pip --version
```

---

# 7. Install Project Dependencies

```bash
pip install -r requirements.txt
```

Verify installed packages.

```bash
pip list
```

---

# 8. Configure Environment Variables

Copy:

```text
.env.example
```

into

```text
.env
```

Example:

```bash
cp .env.example .env
```

or manually duplicate the file on Windows.

Complete the required values.

Never commit:

```text
.env
```

---

# 9. Configure Hugging Face

Login.

```bash
huggingface-cli login
```

Paste your access token.

Verify.

```bash
huggingface-cli whoami
```

---

# 10. Download the Dataset

Execute:

```bash
python scripts/download_dataset.py
```

Expected directory:

```text
data/

train/

validation/

test/
```

---

# 11. Verify the Environment

Run:

```bash
python scripts/check_environment.py
```

Expected checks:

- Python version
- Dependencies
- GPU
- CUDA
- Hugging Face
- Dataset
- Environment variables

Every check should pass.

---

# 12. Verify GPU

Run:

```bash
python
```

Inside Python:

```python
import torch

torch.cuda.is_available()
```

Expected:

```python
True
```

If False:

CPU mode will be used.

---

# 13. Clean Temporary Cache

Run:

```bash
python scripts/clean_cache.py
```

Optional:

```bash
python scripts/clean_cache.py --dry-run
```

---

# 14. First Project Execution

Recommended order:

```text
1.
check_environment.py

↓

2.
download_dataset.py

↓

3.
dataset_loader.py

↓

4.
dataset_validator.py
```

The project is now ready for development.

---

# 15. VS Code Extensions

Recommended:

- Python
- Pylance
- Ruff
- Black Formatter
- GitLens
- Jupyter
- YAML
- Markdown All in One
- Error Lens

---

# 16. Project Structure

```text
configs/

data/

Developer-Pack/

docs/

experiments/

notebooks/

outputs/

scripts/

specifications/

src/

tests/
```

---

# 17. Development Workflow

Recommended workflow.

```text
Pull

↓

Create Branch

↓

Develop

↓

Run Tests

↓

Update Documentation

↓

Commit

↓

Push

↓

Pull Request
```

---

# 18. Common Commands

Activate environment

```bash
.venv\Scripts\activate
```

Install dependency

```bash
pip install package_name
```

Update requirements

```bash
pip freeze > requirements.txt
```

Run tests

```bash
pytest
```

Run a specific test

```bash
pytest tests/
```

Format code

```bash
black .
```

Lint

```bash
ruff check .
```

---

# 19. Updating Dependencies

Upgrade pip.

```bash
python -m pip install --upgrade pip
```

Upgrade packages.

```bash
pip install -U -r requirements.txt
```

---

# 20. Troubleshooting

## Python not found

Verify PATH.

---

## Virtual environment not activating

Delete:

```text
.venv
```

Recreate it.

---

## Missing dependency

Run:

```bash
pip install -r requirements.txt
```

---

## Hugging Face authentication failed

Repeat:

```bash
huggingface-cli login
```

---

## Dataset not found

Execute:

```bash
python scripts/download_dataset.py
```

---

## CUDA unavailable

Check:

- NVIDIA driver
- CUDA Toolkit
- PyTorch installation

---

# 21. Validation Checklist

Before contributing, verify:

- Python installed

- Virtual environment active

- Dependencies installed

- .env configured

- Hugging Face connected

- Dataset downloaded

- Environment validated

- Tests successful

---

# 22. Next Steps

Once the setup is complete:

Read:

```text
README.md
```

Then:

```text
Developer-Pack/
```

Then:

```text
AGENTS.md
```

You are now ready to begin development.

---

# Congratulations!

Your development environment is fully configured.

Welcome to the Grow Tech WAXAL ASR Research Lab.

Happy Coding!