# Grow Tech AI Research Lab

# 06_CODING_STANDARDS

> **Document ID:** BFADP-06
>
> **Version:** 1.0.0
>
> **Status:** Active
>
> **Category:** Coding Standards
>
> **Project:** Google WAXAL ASR Challenge
>
> **Organization:** Grow Tech AI

---

# 1. Purpose of this Document

This document defines the official coding standards adopted by the Grow Tech AI Research Lab.

Its purpose is to ensure that all source code written by human developers and AI assistants is:

- readable;
- maintainable;
- modular;
- consistent;
- reproducible;
- easy to review.

These standards apply to every Python file within the repository.

---

# 2. General Principles

Every source file should prioritize:

- clarity over cleverness;
- simplicity over complexity;
- readability over optimization;
- explicit behavior over implicit behavior;
- modularity over duplication.

Code is written for humans first and machines second.

---

# 3. Python Version

The project targets:

Python 3.11

All code must remain compatible with this version.

---

# 4. Style Guide

The project follows:

- PEP 8
- PEP 257
- Google Python Style Guide (for docstrings)

Formatting should be automated whenever possible.

Recommended tools:

- Black
- Ruff
- isort

---

# 5. File Organization

A Python file should generally follow this structure:

```python
Module docstring

Imports

Constants

Configuration

Classes

Functions

Main execution block (if applicable)
```

Avoid mixing unrelated responsibilities in the same file.

---

# 6. Imports

Imports should be grouped in the following order:

```python
# Standard library

# Third-party packages

# Local project imports
```

Example:

```python
import logging
from pathlib import Path

import pandas as pd
from datasets import load_dataset

from src.utils.logger import get_logger
```

Avoid wildcard imports.

---

# 7. Naming Conventions

Variables:

```python
audio_path
learning_rate
batch_size
```

Functions:

```python
load_dataset()
train_model()
evaluate_predictions()
```

Classes:

```python
DatasetLoader
TrainingPipeline
ExperimentTracker
```

Constants:

```python
DEFAULT_BATCH_SIZE
CACHE_DIRECTORY
```

Private members:

```python
_internal_method()
```

---

# 8. Function Design

Functions should:

- perform one task;
- be short;
- be testable;
- avoid side effects.

Whenever possible:

- fewer than 40 lines;
- limited nesting;
- explicit return values.

---

# 9. Type Hints

All public functions must include type annotations.

Example:

```python
def load_dataset(path: Path) -> Dataset:
    ...
```

Avoid untyped public APIs.

---

# 10. Docstrings

Every public function, class and module should include a Google-style docstring.

Example:

```python
def preprocess_audio(audio_path: Path) -> np.ndarray:
    """
    Load and preprocess an audio file.

    Args:
        audio_path:
            Path to the audio file.

    Returns:
        Preprocessed waveform.

    Raises:
        FileNotFoundError:
            If the file does not exist.
    """
```

---

# 11. Comments

Comments should explain:

- why;
- assumptions;
- non-obvious decisions.

Avoid comments that merely repeat the code.

Poor:

```python
i += 1  # increment i
```

Better:

```python
# Skip corrupted samples to preserve experiment reproducibility.
```

---

# 12. Logging

Use the logging module instead of print().

Example:

```python
logger.info("Dataset successfully loaded.")
logger.warning("Missing metadata detected.")
logger.error("Training failed.")
```

Logs should provide meaningful context.

---

# 13. Error Handling

Catch only expected exceptions.

Example:

```python
try:
    ...
except FileNotFoundError:
    ...
```

Avoid:

```python
except:
    pass
```

Every handled exception should include an informative message.

---

# 14. Configuration

Never hardcode:

- dataset paths;
- learning rates;
- batch sizes;
- API keys.

Use:

- YAML files;
- environment variables;
- configuration classes.

---

# 15. Project Structure

Business logic belongs in:

```
src/
```

Scripts belong in:

```
scripts/
```

Research notebooks belong in:

```
notebooks/
```

Documentation belongs in:

```
docs/
```

---

# 16. Testing Standards

Reusable code should be testable.

Preferred structure:

```
tests/

test_dataset_loader.py
test_preprocessing.py
test_metrics.py
```

Every critical module should eventually receive automated tests.

---

# 17. Performance Guidelines

Optimize only after measuring.

Avoid premature optimization.

Document any optimization that increases code complexity.

---

# 18. Code Reuse

Avoid duplication.

If logic appears multiple times, extract it into:

- utility functions;
- helper classes;
- reusable modules.

---

# 19. Security Standards

Never commit:

- credentials;
- API tokens;
- datasets;
- model checkpoints;
- cache directories.

Sensitive information belongs in:

```
.env
```

---

# 20. Documentation Synchronization

Whenever code changes:

- update documentation;
- update task status;
- update experiment logs if applicable.

Code and documentation must remain synchronized.

---

# 21. AI Coding Standards

AI assistants must:

- preserve repository architecture;
- follow existing naming conventions;
- generate typed code;
- write complete docstrings;
- avoid unnecessary abstractions;
- justify non-trivial implementations.

Generated code should be production-ready whenever possible.

---

# 22. Code Review Checklist

Before submitting code, verify:

- PEP 8 compliance;
- meaningful names;
- type hints;
- docstrings;
- logging;
- error handling;
- modularity;
- readability;
- configuration externalization.

---

# 23. Anti-Patterns

Avoid:

- functions with multiple unrelated responsibilities;
- duplicated logic;
- deeply nested code;
- magic numbers;
- global mutable state;
- hardcoded paths;
- hidden side effects;
- silent exception handling.

---

# 24. Relationship with Other Documents

This document complements:

- 02_TECHNICAL_ARCHITECTURE.md
- 05_DEVELOPMENT_RULES.md
- 07_GIT_WORKFLOW.md
- docs/ai/DEVELOPMENT_GUIDE.md
- docs/ai/QUALITY_ASSURANCE.md

---

# 25. Maintenance Policy

This document should evolve whenever:

- new coding conventions are adopted;
- tooling changes;
- repository architecture evolves;
- quality standards improve.

Every contributor is expected to follow the latest version.

---

# 26. Conclusion

The coding standards defined in this document establish a common programming language for the Grow Tech AI Research Lab.

By following these conventions, contributors ensure that the repository remains readable, maintainable and scalable throughout the lifecycle of the Google WAXAL ASR Challenge and future research projects.

High-quality code is not only correct—it is understandable, reusable and sustainable.
