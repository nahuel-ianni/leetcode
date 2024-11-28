# Solution for the 'Display the First Three Rows' problem.
# Time complexity: O(1). Slicing is a constant-time operation in Pandas.
# Space complexity: O(1). Creates a shallow copy or view without duplicating data.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use .iloc for integer-based row selection.
    # .iloc[:3] selects rows at positions 0, 1, and 2 (exclusive of 3).
    # This works reliably even if the DataFrame has non-integer or unordered indices.
    return employees.iloc[:3]

# Alternative method not benefiting from .iloc:
# import pandas as pd

# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees[0:3]