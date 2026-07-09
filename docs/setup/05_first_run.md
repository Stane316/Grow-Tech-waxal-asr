# Grow Tech AI Research Lab

# SOP-SETUP-005 — First Run & Laboratory Validation

> **Document ID :** SOP-SETUP-005  
> **Catégorie :** Setup  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure décrit la première exécution complète du laboratoire Grow Tech AI.

Son objectif est de vérifier que l'environnement est entièrement opérationnel avant de commencer le développement des modèles ASR.

Cette étape constitue le point de départ officiel du laboratoire de recherche.

Aucun développement ne doit commencer tant que cette validation n'est pas réussie.

---

# 2. Résultat attendu

À la fin de cette procédure, le laboratoire devra être capable de :

- lancer Python correctement ;
- utiliser l'environnement virtuel ;
- accéder au dépôt GitHub ;
- accéder à Hugging Face ;
- télécharger le dataset WAXAL ;
- exécuter les scripts internes ;
- lancer la baseline officielle ;
- préparer les futures expérimentations.

---

# 3. Prérequis

Les procédures suivantes doivent être terminées :

- ✅ SOP-SETUP-001 — Environment Setup
- ✅ SOP-SETUP-002 — Python Installation
- ✅ SOP-SETUP-003 — Hugging Face Setup
- ✅ SOP-SETUP-004 — GPU Setup (si GPU disponible)

---

# 4. Vérification du dépôt Git

Depuis la racine du projet :

```powershell
git status
```

Résultat attendu :

```text
On branch develop

nothing to commit
working tree clean
```

Puis vérifier le dépôt distant :

```powershell
git remote -v
```

---

# 5. Activation de l'environnement virtuel

Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Vérifier :

```powershell
python --version
```

Le terminal doit afficher :

```
(.venv)
```

---

# 6. Vérification de l'environnement

Exécuter :

```powershell
python scripts/check_environment.py
```

Le script doit contrôler :

- version Python ;
- Virtual Environment ;
- Git ;
- dépendances principales ;
- Hugging Face ;
- accès Internet ;
- espace disque ;
- GPU (si disponible).

Aucune erreur critique ne doit être présente.

---

# 7. Vérification Hugging Face

Contrôler l'authentification :

```powershell
hf auth whoami
```

Résultat attendu :

```
<nom_utilisateur>
```

Puis tester l'accès au dataset.

---

# 8. Vérification du dataset

Le téléchargement ne doit pas être réalisé manuellement.

Le projet utilisera le futur module :

```
src/data/dataset_loader.py
```

En attendant son développement, un test minimal peut être réalisé :

```python
from datasets import load_dataset

dataset = load_dataset(
    "google/WaxalNLP",
    "fon",
    split="train[:5]"
)

print(dataset)
```

Le chargement des cinq premiers exemples confirme que la connexion est correcte.

---

# 💡 Pourquoi ?

Le dataset WAXAL complet représente plus de 1,6 To de données.

Le laboratoire adopte une stratégie de téléchargement à la demande (lazy loading) afin de :

- limiter l'espace disque utilisé ;
- accélérer les expérimentations ;
- respecter la logique du notebook officiel.

---

# 9. Vérification des dépendances

Lister les principales bibliothèques :

```powershell
pip list
```

Vérifier notamment :

- torch
- transformers
- datasets
- huggingface_hub
- evaluate
- jiwer
- librosa
- numpy
- pandas
- soundfile

---

# 10. Vérification GPU

Exécuter :

```python
import torch

print(torch.cuda.is_available())

if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
```

Si aucun GPU n'est disponible, le laboratoire doit continuer à fonctionner sur CPU.

---

# 11. Vérification de la structure du projet

Les dossiers suivants doivent exister :

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

Aucun dossier ne doit être supprimé.

---

# 12. Vérification de la branche Git

Le développement doit commencer sur :

```
develop
```

Pour une nouvelle fonctionnalité :

```powershell
git checkout develop

git pull

git checkout -b feature/nom-fonctionnalite
```

Exemple :

```powershell
git checkout -b feature/dataset-loader
```

---

# 13. Premier notebook

Ouvrir :

```
notebooks/
```

À ce stade, seul le notebook officiel de la compétition doit être utilisé comme référence.

Les notebooks personnels devront uniquement servir à :

- l'exploration ;
- l'analyse ;
- les expérimentations.

Le code validé sera ensuite déplacé dans :

```
src/
```

---

# 14. Premier entraînement

Le premier entraînement du projet devra être :

- la baseline officielle ;
- sans modification ;
- avec les paramètres recommandés par les organisateurs.

Objectif :

Obtenir un point de référence (baseline) reproductible avant toute optimisation.

---

# 15. Premier benchmark

Une fois la baseline exécutée, enregistrer :

- temps d'entraînement ;
- temps d'inférence ;
- utilisation mémoire ;
- utilisation GPU ;
- métriques obtenues (WER, CER, etc.).

Ces informations constitueront le benchmark de référence du laboratoire.

---

# 16. Premier journal d'expérience

Créer une première entrée dans :

```
experiments/logs/
```

Cette entrée devra contenir :

- date ;
- auteur ;
- branche Git ;
- matériel utilisé ;
- modèle ;
- dataset ;
- hyperparamètres ;
- résultats ;
- observations.

---

# 17. Validation finale

Le laboratoire est considéré comme opérationnel si :

- [ ] Le dépôt Git est synchronisé
- [ ] Le Virtual Environment fonctionne
- [ ] Python est détecté
- [ ] Les dépendances sont installées
- [ ] Hugging Face est authentifié
- [ ] Le dataset WAXAL est accessible
- [ ] Le GPU est détecté (si disponible)
- [ ] Le script `check_environment.py` réussit
- [ ] La baseline officielle peut être exécutée
- [ ] Un premier journal d'expérience a été créé

---

# 18. Bonnes pratiques

Avant chaque session de travail :

- Mettre à jour la branche `develop`
- Activer `.venv`
- Vérifier l'environnement
- Synchroniser le dépôt

Après chaque session :

- Sauvegarder les expériences
- Mettre à jour la documentation
- Effectuer les commits nécessaires
- Pousser les modifications sur GitHub

---

# 19. Documents associés

- SOP-SETUP-001 — Environment Setup
- SOP-SETUP-002 — Python Installation
- SOP-SETUP-003 — Hugging Face Setup
- SOP-SETUP-004 — GPU Setup
- `Developer-Pack/09_CURRENT_STATUS.md`
- `Developer-Pack/10_TASKS.md`
- `Developer-Pack/14_EXPERIMENT_TRACKING.md`

---

# 20. Historique des versions

| Version | Date        | Auteur       | Description                                                          |
| ------- | ----------- | ------------ | -------------------------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la procédure de premier lancement du laboratoire |
