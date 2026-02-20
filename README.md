# shopflow-dlt-dbt

## Table des matières

- [Contexte](#contexte)

---

## Contexte

ShopFlow Analytics est un projet de data engineering orienté entreprise, conçu pour répondre aux besoins d'une PME e-commerce souhaitant centraliser et exploiter ses données métier.

L'entreprise collecte quotidiennement des données provenant de sources hétérogènes : une API de gestion des commandes et produits, des fichiers de stock au format CSV/JSON, et une base de données CRM interne. Ces données sont jusqu'ici exploitées de manière isolée, sans vision unifiée, ce qui freine la prise de décision de l'équipe business.

L'objectif de ce projet est de construire un pipeline de données robuste et automatisé permettant d'ingérer, transformer et exposer ces données sous forme de tables analytiques fiables et documentées. L'équipe business pourra ainsi accéder à des indicateurs clés sur les ventes, la segmentation client et l'état des stocks, mis à jour de manière automatique et testés pour en garantir la qualité.

Ce projet s'appuie sur un stack moderne : **dlt** pour l'ingestion, **dbt** pour la transformation et la qualité des données, et **GitHub Actions** pour l'automatisation et le CI/CD.

---