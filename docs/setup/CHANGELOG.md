# Grow Tech AI Research Lab

# Setup Documentation Changelog

> **Document ID :** SOP-SETUP-CHANGELOG  
> **Catégorie :** Documentation  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI

---

# Objectif

Ce document retrace l'ensemble des évolutions apportées à la documentation du dossier `docs/setup/`.

Contrairement au changelog principal du projet, ce document ne concerne **que les procédures d'installation, de configuration et de validation du laboratoire**.

Il permet de :

- suivre l'évolution des procédures ;
- documenter les corrections ;
- garantir la reproductibilité du laboratoire ;
- faciliter l'intégration de nouveaux développeurs et d'IA de développement.

---

# Politique de mise à jour

Une nouvelle entrée doit être ajoutée lorsque :

- une procédure est créée ;
- une procédure est supprimée ;
- une commande est modifiée ;
- une nouvelle dépendance est introduite ;
- une nouvelle version majeure d'un outil est adoptée ;
- une erreur importante est corrigée ;
- une nouvelle bonne pratique est documentée.

---

# Format des entrées

Chaque modification doit respecter la structure suivante :

```text
Version

Date

Auteur

Documents concernés

Résumé

Ajouts

Modifications

Corrections

Compatibilité

Actions recommandées
```

---

# Historique

---

## [1.0.0] - Initialisation

**Date :** À compléter

**Auteur :** Grow Tech AI

### Documents créés

- README.md
- 01_environment_setup.md
- 02_python_installation.md
- 03_huggingface_setup.md
- 04_gpu_setup.md
- 05_first_run.md
- 06_troubleshooting.md

### Ajouts

- Architecture complète de la documentation Setup.
- Procédure standardisée d'installation Python.
- Procédure Hugging Face.
- Validation GPU.
- Procédure de premier lancement.
- Base de connaissances des erreurs fréquentes.

### Compatibilité

- Windows 11
- Python 3.11
- Git
- Hugging Face Hub
- PyTorch
- CUDA (optionnel)

---

# Modèle de nouvelle entrée

---

## [X.Y.Z] - Titre de la mise à jour

**Date :**

**Auteur :**

### Documents concernés

-

### Ajouts

-

### Modifications

-

### Corrections

-

### Compatibilité

-

### Impact

Faible / Moyen / Élevé

### Action requise

Aucune / Mise à jour recommandée / Mise à jour obligatoire

---

# Compatibilité des versions

| Version | Python | PyTorch | CUDA | Hugging Face | Statut |
| ------- | ------ | ------- | ---- | ------------ | ------ |
| 1.0.0   | 3.11   | 2.x     | 12.x | Oui          | Stable |

---

# Règles de gestion

Les principes suivants doivent être respectés :

- Ne jamais supprimer une ancienne entrée.
- Corriger une erreur en ajoutant une nouvelle version.
- Utiliser des numéros de version cohérents (SemVer).
- Décrire les impacts potentiels sur les utilisateurs.
- Indiquer clairement les actions à réaliser après une mise à jour.

---

# Convention de versionnement

Le dossier `docs/setup/` suit le versionnement sémantique (Semantic Versioning).

## Version majeure (X.0.0)

Utilisée lorsqu'une procédure est profondément modifiée ou remplacée.

Exemples :

- nouvelle méthode d'installation Python ;
- changement majeur de l'environnement de développement ;
- migration vers un nouvel outil.

---

## Version mineure (0.X.0)

Utilisée lorsqu'une nouvelle procédure est ajoutée.

Exemples :

- ajout d'un guide CUDA ;
- ajout d'un guide WSL ;
- ajout d'un guide Docker.

---

## Correctif (0.0.X)

Utilisé pour :

- correction d'une commande ;
- amélioration d'une explication ;
- mise à jour d'un lien ;
- correction d'une erreur de documentation.

---

# Validation

Avant chaque publication d'une nouvelle version de la documentation Setup, vérifier :

- [ ] Toutes les commandes ont été testées.
- [ ] Les liens sont fonctionnels.
- [ ] Les captures d'écran (si présentes) sont à jour.
- [ ] Les nouvelles dépendances sont documentées.
- [ ] Les documents associés ont été mis à jour.
- [ ] Les anciennes versions restent consultables.

---

# Documents associés

- docs/setup/README.md
- 01_environment_setup.md
- 02_python_installation.md
- 03_huggingface_setup.md
- 04_gpu_setup.md
- 05_first_run.md
- 06_troubleshooting.md

---

# Notes

Ce document est dédié exclusivement à la documentation d'installation.

Les évolutions du code source, des modèles, des scripts et des expériences sont documentées dans leurs propres fichiers de suivi (Developer Pack, Experiment Tracking, Changelog principal, etc.).
