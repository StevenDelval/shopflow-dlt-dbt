import random
import pandas as pd
from datetime import datetime, timedelta

WAREHOUSE_LOCATIONS = [
    "Paris-Nord", "Lyon-Est", "Marseille-Sud",
    "Bordeaux-Ouest", "Lille-Centre", "Toulouse-Sud"
]

NUM_RECORDS = 20
OUTPUT_FILE = "stock.csv"


def generate_last_updated() -> str:
    """Génère une date de dernière mise à jour.

    Returns:
        Chaîne de caractères au format ISO 8601 (ex: '2025-11-01T14:32:00Z').
    """
    dt = datetime.now() 
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def generate_stock_data(num_records: int) -> list[dict]:
    """
    Génère une liste de dictionnaires simulant un stock de produits.

    Args:
        num_records: Nombre d'enregistrements à générer.

    Returns:
        Liste de dictionnaires contenant les colonnes suivantes :
        product_id, warehouse_location, stock_quantity, last_updated, reorder_threshold.
    """
    records = []
    for i in range(1, num_records + 1):
        for warehouse in WAREHOUSE_LOCATIONS:
            stock_quantity = random.randint(0, 500)
            reorder_threshold = random.randint(10, 100)
            records.append({
                "product_id": i,
                "warehouse_location": warehouse,
                "stock_quantity": stock_quantity,
                "last_updated": generate_last_updated(),
                "reorder_threshold": reorder_threshold,
            })
    return records


def write_csv(records: list[dict], output_file: str) -> None:
    """
    Écrit ou ajoute les enregistrements dans un fichier CSV via un DataFrame pandas.
    Si le fichier existe déjà, les nouvelles lignes sont ajoutées sans réécrire l'en-tête.

    Args:
        records: Liste de dictionnaires à écrire.
        output_file: Chemin du fichier CSV de sortie.
    """
    df = pd.DataFrame(records)
    file_exists = pd.io.common.file_exists(output_file)
    df.to_csv(
        output_file,
        mode="a",
        index=False,
        encoding="utf-8",
        header=not file_exists,  # n'écrit l'en-tête que si le fichier n'existe pas
    )
    print(f"{len(df)} enregistrements ajoutés dans '{output_file}'")


def generate_stock_csv() -> None:
    """Point d'entrée principal : génère les données de stock et les sauvegarde dans un fichier CSV."""
    records = generate_stock_data(NUM_RECORDS)
    write_csv(records, OUTPUT_FILE)


if __name__ == "__main__":
    generate_stock_csv()
