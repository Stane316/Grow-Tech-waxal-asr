# Grow Tech AI Research Lab

# Exploratory Data Analysis (EDA) — Google WAXAL Dataset

> **Document ID :** RESEARCH-EDA-001  
> **Catégorie :** Exploratory Data Analysis (EDA)  
> **Version :** 1.0.0  
> **Projet :** Google WAXAL ASR Challenge  
> **Organisation :** Grow Tech AI  
> **Statut :** Living Document

---

# 1. Objectif

Ce document centralise l'ensemble des analyses exploratoires réalisées sur le dataset Google WAXAL.

L'objectif est de comprendre les caractéristiques réelles des données avant toute phase de modélisation.

Une EDA rigoureuse permet notamment de :

- détecter les déséquilibres ;
- identifier les anomalies ;
- comprendre la diversité linguistique ;
- mesurer la qualité des données ;
- guider les choix de prétraitement ;
- orienter les futures expérimentations.

Toutes les statistiques présentées dans ce document doivent être **reproductibles** et **générées automatiquement** à partir des scripts du laboratoire.

---

# 2. Philosophie de l'EDA

Le laboratoire Grow Tech AI considère que :

> **Aucune décision de modélisation ne doit être prise avant une analyse exploratoire complète.**

Chaque hypothèse doit être justifiée par des observations quantitatives.

Les analyses réalisées ici serviront de base à toutes les décisions techniques du projet.

---

# 3. Pipeline EDA

Le pipeline d'analyse suit les étapes suivantes :

```text
Chargement du dataset
        │
        ▼
Validation
        │
        ▼
Inspection des colonnes
        │
        ▼
Statistiques descriptives
        │
        ▼
Analyse audio
        │
        ▼
Analyse texte
        │
        ▼
Analyse linguistique
        │
        ▼
Analyse des métadonnées
        │
        ▼
Détection des anomalies
        │
        ▼
Visualisations
        │
        ▼
Conclusions
```

---

# 4. Informations générales

Cette section résume les caractéristiques globales du dataset.

À compléter automatiquement :

- nombre total d'exemples ;
- nombre de langues ;
- nombre de partitions ;
- taille totale ;
- durée totale des enregistrements ;
- nombre de locuteurs (si disponible).

---

# 5. Analyse des partitions

Objectif :

Étudier la répartition des données entre les différents ensembles.

Indicateurs :

- nombre d'exemples par partition ;
- durée totale par partition ;
- pourcentage du dataset.

Visualisations prévues :

- diagramme circulaire ;
- histogramme.

---

# 6. Analyse des langues

Objectif :

Comprendre la distribution linguistique.

Mesures :

- nombre d'exemples par langue ;
- durée moyenne ;
- durée totale ;
- vocabulaire estimé.

Visualisations :

- histogramme des langues ;
- répartition cumulative.

Questions de recherche :

- Existe-t-il un fort déséquilibre ?
- Certaines langues sont-elles sous-représentées ?

---

# 7. Analyse des durées audio

Mesures :

- durée minimale ;
- durée maximale ;
- moyenne ;
- médiane ;
- écart-type ;
- quartiles.

Visualisations :

- histogramme ;
- boxplot ;
- courbe cumulative.

Questions :

- Les fichiers sont-ils homogènes ?
- Existe-t-il des valeurs extrêmes ?

---

# 8. Analyse des fréquences d'échantillonnage

Objectif :

Identifier les formats audio présents.

Mesures :

- fréquence d'échantillonnage ;
- nombre de canaux ;
- profondeur de quantification (si disponible).

Questions :

- Une normalisation est-elle nécessaire ?
- Tous les fichiers utilisent-ils le même format ?

---

# 9. Analyse des transcriptions

Cette partie étudie les caractéristiques textuelles.

Mesures :

- longueur moyenne ;
- longueur maximale ;
- nombre de mots ;
- nombre de caractères ;
- distribution des longueurs.

Visualisations :

- histogramme ;
- distribution cumulative.

---

# 10. Analyse du vocabulaire

Objectifs :

Comprendre la richesse lexicale.

Mesures :

- taille du vocabulaire ;
- fréquence des mots ;
- mots rares ;
- mots les plus fréquents.

Visualisations :

- nuage de mots (optionnel) ;
- histogramme des fréquences.

Questions :

- Le vocabulaire suit-il une loi de Zipf ?
- Existe-t-il beaucoup de mots rares ?

---

# 11. Analyse des caractères

Étudier :

- alphabet utilisé ;
- caractères spéciaux ;
- caractères Unicode ;
- ponctuation ;
- chiffres ;
- symboles.

Objectif :

Définir la stratégie de normalisation du texte.

---

# 12. Analyse des locuteurs

Lorsque les informations sont disponibles :

Mesures :

- nombre de locuteurs ;
- répartition par langue ;
- équilibre entre locuteurs.

Questions :

- Certains locuteurs dominent-ils le corpus ?
- Existe-t-il un risque de surapprentissage ?

---

# 13. Analyse des métadonnées

Inspection complète des colonnes disponibles.

Pour chaque champ :

- nom ;
- type ;
- taux de valeurs manquantes ;
- rôle potentiel.

Objectif :

Identifier les informations exploitables pendant l'entraînement.

---

# 14. Détection des anomalies

Le laboratoire recherchera notamment :

- audios vides ;
- fichiers corrompus ;
- doublons ;
- transcriptions manquantes ;
- durées anormales ;
- caractères inattendus.

Chaque anomalie sera documentée.

---

# 15. Analyse des déséquilibres

Cette section identifiera :

- déséquilibres entre langues ;
- déséquilibres entre durées ;
- déséquilibres entre locuteurs ;
- déséquilibres textuels.

Ces informations guideront les stratégies de rééchantillonnage et d'augmentation.

---

# 16. Analyse de la qualité

Objectifs :

Évaluer :

- qualité audio ;
- bruit ;
- cohérence des transcriptions ;
- diversité des données.

Des métriques spécifiques pourront être ajoutées au fil des recherches.

---

# 17. Conséquences pour le prétraitement

À partir des analyses précédentes, cette section documentera les décisions retenues concernant :

- normalisation audio ;
- nettoyage des textes ;
- suppression des anomalies ;
- stratégies d'augmentation.

Chaque décision devra être justifiée par les observations de l'EDA.

---

# 18. Conséquences pour les modèles

L'EDA influencera notamment :

- le choix du tokenizer ;
- les stratégies multilingues ;
- les architectures retenues ;
- les hyperparamètres.

Toutes les décisions seront reliées aux résultats observés.

---

# 19. Visualisations générées

Les figures produites automatiquement seront enregistrées dans :

```text
docs/research/assets/

├── figures/
├── plots/
├── tables/
└── reports/
```

Chaque figure devra être :

- numérotée ;
- légendée ;
- référencée dans ce document.

---

# 20. Génération automatique

Les résultats de ce document seront générés par :

```text
scripts/prepare_dataset.py
```

et

```text
src/data/dataset_loader.py
```

Les graphiques pourront être produits par un futur module dédié :

```text
src/evaluation/eda_generator.py
```

---

# 21. Questions de recherche

Les analyses devront répondre notamment aux questions suivantes :

- Les langues sont-elles équilibrées ?
- Les durées sont-elles homogènes ?
- Les textes nécessitent-ils une normalisation ?
- Les fichiers audio présentent-ils des anomalies ?
- Les métadonnées sont-elles exploitables ?
- Quelles stratégies d'augmentation semblent les plus pertinentes ?

---

# 22. Travaux futurs

Après les premières expérimentations, ce document sera enrichi avec :

- statistiques complètes ;
- tableaux automatiques ;
- figures ;
- analyses comparatives entre langues ;
- recommandations issues des expériences.

---

# 23. Documents associés

- `01_Dataset_Audit.md`
- `02_Dataset_Anatomy.md`
- `04_Baseline_Analysis.md`
- `05_Model_Comparison.md`
- `Developer-Pack/03_DATASET_DOCUMENTATION.md`

---

# 24. Historique des versions

| Version | Date        | Auteur       | Description                      |
| ------- | ----------- | ------------ | -------------------------------- |
| 1.0.0   | À compléter | Grow Tech AI | Première version du document EDA |
