# Grow Tech AI Research Lab

# SOP-SETUP-002 — Python Installation and Development Environment

> **Document ID :** SOP-SETUP-002  
> **Catégorie :** Setup  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure décrit l'installation complète de l'environnement Python utilisé par le laboratoire Grow Tech AI.

À l'issue de cette procédure, le poste de travail devra être capable de :

- exécuter du code Python 3.11 ;
- créer des environnements virtuels ;
- installer les dépendances du projet ;
- lancer les scripts du laboratoire ;
- exécuter les notebooks ;
- préparer les futurs entraînements ASR.

---

# 2. Pourquoi Python 3.11 ?

Le laboratoire adopte officiellement **Python 3.11.x**.

Cette version offre un excellent compromis entre :

- stabilité ;
- performances ;
- compatibilité avec PyTorch ;
- compatibilité avec Hugging Face ;
- compatibilité avec les bibliothèques ASR modernes.

Les versions plus anciennes limitent certaines fonctionnalités.

Les versions plus récentes peuvent entraîner des incompatibilités avec certaines bibliothèques.

---

# 3. Logiciels requis

Avant de commencer, les logiciels suivants doivent être installés :

| Logiciel               | Version recommandée     |
| ---------------------- | ----------------------- |
| Python                 | 3.11.x                  |
| Git                    | Dernière version stable |
| Visual Studio Code     | Dernière version stable |
| PowerShell 7 (Windows) | Recommandé              |

---

# 4. Téléchargement de Python

Télécharger Python uniquement depuis le site officiel :

https://www.python.org/downloads/

Version recommandée :

**Python 3.11.x (64 bits)**

Ne jamais installer une version provenant d'une source non officielle.

---

# 5. Installation de Python

Pendant l'installation :

☑️ Add Python to PATH

☑️ Install launcher for all users

☑️ pip

☑️ py launcher

☑️ Tcl/Tk

☑️ Documentation

Conserver les autres options par défaut.

---

# 6. Vérification de l'installation

Ouvrir un nouveau terminal puis exécuter :

```powershell
python --version
```

Résultat attendu :

```text
Python 3.11.x
```

Vérifier ensuite :

```powershell
pip --version
```

Puis :

```powershell
where python
```

Sous Linux :

```bash
which python3
```

---

# 7. Création de l'environnement virtuel

Depuis la racine du dépôt :

```powershell
python -m venv .venv
```

Le dossier suivant doit être créé :

```text
.venv/
```

---

# 8. Activation de l'environnement

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Une fois activé, le terminal doit afficher :

```text
(.venv)
```

---

# 9. Mise à jour des outils

Mettre immédiatement à jour les outils principaux :

```powershell
python -m pip install --upgrade pip
```

Puis :

```powershell
python -m pip install wheel setuptools
```

---

# 10. Installation des dépendances

Installer les dépendances du projet :

```powershell
pip install -r requirements.txt
```

Lorsque le projet adoptera Poetry ou uv, cette procédure sera mise à jour.

---

# 11. Vérification de l'environnement

Contrôler que Python est bien celui du Virtual Environment :

```powershell
python
```

Puis :

```python
import sys

print(sys.executable)
```

Le chemin doit pointer vers :

```text
.../.venv/...
```

---

# 12. Visual Studio Code

Extensions recommandées :

- Python
- Pylance
- Jupyter
- Ruff
- GitLens
- GitHub Pull Requests
- YAML
- Markdown All in One
- Error Lens
- Better Comments

---

# 13. Sélection de l'interpréteur

Dans VS Code :

Ctrl + Shift + P

Puis :

```
Python: Select Interpreter
```

Sélectionner :

```
.venv
```

Ne jamais utiliser un interpréteur global.

---

# 14. Vérification finale

Exécuter :

```powershell
python scripts/check_environment.py
```

Tous les contrôles doivent être validés.

---

# 15. Erreurs fréquentes

## python non reconnu

Solution :

Réinstaller Python avec l'option :

```
Add Python to PATH
```

---

## pip absent

Solution :

```powershell
python -m ensurepip --upgrade
```

---

## Virtual Environment impossible à créer

Causes possibles :

- installation Python incomplète ;
- antivirus ;
- droits insuffisants.

---

## Mauvais interpréteur VS Code

Vérifier :

```
Python: Select Interpreter
```

---

# 16. Bonnes pratiques

Toujours :

- activer le Virtual Environment ;
- mettre à jour pip ;
- installer les dépendances dans `.venv` uniquement ;
- ne jamais installer une bibliothèque globalement pour ce projet.

---

# 17. Documents associés

- SOP-SETUP-001 — Environment Setup
- SOP-SETUP-003 — Hugging Face Setup
- SOP-SETUP-004 — GPU Setup
- SOP-SETUP-005 — First Run

---

# 18. Checklist de validation

- [ ] Python 3.11 installé
- [ ] pip fonctionne
- [ ] Git installé
- [ ] VS Code installé
- [ ] Virtual Environment créé
- [ ] Virtual Environment activé
- [ ] requirements installés
- [ ] Interpréteur VS Code sélectionné
- [ ] check_environment.py exécuté avec succès

---

# 19. Historique des versions

| Version | Date        | Auteur       | Description                                            |
| ------- | ----------- | ------------ | ------------------------------------------------------ |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la procédure d'installation Python |
