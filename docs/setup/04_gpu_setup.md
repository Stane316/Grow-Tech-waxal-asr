# Grow Tech AI Research Lab

# SOP-SETUP-004 — GPU Setup & AI Workstation Validation

> **Document ID :** SOP-SETUP-004  
> **Catégorie :** Setup  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure décrit la configuration, la validation et l'optimisation d'un poste de travail équipé d'un GPU pour les projets d'intelligence artificielle du laboratoire Grow Tech AI.

À l'issue de cette procédure, le système devra être capable de :

- détecter automatiquement le GPU ;
- utiliser CUDA avec PyTorch ;
- entraîner des modèles ASR ;
- optimiser l'utilisation de la mémoire GPU ;
- diagnostiquer rapidement les problèmes matériels ou logiciels.

---

# 2. Pourquoi utiliser un GPU ?

L'entraînement des modèles de reconnaissance automatique de la parole (ASR) est extrêmement coûteux en calcul.

Un GPU permet :

- d'accélérer l'entraînement ;
- d'accélérer l'inférence ;
- d'utiliser des modèles plus volumineux ;
- de réduire le temps d'expérimentation.

Exemple :

| Modèle        | CPU                  | GPU        |
| ------------- | -------------------- | ---------- |
| Whisper Small | Très lent            | Rapide     |
| HuBERT        | Très lent            | Rapide     |
| wav2vec2      | Lent                 | Rapide     |
| Gemma         | Presque inutilisable | Utilisable |

---

# 3. Configuration recommandée

## Minimum

- NVIDIA GTX 1660
- 6 Go VRAM
- CUDA compatible

---

## Recommandé

- RTX 3060
- RTX 4060
- RTX 4070
- RTX A2000
- RTX A4000

avec :

- ≥ 12 Go VRAM

---

## Idéal

- RTX 4090
- RTX 5090
- A100
- H100

---

# 4. Vérifier la présence d'un GPU

Sous Windows :

Ouvrir PowerShell :

```powershell
nvidia-smi
```

Résultat attendu :

```
+-------------------------------------+
| NVIDIA-SMI                          |
| Driver Version                      |
| CUDA Version                        |
+-------------------------------------+
```

Si la commande n'existe pas :

- le pilote NVIDIA est absent ;
- CUDA n'est pas installé ;
- le GPU n'est pas NVIDIA.

---

# 💡 Pourquoi ?

`nvidia-smi` est l'outil officiel permettant de vérifier :

- le GPU détecté ;
- la version du pilote ;
- la mémoire vidéo ;
- les processus utilisant le GPU.

---

# 5. Installation du pilote NVIDIA

Télécharger le pilote uniquement depuis :

https://www.nvidia.com/download/index.aspx

Ne jamais utiliser un pilote provenant d'une source non officielle.

---

# 6. CUDA

Le laboratoire utilise CUDA uniquement via PyTorch.

Dans la majorité des cas, il n'est pas nécessaire d'installer CUDA Toolkit séparément.

L'installation de PyTorch fournit les bibliothèques CUDA adaptées.

---

# ⚠️ Piège fréquent

Installer une version de CUDA incompatible avec PyTorch.

Toujours vérifier :

https://pytorch.org/get-started/locally/

---

# 7. Installation de PyTorch

Exemple (CUDA 12.1) :

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Pour une installation CPU uniquement :

```powershell
pip install torch torchvision torchaudio
```

---

# 8. Vérification de CUDA avec Python

Créer un fichier temporaire :

```python
import torch

print("CUDA disponible :", torch.cuda.is_available())
print("Nombre de GPU :", torch.cuda.device_count())

if torch.cuda.is_available():
    print("GPU :", torch.cuda.get_device_name(0))
```

Résultat attendu :

```
CUDA disponible : True
Nombre de GPU : 1
GPU : NVIDIA ...
```

---

# 9. Informations détaillées

Afficher :

```python
import torch

print(torch.version.cuda)
print(torch.cuda.get_device_properties(0))
```

Ces informations sont utiles lors des rapports d'expériences.

---

# 10. Surveillance du GPU

Pendant l'entraînement :

```powershell
nvidia-smi -l 2
```

Le GPU sera actualisé toutes les deux secondes.

Surveiller :

- mémoire utilisée ;
- température ;
- charge GPU.

---

# 11. Optimisation mémoire

Pour limiter la consommation de VRAM :

- mixed precision (`fp16`) ;
- gradient accumulation ;
- batch size adapté ;
- nettoyage du cache CUDA.

Exemple :

```python
torch.cuda.empty_cache()
```

---

# 12. Erreurs fréquentes

## CUDA unavailable

Causes possibles :

- PyTorch CPU installé ;
- pilote NVIDIA absent ;
- mauvais environnement virtuel.

---

## Out of Memory (OOM)

Solutions :

- réduire le batch size ;
- utiliser `fp16` ;
- activer le gradient checkpointing ;
- fermer les autres applications utilisant le GPU.

---

## GPU non détecté

Vérifier :

```powershell
nvidia-smi
```

Puis :

```python
torch.cuda.is_available()
```

---

# ⚠️ Piège fréquent

Ne pas confondre :

- mémoire RAM ;
- mémoire VRAM.

Une machine peut avoir :

- 64 Go RAM

mais seulement :

- 4 Go VRAM

ce qui limitera fortement l'entraînement.

---

# 13. Cas particulier : ordinateur sans GPU

Le laboratoire fonctionne également :

- sur CPU ;
- sur Google Colab ;
- sur Kaggle ;
- sur Azure ;
- sur d'autres plateformes cloud.

Dans ce cas :

- l'entraînement sera plus lent ;
- certaines expériences devront être adaptées.

---

# 14. Recommandations Grow Tech AI

Toujours :

- utiliser le GPU lorsque disponible ;
- surveiller la mémoire ;
- documenter les caractéristiques matérielles dans chaque expérience.

---

# 15. Validation

La configuration GPU est considérée comme correcte si :

- [ ] `nvidia-smi` fonctionne ;
- [ ] le pilote NVIDIA est installé ;
- [ ] PyTorch détecte CUDA ;
- [ ] le nom du GPU est affiché ;
- [ ] un tenseur peut être déplacé sur le GPU.

---

# 16. Test final

Exécuter :

```python
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x = torch.randn(3, 3).to(device)

print(device)
print(x)
```

Le script doit s'exécuter sans erreur.

---

# 17. Bonnes pratiques

Avant chaque entraînement :

- vérifier le GPU disponible ;
- fermer les applications gourmandes ;
- surveiller la température ;
- enregistrer les caractéristiques matérielles dans le journal d'expérience.

---

# 18. Documents associés

- SOP-SETUP-001 — Environment Setup
- SOP-SETUP-002 — Python Installation
- SOP-SETUP-003 — Hugging Face Setup
- SOP-SETUP-005 — First Run
- `Developer-Pack/14_EXPERIMENT_TRACKING.md`

---

# 19. Historique des versions

| Version | Date        | Auteur       | Description                                           |
| ------- | ----------- | ------------ | ----------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la procédure de configuration GPU |
