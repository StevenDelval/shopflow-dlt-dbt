from typing import  List
import dlt
from dlt.sources.rest_api import rest_api_source


@dlt.transformer(name="carts", primary_key="cart_product_id", write_disposition="merge")
def flatten_carts(carts_data: List[dict]):
    """Aplatir les produits du panier en ligne"""
    for cart in carts_data:
        cart_id = cart.get("id")
        user_id = cart.get("userId")
        date = cart.get("date")
        products = cart.get("products", [])
        
        for product in products:
            yield {
                "cart_product_id": f"{cart_id}_{product.get('productId')}",  # clé composite unique
                "cart_id": cart_id,
                "user_id": user_id,
                "date": date,
                "product_id": product.get("productId"),
                "quantity": product.get("quantity"),
            }

@dlt.transformer(name="users", primary_key="user_id", write_disposition="merge")
def flatten_users(users_data: List[dict]):
    """Aplatir les user en ligne"""
    for user in users_data:
        yield {
            "user_id": user.get("id"),
            "email": user.get("email"),
            "username": user.get("username"),
            "password": user.get("password"),
            "firstname": user.get("name")["firstname"],
            "lastname": user.get("name")["lastname"],
            "phone": user.get("phone"),
            "v": user.get("__v"),
            "city": user.get("address")["city"],
            "street": user.get("address")["street"],
            "address_number": user.get("address")["number"],
            "zipcode": user.get("address")["zipcode"],
            "address_lat": user.get("address")["geolocation"]["lat"],
            "address_long": user.get("address")["geolocation"]["long"],

        }

def load_api_data() -> None:
    """
    Extrait, transforme et charge les données de l'API FakeStore dans une base DuckDB.

    Pipeline DLT 'product_pipeline' → dataset 'raw' → '../duckdb/data.db'

    Ressources chargées :
        - products : catalogue complet des produits (merge sur id)
        - users    : liste des utilisateurs (merge sur id)
        - carts    : paniers d'achat avec chargement incrémental sur 'date'
                     depuis 2000-01-01, puis flattening via flatten_carts
                     (une ligne par produit par panier, merge sur cart_product_id)
    """
    # Créez un pipeline DLT qui chargera les données dans duckDB
    pipeline = dlt.pipeline(
        pipeline_name="product_pipeline",
        dataset_name="raw",
        destination=dlt.destinations.duckdb("../duckdb/data.db")
    )
    # Configure la source REST API FakeStore avec trois ressources :
    # - products : récupère tous les produits
    # - users    : récupère tous les utilisateurs  
    # - carts    : récupère les paniers de manière incrémentale sur le champ 'date'
    fakeshop_source = rest_api_source({
        "client": {
            "base_url": "https://fakestoreapi.com/",
            "paginator": "single_page"
        },
        "resource_defaults": {
            "write_disposition": "merge"
        },
        "resources": [
            {
                "name": "products",
                "primary_key": "id",
                "endpoint": {
                    "path": "products",
                    "method": "GET"
                },
            },
            {
                "name": "users_source",
                "primary_key": "id",
                "endpoint": {
                    "path": "users",
                    "method": "GET",
                },
            },
            {
                "name": "carts_source",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "path": "carts",
                    "method": "GET",
                    "params": {
                        "date": {
                            "type": "incremental",
                            "cursor_path": "date",
                            "initial_value": "2000-01-01T00:00:00Z",
                        }
                    }
                },
            }
        ],
    })
        
    # Appliquer les transformers
    carts_flattened = fakeshop_source.resources["carts_source"] | flatten_carts    
    users_flattened = fakeshop_source.resources["users_source"] | flatten_users    

    # Désactiver les ressources originales pour éviter le conflit d'instances
    fakeshop_source.resources["carts_source"].selected = False
    fakeshop_source.resources["users_source"].selected = False

    # Lancer le pipeline avec les ressources modifiées
    load_info = pipeline.run([
        fakeshop_source,
        users_flattened,
        carts_flattened,
    ])
    print(load_info)  


if __name__ == "__main__":
    load_api_data()
