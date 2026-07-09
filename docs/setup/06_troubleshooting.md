# Grow Tech AI Research Lab

# SOP-SETUP-006 — Troubleshooting & Knowledge Base

> **Document ID :** SOP-SETUP-006  
> **Catégorie :** Setup  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure regroupe les problèmes les plus fréquents rencontrés lors de l'installation et de la configuration du laboratoire Grow Tech AI.

Son objectif est de :

- accélérer le diagnostic ;
- proposer des solutions reproductibles ;
- éviter les pertes de temps ;
- constituer une base de connaissances évolutive.

Avant de demander de l'aide, chaque membre de l'équipe doit consulter ce document.

---

# 2. Méthode de diagnostic

En cas de problème, appliquer systématiquement la démarche suivante :

1. Identifier précisément le message d'erreur.
2. Déterminer à quelle étape du processus l'erreur apparaît.
3. Vérifier les prérequis.
4. Consulter cette documentation.
5. Rechercher si le problème est déjà connu.
6. Tester la solution proposée.
7. Documenter le problème si celui-ci est inédit.

---

# 3. Problèmes liés à Python

## 3.1 `python` n'est pas reconnu

### Symptôme

```text
'python' n'est pas reconnu en tant que commande interne ou externe.
```

### Causes possibles

- Python n'est pas installé.
- Python n'est pas présent dans le PATH.

### Vérification

```powershell
python --version
```

### Solution

- Réinstaller Python depuis le site officiel.
- Cocher **Add Python to PATH** pendant l'installation.

---

## 3.2 `pip` est introuvable

### Symptôme

```text
No module named pip
```

### Vérification

```powershell
python -m pip --version
```

### Solution

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

---

## 3.3 Impossible de créer le Virtual Environment

### Symptôme

```text
python -m venv .venv
```

bloque ou échoue.

### Causes possibles

- Installation Python incomplète.
- Antivirus.
- Permissions insuffisantes.
- Installation via un gestionnaire alternatif (cas rencontré avec `uv`).

### Solution

- Réinstaller Python depuis python.org.
- Vérifier que `pip` est disponible.
- Relancer :

```powershell
python -m venv .venv
```

---

# 4. Problèmes liés à Git

## 4.1 Dépôt distant introuvable

### Vérification

```powershell
git remote -v
```

### Solution

Ajouter ou corriger le dépôt :

```powershell
git remote add origin <URL_DU_REPO>
```

---

## 4.2 Conflit lors d'un Pull

### Symptôme

Conflit de fusion.

### Solution

- Lire les fichiers concernés.
- Résoudre les conflits.
- Tester le projet.
- Finaliser la fusion.

Ne jamais supprimer un conflit sans comprendre son origine.

---

# 5. Problèmes liés à Hugging Face

## 5.1 `huggingface-cli login` ne demande pas le token

### Symptôme

La commande semble ne rien faire.

### Vérification

```powershell
hf --version
```

ou

```powershell
huggingface-cli --version
```

### Solution

Installer ou mettre à jour :

```powershell
pip install -U huggingface_hub
```

Puis utiliser :

```powershell
hf auth login
```

---

## 5.2 Token invalide

### Symptôme

```text
401 Unauthorized
```

### Solution

- Générer un nouveau token.
- Vérifier les permissions.
- Mettre à jour le fichier `.env`.

---

## 5.3 Dataset inaccessible

### Vérification

```python
from datasets import load_dataset
```

### Causes possibles

- Connexion Internet.
- Token incorrect.
- Nom du dataset erroné.

### Solution

Vérifier que l'identifiant est :

```text
google/WaxalNLP
```

---

# 6. Problèmes liés au GPU

## 6.1 `torch.cuda.is_available()` retourne False

### Vérification

```powershell
nvidia-smi
```

### Causes possibles

- Pilote absent.
- Version CPU de PyTorch.
- GPU non compatible.

### Solution

Installer la version CUDA de PyTorch adaptée.

---

## 6.2 Out Of Memory

### Symptôme

```text
CUDA Out Of Memory
```

### Solutions

- Réduire le batch size.
- Utiliser `fp16`.
- Activer le gradient checkpointing.
- Libérer la mémoire :

```python
torch.cuda.empty_cache()
```

---

# 7. Problèmes liés au Dataset WAXAL

## 7.1 Téléchargement trop volumineux

### Symptôme

Tentative de téléchargement de l'ensemble complet (~1,6 To).

### Solution

Ne jamais cloner l'intégralité du dépôt.

Utiliser uniquement :

```python
load_dataset(...)
```

avec les splits nécessaires.

---

## 7.2 Audio introuvable

### Causes possibles

- Mauvais split.
- Cache corrompu.

### Solution

Supprimer le cache concerné puis relancer le téléchargement.

---

# 8. Problèmes liés aux notebooks

## Le notebook fonctionne mais le script Python échoue

### Cause

Le notebook contient souvent du code exploratoire.

### Solution

Ne jamais copier directement un notebook dans `src/`.

Toujours :

1. Comprendre le code.
2. Le modulariser.
3. Le documenter.
4. Le tester.

---

# 9. Problèmes liés aux dépendances

## Conflit de versions

### Vérification

```powershell
pip list
```

### Solution

Créer un nouvel environnement virtuel propre et réinstaller les dépendances.

---

# 10. Vérifications rapides

Avant de signaler un problème, vérifier :

- [ ] Python fonctionne.
- [ ] Le Virtual Environment est activé.
- [ ] Git est opérationnel.
- [ ] Les dépendances sont installées.
- [ ] Hugging Face est authentifié.
- [ ] Le dataset est accessible.
- [ ] CUDA est détecté (si GPU).
- [ ] Le dépôt est à jour.

---

# 11. Journal des incidents

Chaque nouveau problème devra être documenté avec :

| Champ       | Description                          |
| ----------- | ------------------------------------ |
| Identifiant | Ex. TRB-001                          |
| Date        | Date de découverte                   |
| Auteur      | Personne ayant rencontré le problème |
| Contexte    | Situation                            |
| Symptôme    | Message d'erreur                     |
| Cause       | Cause identifiée                     |
| Solution    | Procédure appliquée                  |
| Validation  | Oui / Non                            |
| Références  | Liens utiles                         |

---

# 12. Bonnes pratiques

- Lire attentivement les messages d'erreur.
- Ne pas appliquer de solutions trouvées au hasard sans les comprendre.
- Documenter toute résolution durable.
- Mettre à jour cette base de connaissances après chaque incident significatif.

---

# 13. Documents associés

- SOP-SETUP-001 — Environment Setup
- SOP-SETUP-002 — Python Installation
- SOP-SETUP-003 — Hugging Face Setup
- SOP-SETUP-004 — GPU Setup
- SOP-SETUP-005 — First Run
- `Developer-Pack/12_VALIDATION_CHECKLIST.md`

---

# 14. Historique des versions

| Version | Date        | Auteur       | Description                                            |
| ------- | ----------- | ------------ | ------------------------------------------------------ |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la base de connaissances technique |
