# Solution for the 'Create a New Column' problem.
# Time complexity: O(n).
# Space complexity: O(n).

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees