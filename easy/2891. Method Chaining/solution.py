# Solution for the 'Method Chaining' problem.
# Time complexity: O(n log n).
# Space complexity: O(n).

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals.weight > 100].sort_values(by='weight', ascending=False)[['name']]
