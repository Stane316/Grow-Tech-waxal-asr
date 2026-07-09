# Grow Tech AI Research Lab

# Decision Log — Google WAXAL ASR Challenge

> **Document ID :** RESEARCH-DECISIONS-001  
> **Catégorie :** Architecture & Research Decision Records (ADR)  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document constitue le registre officiel des décisions techniques, scientifiques et organisationnelles prises durant le projet.

Son rôle est de garantir que chaque décision importante soit :

- justifiée ;
- documentée ;
- traçable ;
- reproductible ;
- réévaluable.

Une décision ne doit jamais reposer uniquement sur l'intuition ou la mémoire des membres de l'équipe.

---

# 2. Philosophie

Grow Tech AI applique le principe suivant :

> **Une bonne décision est une décision argumentée, même si elle s'avère imparfaite.**

Une décision doit toujours être fondée sur :

- des observations ;
- des résultats expérimentaux ;
- une revue bibliographique ;
- des contraintes techniques ;
- les objectifs du projet.

---

# 3. Pourquoi un Decision Log ?

Le laboratoire doit pouvoir répondre à tout moment à des questions comme :

- Pourquoi avons-nous choisi Gemma comme baseline ?
- Pourquoi Whisper n'a-t-il pas été retenu ?
- Pourquoi avons-nous adopté LoRA ?
- Pourquoi avons-nous rejeté telle augmentation audio ?
- Pourquoi avons-nous changé le scheduler ?
- Pourquoi avons-nous modifié l'architecture du dépôt ?

Toutes ces réponses doivent être documentées ici.

---

# 4. Cycle de décision

Chaque décision suit le cycle suivant :

```text
Observation
      │
      ▼
Analyse
      │
      ▼
Alternatives
      │
      ▼
Décision
      │
      ▼
Implémentation
      │
      ▼
Validation
      │
      ▼
Réévaluation éventuelle
```

---

# 5. Classification des décisions

Les décisions sont regroupées en plusieurs catégories.

## Architecture

- structure du projet
- organisation du code
- pipeline

---

## Données

- sélection du dataset
- nettoyage
- prétraitement

---

## Modèles

- architecture retenue
- fine-tuning
- transfert

---

## Expérimentation

- protocole
- métriques
- benchmark

---

## Infrastructure

- GPU
- environnement
- Git
- CI/CD

---

## Documentation

- conventions
- Developer Pack
- workflow

---

## Organisation

- répartition des tâches
- branches Git
- revues de code

---

# 6. Format officiel d'une décision

Chaque décision doit respecter exactement la structure suivante.

---

## Identifiant

```text
ADR-2026-001
```

---

## Date

AAAA-MM-JJ

---

## Auteur(s)

Responsable de la décision.

Participants consultés.

---

## Titre

Titre explicite.

Exemple :

```
Adoption de Gemma comme modèle de référence
```

---

## Catégorie

Architecture

Données

Modèle

Infrastructure

Organisation

Documentation

---

## Contexte

Quel problème devait être résolu ?

---

## Observation

Quelles observations ont conduit à cette réflexion ?

---

## Alternatives étudiées

Exemple :

- Gemma
- Whisper
- wav2vec2
- HuBERT

Chaque alternative doit être brièvement analysée.

---

## Critères d'évaluation

Exemple :

- WER
- CER
- VRAM
- Temps
- Simplicité
- Documentation
- Réutilisabilité

---

## Décision retenue

Décrire clairement la décision.

---

## Justification

Pourquoi cette solution est-elle préférable ?

---

## Conséquences attendues

Impacts positifs.

Risques.

Compromis.

---

## Expériences associées

Référence vers :

```
06_Experiment_Log.md
```

---

## Idées associées

Référence vers :

```
07_Research_Ideas.md
```

---

## Livrables concernés

Scripts

Documentation

Modules

Configurations

---

## Statut

- Proposée
- Validée
- En cours
- Abandonnée
- Remplacée

---

## Révision prévue

Date ou condition de réévaluation.

---

# 7. Registre des décisions

| ID           | Décision                                    | Catégorie      | Statut  | Responsable  |
| ------------ | ------------------------------------------- | -------------- | ------- | ------------ |
| ADR-2026-001 | Utiliser Gemma comme baseline officielle    | Modèle         | Validée | Grow Tech AI |
| ADR-2026-002 | Architecture modulaire du dépôt             | Architecture   | Validée | Grow Tech AI |
| ADR-2026-003 | Utilisation de YAML pour les configurations | Infrastructure | Validée | Grow Tech AI |
| ADR-2026-004 | Adoption du BAIP                            | Recherche      | Validée | Grow Tech AI |

Ce tableau sera enrichi au fil du projet.

---

# 8. Décisions fondatrices du laboratoire

Les décisions suivantes sont considérées comme structurantes.

## ADR-2026-001

Architecture logicielle modulaire.

---

## ADR-2026-002

Les notebooks servent uniquement à l'exploration.

Toute logique métier est implémentée dans `src/`.

---

## ADR-2026-003

Toutes les expériences sont reproductibles.

---

## ADR-2026-004

Toutes les configurations sont versionnées.

---

## ADR-2026-005

Chaque nouvelle fonctionnalité est développée dans une branche `feature/*`.

---

## ADR-2026-006

Le BAIP est adopté comme cadre officiel de maturation des innovations.

---

# 9. Critères de qualité d'une décision

Une décision est considérée de qualité lorsqu'elle est :

- argumentée ;
- fondée sur des preuves ;
- reproductible ;
- documentée ;
- réversible si nécessaire.

---

# 10. Réévaluation des décisions

Une décision peut être révisée si :

- une nouvelle publication scientifique apparaît ;
- un nouveau modèle est disponible ;
- une expérience invalide l'hypothèse initiale ;
- les contraintes du projet évoluent.

Une révision crée un nouvel ADR qui référence l'ancien.

---

# 11. Relations avec les autres documents

Le Decision Log est au centre du laboratoire.

Il reçoit des informations provenant de :

- `01_Dataset_Audit.md`
- `02_Dataset_Anatomy.md`
- `03_EDA.md`
- `04_Baseline_Analysis.md`
- `05_Model_Comparison.md`
- `06_Experiment_Log.md`
- `07_Research_Ideas.md`

Et alimente :

- `10_TASKS.md`
- `11_DELIVERABLES.md`
- `08_PROJECT_ROADMAP.md`
- `09_CURRENT_STATUS.md`

---

# 12. Gouvernance des décisions

Pour toute décision majeure, le processus suivant est recommandé :

1. Proposition d'une idée (`07_Research_Ideas.md`)
2. Revue documentaire
3. Étude de faisabilité (BAIP)
4. Expérimentation (`06_Experiment_Log.md`)
5. Analyse des résultats
6. Validation collective de l'équipe
7. Enregistrement dans le `Decision_Log`
8. Implémentation dans une branche `feature/*`

Ainsi, aucune décision stratégique n'est prise sans justification.

---

# 13. Perspectives

Au-delà de ce hackathon, ce registre deviendra la mémoire stratégique de Grow Tech AI.

Il permettra :

- de réutiliser les bonnes pratiques ;
- de comprendre rapidement les anciens projets ;
- de former de nouveaux membres ;
- de faciliter les revues techniques ;
- de capitaliser les connaissances acquises.

---

# 14. Historique des versions

| Version | Date        | Auteur       | Description                                         |
| ------- | ----------- | ------------ | --------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du registre officiel des décisions |
