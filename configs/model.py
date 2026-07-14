"""
===============================================================================
model.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized model configuration.

Purpose:
    This module defines the official model architecture and all model-related
    parameters used throughout the project.

    It formalizes the project's architecture decisions regarding:
        • multilingual training
        • tokenizer
        • feature extraction
        • LoRA fine-tuning
        • inference
        • evaluation
        • reproducibility

    Every training, evaluation and inference script MUST import this module.

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    2.0.0
===============================================================================
"""

from enum import Enum

# =============================================================================
# OFFICIAL ARCHITECTURE DECISION
# =============================================================================

MODEL_STRATEGY = "multilingual"

MULTILINGUAL_MODEL = True

MONOLINGUAL_EXPERIMENTS_ALLOWED = True

PRIMARY_MODEL_ONLY = True

SUPPORTED_LANGUAGES = (
    "luganda",
    "lingala",
    "shona",
)

NUMBER_OF_LANGUAGES = len(SUPPORTED_LANGUAGES)

# =============================================================================
# MODEL IDENTIFICATION
# =============================================================================

MODEL_NAME = "google/gemma-3n"

MODEL_PROVIDER = "Google"

MODEL_VERSION = "1.0"

TASK = "Automatic Speech Recognition"

FRAMEWORK = "Transformers"

# =============================================================================
# MODEL SELECTION
# =============================================================================

class ModelFamily(str, Enum):
    GEMMA = "gemma"
    WHISPER = "whisper"
    MMS = "mms"
    SEAMLESS = "seamless"
    WAV2VEC2 = "wav2vec2"


PRIMARY_MODEL = MODEL_NAME

BENCHMARK_MODELS = [
    "openai/whisper-large-v3",
    "facebook/mms-1b-all",
    "facebook/seamless-m4t-v2-large",
    "wav2vec2",
]

# =============================================================================
# MODEL TYPE
# =============================================================================

class ModelType(str, Enum):
    ENCODER_DECODER = "encoder_decoder"
    DECODER_ONLY = "decoder_only"
    CTC = "ctc"
    SEQ2SEQ = "seq2seq"


MODEL_TYPE = ModelType.SEQ2SEQ

# =============================================================================
# TOKENIZER
# =============================================================================

TOKENIZER_NAME = MODEL_NAME

USE_FAST_TOKENIZER = True

TOKENIZER_PADDING = "longest"

TOKENIZER_TRUNCATION = True

# IMPORTANT:
# This value will later be automatically computed from corpus statistics.
MAX_SEQUENCE_LENGTH = None

PADDING_SIDE = "right"

# =============================================================================
# FEATURE EXTRACTION
# =============================================================================

USE_FEATURE_EXTRACTOR = True

FEATURE_EXTRACTOR_NAME = MODEL_NAME

NORMALIZE_AUDIO = True

RETURN_ATTENTION_MASK = True

# =============================================================================
# TRAINING PRECISION
# =============================================================================

USE_FP16 = True

USE_BF16 = False

USE_FP32 = False

MIXED_PRECISION = True

# =============================================================================
# QUANTIZATION
# =============================================================================

LOAD_IN_8BIT = False

LOAD_IN_4BIT = False

USE_BITSANDBYTES = False

# =============================================================================
# DEVICE
# =============================================================================

AUTO_DEVICE_MAPPING = True

DEVICE = "auto"

USE_CPU = False

USE_GPU = True

USE_MPS = False

# =============================================================================
# LoRA
# =============================================================================

USE_LORA = True

LORA_R = 16

LORA_ALPHA = 32

LORA_DROPOUT = 0.05

LORA_BIAS = "none"

TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
]

# =============================================================================
# TRAINABLE PARAMETERS
# =============================================================================

FREEZE_EMBEDDINGS = False

FREEZE_ENCODER = False

FREEZE_DECODER = False

TRAINABLE_LAYERS = "all"

# =============================================================================
# GENERATION
# =============================================================================

MAX_NEW_TOKENS = 256

MIN_NEW_TOKENS = 1

NUM_BEAMS = 4

DO_SAMPLE = False

TEMPERATURE = 1.0

TOP_K = 50

TOP_P = 0.95

REPETITION_PENALTY = 1.1

EARLY_STOPPING = True

# =============================================================================
# CHECKPOINTS
# =============================================================================

SAVE_CHECKPOINTS = True

MAX_CHECKPOINTS = 5

LOAD_BEST_MODEL = True

STRICT_LOADING = False

# =============================================================================
# EVALUATION
# =============================================================================

PRIMARY_METRIC = "WER"

SECONDARY_METRICS = [
    "CER",
]

LOWER_IS_BETTER = True

# =============================================================================
# INFERENCE
# =============================================================================

BATCH_INFERENCE = True

INFERENCE_BATCH_SIZE = 8

RETURN_CONFIDENCE = False

RETURN_TIMESTAMPS = False

# =============================================================================
# REPRODUCIBILITY
# =============================================================================

USE_DETERMINISTIC_ALGORITHMS = True

ENABLE_BENCHMARK = False

RANDOM_SEED = 42

# =============================================================================
# EXPORT
# =============================================================================

EXPORT_ONNX = False

EXPORT_TORCHSCRIPT = False

EXPORT_SAFETENSORS = True

# =============================================================================
# FUTURE EXPERIMENTS
# =============================================================================

SUPPORTED_MODELS = [
    MODEL_NAME,
    *BENCHMARK_MODELS,
]

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    "MODEL_STRATEGY",
    "MULTILINGUAL_MODEL",
    "MONOLINGUAL_EXPERIMENTS_ALLOWED",
    "PRIMARY_MODEL_ONLY",
    "SUPPORTED_LANGUAGES",
    "NUMBER_OF_LANGUAGES",
    "MODEL_NAME",
    "MODEL_PROVIDER",
    "MODEL_VERSION",
    "TASK",
    "FRAMEWORK",
    "ModelFamily",
    "PRIMARY_MODEL",
    "BENCHMARK_MODELS",
    "ModelType",
    "MODEL_TYPE",
    "TOKENIZER_NAME",
    "USE_FAST_TOKENIZER",
    "TOKENIZER_PADDING",
    "TOKENIZER_TRUNCATION",
    "MAX_SEQUENCE_LENGTH",
    "PADDING_SIDE",
    "USE_FEATURE_EXTRACTOR",
    "FEATURE_EXTRACTOR_NAME",
    "NORMALIZE_AUDIO",
    "RETURN_ATTENTION_MASK",
    "USE_FP16",
    "USE_BF16",
    "USE_FP32",
    "MIXED_PRECISION",
    "LOAD_IN_8BIT",
    "LOAD_IN_4BIT",
    "USE_BITSANDBYTES",
    "AUTO_DEVICE_MAPPING",
    "DEVICE",
    "USE_CPU",
    "USE_GPU",
    "USE_MPS",
    "USE_LORA",
    "LORA_R",
    "LORA_ALPHA",
    "LORA_DROPOUT",
    "LORA_BIAS",
    "TARGET_MODULES",
    "FREEZE_EMBEDDINGS",
    "FREEZE_ENCODER",
    "FREEZE_DECODER",
    "TRAINABLE_LAYERS",
    "MAX_NEW_TOKENS",
    "MIN_NEW_TOKENS",
    "NUM_BEAMS",
    "DO_SAMPLE",
    "TEMPERATURE",
    "TOP_K",
    "TOP_P",
    "REPETITION_PENALTY",
    "EARLY_STOPPING",
    "SAVE_CHECKPOINTS",
    "MAX_CHECKPOINTS",
    "LOAD_BEST_MODEL",
    "STRICT_LOADING",
    "PRIMARY_METRIC",
    "SECONDARY_METRICS",
    "LOWER_IS_BETTER",
    "BATCH_INFERENCE",
    "INFERENCE_BATCH_SIZE",
    "RETURN_CONFIDENCE",
    "RETURN_TIMESTAMPS",
    "USE_DETERMINISTIC_ALGORITHMS",
    "ENABLE_BENCHMARK",
    "RANDOM_SEED",
    "EXPORT_ONNX",
    "EXPORT_TORCHSCRIPT",
    "EXPORT_SAFETENSORS",
    "SUPPORTED_MODELS",
]