# Solution for the 'First Letter to Appear Twice' problem.
# Time complexity: O(n)
# Space complexity: O(n) -> (Maximum 26 chars)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        x = set()
        for ch in s:
            if ch in x:
                return ch

            x.add(ch)
        
        return None