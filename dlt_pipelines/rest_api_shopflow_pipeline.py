from typing import Optional
import pandas as pd
import sqlalchemy as sa
import os

import dlt
from dlt.sources.helpers import requests


def load_api_data() -> None:
    """

    """
    # Create a dlt pipeline that will load
    pipeline = dlt.pipeline(
        pipeline_name="product_pipeline",
        dataset_name="products_data",
        destination="duckdb"
    )

    response = requests.get('https://fakestoreapi.com/products')
    response.raise_for_status()
    data = response.json()   
        

    # Extract, normalize, and load the data
    load_info = pipeline.run(data, table_name="products")
    print(load_info)  # noqa: T201




if __name__ == "__main__":
    load_api_data()
