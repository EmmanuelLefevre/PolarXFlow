# PARQUETFLOW

## SOMMAIRE
- [INTRODUCTION](#introduction)
- [PYTHON](#python)
- [REQUIREMENTS](#requirements)
- [GETTING STARTED](#getting-started)
- [DBT CONFIGURATION](#dbt-configuration)
- [PIPELINE DE DONNÉES](#pipeline-de-données)
  - [Sources](#sources)
  - [Modèles Cleansed](#modèles-cleansed)
  - [Dimensions et Faits](#dimensions-et-faits)
- [TO DO](#to-do)
- [CONTRIBUTION](#contribution)

---

## INTRODUCTION
Dans un monde où les volumes de données augmentent de manière exponentielle, leur collecte et leur transformation deviennent des enjeux cruciaux. Ce projet s'inscrit dans cette démarche en automatisant la récupération de données depuis des sources externes, leur transformation et leur structuration pour une analyse efficace.

Les fonctionnalités incluent :
- **Récupération des données** à partir de sources en ligne via des URL (API REST ou autres endpoints web), avec prise en charge des formats JSON et CSV.
- **Transformation des données brutes** en modèles structurés optimisés pour l'analyse.
- **Export des données au format Parquet**, idéal pour les pipelines d'analyse et d'ingestion performants.
- **Normalisation et enrichissement** des données brutes à l'aide de DBT et DuckDB pour créer des tables cleansed, des dimensions, et une table de faits.

Ce projet est conçu pour les développeurs, data engineers, ou analystes souhaitant automatiser la gestion de flux de données complexes tout en garantissant performance et évolutivité.

---

## PYTHON
[Guide d'installation Python](https://github.com/EmmanuelLefevre/Documentations/blob/master/Tutorials/python_install.md)

---

## REQUIREMENTS
Les bibliothèques Python nécessaires pour exécuter ce projet sont :
- `colorama`
- `pandas`
- `pyarrow`
- `python-dotenv`
- `requests`
- `duckdb`
- `dbt-core`
- `dbt-duckdb`

---

## GETTING STARTED

### Installation des librairies
1. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
2. Vérifiez l'installation des librairies :
   ```bash
   pip list
   ```

### Lancement du script Python
1. Exécutez le script principal :
   ```bash
   python app.py
   ```
2. Testez le fonctionnement avec les URLs fournies dans la section suivante.

### Exemples d'URL
#### JSON
- **Avec paramètres de pagination** :  
  URL pour récupérer les contributeurs du projet VSCode sur GitHub :
  ```bash
  https://api.github.com/repos/microsoft/vscode/contributors
  ```

- **Sans paramètres de pagination** :  
  URL pour récupérer la population américaine par année via l'API DataUSA :
  ```bash
  https://datausa.io/api/data?drilldowns=Nation&measures=Population
  ```

#### CSV
- **Avec paramètres de limite** :  
  URL pour récupérer les points d'impact des météorites depuis l'API NASA :
  ```bash
  https://data.nasa.gov/resource/gh4g-9sfh.csv?$limit=50000
  ```

Les fichiers Parquet générés seront disponibles dans le dossier `data_frame`.

---

## DBT CONFIGURATION

1. **Initialisation du projet DBT :**
   - Installez DBT avec DuckDB comme adaptateur :
     ```bash
     pip install dbt-core dbt-duckdb
     ```
   - Initialisez un projet DBT :
     ```bash
     dbt init raw
     ```
2. **Configuration du fichier `profiles.yml` :**
   Ajoutez le fichier `profiles.yml` dans `~/.dbt/` :
   ```yaml
   raw:
     outputs:
       dev:
         type: duckdb
         path: file.duckdb
         threads: 1
     target: dev
   ```

3. **Création des modèles :**
   - Modèles bruts (`raw`).
   - Modèles nettoyés (`cleansed`).
   - Dimensions et table de faits (`application`).

4. **Exécution des transformations :**
   ```bash
   dbt build
   ```

5. **Documentation et Graphe DAG :**
   - Génération de la documentation :
     ```bash
     dbt docs generate
     ```
   - Serveur interactif pour visualiser le graphe :
     ```bash
     dbt docs serve
     ```

---

## PIPELINE DE DONNÉES

### Sources
Les données brutes sont extraites des endpoints suivants :
- **Contributeurs** : `https://api.github.com/repos/microsoft/vscode/contributors`
- **Commits** : `https://api.github.com/repos/microsoft/vscode/commits`
- **Pull Requests** : `https://api.github.com/repos/microsoft/vscode/pulls`
- **Tags** : `https://api.github.com/repos/microsoft/vscode/tags`
- **Contenus** : `https://api.github.com/repos/microsoft/vscode/contents`

### Modèles Cleansed
Chaque source brute est transformée en un modèle nettoyé dans le schéma `cleansed`. Par exemple :
- `contributors_cleaned` : Ne garde que les contributeurs ayant des contributions positives.
- `commits_cleaned` : Filtre les commits valides avec auteur et message.

### Dimensions et Faits
Les dimensions (schéma `application`) décrivent les entités clés :
- `dim_contributors` : Détails des contributeurs.
- `dim_commits` : Informations sur les commits.
- `dim_pull_requests` : Pull requests avec leur statut.
- `dim_tags` : Tags associés aux commits.
- `dim_contents` : Détails des fichiers et dossiers.

La table de faits (`fact_activity`) combine ces dimensions pour analyser l'activité globale.

---

## TO DO
- Passer de `pandas` à `polars` pour des performances optimisées.
- Ajouter des prompts pour gérer les tokens de manière dynamique.
- Implémenter des contrôles pour les saisies incorrectes.
- Automatiser les tests DBT.

---

## CONTRIBUTION
Si vous souhaitez contribuer à ce projet :
1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/amélioration
   ```
3. Soumettez une pull request.

---

⭐⭐⭐ Merci pour votre intérêt ! N'hésitez pas à laisser une étoile ⭐ sur ce dépôt si vous le trouvez utile. 😊
