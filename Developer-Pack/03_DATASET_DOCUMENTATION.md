# 03_DATASET_DOCUMENTATION.md

# Developer Pack

## Google WAXAL ASR Challenge

Version : 2.0.0

Statut : Référence officielle

---

# 1. Objectif du document

Ce document décrit la structure officielle du dataset utilisé dans le projet Grow Tech AI pour le Google WAXAL ASR Challenge.

Il constitue la référence unique concernant :

- l'organisation des données ;
- les sources officielles ;
- les métadonnées ;
- les règles de téléchargement ;
- les contraintes techniques ;
- les décisions d'architecture relatives au dataset.

Tous les développeurs, collaborateurs et agents IA doivent s'y conformer.

---

# 2. Sources officielles

Le projet s'appuie exclusivement sur les ressources publiées par les organisateurs de la compétition.

## Plateforme de compétition

- Zindi — Google WAXAL ASR Challenge

## Dataset

- Hugging Face — `google/WaxalNLP`

## Documentation officielle

- Notebook officiel fourni par les organisateurs
- Métadonnées (`Train.csv`, `Validation.csv`, `Test.csv`)
- Règlement de la compétition

Aucune source tierce ne doit être utilisée sans validation préalable.

---

# 3. Description générale du dataset

Le dataset WAXAL est un corpus de reconnaissance automatique de la parole (ASR) destiné à entraîner et évaluer des modèles multilingues pour plusieurs langues africaines.

Le dépôt Hugging Face contient davantage de données que celles effectivement utilisées pendant la compétition.

Le sous-ensemble officiel est défini exclusivement par les fichiers de métadonnées fournis par Zindi.

---

# 4. Langues officielles

Le projet prend en charge les trois langues de la compétition :

- Luganda
- Lingala
- Shona

La stratégie retenue est un **modèle multilingue unique** couvrant simultanément ces trois langues.

---

# 5. Architecture des données

```text
data/
│
├── metadata/
│   ├── Train.csv
│   ├── Validation.csv
│   └── Test.csv
│
├── raw/
│   ├── luganda/
│   ├── lingala/
│   └── shona/
│
├── cache/
│
└── reports/
```

Les fichiers de métadonnées décrivent les échantillons à utiliser.

Les fichiers audio sont stockés dans `data/raw/`.

Les rapports et caches sont générés automatiquement par les scripts.

---

# 6. Métadonnées officielles

Trois fichiers CSV définissent le corpus de la compétition :

- `Train.csv`
- `Validation.csv`
- `Test.csv`

Ces fichiers contiennent notamment :

- identifiant de l'échantillon ;
- langue ;
- transcription ;
- informations complémentaires selon le split.

Ils constituent la référence unique pour sélectionner les données.

---

# 7. Décision d'architecture ADR-001

## Téléchargement filtré par les IDs Zindi

### Statut

Acceptée.

### Décision

Le projet ne téléchargera jamais l'intégralité du dataset Hugging Face.

Les téléchargements seront effectués uniquement à partir des identifiants présents dans les fichiers :

- `Train.csv`
- `Validation.csv`
- `Test.csv`

### Justification

Cette approche :

- réduit fortement l'espace disque utilisé ;
- diminue le temps de téléchargement ;
- évite les données inutiles ;
- garantit la reproductibilité ;
- assure un alignement strict avec la compétition.

---

# 8. Pipeline officiel des données

Le pipeline adopté est le suivant :

```text
Métadonnées Zindi
        │
        ▼
Extraction des IDs
        │
        ▼
Téléchargement filtré
        │
        ▼
Validation du dataset
        │
        ▼
Création du cache
        │
        ▼
Prétraitement
        │
        ▼
Entraînement
```

Aucun entraînement ne peut démarrer sans validation préalable.

---

# 9. Validation des données

Avant toute utilisation, le pipeline vérifie :

- présence des métadonnées ;
- présence des fichiers audio ;
- cohérence des identifiants ;
- langues valides ;
- transcriptions présentes ;
- fichiers lisibles ;
- absence de doublons ;
- intégrité générale du dataset.

Toute anomalie bloque le pipeline.

---

# 10. Politique de téléchargement

Le téléchargement doit respecter les règles suivantes :

- téléchargement filtré uniquement ;
- reprise automatique (`resume`) en cas d'interruption ;
- réutilisation du cache ;
- validation après téléchargement ;
- génération d'un rapport de téléchargement.

Le téléchargement complet du dataset est interdit.

---

# 11. Configuration Hugging Face

Le projet utilise un cache dédié :

```text
HF_HOME=cache/huggingface
```

Pré-requis obligatoires :

1. créer un compte Hugging Face ;
2. accepter la licence Gemma 3n si nécessaire ;
3. générer un token d'accès ;
4. exécuter `huggingface-cli login`.

---

# 12. Organisation des scripts

Les principaux composants liés au dataset sont :

- `download_dataset.py`
- `dataset_loader.py`
- `dataset_validator.py`
- `metadata_loader.py`
- `cache_manager.py`

Tous doivent respecter les décisions d'architecture documentées ici.

---

# 13. Bonnes pratiques

Les développeurs doivent :

- utiliser exclusivement les fichiers de métadonnées officiels ;
- ne jamais modifier les CSV d'origine ;
- conserver la structure du dossier `data/` ;
- centraliser les paramètres dans `configs/dataset.py` ;
- documenter toute évolution du pipeline.

---

# 14. Risques identifiés

Les principaux risques sont :

- téléchargement du dataset complet par erreur ;
- métadonnées obsolètes ;
- cache corrompu ;
- incohérence entre les fichiers audio et les CSV ;
- licence Hugging Face non acceptée ;
- environnement différent entre collaborateurs.

Ces risques sont traités par les mécanismes de validation et de contrôle décrits dans ce document.

---

# 15. Références

- Documentation officielle Zindi
- Dataset Hugging Face `google/WaxalNLP`
- Notebook officiel de la compétition
- `specifications/infrastructure/download_dataset.md`
- `specifications/data/dataset_loader.md`
- `configs/dataset.py`
- `docs/architecture/ARCHITECTURE_DECISIONS.md` (à créer)