# Solution for the 'Drop Missing Data' problem.
# Time complexity: O(n).
# Space complexity: O(n).

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
