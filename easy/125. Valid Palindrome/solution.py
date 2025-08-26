# Solution for the 'Valid Palindrome' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        # Process:
        #   1. Use a two-pointer approach to iterate over the string.
        #   2. Skip non-alphanumeric characters by adjusting 'left' and 'right' pointers.
        #   3. Compare characters from both ends, ensuring case insensitivity.
        
        while left < right:
            # Move 'left' pointer to the next alphanumeric character.
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move 'right' pointer to the previous alphanumeric character.
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
        
        return True
