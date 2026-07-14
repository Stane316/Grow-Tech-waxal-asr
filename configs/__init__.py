"""
===============================================================================
configs/__init__.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Central entry point for the project's configuration system.

Purpose:
    This module re-exports the most commonly used configuration
    variables from all configuration modules.

    Developers should preferably import configuration values from this
    package instead of importing each module individually.

Example:

    from configs import (
        DATA_DIR,
        MODEL_NAME,
        LEARNING_RATE,
        TARGET_SAMPLE_RATE,
        LOG_FORMAT
    )

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    1.0.0
===============================================================================
"""

# =============================================================================
# PATHS
# =============================================================================

from .paths import *

# =============================================================================
# DATASET
# =============================================================================

from .dataset import *

# =============================================================================
# MODEL
# =============================================================================

from .model import *

# =============================================================================
# TRAINING
# =============================================================================

from .training import *

# =============================================================================
# LOGGING
# =============================================================================

from .logging import *

# =============================================================================
# EXPERIMENT
# =============================================================================

from .experiment import *

# =============================================================================
# PACKAGE METADATA
# =============================================================================

__package_name__ = "configs"

__version__ = "1.0.0"

__author__ = "Grow Tech AI"

__description__ = (
    "Central configuration package for the "
    "Google WAXAL ASR Challenge project."
)

# =============================================================================
# MODULES
# =============================================================================

AVAILABLE_MODULES = (
    "paths",
    "dataset",
    "model",
    "training",
    "logging",
    "experiment",
)

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    *paths.__all__,
    *dataset.__all__,
    *model.__all__,
    *training.__all__,
    *logging.__all__,
    *experiment.__all__,
]