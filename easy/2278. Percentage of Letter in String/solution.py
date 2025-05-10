# Solution for the 'Percentage of Letter in String' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) / len(s) * 100)
