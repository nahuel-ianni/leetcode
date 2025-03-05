# Solution for the 'Ransom Note' problem.
# Time complexity: O(n + m)
# Space complexity: O(n + m)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        return (a & b) == a
