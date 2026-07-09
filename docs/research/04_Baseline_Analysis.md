# Grow Tech AI Research Lab

# Baseline Analysis — Google WAXAL ASR Challenge

> **Document ID :** RESEARCH-BASELINE-001  
> **Catégorie :** Baseline Analysis  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document analyse en profondeur la solution officielle (_Starter Notebook_) fournie par les organisateurs du Google WAXAL ASR Challenge.

L'objectif n'est pas uniquement de comprendre son fonctionnement, mais d'en extraire les hypothèses, les choix techniques et les limites afin de construire une solution plus performante.

Cette analyse servira de référence tout au long du projet.

---

# 2. Pourquoi analyser la baseline ?

La baseline officielle représente :

- un point de départ technique ;
- une démonstration du pipeline attendu ;
- une preuve que les données sont exploitables.

Cependant, elle **n'est pas conçue pour gagner la compétition**.

Elle privilégie :

- la simplicité ;
- la reproductibilité ;
- la lisibilité.

Notre objectif est donc :

- conserver les bonnes idées ;
- identifier les limites ;
- proposer des améliorations mesurables.

---

# 3. Vue d'ensemble de la baseline

Le notebook officiel implémente un pipeline ASR complet mais minimal.

Pipeline général :

```text
Chargement des données
        │
        ▼
Prétraitement
        │
        ▼
Tokenisation
        │
        ▼
Chargement du modèle Gemma
        │
        ▼
Fine-tuning
        │
        ▼
Inférence
        │
        ▼
Génération des prédictions
        │
        ▼
Création du fichier de soumission
```

---

# 4. Objectifs implicites de la baseline

L'analyse du notebook montre que les organisateurs souhaitent principalement :

- familiariser les participants avec le dataset ;
- démontrer le pipeline officiel ;
- fournir une base reproductible ;
- standardiser les premières expérimentations.

La baseline n'a pas vocation à être optimale.

---

# 5. Architecture générale

Le pipeline est composé des blocs suivants :

```text
Dataset
      │
      ▼
Dataset Loader
      │
      ▼
Audio Processing
      │
      ▼
Tokenizer
      │
      ▼
Gemma ASR
      │
      ▼
Trainer
      │
      ▼
Prediction
      │
      ▼
Submission
```

---

# 6. Analyse cellule par cellule

Le notebook comporte **17 cellules**.

Pour chacune, une fiche d'analyse est réalisée selon le modèle suivant :

### Cellule X

#### Rôle

Décrire précisément la fonction de la cellule.

#### Pourquoi ce choix ?

Identifier les motivations probables des organisateurs.

#### Ce que nous conservons

Lister les éléments réutilisables.

#### Ce que nous améliorerons

Identifier les optimisations possibles.

> **Remarque :** Une analyse détaillée de chacune des 17 cellules a été réalisée séparément et pourra être intégrée progressivement dans cette section.

---

# 7. Analyse du chargement des données

Objectif :

Comprendre :

- les bibliothèques utilisées ;
- la méthode de chargement ;
- le cache ;
- la gestion des partitions.

Questions étudiées :

- Pourquoi `datasets.load_dataset()` ?
- Pourquoi le streaming n'est-il pas utilisé ?
- Comment optimiser le chargement ?

---

# 8. Analyse du prétraitement

Étudier :

- nettoyage audio ;
- normalisation ;
- tokenisation ;
- préparation des labels.

Évaluer :

- ce qui est indispensable ;
- ce qui est simplifié ;
- ce qui pourrait être amélioré.

---

# 9. Analyse du modèle Gemma

Le notebook utilise un modèle Gemma comme baseline.

Cette section documente :

- les raisons de ce choix ;
- les avantages ;
- les limites ;
- les contraintes mémoire ;
- les possibilités de fine-tuning.

Une comparaison approfondie sera réalisée dans `05_Model_Comparison.md`.

---

# 10. Analyse du processus d'entraînement

Étudier :

- hyperparamètres ;
- batch size ;
- learning rate ;
- scheduler ;
- optimizer ;
- nombre d'époques.

Questions :

- Quels paramètres sont adaptés ?
- Quels paramètres doivent être optimisés ?

---

# 11. Analyse de l'inférence

Étudier :

- pipeline de génération ;
- décodage ;
- vitesse ;
- mémoire.

Identifier les possibilités :

- batching ;
- beam search ;
- optimisation GPU.

---

# 12. Analyse de la génération des soumissions

Objectifs :

Comprendre :

- format attendu ;
- structure des fichiers ;
- contraintes imposées par Zindi.

Le futur script `generate_submission.py` devra reproduire ce comportement de manière entièrement automatisée.

---

# 13. Forces de la baseline

La baseline présente plusieurs qualités :

- pipeline complet ;
- code clair ;
- reproductibilité ;
- bonne intégration avec Hugging Face ;
- simplicité d'utilisation.

---

# 14. Limites identifiées

Plusieurs limites ont été observées :

- peu de modularité ;
- notebook monolithique ;
- faible séparation des responsabilités ;
- peu de journalisation ;
- absence de gestion avancée des expériences ;
- peu de contrôles qualité ;
- documentation limitée.

Ces limites justifient notre architecture modulaire.

---

# 15. Décisions de Grow Tech AI

À partir de cette analyse, le laboratoire adopte les décisions suivantes :

✅ Conserver :

- la logique générale du pipeline ;
- la compatibilité avec Hugging Face ;
- le format de soumission.

Améliorer :

- architecture logicielle ;
- reproductibilité ;
- modularité ;
- suivi des expériences ;
- gestion des configurations ;
- documentation ;
- automatisation.

---

# 16. Opportunités d'amélioration

Axes prioritaires :

## Architecture

- découpage en modules Python ;
- séparation claire des responsabilités.

## Données

- validation automatique ;
- EDA automatisée ;
- contrôle qualité.

## Entraînement

- gestion des expériences ;
- configurations YAML ;
- callbacks personnalisés.

## Évaluation

- métriques complètes ;
- analyse des erreurs ;
- comparaison automatique des modèles.

## Déploiement

- scripts CLI ;
- génération automatique des soumissions.

---

# 17. Impact sur notre feuille de route

Cette analyse influence directement :

- `dataset_loader.py`
- `prepare_dataset.py`
- `trainer.py`
- `predict.py`
- `generate_submission.py`
- `evaluation_pipeline.py`

Toutes les futures implémentations devront rester compatibles avec la logique générale de la baseline tout en améliorant sa qualité.

---

# 18. Questions de recherche

Cette analyse ouvre plusieurs pistes :

- Gemma est-il réellement le meilleur choix ?
- Whisper est-il plus robuste ?
- Les modèles multilingues généralisent-ils mieux ?
- L'augmentation des données améliore-t-elle les performances ?
- Quels hyperparamètres sont les plus sensibles ?

Ces questions alimenteront les expérimentations futures.

---

# 19. Éléments à automatiser

Les futures versions du laboratoire devront permettre :

- l'exécution automatique de la baseline ;
- l'enregistrement des métriques ;
- la comparaison avec les modèles Grow Tech AI ;
- la génération d'un rapport automatique.

---

# 20. Documents associés

- `01_Dataset_Audit.md`
- `02_Dataset_Anatomy.md`
- `03_EDA.md`
- `05_Model_Comparison.md`
- `06_Experiment_Log.md`

---

# 21. Travaux futurs

Ce document sera enrichi avec :

- les résultats des premières exécutions ;
- les métriques obtenues ;
- les comparaisons entre modèles ;
- les analyses d'erreurs ;
- les recommandations issues des expérimentations.

Il constituera la référence officielle pour toute évolution de la baseline.

---

# 22. Historique des versions

| Version | Date        | Auteur       | Description                                  |
| ------- | ----------- | ------------ | -------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de l'analyse de la baseline |
