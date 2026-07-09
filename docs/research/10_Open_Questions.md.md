# Grow Tech AI Research Lab

# Open Questions — Google WAXAL ASR Challenge

> **Document ID :** RESEARCH-OPEN-QUESTIONS-001  
> **Catégorie :** Open Research Questions & Unknowns  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document centralise toutes les questions scientifiques, techniques et stratégiques qui restent sans réponse au cours du projet.

Il constitue le registre officiel des inconnues du laboratoire.

Ses objectifs sont :

- éviter d'oublier une question importante ;
- guider les futures expérimentations ;
- identifier les besoins en recherche documentaire ;
- alimenter le BAIP (Grow Tech AI Innovation Pipeline) ;
- documenter les limites actuelles de notre compréhension.

---

# 2. Philosophie

Une question non résolue n'est pas un échec.

C'est une opportunité de recherche.

Chaque question doit progressivement évoluer vers :

```text
Question
      │
      ▼
Recherche documentaire
      │
      ▼
Hypothèse
      │
      ▼
Expérience
      │
      ▼
Décision
```

Les réponses devront être documentées dans :

- `07_Research_Ideas.md`
- `06_Experiment_Log.md`
- `08_Decision_Log.md`

---

# 3. Classification des questions

Toutes les questions sont classées par domaine.

## Données

- qualité
- couverture
- biais
- équilibre
- langues
- locuteurs

---

## Prétraitement

- nettoyage
- normalisation
- segmentation
- augmentation

---

## Modèles

- architecture
- fine-tuning
- décodage
- adaptation

---

## Entraînement

- hyperparamètres
- scheduler
- batch size
- learning rate
- stratégies de convergence

---

## Évaluation

- métriques
- WER
- CER
- robustesse
- généralisation

---

## Infrastructure

- GPU
- mémoire
- optimisation
- stockage

---

## Compétition

- attentes implicites du jury
- stratégie de leaderboard
- généralisation Phase 2
- erreurs fréquentes

---

## Produit

- réutilisation
- industrialisation
- GrowTech
- FacturaPro

---

# 4. Structure officielle d'une question

Chaque question suit le format suivant.

---

## Identifiant

```text
QUESTION-2026-001
```

---

## Date

AAAA-MM-JJ

---

## Auteur

Nom de la personne ayant soulevé la question.

---

## Domaine

Exemple :

- Modèle
- Données
- Infrastructure
- Évaluation

---

## Question

Question formulée clairement.

---

## Pourquoi cette question est-elle importante ?

Quel impact aurait sa réponse ?

---

## État actuel

- inconnue ;
- partiellement comprise ;
- en cours d'étude ;
- résolue.

---

## Hypothèses envisagées

Lister les hypothèses possibles.

---

## Sources potentielles

Où chercher la réponse ?

- littérature scientifique ;
- GitHub ;
- Hugging Face ;
- documentation officielle ;
- communauté Zindi ;
- forums spécialisés.

---

## Expériences nécessaires

Quelles expériences permettraient de répondre à cette question ?

---

## Documents associés

Références vers :

- Experiment Log
- Research Ideas
- Decision Log
- Related Work

---

## Priorité

⭐⭐⭐⭐⭐

---

## Responsable

À compléter.

---

## Date cible

À compléter.

---

## Réponse finale

À compléter une fois la question résolue.

---

# 5. Questions ouvertes actuelles

## QUESTION-2026-001

### Quel modèle généralise le mieux sur des langues africaines peu représentées ?

Statut :

En étude.

---

## QUESTION-2026-002

### Gemma est-il réellement supérieur à Whisper pour WAXAL ?

Statut :

Recherche documentaire.

---

## QUESTION-2026-003

### LoRA est-il suffisant ou faut-il utiliser QLoRA ?

Statut :

À étudier.

---

## QUESTION-2026-004

### Quelle stratégie d'augmentation améliore réellement le WER ?

Statut :

Non résolue.

---

## QUESTION-2026-005

### Quelle taille de batch maximise les performances sans dépasser la VRAM ?

Statut :

À expérimenter.

---

## QUESTION-2026-006

### Le Beam Search apporte-t-il un gain significatif par rapport au Greedy Decoding ?

Statut :

À vérifier.

---

## QUESTION-2026-007

### Les modèles multilingues souffrent-ils d'interférences entre langues africaines ?

Statut :

Ouverte.

---

## QUESTION-2026-008

### Comment maximiser la généralisation pour la Phase 2 ?

Statut :

Critique.

---

## QUESTION-2026-009

### Quels biais existent dans le dataset WAXAL ?

Statut :

À analyser.

---

## QUESTION-2026-010

### Quelle partie de la pipeline est actuellement le principal goulot d'étranglement ?

Statut :

À identifier.

---

# 6. Tableau de suivi

| ID                | Domaine       | Priorité   | Statut         | Responsable | BAIP   |
| ----------------- | ------------- | ---------- | -------------- | ----------- | ------ |
| QUESTION-2026-001 | Modèle        | ⭐⭐⭐⭐⭐ | En étude       | À définir   | BAIP-2 |
| QUESTION-2026-002 | Modèle        | ⭐⭐⭐⭐☆  | Recherche      | À définir   | BAIP-2 |
| QUESTION-2026-003 | Fine-Tuning   | ⭐⭐⭐⭐⭐ | Ouverte        | À définir   | BAIP-2 |
| QUESTION-2026-004 | Prétraitement | ⭐⭐⭐⭐☆  | Ouverte        | À définir   | BAIP-3 |
| QUESTION-2026-005 | Entraînement  | ⭐⭐⭐☆☆   | À expérimenter | À définir   | BAIP-4 |

---

# 7. Priorisation des recherches

Les questions sont classées selon leur impact potentiel sur :

- le WER ;
- le CER ;
- la robustesse ;
- la généralisation ;
- le coût GPU ;
- le temps d'entraînement ;
- la réutilisabilité.

Une note globale sur 100 pourra être attribuée.

---

# 8. Intégration avec le BAIP

Chaque question suit le pipeline suivant :

```text
Question
      │
      ▼
BAIP-2
Recherche documentaire
      │
      ▼
BAIP-3
Hypothèse
      │
      ▼
BAIP-5
Prototype
      │
      ▼
BAIP-6
Expérience
      │
      ▼
BAIP-7
Validation
      │
      ▼
Decision Log
```

---

# 9. Relations avec les autres documents

Ce document est relié à :

- `01_Dataset_Audit.md`
- `02_Dataset_Anatomy.md`
- `03_EDA.md`
- `04_Baseline_Analysis.md`
- `05_Model_Comparison.md`
- `06_Experiment_Log.md`
- `07_Research_Ideas.md`
- `08_Decision_Log.md`
- `09_Related_Work.md`

Une question résolue doit toujours conduire à une mise à jour des documents concernés.

---

# 10. Gouvernance

Lors de chaque réunion technique, l'équipe devra :

1. revoir les nouvelles questions ;
2. mettre à jour leur statut ;
3. prioriser celles qui auront le plus d'impact ;
4. transformer les plus importantes en hypothèses de recherche.

Ainsi, le registre reste vivant et guide les travaux du laboratoire.

---

# 11. Vision à long terme

Ce document sera conservé au-delà du Google WAXAL ASR Challenge.

Il constituera un historique des interrogations rencontrées dans les différents projets de Grow Tech AI.

À terme, il permettra :

- d'accélérer les futurs projets ;
- de former les nouveaux membres ;
- de documenter les connaissances acquises ;
- d'éviter de reposer plusieurs fois les mêmes questions.

---

# 12. Historique des versions

| Version | Date        | Auteur       | Description                                         |
| ------- | ----------- | ------------ | --------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du registre des questions ouvertes |
