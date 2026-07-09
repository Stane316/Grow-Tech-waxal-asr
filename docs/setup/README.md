# Grow Tech AI Research Lab

## Setup Documentation

> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Ce dossier contient l'ensemble des procédures nécessaires pour installer, configurer, vérifier et exécuter correctement le laboratoire de recherche Grow Tech AI développé dans le cadre du **Google WAXAL ASR Challenge**.

L'objectif de cette documentation est de garantir qu'un nouveau membre de l'équipe — humain ou IA — puisse préparer un environnement de développement entièrement fonctionnel sans assistance supplémentaire.

Toutes les procédures décrites ici sont conçues pour être **reproductibles**, **documentées** et **réutilisables** dans les futurs projets Grow Tech AI.

---

# 2. À qui s'adresse cette documentation ?

Cette documentation est destinée aux :

- développeurs rejoignant le projet ;
- chercheurs en intelligence artificielle ;
- membres de l'équipe Grow Tech AI ;
- contributeurs open source ;
- IA de développement (Codex, Claude Code, Cursor, Gemini CLI, Windsurf, etc.).

Aucune connaissance préalable du projet n'est supposée.

---

# 3. Objectifs de l'installation

À la fin des procédures décrites dans ce dossier, l'environnement devra permettre de :

- exécuter le projet sans erreur ;
- accéder au dataset WAXAL ;
- télécharger les modèles Hugging Face ;
- utiliser le GPU si disponible ;
- entraîner un modèle ASR ;
- générer une soumission Zindi ;
- reproduire les expériences de recherche.

---

# 4. Ordre recommandé de lecture

Les documents doivent être lus dans l'ordre suivant :

| Étape | Document                  | Description                                             |
| ----- | ------------------------- | ------------------------------------------------------- |
| 1     | 01_environment_setup.md   | Présentation générale et préparation de l'environnement |
| 2     | 02_python_installation.md | Installation de Python et des dépendances               |
| 3     | 03_huggingface_setup.md   | Configuration de Hugging Face                           |
| 4     | 04_gpu_setup.md           | Vérification de CUDA et du GPU                          |
| 5     | 05_first_run.md           | Premier lancement du projet                             |
| 6     | 06_troubleshooting.md     | Résolution des problèmes fréquents                      |

Il est fortement déconseillé de modifier cet ordre.

---

# 5. Plateformes supportées

Le laboratoire est officiellement compatible avec :

| Système               | Support                   |
| --------------------- | ------------------------- |
| Windows 11            | ✅ Officiel               |
| Windows 10            | ✅ Officiel               |
| Ubuntu 22.04+         | ✅ Recommandé             |
| Ubuntu 24.04+         | ✅ Recommandé             |
| WSL2                  | ✅ Supporté               |
| macOS (Apple Silicon) | ⚠️ Partiellement supporté |

---

# 6. Versions logicielles recommandées

Les versions suivantes constituent la référence officielle du projet.

| Logiciel         | Version recommandée                 |
| ---------------- | ----------------------------------- |
| Python           | 3.11.x                              |
| Git              | dernière version stable             |
| VS Code          | dernière version stable             |
| CUDA             | selon la version de PyTorch retenue |
| PyTorch          | version stable compatible CUDA      |
| Hugging Face Hub | dernière version stable             |

Ces versions pourront évoluer au cours du projet.

---

# 7. Philosophie du laboratoire

Le laboratoire Grow Tech AI repose sur plusieurs principes fondamentaux.

## Reproductibilité

Toutes les expériences doivent pouvoir être reproduites.

---

## Documentation

Chaque décision importante doit être documentée.

---

## Modularité

Chaque composant doit être indépendant.

---

## Qualité

Le code doit être lisible, testé et maintenable.

---

## Collaboration

Toutes les modifications importantes passent par Git Flow et Pull Request.

---

# 8. Arborescence du laboratoire

Le projet est organisé autour des principaux espaces suivants.

```text
Developer-Pack/
docs/
src/
scripts/
config/
data/
experiments/
tests/
output/
notebooks/
```

Chaque dossier possède une responsabilité clairement définie.

---

# 9. Vérification de l'installation

Une installation est considérée comme réussie lorsque :

- Python est détecté ;
- Git fonctionne ;
- le Virtual Environment est actif ;
- Hugging Face est authentifié ;
- le GPU est détecté (si disponible) ;
- le dataset est accessible ;
- les dépendances sont installées ;
- le script `check_environment.py` s'exécute sans erreur.

---

# 10. Temps estimé

| Étape                        | Durée estimée |
| ---------------------------- | ------------- |
| Installation de Python       | 5 à 10 min    |
| Installation des dépendances | 5 à 15 min    |
| Configuration Hugging Face   | 5 min         |
| Vérification GPU             | 5 min         |
| Premier lancement            | 10 min        |

Temps total estimé :

**30 à 45 minutes**

---

# 11. Documents associés

Cette documentation est complétée par :

- `Developer-Pack/00_PROJECT_CONTEXT.md`
- `Developer-Pack/02_TECHNICAL_ARCHITECTURE.md`
- `Developer-Pack/05_DEVELOPMENT_RULES.md`
- `Developer-Pack/07_GIT_WORKFLOW.md`
- `Developer-Pack/13_AI_INSTRUCTIONS.md`
- `AGENTS.md`
- `AI_ONBOARDING.md`

---

# 12. Bonnes pratiques

Avant toute modification importante :

- synchroniser la branche `develop` ;
- créer une branche `feature/*` dédiée ;
- documenter les changements ;
- vérifier l'environnement ;
- exécuter les tests concernés.

---

# 13. Support

En cas de problème :

1. consulter `06_troubleshooting.md` ;
2. vérifier la documentation officielle des outils concernés ;
3. ouvrir une issue GitHub si le problème persiste.

---

# 14. Historique des versions

| Version | Date        | Auteur       | Description                               |
| ------- | ----------- | ------------ | ----------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du manuel d'installation |
