# dataset_validator.py — Software Specification

Version: 2.0

Status: Approved

Category: Data Validation

Priority: Critical

---

# 1. Purpose

## Objective

Validate the integrity, consistency, completeness and quality of the official Google WAXAL ASR Challenge dataset before any downstream operation.

The validator acts as the project's official **Quality Gate**.

No preprocessing, training, evaluation or inference script may execute if the dataset validation fails.

---

# 2. Background

The Google WAXAL ASR Challenge relies on a filtered subset of the official WAXAL corpus.

Any inconsistency may lead to:

- invalid experiments
- non reproducible results
- training crashes
- incorrect evaluation
- leaderboard penalties

This validator guarantees that every experiment starts from a trusted dataset.

---

# 3. Responsibilities

The validator must:

✔ verify directory structure

✔ verify metadata

✔ verify CSV files

✔ verify dataset splits

✔ verify official IDs

✔ verify audio files

✔ verify transcripts

✔ verify language consistency

✔ verify sampling rate

✔ verify durations

✔ detect duplicates

✔ detect missing samples

✔ detect corrupted files

✔ generate validation reports

✔ assign a validation status

---

# 4. Inputs

Expected folders

```text
data/

    raw/

    filtered/

    metadata/

reports/

configs/
```

Expected files

```text
Train.csv

Validation.csv

Test.csv

dataset.arrow

metadata.json
```

Configuration

```text
configs/

dataset.py

paths.py
```

---

# 5. Outputs

Reports

```text
reports/

validation_report.json

validation_report.md

dataset_statistics.json

validation.log
```

Validation status

```text
PASS

WARNING

FAIL
```

---

# 6. Validation Pipeline

Step 1

Verify folder structure

↓

Step 2

Verify required files

↓

Step 3

Load metadata

↓

Step 4

Validate CSV files

↓

Step 5

Validate IDs

↓

Step 6

Validate dataset

↓

Step 7

Validate audio

↓

Step 8

Validate transcripts

↓

Step 9

Compute statistics

↓

Step 10

Generate reports

↓

Step 11

Return validation status

---

# 7. Dataset Validation

Verify

✔ number of samples

✔ split consistency

✔ unique IDs

✔ missing IDs

✔ duplicated IDs

✔ language distribution

✔ metadata consistency

✔ orphan samples

---

# 8. CSV Validation

Verify

✔ encoding (UTF-8)

✔ schema

✔ mandatory columns

✔ null values

✔ malformed rows

✔ duplicated rows

✔ invalid delimiters

✔ empty files

---

# 9. Audio Validation

Every audio file must verify

✔ file exists

✔ readable

✔ non empty

✔ supported format

✔ sample rate = 16 kHz

✔ duration > 0

✔ duration within expected range

✔ no corruption

✔ waveform readable

---

# 10. Transcript Validation

Verify

✔ transcript exists

✔ UTF-8 encoding

✔ non empty

✔ no duplicated transcript

✔ acceptable length

✔ language consistency

✔ excessive whitespace

✔ unexpected characters

---

# 11. Language Validation

Supported languages

```text
lug
lin
sna
```

Verify

✔ language code valid

✔ language matches metadata

✔ language distribution

Reject unknown languages.

---

# 12. Metadata Validation

Verify

✔ metadata exists

✔ IDs consistent

✔ language consistent

✔ split consistent

✔ audio path exists

✔ transcript path exists

---

# 13. Dataset Statistics

Compute

Number of samples

Hours of speech

Average duration

Median duration

Min duration

Max duration

Samples per language

Samples per split

Vocabulary size

Average transcript length

Maximum transcript length

Minimum transcript length

Character distribution

Word distribution

---

# 14. Quality Metrics

Generate

Missing samples %

Duplicated IDs %

Corrupted files %

Empty transcripts %

Average duration

Median duration

Audio coverage

Dataset completeness score

Validation score

---

# 15. Validation Rules

Critical Errors

Missing dataset

Missing metadata

Missing audio

Missing transcript

Duplicate IDs

Corrupted dataset

Unknown language

Invalid schema

↓

Execution stops immediately.

Warnings

Long transcript

Short transcript

Small language imbalance

Optional metadata missing

↓

Execution continues.

---

# 16. Reports

Generate

```text
validation_report.md
```

Containing

Executive Summary

Validation Results

Detected Errors

Warnings

Dataset Statistics

Recommendations

---

Generate

```text
validation_report.json
```

Machine-readable report.

---

Generate

```text
dataset_statistics.json
```

Reusable statistics.

---

# 17. Logging

Generate

```text
logs/dataset_validator.log
```

Log

timestamp

validation step

warnings

errors

duration

---

# 18. Public API

validate()

verify_structure()

verify_csv()

verify_audio()

verify_metadata()

verify_ids()

verify_transcripts()

compute_statistics()

generate_reports()

summary()

---

# 19. CLI

Default

```bash
python scripts/dataset_validator.py
```

Options

```bash
--quick

--full

--verify-audio

--verify-csv

--verify-metadata

--stats

--report

--json

--verbose
```

---

# 20. Unit Tests

Verify

Missing folders

Missing files

Duplicate IDs

Invalid CSV

Corrupted audio

Missing transcript

Unknown language

Wrong sample rate

Statistics generation

Report generation

---

# 21. Integration Tests

download_dataset.py

↓

dataset_loader.py

↓

dataset_validator.py

↓

EDA

↓

Training

↓

Evaluation

Validation must pass before continuing.

---

# 22. Performance Requirements

Validation time

< 5 minutes

Memory

< 4 GB

Parallel audio verification

Progress bars

Incremental validation supported

---

# 23. Security

Never expose

HF_TOKEN

absolute paths

private metadata

temporary cache

---

# 24. Future Improvements

Audio quality scoring

Automatic transcript normalization

Dataset version comparison

Checksum verification

Cloud dataset validation

Continuous validation (CI/CD)

Automatic HTML reports

---

# 25. Deliverables

After execution

```text
reports/

validation_report.md

validation_report.json

dataset_statistics.json

logs/

dataset_validator.log
```

The validator becomes the official Quality Gate of the project.

Every experiment must begin with a successful validation.

No downstream script is authorized to run if validation status is FAIL.