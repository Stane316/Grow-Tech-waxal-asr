# Grow Tech AI Research Lab

# Dataset Anatomy — Google WAXAL Dataset

> **Document ID :** RESEARCH-DATASET-002  
> **Catégorie :** Dataset Documentation  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document décrit l'anatomie complète du dataset Google WAXAL.

Contrairement au document **01_Dataset_Audit.md**, qui présente une vue globale du dataset, ce document analyse en profondeur la structure interne de chaque observation.

Il constitue la référence scientifique utilisée pour :

- comprendre les données ;
- concevoir les pipelines de prétraitement ;
- guider le développement des modèles ASR ;
- identifier les défis liés aux langues africaines ;
- documenter les choix techniques du laboratoire.

---

# 2. Vue d'ensemble

Chaque observation du dataset représente un exemple de reconnaissance automatique de la parole.

Une observation est composée de trois familles d'informations :

```
Observation

│

├── Audio

├── Transcription

└── Métadonnées
```

L'ensemble de ces éléments forme une unité d'entraînement pour un modèle ASR.

---

# 3. Anatomie générale d'un exemple

Schéma conceptuel :

```
┌─────────────────────────────┐
│ Exemple                     │
├─────────────────────────────┤
│ ID                          │
│ Audio                       │
│ Transcription               │
│ Langue                      │
│ Métadonnées                 │
└─────────────────────────────┘
```

Chaque champ possède un rôle précis dans le pipeline de traitement.

---

# 4. Le signal audio

## Définition

Le signal audio constitue l'entrée principale du système ASR.

Il représente une onde acoustique numérisée contenant la voix d'un locuteur.

---

## Informations attendues

Lors du chargement réel des données, les éléments suivants seront extraits automatiquement :

- fréquence d'échantillonnage ;
- durée ;
- nombre de canaux ;
- profondeur de quantification ;
- format audio.

Ces caractéristiques seront intégrées automatiquement après l'exécution de `dataset_loader.py`.

---

## Variabilité attendue

Le signal peut varier selon :

- le locuteur ;
- l'environnement ;
- le microphone ;
- le niveau de bruit ;
- le débit de parole ;
- l'accent.

Cette variabilité constitue l'un des principaux défis du projet.

---

# 5. Les transcriptions

Chaque signal audio est associé à une transcription textuelle.

La transcription constitue la vérité terrain (_ground truth_) utilisée pour entraîner le modèle.

---

## Rôle

Pendant l'entraînement :

```
Audio

↓

Modèle

↓

Texte prédit

↓

Comparaison avec la transcription

↓

Calcul de la perte (Loss)

↓

Optimisation
```

---

## Points à analyser

Le laboratoire étudiera notamment :

- longueur moyenne des phrases ;
- distribution des longueurs ;
- vocabulaire ;
- ponctuation ;
- caractères Unicode ;
- caractères rares ;
- mots fréquents ;
- mots rares.

---

# 6. Les langues

Le dataset est multilingue.

Chaque exemple appartient à une langue africaine.

Les langues seront caractérisées selon :

- nombre d'exemples ;
- durée totale ;
- vocabulaire ;
- alphabet ;
- spécificités linguistiques.

Les statistiques exactes seront générées automatiquement.

---

# 7. Les locuteurs

Le dataset contient plusieurs locuteurs.

Les caractéristiques suivantes seront étudiées lorsque disponibles :

- nombre de locuteurs ;
- répartition par langue ;
- diversité des voix ;
- équilibre entre locuteurs.

Cette diversité est essentielle pour améliorer la capacité de généralisation des modèles.

---

# 8. Les métadonnées

Selon les partitions du dataset, plusieurs métadonnées peuvent être présentes :

- identifiant ;
- langue ;
- informations descriptives.

⚠️ En Phase 2 de la compétition, certaines métadonnées seront volontairement absentes afin d'empêcher les modèles d'utiliser des raccourcis.

Le laboratoire devra donc concevoir des modèles capables de s'appuyer uniquement sur le signal vocal.

---

# 9. Pipeline de traitement des données

Le laboratoire adopte le pipeline suivant :

```
Dataset

↓

Chargement

↓

Validation

↓

Prétraitement audio

↓

Prétraitement texte

↓

Augmentation

↓

Extraction des caractéristiques

↓

Tokenisation

↓

Création des batches

↓

Entraînement
```

Chaque étape sera implémentée dans un module dédié de `src/`.

---

# 10. Prétraitement audio

Les opérations envisagées sont :

- normalisation ;
- suppression des silences ;
- rééchantillonnage si nécessaire ;
- contrôle de la qualité ;
- augmentation audio.

Toutes les transformations devront être documentées et reproductibles.

---

# 11. Prétraitement texte

Les traitements envisagés comprennent :

- normalisation Unicode ;
- nettoyage des espaces ;
- gestion de la ponctuation ;
- homogénéisation des caractères.

Aucune modification ne devra altérer le sens de la transcription.

---

# 12. Augmentation des données

Des techniques d'augmentation pourront être étudiées :

- ajout de bruit ;
- variation de vitesse ;
- variation de hauteur ;
- SpecAugment ;
- mélange de données.

Chaque méthode devra être évaluée expérimentalement avant d'être intégrée au pipeline principal.

---

# 13. Défis scientifiques

Le dataset présente plusieurs défis majeurs :

- diversité linguistique ;
- déséquilibre entre langues ;
- accents variés ;
- qualité hétérogène des enregistrements ;
- bruit environnemental ;
- généralisation vers des données inédites.

Ces défis orienteront les axes de recherche du laboratoire.

---

# 14. Implications pour le choix des modèles

L'anatomie du dataset influence directement les modèles retenus.

Le laboratoire privilégiera des architectures capables de :

- apprendre à partir de plusieurs langues ;
- généraliser à de nouveaux locuteurs ;
- gérer des enregistrements bruités ;
- être adaptées au fine-tuning.

Une comparaison détaillée sera présentée dans `05_Model_Comparison.md`.

---

# 15. Informations à compléter automatiquement

Les éléments suivants seront renseignés après l'exécution des scripts d'analyse :

- fréquence d'échantillonnage réelle ;
- durée moyenne des fichiers ;
- durée médiane ;
- durée maximale ;
- taille moyenne des transcriptions ;
- distribution des longueurs ;
- nombre exact de locuteurs ;
- nombre exact de langues ;
- répartition des exemples.

Ces informations seront générées par :

```
src/data/dataset_loader.py
```

et

```
scripts/prepare_dataset.py
```

---

# 16. Relations avec les autres documents

Ce document complète :

- `01_Dataset_Audit.md`
- `03_EDA.md`
- `04_Baseline_Analysis.md`
- `05_Model_Comparison.md`

Ensemble, ils constituent la base scientifique de la compréhension du dataset.

---

# 17. Travaux futurs

Après l'analyse réelle des données, ce document sera enrichi avec :

- schémas détaillés ;
- statistiques descriptives ;
- visualisations ;
- exemples annotés ;
- analyses comparatives entre langues.

Il deviendra alors la référence anatomique complète du dataset WAXAL.

---

# 18. Historique des versions

| Version | Date        | Auteur       | Description                               |
| ------- | ----------- | ------------ | ----------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de l'anatomie du dataset |
