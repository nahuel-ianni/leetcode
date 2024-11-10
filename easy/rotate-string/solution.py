# Solution for the 'Rotate String' problem.
# Time complexity: O(n).
# Space complexity: O(n).
 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1st check: Lengths must be the same if a rotation is to lead to equal strings.
        # 2nd check: By concatenating the string twice, goal should be within. This removes
        #            the need to iterate and exchange chars, reducing time complexity.
        return len(s) == len(goal) and goal in (s + s)
