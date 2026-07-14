"""
===============================================================================
logging.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized logging configuration.

Purpose:
    This module provides a unified logging configuration for the entire
    project.

    Every script MUST create its logger through this module.

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    1.0.0
===============================================================================
"""

from enum import Enum
from pathlib import Path

from configs.paths import LOGS_DIR

# =============================================================================
# LOG LEVELS
# =============================================================================

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


DEFAULT_LOG_LEVEL = LogLevel.INFO

# =============================================================================
# GLOBAL CONFIGURATION
# =============================================================================

ENABLE_CONSOLE_LOGGING = True

ENABLE_FILE_LOGGING = True

ENABLE_JSON_LOGGING = False

ENABLE_COLORED_OUTPUT = True

ENABLE_TIMESTAMP = True

ENABLE_CALLER_INFORMATION = True

ENABLE_EXCEPTION_TRACEBACK = True

# =============================================================================
# LOG FORMAT
# =============================================================================

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

JSON_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

# =============================================================================
# LOG FILES
# =============================================================================

MAIN_LOG_FILE = LOGS_DIR / "project.log"

TRAINING_LOG_FILE = LOGS_DIR / "training.log"

DATASET_LOG_FILE = LOGS_DIR / "dataset.log"

DOWNLOAD_LOG_FILE = LOGS_DIR / "download.log"

CACHE_LOG_FILE = LOGS_DIR / "cache.log"

EVALUATION_LOG_FILE = LOGS_DIR / "evaluation.log"

INFERENCE_LOG_FILE = LOGS_DIR / "inference.log"

SYSTEM_LOG_FILE = LOGS_DIR / "system.log"

EXPERIMENT_LOG_FILE = LOGS_DIR / "experiment.log"

# =============================================================================
# FILE ROTATION
# =============================================================================

ENABLE_ROTATION = True

MAX_LOG_SIZE_MB = 50

BACKUP_COUNT = 10

COMPRESS_OLD_LOGS = False

# =============================================================================
# CONSOLE
# =============================================================================

CONSOLE_LOG_LEVEL = LogLevel.INFO

SHOW_PROGRESS_BARS = True

SHOW_WARNINGS = True

SHOW_ERRORS = True

# =============================================================================
# DEBUGGING
# =============================================================================

ENABLE_DEBUG_MODE = False

LOG_ENVIRONMENT = True

LOG_CONFIGURATION = True

LOG_SYSTEM_INFORMATION = True

LOG_GPU_INFORMATION = True

LOG_DATASET_INFORMATION = True

# =============================================================================
# PERFORMANCE
# =============================================================================

LOG_MEMORY_USAGE = True

LOG_CPU_USAGE = True

LOG_GPU_USAGE = True

LOG_EXECUTION_TIME = True

LOG_DISK_USAGE = False

# =============================================================================
# TRAINING
# =============================================================================

LOG_TRAINING_LOSS = True

LOG_VALIDATION_LOSS = True

LOG_LEARNING_RATE = True

LOG_METRICS = True

LOG_CHECKPOINTS = True

# =============================================================================
# DATASET
# =============================================================================

LOG_DOWNLOAD_PROGRESS = True

LOG_CACHE_USAGE = True

LOG_DATASET_VALIDATION = True

LOG_CORRUPTED_FILES = True

LOG_DUPLICATES = True

# =============================================================================
# SECURITY
# =============================================================================

HIDE_HF_TOKEN = True

HIDE_API_KEYS = True

HIDE_PASSWORDS = True

HIDE_PRIVATE_PATHS = False

# =============================================================================
# THIRD-PARTY LOGGERS
# =============================================================================

DISABLE_TRANSFORMERS_WARNING = False

DISABLE_DATASETS_WARNING = False

DISABLE_TOKENIZERS_WARNING = False

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    "LogLevel",
    "DEFAULT_LOG_LEVEL",
    "ENABLE_CONSOLE_LOGGING",
    "ENABLE_FILE_LOGGING",
    "ENABLE_JSON_LOGGING",
    "ENABLE_COLORED_OUTPUT",
    "ENABLE_TIMESTAMP",
    "ENABLE_CALLER_INFORMATION",
    "ENABLE_EXCEPTION_TRACEBACK",
    "DATE_FORMAT",
    "LOG_FORMAT",
    "JSON_DATE_FORMAT",
    "MAIN_LOG_FILE",
    "TRAINING_LOG_FILE",
    "DATASET_LOG_FILE",
    "DOWNLOAD_LOG_FILE",
    "CACHE_LOG_FILE",
    "EVALUATION_LOG_FILE",
    "INFERENCE_LOG_FILE",
    "SYSTEM_LOG_FILE",
    "EXPERIMENT_LOG_FILE",
    "ENABLE_ROTATION",
    "MAX_LOG_SIZE_MB",
    "BACKUP_COUNT",
    "COMPRESS_OLD_LOGS",
    "CONSOLE_LOG_LEVEL",
    "SHOW_PROGRESS_BARS",
    "SHOW_WARNINGS",
    "SHOW_ERRORS",
    "ENABLE_DEBUG_MODE",
    "LOG_ENVIRONMENT",
    "LOG_CONFIGURATION",
    "LOG_SYSTEM_INFORMATION",
    "LOG_GPU_INFORMATION",
    "LOG_DATASET_INFORMATION",
    "LOG_MEMORY_USAGE",
    "LOG_CPU_USAGE",
    "LOG_GPU_USAGE",
    "LOG_EXECUTION_TIME",
    "LOG_DISK_USAGE",
    "LOG_TRAINING_LOSS",
    "LOG_VALIDATION_LOSS",
    "LOG_LEARNING_RATE",
    "LOG_METRICS",
    "LOG_CHECKPOINTS",
    "LOG_DOWNLOAD_PROGRESS",
    "LOG_CACHE_USAGE",
    "LOG_DATASET_VALIDATION",
    "LOG_CORRUPTED_FILES",
    "LOG_DUPLICATES",
    "HIDE_HF_TOKEN",
    "HIDE_API_KEYS",
    "HIDE_PASSWORDS",
    "HIDE_PRIVATE_PATHS",
    "DISABLE_TRANSFORMERS_WARNING",
    "DISABLE_DATASETS_WARNING",
    "DISABLE_TOKENIZERS_WARNING",
]