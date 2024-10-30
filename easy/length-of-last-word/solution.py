# This is my solution for the 'Length of Last Word' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.rstrip()      # Remove trailing whitespace

        for char in reversed(s):
            if char == ' ':
                break
            
            length += 1

        return length
