"""
===============================================================================
training.py
===============================================================================

Project:
    Grow Tech AI - Google WAXAL ASR Challenge

Description:
    Centralized training configuration.

Purpose:
    This module defines every parameter related to model training,
    optimization, evaluation scheduling, checkpointing and
    reproducibility.

    Every training script MUST import this module instead of defining
    hyperparameters locally.

Author:
    Grow Tech AI Team

Status:
    Production Ready

Version:
    1.0.0
===============================================================================
"""

from enum import Enum

# =============================================================================
# EXPERIMENT
# =============================================================================

EXPERIMENT_NAME = "baseline"

RUN_NAME = "baseline_v1"

PROJECT_NAME = "growtech-waxal-asr"

# =============================================================================
# RANDOMNESS
# =============================================================================

RANDOM_SEED = 42

ENABLE_REPRODUCIBILITY = True

DETERMINISTIC = True

# =============================================================================
# TRAINING STRATEGY
# =============================================================================

NUM_EPOCHS = 10

MAX_TRAINING_STEPS = None

TRAIN_BATCH_SIZE = 8

EVAL_BATCH_SIZE = 8

GRADIENT_ACCUMULATION_STEPS = 4

AUTO_FIND_BATCH_SIZE = False

# =============================================================================
# OPTIMIZER
# =============================================================================

class Optimizer(str, Enum):
    ADAMW = "adamw_torch"
    SGD = "sgd"
    ADAM = "adam"

OPTIMIZER = Optimizer.ADAMW

LEARNING_RATE = 2e-5

WEIGHT_DECAY = 0.01

BETA1 = 0.9

BETA2 = 0.999

EPSILON = 1e-8

MAX_GRAD_NORM = 1.0

# =============================================================================
# LEARNING RATE SCHEDULER
# =============================================================================

class Scheduler(str, Enum):
    LINEAR = "linear"
    COSINE = "cosine"
    CONSTANT = "constant"
    POLYNOMIAL = "polynomial"

LR_SCHEDULER = Scheduler.LINEAR

WARMUP_RATIO = 0.10

WARMUP_STEPS = 0

# =============================================================================
# VALIDATION
# =============================================================================

DO_EVALUATION = True

EVALUATION_STRATEGY = "steps"

EVAL_STEPS = 500

PREDICT_WITH_GENERATE = True

# =============================================================================
# CHECKPOINTS
# =============================================================================

SAVE_STRATEGY = "steps"

SAVE_STEPS = 500

SAVE_TOTAL_LIMIT = 5

LOAD_BEST_MODEL_AT_END = True

METRIC_FOR_BEST_MODEL = "wer"

GREATER_IS_BETTER = False

# =============================================================================
# LOGGING
# =============================================================================

LOGGING_STRATEGY = "steps"

LOGGING_STEPS = 50

LOG_FIRST_STEP = True

DISABLE_TQDM = False

REPORT_TO = [
    "tensorboard",
]

# =============================================================================
# EARLY STOPPING
# =============================================================================

USE_EARLY_STOPPING = True

EARLY_STOPPING_PATIENCE = 5

EARLY_STOPPING_THRESHOLD = 0.0

# =============================================================================
# MIXED PRECISION
# =============================================================================

USE_FP16 = True

USE_BF16 = False

USE_TF32 = False

# =============================================================================
# DATALOADER
# =============================================================================

NUM_WORKERS = 4

PIN_MEMORY = True

PERSISTENT_WORKERS = True

PREFETCH_FACTOR = 2

DROP_LAST_BATCH = False

SHUFFLE = True

# =============================================================================
# CHECKPOINT RESUME
# =============================================================================

RESUME_FROM_CHECKPOINT = True

CHECKPOINT_PATH = None

IGNORE_DATA_SKIP = False

# =============================================================================
# MONITORING
# =============================================================================

TRACK_MEMORY = True

TRACK_GPU = True

TRACK_CPU = True

TRACK_TRAINING_TIME = True

# =============================================================================
# EVALUATION METRICS
# =============================================================================

PRIMARY_METRIC = "wer"

SECONDARY_METRICS = [
    "cer",
]

# =============================================================================
# CALLBACKS
# =============================================================================

ENABLE_PROGRESS_BAR = True

ENABLE_MODEL_CHECKPOINT = True

ENABLE_EARLY_STOPPING = True

ENABLE_LR_MONITOR = True

# =============================================================================
# DISTRIBUTED TRAINING
# =============================================================================

USE_DDP = False

USE_DEEPSPEED = False

USE_FSDP = False

USE_ACCELERATE = True

# =============================================================================
# EXPORT
# =============================================================================

SAVE_FINAL_MODEL = True

SAVE_TOKENIZER = True

SAVE_TRAINER_STATE = True

SAVE_OPTIMIZER_STATE = True

# =============================================================================
# PUBLIC API
# =============================================================================

__all__ = [
    "EXPERIMENT_NAME",
    "RUN_NAME",
    "PROJECT_NAME",
    "RANDOM_SEED",
    "ENABLE_REPRODUCIBILITY",
    "DETERMINISTIC",
    "NUM_EPOCHS",
    "MAX_TRAINING_STEPS",
    "TRAIN_BATCH_SIZE",
    "EVAL_BATCH_SIZE",
    "GRADIENT_ACCUMULATION_STEPS",
    "AUTO_FIND_BATCH_SIZE",
    "Optimizer",
    "OPTIMIZER",
    "LEARNING_RATE",
    "WEIGHT_DECAY",
    "BETA1",
    "BETA2",
    "EPSILON",
    "MAX_GRAD_NORM",
    "Scheduler",
    "LR_SCHEDULER",
    "WARMUP_RATIO",
    "WARMUP_STEPS",
    "DO_EVALUATION",
    "EVALUATION_STRATEGY",
    "EVAL_STEPS",
    "PREDICT_WITH_GENERATE",
    "SAVE_STRATEGY",
    "SAVE_STEPS",
    "SAVE_TOTAL_LIMIT",
    "LOAD_BEST_MODEL_AT_END",
    "METRIC_FOR_BEST_MODEL",
    "GREATER_IS_BETTER",
    "LOGGING_STRATEGY",
    "LOGGING_STEPS",
    "LOG_FIRST_STEP",
    "DISABLE_TQDM",
    "REPORT_TO",
    "USE_EARLY_STOPPING",
    "EARLY_STOPPING_PATIENCE",
    "EARLY_STOPPING_THRESHOLD",
    "USE_FP16",
    "USE_BF16",
    "USE_TF32",
    "NUM_WORKERS",
    "PIN_MEMORY",
    "PERSISTENT_WORKERS",
    "PREFETCH_FACTOR",
    "DROP_LAST_BATCH",
    "SHUFFLE",
    "RESUME_FROM_CHECKPOINT",
    "CHECKPOINT_PATH",
    "IGNORE_DATA_SKIP",
    "TRACK_MEMORY",
    "TRACK_GPU",
    "TRACK_CPU",
    "TRACK_TRAINING_TIME",
    "PRIMARY_METRIC",
    "SECONDARY_METRICS",
    "ENABLE_PROGRESS_BAR",
    "ENABLE_MODEL_CHECKPOINT",
    "ENABLE_EARLY_STOPPING",
    "ENABLE_LR_MONITOR",
    "USE_DDP",
    "USE_DEEPSPEED",
    "USE_FSDP",
    "USE_ACCELERATE",
    "SAVE_FINAL_MODEL",
    "SAVE_TOKENIZER",
    "SAVE_TRAINER_STATE",
    "SAVE_OPTIMIZER_STATE",
]