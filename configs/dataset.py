"""
===============================================================================
dataset.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized dataset configuration.

Purpose:
    This module defines every dataset-related configuration used
    throughout the project.

    It also formalizes the official architecture decisions concerning
    dataset management.

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    2.0.0
===============================================================================
"""

from enum import Enum
from pathlib import Path

from configs.paths import DATA_DIR

# =============================================================================
# OFFICIAL DATASET
# =============================================================================

DATASET_NAME = "google/WaxalNLP"

DATASET_PROVIDER = "Google"

DATASET_PLATFORM = "Hugging Face"

DATASET_VERSION = "official"

# =============================================================================
# OFFICIAL ARCHITECTURE DECISION
# =============================================================================

DATASET_DOWNLOAD_POLICY = "filtered_by_zindi_metadata"

DOWNLOAD_FULL_DATASET = False

FILTER_BY_METADATA = True

ALLOW_EXTRA_SAMPLES = False

VALIDATE_SAMPLE_IDS = True

# =============================================================================
# DATASET STRUCTURE
# =============================================================================

METADATA_DIR = DATA_DIR / "metadata"

RAW_DATA_DIR = DATA_DIR / "raw"

CACHE_DIR = DATA_DIR / "cache"

REPORTS_DIR = DATA_DIR / "reports"

# =============================================================================
# OFFICIAL METADATA FILES
# =============================================================================

TRAIN_METADATA = METADATA_DIR / "Train.csv"

VALIDATION_METADATA = METADATA_DIR / "Validation.csv"

TEST_METADATA = METADATA_DIR / "Test.csv"

OFFICIAL_METADATA_FILES = (
    TRAIN_METADATA,
    VALIDATION_METADATA,
    TEST_METADATA,
)

# =============================================================================
# SPLITS
# =============================================================================

class DatasetSplit(str, Enum):
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"


SUPPORTED_SPLITS = tuple(split.value for split in DatasetSplit)

# =============================================================================
# LANGUAGES
# =============================================================================

class Language(str, Enum):
    LUGANDA = "luganda"
    LINGALA = "lingala"
    SHONA = "shona"


SUPPORTED_LANGUAGES = tuple(language.value for language in Language)

NUMBER_OF_LANGUAGES = len(SUPPORTED_LANGUAGES)

MULTILINGUAL_DATASET = True

# =============================================================================
# AUDIO
# =============================================================================

SUPPORTED_AUDIO_EXTENSIONS = (
    ".wav",
    ".flac",
)

DEFAULT_AUDIO_EXTENSION = ".wav"

# =============================================================================
# VALIDATION POLICY
# =============================================================================

VALIDATE_DATASET_BEFORE_TRAINING = True

VALIDATE_METADATA = True

VALIDATE_AUDIO_FILES = True

VALIDATE_TRANSCRIPTIONS = True

VALIDATE_LANGUAGE = True

VALIDATE_DUPLICATES = True

VALIDATE_EMPTY_AUDIO = True

VALIDATE_CORRUPTED_AUDIO = True

# =============================================================================
# FILTERING POLICY
# =============================================================================

REMOVE_DUPLICATES = True

IGNORE_UNKNOWN_LANGUAGES = True

IGNORE_CORRUPTED_FILES = True

IGNORE_EMPTY_TRANSCRIPTIONS = True

IGNORE_MISSING_AUDIO = True

STRICT_METADATA_VALIDATION = True

# =============================================================================
# DATA LOADER
# =============================================================================

ENABLE_LAZY_LOADING = True

ENABLE_STREAMING = False

ENABLE_CACHE = True

CACHE_METADATA = True

CACHE_DATASET = True

REBUILD_CACHE_IF_INVALID = True

# =============================================================================
# STATISTICS
# =============================================================================

GENERATE_DATASET_STATISTICS = True

COMPUTE_DURATION_STATISTICS = True

COMPUTE_LANGUAGE_STATISTICS = True

COMPUTE_SPLIT_STATISTICS = True

COMPUTE_DUPLICATE_STATISTICS = True

SAVE_DATASET_REPORT = True

# =============================================================================
# DOWNLOAD
# =============================================================================

ENABLE_RESUME_DOWNLOAD = True

VERIFY_DOWNLOADED_FILES = True

VERIFY_METADATA_AFTER_DOWNLOAD = True

VERIFY_DATASET_STRUCTURE = True

MAX_DOWNLOAD_RETRIES = 3

DOWNLOAD_TIMEOUT = 300

# =============================================================================
# SECURITY
# =============================================================================

REQUIRE_HF_AUTHENTICATION = True

REQUIRE_GEMMA_LICENSE = True

ALLOW_ANONYMOUS_DOWNLOAD = False

# =============================================================================
# REPRODUCIBILITY
# =============================================================================

DATASET_FINGERPRINT = True

SAVE_DOWNLOAD_MANIFEST = True

SAVE_DATASET_MANIFEST = True

SAVE_VALIDATION_REPORT = True

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    "DATASET_NAME",
    "DATASET_PROVIDER",
    "DATASET_PLATFORM",
    "DATASET_VERSION",
    "DATASET_DOWNLOAD_POLICY",
    "DOWNLOAD_FULL_DATASET",
    "FILTER_BY_METADATA",
    "ALLOW_EXTRA_SAMPLES",
    "VALIDATE_SAMPLE_IDS",
    "METADATA_DIR",
    "RAW_DATA_DIR",
    "CACHE_DIR",
    "REPORTS_DIR",
    "TRAIN_METADATA",
    "VALIDATION_METADATA",
    "TEST_METADATA",
    "OFFICIAL_METADATA_FILES",
    "DatasetSplit",
    "SUPPORTED_SPLITS",
    "Language",
    "SUPPORTED_LANGUAGES",
    "NUMBER_OF_LANGUAGES",
    "MULTILINGUAL_DATASET",
    "SUPPORTED_AUDIO_EXTENSIONS",
    "DEFAULT_AUDIO_EXTENSION",
    "VALIDATE_DATASET_BEFORE_TRAINING",
    "VALIDATE_METADATA",
    "VALIDATE_AUDIO_FILES",
    "VALIDATE_TRANSCRIPTIONS",
    "VALIDATE_LANGUAGE",
    "VALIDATE_DUPLICATES",
    "VALIDATE_EMPTY_AUDIO",
    "VALIDATE_CORRUPTED_AUDIO",
    "REMOVE_DUPLICATES",
    "IGNORE_UNKNOWN_LANGUAGES",
    "IGNORE_CORRUPTED_FILES",
    "IGNORE_EMPTY_TRANSCRIPTIONS",
    "IGNORE_MISSING_AUDIO",
    "STRICT_METADATA_VALIDATION",
    "ENABLE_LAZY_LOADING",
    "ENABLE_STREAMING",
    "ENABLE_CACHE",
    "CACHE_METADATA",
    "CACHE_DATASET",
    "REBUILD_CACHE_IF_INVALID",
    "GENERATE_DATASET_STATISTICS",
    "COMPUTE_DURATION_STATISTICS",
    "COMPUTE_LANGUAGE_STATISTICS",
    "COMPUTE_SPLIT_STATISTICS",
    "COMPUTE_DUPLICATE_STATISTICS",
    "SAVE_DATASET_REPORT",
    "ENABLE_RESUME_DOWNLOAD",
    "VERIFY_DOWNLOADED_FILES",
    "VERIFY_METADATA_AFTER_DOWNLOAD",
    "VERIFY_DATASET_STRUCTURE",
    "MAX_DOWNLOAD_RETRIES",
    "DOWNLOAD_TIMEOUT",
    "REQUIRE_HF_AUTHENTICATION",
    "REQUIRE_GEMMA_LICENSE",
    "ALLOW_ANONYMOUS_DOWNLOAD",
    "DATASET_FINGERPRINT",
    "SAVE_DOWNLOAD_MANIFEST",
    "SAVE_DATASET_MANIFEST",
    "SAVE_VALIDATION_REPORT",
]