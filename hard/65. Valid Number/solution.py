# Solution for the 'Valid Number' problem.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        if s in {"inf", "+inf", "-inf", "Infinity", "+Infinity", "-Infinity", "nan"}:
            return False

        try:
            _ = float(s)
            return True
        
        except ValueError:
            return False
