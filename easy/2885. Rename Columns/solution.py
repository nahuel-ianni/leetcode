# Solution for the 'Rename Columns' problem.
# Time complexity: O(n).
# Space complexity: O(n * m).

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns=
        {
            'id': 'student_id',
            'first': 'first_name',
            'last': 'last_name',
            'age': 'age_in_years'
         })