# Solution for the 'Find the Difference' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for ch in s + t:
            diff ^= ord(ch)
        
        return chr(diff)