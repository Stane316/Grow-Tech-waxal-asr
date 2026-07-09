# Grow Tech AI Research Lab

# SOP-SETUP-003 — Hugging Face Setup

> **Document ID :** SOP-SETUP-003  
> **Catégorie :** Setup  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Active Development

---

# 1. Objectif

Cette procédure décrit la configuration complète de Hugging Face Hub au sein du laboratoire Grow Tech AI.

À la fin de cette procédure, le poste de travail devra être capable de :

- télécharger les datasets nécessaires ;
- télécharger les modèles pré-entraînés ;
- s'authentifier automatiquement auprès de Hugging Face ;
- utiliser les bibliothèques `datasets`, `transformers` et `huggingface_hub` sans intervention supplémentaire.

---

# 2. Pourquoi utilisons-nous Hugging Face ?

Hugging Face est la plateforme de référence pour le partage de modèles et de jeux de données en intelligence artificielle.

Dans le cadre du Google WAXAL ASR Challenge, elle est utilisée pour :

- héberger le dataset **WaxalNLP** ;
- distribuer les modèles de base (Gemma, Whisper, HuBERT, etc.) ;
- faciliter les téléchargements reproductibles ;
- centraliser les ressources open source.

Le laboratoire Grow Tech AI adopte Hugging Face comme source officielle des modèles et datasets.

---

# 3. Création du compte

Créer un compte gratuit sur :

https://huggingface.co

Choisir un nom d'utilisateur professionnel et pérenne.

Par exemple :

```
Grow Tech-ai
```

ou

```
stane-ai
```

Éviter les pseudonymes temporaires.

---

# 💡 Pourquoi ?

Le nom du compte peut apparaître :

- sur les modèles publiés ;
- sur les Spaces ;
- dans les collaborations open source ;
- dans les publications scientifiques.

Il constitue donc une partie de votre identité technique.

---

# 4. Création d'un Access Token

Après connexion :

Profil → **Settings** → **Access Tokens**

Créer un nouveau token.

Nom conseillé :

```
Grow Tech-WAXAL
```

Type :

```
Read
```

Le niveau **Read** est suffisant pour :

- télécharger les datasets ;
- télécharger les modèles ;
- accéder aux ressources publiques.

Le niveau **Write** n'est nécessaire que pour publier des modèles.

---

# ⚠️ Piège fréquent

Ne jamais utiliser un token **Write** si cela n'est pas indispensable.

Limiter les permissions réduit les risques de sécurité.

---

# 5. Conservation du token

Copier immédiatement le token.

Il ne sera plus affiché une seconde fois.

Le conserver dans un gestionnaire de mots de passe sécurisé.

Ne jamais :

- l'envoyer par e-mail ;
- le publier sur GitHub ;
- le partager dans un notebook ;
- le stocker dans un fichier versionné.

---

# 6. Création du fichier `.env`

À la racine du dépôt :

```
.env
```

Ajouter :

```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Le fichier `.env` ne doit jamais être versionné.

Le fichier `.gitignore` doit contenir :

```
.env
```

---

# 7. Authentification via la CLI

Installer les dépendances :

```powershell
pip install huggingface_hub
```

Puis vérifier :

```powershell
huggingface-cli --version
```

ou

```powershell
hf --version
```

Selon la version installée.

---

# 8. Connexion

Lancer :

```powershell
huggingface-cli login
```

ou, avec les versions récentes :

```powershell
hf auth login
```

Coller le token lorsque celui-ci est demandé.

Résultat attendu :

```
Login successful
```

---

# ⚠️ Piège fréquent

Si aucune invite n'apparaît après `huggingface-cli login`, vérifier que :

- le package `huggingface_hub` est bien installé ;
- le Virtual Environment est activé ;
- la commande `hf auth login` est disponible (nouvelle CLI).

---

# 9. Vérification de l'authentification

Exécuter :

```powershell
hf auth whoami
```

Résultat attendu :

```
username
```

Le nom du compte Hugging Face doit être affiché.

---

# 10. Test de téléchargement

Créer un fichier temporaire :

```python
from datasets import load_dataset

dataset = load_dataset(
    "google/WaxalNLP",
    "fon",
    split="train[:5]"
)

print(dataset)
```

Si les cinq premiers exemples sont chargés sans erreur, l'authentification est correcte.

---

# 11. Cache Hugging Face

Les téléchargements sont automatiquement mis en cache.

Sous Windows :

```
C:\Users\<Nom>\.cache\huggingface
```

Sous Linux :

```
~/.cache/huggingface
```

---

# 💡 Pourquoi ?

Le cache évite de télécharger plusieurs fois les mêmes modèles et datasets.

Cela réduit considérablement le temps de développement.

---

# 12. Nettoyage du cache

Afficher l'espace utilisé :

```powershell
hf cache ls
```

Supprimer des éléments inutilisés :

```powershell
hf cache delete
```

Ne jamais supprimer le cache pendant un entraînement.

---

# 13. Dataset WAXAL

Le dataset officiel est :

```
google/WaxalNLP
```

Pour cette compétition, **il n'est pas nécessaire de télécharger les 1,6 To de données**.

Les organisateurs demandent d'utiliser uniquement les splits :

- train
- validation
- test

correspondant à la Phase 1 du challenge.

Le téléchargement doit être piloté par le futur module `dataset_loader.py`, qui récupérera uniquement les données utiles.

---

# ⚠️ Piège fréquent

Ne pas tenter de cloner l'intégralité du dépôt Hugging Face avec Git LFS.

Le notebook officiel utilise directement l'API `datasets`, qui télécharge uniquement les ressources nécessaires.

C'est l'approche recommandée par les organisateurs.

---

# 14. Bonnes pratiques

Toujours :

- utiliser un token `Read` lorsque c'est suffisant ;
- conserver le token dans `.env` ;
- utiliser la bibliothèque `datasets` plutôt que des téléchargements manuels ;
- documenter toute ressource externe utilisée.

---

# 15. Validation

La configuration est considérée comme correcte si :

- [ ] le compte Hugging Face existe ;
- [ ] le token a été créé ;
- [ ] le token est stocké dans `.env` ;
- [ ] `hf auth whoami` fonctionne ;
- [ ] un extrait du dataset WAXAL est chargé avec succès ;
- [ ] le cache Hugging Face est opérationnel.

---

# 16. Documents associés

- SOP-SETUP-001 — Environment Setup
- SOP-SETUP-002 — Python Installation
- SOP-SETUP-004 — GPU Setup
- SOP-SETUP-005 — First Run
- `Developer-Pack/03_DATASET_DOCUMENTATION.md`

---

# 17. Historique des versions

| Version | Date        | Auteur       | Description                                                    |
| ------- | ----------- | ------------ | -------------------------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version de la procédure de configuration Hugging Face |
