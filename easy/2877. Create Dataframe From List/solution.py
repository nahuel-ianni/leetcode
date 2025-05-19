# Solution for the 'Create a Dataframe From List' problem.
# Time complexity: O(n).
# Space complexity: O(n).

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
