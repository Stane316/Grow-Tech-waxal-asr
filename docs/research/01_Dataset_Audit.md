# Grow Tech AI Research Lab

# Dataset Audit — Google WAXAL Dataset

> **Document ID :** RESEARCH-DATASET-001  
> **Catégorie :** Dataset Documentation  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document constitue l'audit officiel du dataset **Google WAXAL** utilisé dans le cadre du Google WAXAL ASR Challenge.

Il centralise toutes les informations techniques, scientifiques et organisationnelles concernant le dataset afin de :

- comprendre sa structure ;
- documenter ses caractéristiques ;
- identifier ses forces et ses limites ;
- préparer les expérimentations futures ;
- garantir la reproductibilité des recherches.

Ce document est considéré comme la référence principale concernant le dataset au sein du laboratoire Grow Tech AI.

---

# 2. Présentation générale

## Nom

Google WAXAL Dataset

## Fournisseur

Google Research

## Hébergement

- Hugging Face Hub
- Utilisé dans la compétition Zindi Google WAXAL ASR Challenge

## Domaine

Reconnaissance Automatique de la Parole (Automatic Speech Recognition – ASR)

## Type

Dataset multimodal :

- audio
- texte
- métadonnées

---

# 3. Objectifs du dataset

Le dataset WAXAL a été conçu pour :

- favoriser la recherche sur les langues africaines ;
- améliorer les performances des systèmes ASR multilingues ;
- fournir un corpus ouvert de grande ampleur ;
- permettre le développement de modèles robustes pour des langues peu dotillées.

---

# 4. Utilisation dans la compétition

Le dataset est utilisé en deux phases.

## Phase 1

Les participants disposent :

- du train set ;
- du validation set ;
- du test set (sans labels publics pour l'évaluation).

Objectif :

Développer le meilleur modèle possible.

---

## Phase 2

Les organisateurs publient :

- un nouveau jeu de test totalement inédit.

Aucune métadonnée supplémentaire n'est fournie.

Cette phase mesure uniquement la capacité de généralisation des modèles.

---

# 5. Source officielle

## Hugging Face

```
google/WaxalNLP
```

## Compétition

Google WAXAL ASR Challenge (Zindi)

---

# 6. Taille du dataset

Le dépôt Hugging Face représente environ :

> **1,6 To**

Important :

Le projet n'exige **pas** de télécharger l'intégralité du dataset.

Le chargement s'effectue dynamiquement via :

```python
load_dataset(...)
```

Le téléchargement est réalisé à la demande selon :

- la langue ;
- le split ;
- les besoins expérimentaux.

---

# 7. Organisation générale

Le dataset est organisé par :

- langues ;
- splits ;
- exemples.

Chaque exemple contient plusieurs informations.

---

# 8. Structure logique

Chaque observation contient notamment :

- identifiant
- audio
- transcription
- langue
- métadonnées éventuelles

Le détail complet est documenté dans :

```
02_Dataset_Anatomy.md
```

---

# 9. Splits disponibles

Le dataset est organisé autour de plusieurs partitions.

Les principales sont :

- Train
- Validation
- Test

Chaque partition joue un rôle spécifique dans le développement du modèle.

---

# 10. Langues

Le dataset couvre plusieurs langues africaines.

Le nombre exact de langues et leurs statistiques seront validés automatiquement après exécution du module :

```
dataset_loader.py
```

Une mise à jour sera effectuée à partir des données réellement téléchargées.

---

# 11. Nature des données

Le dataset contient :

## Audio

Enregistrements vocaux.

---

## Texte

Transcriptions manuelles.

---

## Métadonnées

Selon les partitions :

- langue
- identifiants
- autres informations descriptives

Certaines métadonnées disparaissent volontairement en Phase 2 afin d'évaluer la robustesse des modèles.

---

# 12. Formats

## Audio

À confirmer automatiquement lors du chargement.

Informations à documenter :

- format
- fréquence d'échantillonnage
- nombre de canaux
- durée moyenne

---

## Texte

À documenter :

- alphabet
- Unicode
- ponctuation
- caractères spéciaux
- normalisation

---

# 13. Taille réelle utilisée par le laboratoire

Le laboratoire Grow Tech AI adopte une politique de téléchargement minimal.

Ne sont téléchargées que :

- les langues étudiées ;
- les partitions nécessaires ;
- les échantillons utiles aux expériences.

Cette stratégie :

- réduit l'espace disque ;
- accélère les expérimentations ;
- améliore la reproductibilité.

---

# 14. Contraintes du dataset

Le dataset présente plusieurs contraintes importantes.

## Taille

Très volumineux.

---

## Déséquilibre

Certaines langues peuvent être sous-représentées.

---

## Bruit

Présence probable :

- de bruit de fond ;
- de variations d'enregistrement.

---

## Généralisation

Le jeu de test final est totalement inédit.

Le surapprentissage est fortement pénalisé.

---

# 15. Forces

Le dataset présente plusieurs avantages.

- corpus ouvert ;
- très grande taille ;
- nombreuses langues africaines ;
- diversité des locuteurs ;
- cas réel de recherche.

---

# 16. Limites

Plusieurs limites doivent être prises en compte.

- volume très important ;
- coût d'entraînement élevé ;
- hétérogénéité des langues ;
- qualité variable des enregistrements ;
- absence de certaines métadonnées en Phase 2.

---

# 17. Implications pour notre stratégie

Compte tenu de cet audit, notre stratégie sera basée sur :

- un chargement dynamique ;
- des expériences reproductibles ;
- des modèles capables de généraliser ;
- une forte attention portée au prétraitement ;
- une évaluation rigoureuse.

---

# 18. Informations restant à confirmer

Les éléments suivants seront automatiquement extraits lors de l'analyse réelle du dataset :

- nombre exact de langues ;
- nombre d'exemples par langue ;
- durée totale ;
- durée moyenne ;
- fréquence d'échantillonnage ;
- statistiques des transcriptions ;
- répartition des locuteurs ;
- taille réelle de chaque split.

Ces informations seront produites par :

```
src/data/dataset_loader.py
```

et intégrées automatiquement au présent document.

---

# 19. Documents associés

- `02_Dataset_Anatomy.md`
- `03_EDA.md`
- `04_Baseline_Analysis.md`
- `Developer-Pack/03_DATASET_DOCUMENTATION.md`

---

# 20. Travaux futurs

Après le développement du `dataset_loader.py`, ce document sera enrichi avec :

- statistiques détaillées ;
- tableaux automatiques ;
- graphiques ;
- distributions ;
- métriques descriptives.

Il deviendra alors le document de référence définitif sur le dataset WAXAL utilisé par Grow Tech AI.

---

# 21. Historique des versions

| Version | Date        | Auteur       | Description                                     |
| ------- | ----------- | ------------ | ----------------------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du document d'audit du dataset |
