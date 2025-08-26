# Solution for the 'Check if Two String Arrays are Equivalent' problem.
# Time complexity: O(n + m).
# Space complexity: O(n + m).

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)