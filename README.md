# shopflow-dlt-dbt

## Table des matières
- [Contexte](#contexte)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Commandes UV](#commandes-uv)

---

## Contexte
ShopFlow Analytics est un projet de data engineering orienté entreprise, conçu pour répondre aux besoins d'une PME e-commerce souhaitant centraliser et exploiter ses données métier.

L'entreprise collecte quotidiennement des données provenant de sources hétérogènes : une API de gestion des commandes et produits, des fichiers de stock au format CSV/JSON, et une base de données CRM interne. Ces données sont jusqu'ici exploitées de manière isolée, sans vision unifiée, ce qui freine la prise de décision de l'équipe business.

L'objectif de ce projet est de construire un pipeline de données robuste et automatisé permettant d'ingérer, transformer et exposer ces données sous forme de tables analytiques fiables et documentées. L'équipe business pourra ainsi accéder à des indicateurs clés sur les ventes, la segmentation client et l'état des stocks, mis à jour de manière automatique et testés pour en garantir la qualité.

Ce projet s'appuie sur un stack moderne : **dlt** pour l'ingestion, **dbt** pour la transformation et la qualité des données, et **GitHub Actions** pour l'automatisation et le CI/CD.

---

## Prérequis

- Python **3.10+**
- [uv](https://docs.astral.sh/uv/) — gestionnaire de paquets et d'environnements virtuels
- Git

---

## Installation
```bash
# Cloner le dépôt
git clone https://github.com//shopflow-dlt-dbt.git
cd shopflow-dlt-dbt

# Créer l'environnement virtuel et installer les dépendances
uv sync
```

---

## Commandes UV

| Commande | Description |
|---|---|
| `uv sync` | Installe toutes les dépendances du projet |
| `uv add <paquet>` | Ajoute une dépendance et met à jour `pyproject.toml` |
| `uv remove <paquet>` | Supprime une dépendance |
| `uv run <script.py>` | Exécute un script dans l'environnement du projet |
| `uv run pytest` | Lance les tests |
| `uv lock` | Regénère le fichier `uv.lock` |
| `uv pip list` | Liste les paquets installés |
| `uv python pin 3.10` | Épingle la version Python du projet dans .python-version |

### Activer l'environnement virtuel
```bash
# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Désactiver l'environnement
deactivate
```