# Solution for the 'Modify Columns' problem.
# Time complexity: O(n).
# Space complexity: O(1) for in-place updates, O(n) for immutable solution.

import pandas as pd

# In-place modification solution (when explicitly required or performance-critical)
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2

    return employees

# Alternative implementation for an immutable solution.
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.assign(salary=employees["salary"] * 2)