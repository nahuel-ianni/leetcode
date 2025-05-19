# Solution for the 'Select Data' problem.
# Time complexity: O(n).
# Space complexity: O(n).

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name","age"]]
    # return students[students['student_id'] == 101][['name', 'age']]