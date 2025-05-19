# Solution for the 'Get the Size of a DataFrame' problem.
# Time complexity: O(1).
# Space complexity: O(1).

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
    # return [players.shape[0], players.shape[1]]