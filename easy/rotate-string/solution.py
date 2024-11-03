# This is my solution for the 'Rotate String' problem.
# Time complexity: O(n).
# Space complexity: O(n).
 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If the lengths are different, then they can't reach the desired goal.
        if len(s) != len(goal):
            return False

        # To reduce time complexity, check if goal is within 2 's' in a row,
        # removing the need to iterate and exchange chars.
        return goal in (s + s)
