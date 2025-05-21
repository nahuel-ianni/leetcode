# Solution for the 'Change Data Type' problem.
# Time complexity: O(n).
# Space complexity: O(n).

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int64')
    return students
