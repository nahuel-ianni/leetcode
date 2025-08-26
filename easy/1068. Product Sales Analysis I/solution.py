# Solution to the 'Product Sales Analysis I' problem.

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, product, on='product_id')
    return df[['product_name', 'year', 'price']]