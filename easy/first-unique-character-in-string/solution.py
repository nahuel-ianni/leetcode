# Solution for the 'First Unique Character in a String' problem.
# Time complexity: O(n).
# Space complexity: O(n).

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)
        
        for index, char in enumerate(s):
            if chars[char] == 1:
                return index
        
        return -1