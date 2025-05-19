# Solution for the 'Drop Duplicate Rows' problem.
# Time complexity: O(n * m).
# Space complexity: O(n).

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')