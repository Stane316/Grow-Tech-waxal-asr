# dataset_loader.py — Technical Specification

---

# 1. Overview

## Script Name

dataset_loader.py

## Category

Data Management

## Purpose

Provide the official data loading pipeline for the Google WAXAL ASR Challenge.

This script is the single entry point responsible for loading the competition dataset.

It guarantees that every downstream component (training, evaluation, inference) operates exclusively on the official Zindi subset downloaded from Hugging Face.

---

# 2. Official Architecture Decision

Decision ID

ADR-001

Status

Accepted

Rule

Only the dataset samples referenced by the official Zindi metadata files shall be loaded.

The loader must never expose recordings outside the competition subset.

---

# 3. Responsibilities

The loader is responsible for

✓ loading metadata

✓ locating downloaded files

✓ validating file existence

✓ verifying dataset integrity

✓ constructing dataset objects

✓ filtering invalid samples

✓ exposing unified APIs

✓ preparing the dataset for preprocessing

It is **not** responsible for

training

feature extraction

tokenization

augmentation

evaluation

---

# 4. Inputs

Required inputs

data/

    metadata/

        Train.csv

        Validation.csv

        Test.csv

data/

    raw/

        luganda/

        lingala/

        shona/

Optional

cache/

configuration files

---

# 5. Outputs

The loader returns

Training Dataset

Validation Dataset

Test Dataset

Metadata

Statistics

Integrity Report

No preprocessing is performed.

---

# 6. Supported Splits

The loader shall expose

train

validation

test

No additional split is authorized.

---

# 7. Loading Pipeline

Initialize Configuration

↓

Verify Folder Structure

↓

Load Metadata

↓

Validate Metadata

↓

Extract Audio IDs

↓

Locate Local Audio

↓

Verify File Existence

↓

Validate Audio

↓

Create Dataset Objects

↓

Generate Statistics

↓

Return Dataset

---

# 8. Metadata Loading

Load

Train.csv

Validation.csv

Test.csv

Extract

sample_id

language

transcription

audio_path

duration (if available)

speaker (if available)

Store internally.

---

# 9. Audio Resolution

Each metadata row must resolve to

data/raw/<language>/<audio_file>

Missing files are rejected.

---

# 10. Dataset Validation

Before returning data verify

✓ metadata consistency

✓ file existence

✓ readable audio

✓ transcription present

✓ language valid

✓ duplicate IDs

✓ duplicate files

✓ corrupted recordings

Validation is mandatory.

---

# 11. Supported Languages

Official languages

Luganda

Lingala

Shona

No additional language.

---

# 12. Filtering Policy

Reject

missing transcription

missing audio

unknown language

duplicate sample ID

empty recording

corrupted audio

invalid metadata

Generate warnings.

---

# 13. Statistics

Generate

number of samples

samples per split

samples per language

duration statistics

missing samples

invalid samples

duplicate samples

These statistics are returned with the dataset.

---

# 14. Caching

The loader shall support

cache reuse

lazy loading

memory-efficient loading

No duplicate cache generation.

---

# 15. Public API

The implementation should expose functions similar to

load_train()

load_validation()

load_test()

load_all()

load_split(split_name)

load_metadata()

get_statistics()

validate_dataset()

The exact implementation may evolve, but these capabilities are mandatory.

---

# 16. Error Handling

Handle

missing metadata

missing folders

missing audio

unsupported language

invalid CSV

corrupted files

permission errors

cache errors

Meaningful exceptions shall be raised.

---

# 17. Logging

Generate

logs/dataset.log

Log

dataset loading

split loaded

validation status

missing samples

duplicates

loading time

errors

warnings

---

# 18. Performance Requirements

The loader shall

avoid duplicate scans

use caching

support lazy loading

minimize memory usage

reuse metadata

support thousands of files

---

# 19. Dependencies

datasets

pandas

numpy

soundfile

pathlib

logging

typing

---

# 20. Integration

Used by

dataset_validator.py

metadata_loader.py

cache_manager.py

preprocessing pipeline

feature extraction

training pipeline

evaluation pipeline

inference pipeline

---

# 21. Acceptance Criteria

The specification is satisfied when

✓ only official Zindi samples are loaded

✓ every split is reproducible

✓ dataset validation succeeds

✓ no external recordings appear

✓ statistics generated

✓ logs generated

✓ corrupted samples rejected

✓ loader reusable by all modules

---

# 22. Future Improvements

Support

streaming datasets

distributed loading

parallel loading

memory mapping

incremental loading

automatic dataset versioning

remote storage

dataset fingerprinting