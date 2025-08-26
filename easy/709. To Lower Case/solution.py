# Solution for the 'To Lower Case' problem.
# Time complexity: O(n).
# Space complexity: O(n).
# ASCII code table: https://www.ascii-code.com/characters/ascii-alphabet-characters

class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(
            chr(ord(ch) + 32) if 'A' <= ch <= 'Z' else ch for ch in s
        )
