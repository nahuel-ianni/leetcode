# Solution to the 'Recyclable and Low Fat Products' problem

import pandas as pd


def find_products(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["low_fats"]=="Y") & (df["recyclable"]=="Y")] [["product_id"]]

# # Alternative solution
# def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    # return df[['product_id']]
