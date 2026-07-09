# Grow Tech AI Research Lab

# Model Comparison — Google WAXAL ASR Challenge

> **Document ID :** RESEARCH-MODELS-001  
> **Catégorie :** Model Benchmark & Decision Support  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document centralise l'analyse comparative de toutes les architectures étudiées dans le cadre du Google WAXAL ASR Challenge.

Son objectif est de permettre au laboratoire Grow Tech AI de sélectionner les modèles les plus adaptés aux contraintes de la compétition et aux objectifs scientifiques du projet.

Chaque modèle sera évalué de manière reproductible selon des critères objectifs.

---

# 2. Philosophie

Grow Tech AI ne cherche pas à utiliser le modèle "le plus récent".

Nous recherchons le modèle qui offre le meilleur compromis entre :

- précision ;
- généralisation ;
- coût d'entraînement ;
- coût d'inférence ;
- facilité de fine-tuning ;
- robustesse ;
- potentiel de réutilisation.

Un modèle est retenu uniquement si son adoption est justifiée par des résultats expérimentaux.

---

# 3. Processus d'évaluation

Chaque modèle suit le même protocole.

```text
Étude documentaire
        │
        ▼
Analyse théorique
        │
        ▼
Implémentation
        │
        ▼
Fine-tuning
        │
        ▼
Évaluation
        │
        ▼
Analyse des erreurs
        │
        ▼
Comparaison
        │
        ▼
Décision
```

---

# 4. Critères d'évaluation

Tous les modèles seront évalués selon les critères suivants.

## Performances

- WER
- CER
- Exact Match
- Robustesse

---

## Généralisation

- nouvelles langues
- nouveaux locuteurs
- nouveaux accents
- bruit

---

## Ressources

- VRAM
- RAM
- stockage
- temps d'entraînement
- temps d'inférence

---

## Développement

- documentation
- communauté
- facilité de déploiement
- maintenance

---

## Réutilisation

- autres compétitions
- autres projets Grow Tech AI
- intégration dans GrowTech
- potentiel open source

---

# 5. Tableau comparatif

| Critère              | Gemma       | Whisper     | wav2vec2    | HuBERT      | MMS         | Canary      | SeamlessM4T | Futurs modèles |
| -------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | -------------- |
| Architecture         | À compléter | À compléter | À compléter | À compléter | À compléter | À compléter | À compléter | À compléter    |
| Taille               |             |             |             |             |             |             |             |                |
| Fine-tuning          |             |             |             |             |             |             |             |                |
| WER                  |             |             |             |             |             |             |             |                |
| CER                  |             |             |             |             |             |             |             |                |
| Généralisation       |             |             |             |             |             |             |             |                |
| Coût GPU             |             |             |             |             |             |             |             |                |
| Temps d'entraînement |             |             |             |             |             |             |             |                |
| Temps d'inférence    |             |             |             |             |             |             |             |                |
| Documentation        |             |             |             |             |             |             |             |                |
| Réutilisabilité      |             |             |             |             |             |             |             |                |

Les valeurs seront complétées au fil des expérimentations.

---

# 6. Analyse détaillée des modèles

Chaque modèle possède une fiche dédiée.

---

# 6.1 Gemma

## Description

Modèle fourni dans la baseline officielle.

---

### Avantages

- support officiel ;
- pipeline validé ;
- bonne compatibilité avec la compétition.

---

### Limites

- baseline volontairement simple ;
- peu d'optimisations.

---

### Cas d'utilisation

- point de référence ;
- validation du pipeline.

---

### Priorité

⭐⭐⭐⭐☆

---

# 6.2 Whisper

## Description

Famille de modèles ASR développée par OpenAI.

---

### Avantages

- excellente robustesse ;
- très bonnes performances multilingues ;
- communauté importante.

---

### Limites

- coût mémoire plus élevé ;
- fine-tuning plus complexe.

---

### Cas d'utilisation

- benchmark principal.

---

### Priorité

⭐⭐⭐⭐⭐

---

# 6.3 wav2vec2

## Description

Architecture auto-supervisée développée par Meta.

---

### Avantages

- nombreuses variantes ;
- excellent support Hugging Face.

---

### Limites

- sensible au domaine d'entraînement.

---

### Priorité

⭐⭐⭐⭐☆

---

# 6.4 HuBERT

## Description

Modèle d'apprentissage auto-supervisé.

---

### Avantages

- bonnes représentations audio.

---

### Limites

- moins utilisé récemment.

---

### Priorité

⭐⭐⭐☆☆

---

# 6.5 MMS

Massively Multilingual Speech.

Architecture spécialisée pour de nombreuses langues.

Priorité actuelle :

⭐⭐⭐⭐☆

---

# 6.6 Canary

Architecture NVIDIA.

Potentiel intéressant.

À évaluer.

---

# 6.7 SeamlessM4T

Architecture Meta.

Très prometteuse pour les langues africaines.

À surveiller.

---

# 6.8 Autres modèles

Cette section accueillera les modèles découverts pendant la veille scientifique.

---

# 7. Stratégie d'expérimentation

Le laboratoire adopte une approche incrémentale.

Phase 1 :

- Baseline Gemma.

Phase 2 :

- Whisper.

Phase 3 :

- wav2vec2.

Phase 4 :

- HuBERT.

Phase 5 :

- MMS.

Phase 6 :

- Ensembles.

Chaque phase ne commence qu'après validation de la précédente.

---

# 8. Critères de décision

Un modèle est retenu uniquement si :

- amélioration significative du WER ;
- coût acceptable ;
- reproductibilité démontrée ;
- documentation complète ;
- intégration possible dans l'architecture Grow Tech AI.

---

# 9. Analyse comparative

Après chaque campagne d'entraînement, ce document sera enrichi avec :

- tableaux comparatifs ;
- graphiques ;
- courbes d'apprentissage ;
- consommation mémoire ;
- temps d'exécution ;
- erreurs typiques.

Toutes les comparaisons devront être réalisées dans des conditions identiques.

---

# 10. Perspectives de recherche

Les pistes suivantes seront étudiées :

- fine-tuning multilingue ;
- transfer learning ;
- curriculum learning ;
- LoRA / QLoRA ;
- PEFT ;
- ensembles de modèles ;
- distillation ;
- fusion de modèles.

---

# 11. Décisions du laboratoire

Les décisions issues de cette analyse seront reportées dans :

```
docs/research/08_Decision_Log.md
```

Les expériences correspondantes seront documentées dans :

```
docs/research/06_Experiment_Log.md
```

---

# 12. Automatisation

Les futures versions du laboratoire devront générer automatiquement :

- tableaux comparatifs ;
- métriques ;
- graphiques ;
- classement interne des modèles.

Les scripts concernés seront notamment :

```text
src/evaluation/model_benchmark.py
src/evaluation/benchmark_report.py
scripts/benchmark.py
```

---

# 13. Documents associés

- `01_Dataset_Audit.md`
- `02_Dataset_Anatomy.md`
- `03_EDA.md`
- `04_Baseline_Analysis.md`
- `06_Experiment_Log.md`
- `08_Decision_Log.md`
- `Developer-Pack/04_RESEARCH_OBJECTIVES.md`

---

# 14. Travaux futurs

Ce document évoluera tout au long du projet avec :

- les nouveaux modèles ;
- les résultats expérimentaux ;
- les analyses d'erreurs ;
- les recommandations finales.

Il deviendra progressivement la référence décisionnelle du laboratoire Grow Tech AI pour tous les projets ASR.

---

# 15. Historique des versions

| Version | Date        | Auteur       | Description                                |
| ------- | ----------- | ------------ | ------------------------------------------ |
| 1.0.0   | À compléter | Grow Tech AI | Première version du comparatif des modèles |
