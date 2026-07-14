"""
===============================================================================
experiment.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized experiment configuration.

Purpose:
    This module centralizes every parameter related to experiment
    management, reproducibility, versioning, checkpoints,
    experiment tracking and result organization.

    Every training, evaluation and inference script MUST import this
    module instead of defining experiment parameters locally.

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    1.0.0
===============================================================================
"""

from datetime import datetime
from enum import Enum

from configs.paths import (
    EXPERIMENTS_DIR,
    RUNS_DIR,
    CHECKPOINTS_DIR,
    REPORTS_DIR,
)

# =============================================================================
# EXPERIMENT IDENTIFICATION
# =============================================================================

PROJECT_NAME = "growtech-waxal-asr"

TEAM_NAME = "Grow Tech AI"

EXPERIMENT_NAME = "baseline"

EXPERIMENT_VERSION = "v1.0.0"

RUN_NAME = "baseline_run"

DESCRIPTION = (
    "Official baseline configuration for the Google WAXAL ASR Challenge."
)

# =============================================================================
# RUN IDENTIFICATION
# =============================================================================

RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

RUN_ID = f"{EXPERIMENT_NAME}_{RUN_TIMESTAMP}"

# =============================================================================
# DIRECTORIES
# =============================================================================

EXPERIMENT_ROOT = EXPERIMENTS_DIR

RUN_DIRECTORY = RUNS_DIR / RUN_ID

CHECKPOINT_DIRECTORY = CHECKPOINTS_DIR / RUN_ID

REPORT_DIRECTORY = REPORTS_DIR / RUN_ID

# =============================================================================
# VERSIONING
# =============================================================================

PROJECT_VERSION = "1.0.0"

DATASET_VERSION = "official"

MODEL_VERSION = "1.0"

CONFIG_VERSION = "1.0"

CODE_VERSION = "main"

# =============================================================================
# REPRODUCIBILITY
# =============================================================================

ENABLE_REPRODUCIBILITY = True

SAVE_CONFIGURATION = True

SAVE_ENVIRONMENT = True

SAVE_REQUIREMENTS = True

SAVE_GIT_COMMIT = True

SAVE_RANDOM_SEED = True

SAVE_HARDWARE_INFORMATION = True

# =============================================================================
# CHECKPOINT POLICY
# =============================================================================

SAVE_BEST_MODEL = True

SAVE_LAST_MODEL = True

SAVE_EVERY_CHECKPOINT = False

MAX_CHECKPOINTS = 5

KEEP_BEST_ONLY = False

AUTO_RESUME = True

# =============================================================================
# EXPERIMENT TRACKING
# =============================================================================

class TrackingBackend(str, Enum):
    NONE = "none"
    TENSORBOARD = "tensorboard"
    WANDB = "wandb"
    MLFLOW = "mlflow"


TRACKING_BACKEND = TrackingBackend.TENSORBOARD

ENABLE_TRACKING = True

TRACK_PARAMETERS = True

TRACK_METRICS = True

TRACK_SYSTEM_INFORMATION = True

TRACK_GPU = True

TRACK_CPU = True

TRACK_MEMORY = True

TRACK_EXECUTION_TIME = True

# =============================================================================
# METRICS
# =============================================================================

PRIMARY_METRIC = "wer"

SECONDARY_METRICS = [
    "cer",
]

LOWER_IS_BETTER = True

# =============================================================================
# REPORT GENERATION
# =============================================================================

GENERATE_SUMMARY = True

GENERATE_HTML_REPORT = True

GENERATE_JSON_REPORT = True

GENERATE_MARKDOWN_REPORT = True

SAVE_PLOTS = True

SAVE_CONFUSION_ANALYSIS = False

# =============================================================================
# EXPORTS
# =============================================================================

EXPORT_MODEL = True

EXPORT_TOKENIZER = True

EXPORT_CONFIGURATION = True

EXPORT_RESULTS = True

EXPORT_METRICS = True

EXPORT_LOGS = True

# =============================================================================
# COMPARISON
# =============================================================================

ENABLE_EXPERIMENT_COMPARISON = True

COMPARE_WITH_BASELINE = True

COMPARE_TOP_N = 10

# =============================================================================
# CLEANUP
# =============================================================================

REMOVE_TEMPORARY_FILES = False

COMPRESS_EXPERIMENT = False

DELETE_FAILED_RUNS = False

# =============================================================================
# TAGS
# =============================================================================

DEFAULT_TAGS = [
    "google",
    "waxal",
    "asr",
    "speech-recognition",
    "huggingface",
    "growtech",
]

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    "PROJECT_NAME",
    "TEAM_NAME",
    "EXPERIMENT_NAME",
    "EXPERIMENT_VERSION",
    "RUN_NAME",
    "DESCRIPTION",
    "RUN_TIMESTAMP",
    "RUN_ID",
    "EXPERIMENT_ROOT",
    "RUN_DIRECTORY",
    "CHECKPOINT_DIRECTORY",
    "REPORT_DIRECTORY",
    "PROJECT_VERSION",
    "DATASET_VERSION",
    "MODEL_VERSION",
    "CONFIG_VERSION",
    "CODE_VERSION",
    "ENABLE_REPRODUCIBILITY",
    "SAVE_CONFIGURATION",
    "SAVE_ENVIRONMENT",
    "SAVE_REQUIREMENTS",
    "SAVE_GIT_COMMIT",
    "SAVE_RANDOM_SEED",
    "SAVE_HARDWARE_INFORMATION",
    "SAVE_BEST_MODEL",
    "SAVE_LAST_MODEL",
    "SAVE_EVERY_CHECKPOINT",
    "MAX_CHECKPOINTS",
    "KEEP_BEST_ONLY",
    "AUTO_RESUME",
    "TrackingBackend",
    "TRACKING_BACKEND",
    "ENABLE_TRACKING",
    "TRACK_PARAMETERS",
    "TRACK_METRICS",
    "TRACK_SYSTEM_INFORMATION",
    "TRACK_GPU",
    "TRACK_CPU",
    "TRACK_MEMORY",
    "TRACK_EXECUTION_TIME",
    "PRIMARY_METRIC",
    "SECONDARY_METRICS",
    "LOWER_IS_BETTER",
    "GENERATE_SUMMARY",
    "GENERATE_HTML_REPORT",
    "GENERATE_JSON_REPORT",
    "GENERATE_MARKDOWN_REPORT",
    "SAVE_PLOTS",
    "SAVE_CONFUSION_ANALYSIS",
    "EXPORT_MODEL",
    "EXPORT_TOKENIZER",
    "EXPORT_CONFIGURATION",
    "EXPORT_RESULTS",
    "EXPORT_METRICS",
    "EXPORT_LOGS",
    "ENABLE_EXPERIMENT_COMPARISON",
    "COMPARE_WITH_BASELINE",
    "COMPARE_TOP_N",
    "REMOVE_TEMPORARY_FILES",
    "COMPRESS_EXPERIMENT",
    "DELETE_FAILED_RUNS",
    "DEFAULT_TAGS",
]