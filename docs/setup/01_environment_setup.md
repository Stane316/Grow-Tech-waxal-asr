# Grow Tech AI Research Lab

# 01 — Environment Setup

> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure décrit l'ensemble des étapes nécessaires pour préparer un environnement de développement conforme aux standards du laboratoire Grow Tech AI.

Elle constitue le point de départ obligatoire pour toute personne ou toute IA rejoignant le projet.

À l'issue de cette procédure, l'environnement de travail devra être prêt à accueillir les composants du projet, garantir la reproductibilité des expériences et respecter les conventions définies par Grow Tech AI.

---

# 2. Public concerné

Cette procédure est destinée aux :

- développeurs ;
- chercheurs ;
- étudiants ;
- collaborateurs ;
- IA de développement (Codex, Claude Code, Cursor, Gemini CLI, Windsurf, etc.).

---

# 3. Résultat attendu

À la fin de cette procédure, vous devrez disposer de :

- un dépôt Git correctement configuré ;
- une architecture de dossiers conforme au projet ;
- un environnement Python isolé ;
- les outils de développement installés ;
- une connexion fonctionnelle à Hugging Face ;
- une configuration Git opérationnelle ;
- une base prête pour l'entraînement des modèles.

---

# 4. Philosophie du laboratoire

Le laboratoire Grow Tech AI repose sur plusieurs principes fondamentaux.

## 4.1 Reproductibilité

Toutes les expériences doivent pouvoir être reproduites.

Aucune étape importante ne doit être réalisée manuellement sans être documentée.

---

## 4.2 Documentation

Toute décision importante doit être documentée.

Si une procédure n'est pas documentée, elle est considérée comme inexistante.

---

## 4.3 Modularité

Le projet est conçu comme un ensemble de composants indépendants.

Chaque module possède une responsabilité unique.

---

## 4.4 Réutilisabilité

Chaque composant développé doit pouvoir être réutilisé dans un futur projet.

Le hackathon est considéré comme un laboratoire de création de briques logicielles.

---

## 4.5 Qualité

La qualité du code est prioritaire sur la vitesse de développement.

Le laboratoire privilégie :

- la lisibilité ;
- la robustesse ;
- la maintenabilité ;
- les tests ;
- la documentation.

---

# 5. Prérequis matériels

Configuration minimale recommandée :

| Ressource          | Minimum    | Recommandé        |
| ------------------ | ---------- | ----------------- |
| RAM                | 16 Go      | 32 Go             |
| Stockage libre     | 150 Go SSD | 300 Go SSD        |
| GPU                | Facultatif | NVIDIA CUDA       |
| VRAM               | 6 Go       | ≥ 12 Go           |
| Connexion Internet | Stable     | Fibre recommandée |

---

# 6. Prérequis logiciels

Les logiciels suivants doivent être installés :

- Git
- Python 3.11.x
- Visual Studio Code
- GitHub Desktop (optionnel)
- NVIDIA Driver (si GPU)
- CUDA Toolkit (si GPU)
- Hugging Face CLI
- FFmpeg

Les procédures détaillées sont décrites dans les documents suivants.

---

# 7. Architecture du dépôt

Le dépôt suit l'organisation standard Grow Tech AI.

```text
config/
data/
docs/
Developer-Pack/
experiments/
notebooks/
output/
scripts/
src/
tests/
```

Chaque dossier possède une responsabilité unique.

Aucun code ne doit être ajouté dans un dossier inadapté.

---

# 8. Organisation Git

Le projet suit le modèle Git Flow simplifié.

Branches principales :

```text
main
develop
```

Branches de développement :

```text
feature/*
```

Exemples :

```text
feature/dataset-loader
feature/gemma-training
feature/whisper-baseline
feature/evaluation
```

Chaque fonctionnalité possède sa propre branche.

---

# 9. Workflow de développement

Le cycle de développement est le suivant :

```text
Créer une branche feature

↓

Développer

↓

Tester

↓

Créer une Pull Request

↓

Revue technique

↓

Fusion vers develop

↓

Validation

↓

Fusion vers main
```

Aucun développement direct sur `main` n'est autorisé.

---

# 10. Conventions générales

Le laboratoire applique les conventions suivantes.

## Python

- Python 3.11 uniquement

- Type hints obligatoires

- Docstrings Google Style

- Ruff / Black pour le formatage

- Logging au lieu de print()

---

## Git

Un commit = une idée.

Messages de commit explicites.

Exemple :

```text
feat(dataset): add dataset loader

fix(training): resolve CUDA memory issue

docs(setup): update installation guide
```

---

## Documentation

Toute fonctionnalité validée doit être documentée.

Les notebooks servent uniquement à :

- explorer ;
- expérimenter ;
- visualiser.

Le code final est toujours déplacé dans `src/`.

---

# 11. Arborescence logique du laboratoire

Le laboratoire est organisé selon quatre niveaux.

```
Documentation

↓

Recherche

↓

Développement

↓

Expérimentation
```

Cette hiérarchie doit être respectée durant tout le projet.

---

# 12. Vérification de l'installation

Avant de commencer le développement, vérifier que :

- Git fonctionne ;
- Python fonctionne ;
- le Virtual Environment est actif ;
- les dépendances sont installées ;
- Hugging Face est configuré ;
- CUDA est détecté (si disponible) ;
- `check_environment.py` s'exécute correctement.

Aucun développement ne doit commencer tant que cette validation n'est pas réussie.

---

# 13. Critères de validation

L'environnement est considéré comme correctement installé lorsque :

- tous les outils sont opérationnels ;
- la structure du dépôt est conforme ;
- le projet démarre sans erreur ;
- le script de vérification retourne un diagnostic positif.

---

# 14. Documents associés

Les procédures détaillées sont disponibles dans :

- `02_python_installation.md`
- `03_huggingface_setup.md`
- `04_gpu_setup.md`
- `05_first_run.md`
- `06_troubleshooting.md`

Les règles du projet sont décrites dans :

- `Developer-Pack/05_DEVELOPMENT_RULES.md`
- `Developer-Pack/06_CODING_STANDARDS.md`
- `Developer-Pack/07_GIT_WORKFLOW.md`

---

# 15. Bonnes pratiques

Avant chaque nouvelle session de travail :

- mettre à jour la branche `develop` ;
- vérifier l'environnement virtuel ;
- synchroniser le dépôt ;
- lancer les contrôles automatiques si disponibles.

Après chaque session :

- documenter les changements ;
- pousser les commits ;
- mettre à jour le journal des expériences si nécessaire.

---

# 16. Historique des versions

| Version | Date        | Auteur       | Description                                                 |
| ------- | ----------- | ------------ | ----------------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du guide d'installation de l'environnement |
