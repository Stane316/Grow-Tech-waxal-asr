"""
===========================================================================
paths.py
===========================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized project path configuration.

Purpose:
    This module is the single source of truth for every filesystem path
    used throughout the project.

    No script should manually construct paths using Path(...) or
    os.path.join(...).

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    1.0.0
===========================================================================
"""

from pathlib import Path

# ==========================================================================
# PROJECT ROOT
# ==========================================================================

# configs/
CONFIG_DIR = Path(__file__).resolve().parent

# Repository root
PROJECT_ROOT = CONFIG_DIR.parent

# ==========================================================================
# DOCUMENTATION
# ==========================================================================

DOCS_DIR = PROJECT_ROOT / "docs"

SPECIFICATIONS_DIR = PROJECT_ROOT / "specifications"

DEVELOPER_PACK_DIR = PROJECT_ROOT / "Developer-Pack"

AI_DOCUMENTATION_DIR = DOCS_DIR / "ai"

RESEARCH_DIR = DOCS_DIR / "research"

# ==========================================================================
# DATA DIRECTORIES
# ==========================================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

FILTERED_DATA_DIR = DATA_DIR / "filtered"

METADATA_DIR = DATA_DIR / "metadata"

CACHE_DATA_DIR = DATA_DIR / "cache"

# ==========================================================================
# DATASET FILES
# ==========================================================================

TRAIN_CSV = METADATA_DIR / "Train.csv"

VALIDATION_CSV = METADATA_DIR / "Validation.csv"

TEST_CSV = METADATA_DIR / "Test.csv"

DATASET_INFO = METADATA_DIR / "dataset_info.json"

# ==========================================================================
# CACHE
# ==========================================================================

CACHE_DIR = PROJECT_ROOT / "cache"

HF_HOME = CACHE_DIR / "huggingface"

HF_DATASETS_CACHE = HF_HOME / "datasets"

HF_HUB_CACHE = HF_HOME / "hub"

ARROW_CACHE = CACHE_DIR / "arrow"

FEATURE_CACHE = CACHE_DIR / "features"

TOKENIZER_CACHE = CACHE_DIR / "tokenizers"

EMBEDDING_CACHE = CACHE_DIR / "embeddings"

TEMP_CACHE = CACHE_DIR / "temp"

# ==========================================================================
# MODELS
# ==========================================================================

MODELS_DIR = PROJECT_ROOT / "models"

PRETRAINED_MODELS_DIR = MODELS_DIR / "pretrained"

CHECKPOINTS_DIR = MODELS_DIR / "checkpoints"

BEST_MODELS_DIR = MODELS_DIR / "best"

TOKENIZERS_DIR = MODELS_DIR / "tokenizers"

# ==========================================================================
# OUTPUTS
# ==========================================================================

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

SUBMISSIONS_DIR = OUTPUTS_DIR / "submissions"

PREDICTIONS_DIR = OUTPUTS_DIR / "predictions"

INFERENCE_DIR = OUTPUTS_DIR / "inference"

REPORTS_DIR = OUTPUTS_DIR / "reports"

FIGURES_DIR = OUTPUTS_DIR / "figures"

EXPORTS_DIR = OUTPUTS_DIR / "exports"

# ==========================================================================
# LOGGING
# ==========================================================================

LOGS_DIR = PROJECT_ROOT / "logs"

TRAINING_LOGS_DIR = LOGS_DIR / "training"

DATA_LOGS_DIR = LOGS_DIR / "data"

SYSTEM_LOGS_DIR = LOGS_DIR / "system"

EXPERIMENT_LOGS_DIR = LOGS_DIR / "experiments"

# ==========================================================================
# EXPERIMENTS
# ==========================================================================

EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"

RUNS_DIR = EXPERIMENTS_DIR / "runs"

MLFLOW_DIR = EXPERIMENTS_DIR / "mlflow"

WANDB_DIR = EXPERIMENTS_DIR / "wandb"

TENSORBOARD_DIR = EXPERIMENTS_DIR / "tensorboard"

# ==========================================================================
# SOURCE CODE
# ==========================================================================

SRC_DIR = PROJECT_ROOT / "src"

DATA_SRC_DIR = SRC_DIR / "data"

MODELS_SRC_DIR = SRC_DIR / "models"

TRAINING_SRC_DIR = SRC_DIR / "training"

EVALUATION_SRC_DIR = SRC_DIR / "evaluation"

INFERENCE_SRC_DIR = SRC_DIR / "inference"

UTILS_SRC_DIR = SRC_DIR / "utils"

# ==========================================================================
# SCRIPTS
# ==========================================================================

SCRIPTS_DIR = PROJECT_ROOT / "scripts"

INFRASTRUCTURE_SCRIPTS = SCRIPTS_DIR / "infrastructure"

DATA_SCRIPTS = SCRIPTS_DIR / "data"

TRAINING_SCRIPTS = SCRIPTS_DIR / "training"

# ==========================================================================
# TESTS
# ==========================================================================

TESTS_DIR = PROJECT_ROOT / "tests"

UNIT_TESTS_DIR = TESTS_DIR / "unit"

INTEGRATION_TESTS_DIR = TESTS_DIR / "integration"

# ==========================================================================
# CONFIGURATION
# ==========================================================================

ENV_FILE = PROJECT_ROOT / ".env"

ENV_EXAMPLE = PROJECT_ROOT / ".env.example"

REQUIREMENTS = PROJECT_ROOT / "requirements.txt"

PYPROJECT = PROJECT_ROOT / "pyproject.toml"

README = PROJECT_ROOT / "README.md"

SETUP = PROJECT_ROOT / "SETUP.md"

# ==========================================================================
# TEMPORARY
# ==========================================================================

TEMP_DIR = PROJECT_ROOT / "tmp"

DOWNLOADS_DIR = TEMP_DIR / "downloads"

EXTRACTION_DIR = TEMP_DIR / "extraction"

# ==========================================================================
# PROJECT DIRECTORIES
# ==========================================================================

PROJECT_DIRECTORIES = [
    DATA_DIR,
    RAW_DATA_DIR,
    FILTERED_DATA_DIR,
    METADATA_DIR,
    CACHE_DIR,
    HF_HOME,
    HF_DATASETS_CACHE,
    HF_HUB_CACHE,
    ARROW_CACHE,
    FEATURE_CACHE,
    TOKENIZER_CACHE,
    EMBEDDING_CACHE,
    TEMP_CACHE,
    MODELS_DIR,
    PRETRAINED_MODELS_DIR,
    CHECKPOINTS_DIR,
    BEST_MODELS_DIR,
    TOKENIZERS_DIR,
    OUTPUTS_DIR,
    SUBMISSIONS_DIR,
    PREDICTIONS_DIR,
    INFERENCE_DIR,
    REPORTS_DIR,
    FIGURES_DIR,
    EXPORTS_DIR,
    LOGS_DIR,
    TRAINING_LOGS_DIR,
    DATA_LOGS_DIR,
    SYSTEM_LOGS_DIR,
    EXPERIMENT_LOGS_DIR,
    EXPERIMENTS_DIR,
    RUNS_DIR,
    MLFLOW_DIR,
    WANDB_DIR,
    TENSORBOARD_DIR,
    TEMP_DIR,
    DOWNLOADS_DIR,
    EXTRACTION_DIR,
]

# ==========================================================================
# PUBLIC API
# ==========================================================================

__all__ = [
    "PROJECT_ROOT",
    "CONFIG_DIR",
    "DOCS_DIR",
    "SPECIFICATIONS_DIR",
    "DEVELOPER_PACK_DIR",
    "AI_DOCUMENTATION_DIR",
    "RESEARCH_DIR",
    "DATA_DIR",
    "RAW_DATA_DIR",
    "FILTERED_DATA_DIR",
    "METADATA_DIR",
    "CACHE_DATA_DIR",
    "TRAIN_CSV",
    "VALIDATION_CSV",
    "TEST_CSV",
    "DATASET_INFO",
    "CACHE_DIR",
    "HF_HOME",
    "HF_DATASETS_CACHE",
    "HF_HUB_CACHE",
    "ARROW_CACHE",
    "FEATURE_CACHE",
    "TOKENIZER_CACHE",
    "EMBEDDING_CACHE",
    "TEMP_CACHE",
    "MODELS_DIR",
    "PRETRAINED_MODELS_DIR",
    "CHECKPOINTS_DIR",
    "BEST_MODELS_DIR",
    "TOKENIZERS_DIR",
    "OUTPUTS_DIR",
    "SUBMISSIONS_DIR",
    "PREDICTIONS_DIR",
    "INFERENCE_DIR",
    "REPORTS_DIR",
    "FIGURES_DIR",
    "EXPORTS_DIR",
    "LOGS_DIR",
    "TRAINING_LOGS_DIR",
    "DATA_LOGS_DIR",
    "SYSTEM_LOGS_DIR",
    "EXPERIMENT_LOGS_DIR",
    "EXPERIMENTS_DIR",
    "RUNS_DIR",
    "MLFLOW_DIR",
    "WANDB_DIR",
    "TENSORBOARD_DIR",
    "SRC_DIR",
    "DATA_SRC_DIR",
    "MODELS_SRC_DIR",
    "TRAINING_SRC_DIR",
    "EVALUATION_SRC_DIR",
    "INFERENCE_SRC_DIR",
    "UTILS_SRC_DIR",
    "SCRIPTS_DIR",
    "INFRASTRUCTURE_SCRIPTS",
    "DATA_SCRIPTS",
    "TRAINING_SCRIPTS",
    "TESTS_DIR",
    "UNIT_TESTS_DIR",
    "INTEGRATION_TESTS_DIR",
    "ENV_FILE",
    "ENV_EXAMPLE",
    "REQUIREMENTS",
    "PYPROJECT",
    "README",
    "SETUP",
    "TEMP_DIR",
    "DOWNLOADS_DIR",
    "EXTRACTION_DIR",
    "PROJECT_DIRECTORIES",
]