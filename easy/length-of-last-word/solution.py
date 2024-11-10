# Solution for the 'Length of Last Word' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Process:
        #     1. Remove trailing whitespace from the string.
        #     2. Traverse characters from the end, counting until reaching a space.
        
        length = 0
        s = s.rstrip()      # Remove trailing whitespace

        for char in reversed(s):
            if char == ' ':
                break
            
            length += 1

        return length
