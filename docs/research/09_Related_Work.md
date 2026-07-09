# Grow Tech AI Research Lab

# Related Work — Google WAXAL ASR Challenge

> **Document ID :** RESEARCH-RELATED-WORK-001  
> **Catégorie :** Literature Review & State of the Art  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document centralise l'ensemble des travaux existants pertinents pour le projet.

Il constitue la revue bibliographique officielle du laboratoire Grow Tech AI.

Ses objectifs sont :

- comprendre l'état de l'art de l'ASR moderne ;
- identifier les meilleures pratiques ;
- éviter de reproduire des erreurs déjà connues ;
- découvrir de nouvelles pistes d'amélioration ;
- justifier les choix techniques du projet.

---

# 2. Philosophie

Avant de développer une nouvelle solution, nous devons répondre à une question simple :

> **Qui a déjà essayé cette idée, avec quels résultats et dans quelles conditions ?**

Le développement doit être guidé par la littérature scientifique et les retours d'expérience de la communauté.

---

# 3. Domaines de recherche couverts

Cette revue documentaire couvre les thèmes suivants :

## Reconnaissance automatique de la parole (ASR)

- architectures modernes ;
- entraînement supervisé ;
- modèles auto-supervisés ;
- décodage ;
- adaptation de domaine.

---

## Speech Foundation Models

- Gemma
- Whisper
- wav2vec 2.0
- HuBERT
- MMS
- SeamlessM4T
- XLS-R
- Canary
- Parakeet

---

## Fine-Tuning

- LoRA
- QLoRA
- PEFT
- Adapters
- Prompt Tuning

---

## Data Augmentation

- SpecAugment
- Bruit additif
- Changement de vitesse
- Pitch shifting
- Reverberation
- Mixup

---

## Optimisation de l'entraînement

- Mixed Precision
- Gradient Checkpointing
- Flash Attention
- DeepSpeed
- FSDP
- Quantization

---

## Décodage

- Greedy Search
- Beam Search
- Diverse Beam Search
- Language Model Fusion
- Rescoring

---

## Évaluation

- WER
- CER
- PER
- Analyse qualitative des erreurs

---

# 4. Sources officielles

Les références sont classées par niveau de priorité.

## Niveau 1 — Publications scientifiques

Sources privilégiées :

- arXiv
- ACL Anthology
- Interspeech
- ICASSP
- NeurIPS
- ICML
- ICLR
- EMNLP

---

## Niveau 2 — Documentation technique

- Hugging Face
- PyTorch
- NVIDIA
- Google Research
- Meta AI
- OpenAI
- Microsoft Research

---

## Niveau 3 — Implémentations

- GitHub
- Hugging Face Models
- Kaggle
- Zindi

---

## Niveau 4 — Retours d'expérience

- Blogs techniques
- Reddit
- Medium
- Conférences YouTube
- Présentations de compétitions

---

# 5. Fiche standard d'une référence

Chaque ressource étudiée doit être documentée selon le modèle suivant.

---

## Identifiant

```text
REF-2026-001
```

---

## Titre

Titre complet de la publication.

---

## Auteurs

Nom des auteurs.

---

## Année

AAAA

---

## Source

- arXiv
- ACL
- GitHub
- Hugging Face
- etc.

---

## Domaine

Exemple :

ASR

Fine-Tuning

Speech Foundation Model

Data Augmentation

---

## Résumé

Synthèse en quelques paragraphes.

---

## Contributions principales

- contribution 1 ;
- contribution 2 ;
- contribution 3.

---

## Technologies utilisées

- PyTorch
- Transformers
- PEFT
- CUDA
- etc.

---

## Points forts

Quels sont les principaux avantages ?

---

## Limites

Quelles sont les limites identifiées ?

---

## Applicabilité au projet

Cette ressource est-elle pertinente pour WAXAL ?

Pourquoi ?

---

## Niveau de pertinence

⭐⭐⭐⭐⭐

---

## BAIP associé

Exemple :

BAIP-2 — Recherche documentaire

---

## Références liées

Autres travaux similaires.

---

# 6. Bibliographie initiale

## REF-2026-001

### Whisper

Catégorie :

Speech Foundation Model

Pourquoi l'étudier ?

- modèle de référence ;
- multilingue ;
- robuste ;
- nombreuses implémentations.

---

## REF-2026-002

### wav2vec 2.0

Catégorie :

Self-supervised Speech Representation Learning.

---

## REF-2026-003

### HuBERT

Apprentissage auto-supervisé.

---

## REF-2026-004

### XLS-R

Modèle multilingue Meta AI.

---

## REF-2026-005

### Gemma Speech

Baseline officielle du challenge.

---

## REF-2026-006

### LoRA

Fine-tuning efficace.

---

## REF-2026-007

### PEFT

Parameter Efficient Fine-Tuning.

---

## REF-2026-008

### SpecAugment

Référence majeure pour l'augmentation audio.

---

# 7. Travaux liés aux compétitions

Une attention particulière est portée aux compétitions similaires :

- Google WAXAL ASR Challenge ;
- Mozilla Common Voice ;
- Kaggle Speech Recognition ;
- Hugging Face Challenges ;
- autres compétitions Zindi en ASR.

Pour chacune :

- objectif ;
- données ;
- modèles gagnants ;
- stratégies ;
- erreurs fréquentes ;
- enseignements.

---

# 8. Veille technologique

Une veille continue est réalisée sur :

## Nouveaux modèles

- nouveaux Foundation Models ;
- nouvelles architectures.

---

## Nouveaux datasets

- datasets africains ;
- datasets multilingues ;
- corpus open source.

---

## Nouveaux outils

- bibliothèques ;
- frameworks ;
- accélérations GPU.

---

## Nouveaux articles

Les publications pertinentes seront ajoutées au fil du projet.

---

# 9. Critères d'évaluation d'une référence

Chaque ressource est évaluée selon :

| Critère              | Description                             |
| -------------------- | --------------------------------------- |
| Pertinence           | Lien avec le projet                     |
| Qualité scientifique | Rigueur de la source                    |
| Reproductibilité     | Possibilité de reproduire les résultats |
| Impact               | Influence dans le domaine               |
| Réutilisabilité      | Potentiel pour Grow Tech AI             |

Une note globale sur 100 peut être attribuée.

---

# 10. Relations avec les autres documents

Cette revue documentaire alimente :

- `07_Research_Ideas.md`
- `08_Decision_Log.md`
- `06_Experiment_Log.md`
- `05_Model_Comparison.md`
- `10_TASKS.md`
- `13_AI_INSTRUCTIONS.md`

Toute idée issue d'une publication devra être référencée avant d'être transformée en expérimentation.

---

# 11. Stratégie de mise à jour

Ce document est vivant.

À chaque nouvelle publication ou ressource pertinente :

1. créer une nouvelle fiche `REF-XXXX` ;
2. évaluer sa pertinence ;
3. identifier les idées exploitables ;
4. créer, si nécessaire, une nouvelle entrée dans `07_Research_Ideas.md`.

---

# 12. Vision à long terme

Ce document ne se limite pas au Google WAXAL ASR Challenge.

Il constitue progressivement une bibliothèque scientifique réutilisable pour :

- les futurs hackathons IA ;
- les projets ASR de Grow Tech AI ;
- GrowTech ;
- FacturaPro ;
- les travaux de recherche académique ;
- les futures publications techniques de l'équipe.

---

# 13. Historique des versions

| Version | Date        | Auteur       | Description                               |
| ------- | ----------- | ------------ | ----------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la revue documentaire |
