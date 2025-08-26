# Solution to the 'Customer Who Visited but Did Not Make Any Transactions' problem.

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    missing = visits[~visits['visit_id'].isin(transactions['visit_id'])]
    grouped = missing.groupby('customer_id',as_index= False)['visit_id'].count()
    return grouped.rename(columns={'visit_id':'count_no_trans'})

# # Alternative [less-performant] option.
# # This creates a new DF, increasing memory usage.
# def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
#     df = pd.merge(visits, transactions, on='visit_id', how='left', indicator=True)
#     df = df[df['_merge'] == 'left_only']
#     return df.groupby('customer_id').size().reset_index(name='count_no_trans')