# download_dataset.py — Technical Specification

---

# 1. Overview

## Script Name

download_dataset.py

## Category

Infrastructure

## Purpose

Download only the dataset samples required for the Google WAXAL ASR Challenge.

This script **must not** download the entire Hugging Face dataset.

Instead, it must download only the audio samples referenced by the official Zindi metadata files.

This specification supersedes all previous download strategies.

---

# 2. Background

The official WAXAL dataset hosted on Hugging Face contains a much larger collection of recordings than those required for the competition.

The competition organizers provide official metadata files:

- Train.csv
- Validation.csv
- Test.csv

These files define the exact subset used during the challenge.

Downloading the full dataset would:

- waste bandwidth;
- waste disk space;
- slow down preprocessing;
- complicate dataset validation;
- reduce reproducibility.

Therefore the project adopts a filtered download strategy.

---

# 3. Official Decision

Decision ID:

ADR-001

Status:

Accepted

Rule:

Only download samples whose IDs appear in the official Zindi metadata.

Downloading the full Hugging Face dataset is forbidden.

---

# 4. Inputs

The script expects:

• Hugging Face authentication token

• Accepted Gemma 3n license

• HF_HOME configured

• Project directory structure initialized

• Metadata files

    data/
        metadata/
            Train.csv
            Validation.csv
            Test.csv

---

# 5. Outputs

The script produces

data/

    raw/

        luganda/

        lingala/

        shona/

Only the required files.

No unused recordings.

---

# 6. Download Pipeline

The official pipeline is

Initialize Environment

↓

Load Metadata

↓

Extract Audio IDs

↓

Remove Duplicates

↓

Authenticate Hugging Face

↓

Verify Dataset Access

↓

Download Required Samples

↓

Verify Download Integrity

↓

Generate Download Report

↓

Finish

---

# 7. Metadata Processing

The script shall

Load

Train.csv

Validation.csv

Test.csv

Extract every audio identifier.

Merge all identifiers.

Remove duplicates.

Create one unified download list.

---

# 8. Download Strategy

The implementation shall

Never iterate over the entire dataset.

Instead

For each required ID

Locate the corresponding sample

Download audio

Download transcription

Download metadata

Store locally

Continue

This dramatically reduces download time.

---

# 9. Directory Structure

data/

    metadata/

        Train.csv

        Validation.csv

        Test.csv

    raw/

        luganda/

        lingala/

        shona/

    cache/

    reports/

---

# 10. Hugging Face Configuration

HF_HOME shall be

cache/huggingface/

No global cache may be used.

Authentication is mandatory.

huggingface-cli login

must succeed before execution.

---

# 11. Download Validation

For every downloaded sample verify

✓ audio exists

✓ metadata exists

✓ transcription exists

✓ language exists

✓ checksum (if available)

✓ readable audio

Invalid samples are reported.

---

# 12. Failure Management

Possible failures

Missing token

↓

Authentication error

↓

Dataset access denied

↓

License not accepted

↓

Network timeout

↓

Missing metadata

↓

Corrupted audio

↓

Interrupted download

Each error must be logged.

Recovery must be supported.

---

# 13. Logging

Generate

logs/download.log

Log

start time

end time

download speed

downloaded samples

missing samples

failed samples

warnings

errors

---

# 14. Progress Reporting

Console output shall display

Current split

Current language

Downloaded files

Remaining files

Estimated remaining time

Download percentage

---

# 15. Generated Reports

At completion generate

reports/download_report.json

reports/download_summary.md

Reports include

Total requested files

Downloaded files

Missing files

Failed files

Elapsed time

Dataset size

Average download speed

---

# 16. Performance Requirements

The implementation shall

Avoid duplicate downloads.

Support resume.

Support caching.

Minimize API requests.

Parallelize downloads when possible.

---

# 17. Security

Never log

HF token

API keys

Private credentials

Temporary credentials

---

# 18. Dependencies

datasets

huggingface_hub

pandas

tqdm

pathlib

logging

hashlib

soundfile

---

# 19. Acceptance Criteria

The specification is considered satisfied when

✓ only Zindi samples are downloaded

✓ no extra recordings exist

✓ metadata matches downloaded files

✓ reports generated

✓ validation successful

✓ reproducible download

✓ cache reused

✓ logs generated

---

# 20. Future Improvements

Support

automatic retries

download queue

mirror servers

download checksum verification

download manifest

parallel workers

incremental updates

offline validation
