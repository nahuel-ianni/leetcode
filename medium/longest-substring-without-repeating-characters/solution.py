# Solution for the "Longest Substring Without Repeating Characters" problem.
# Time complexity: O(n), where n is the length of the string.
# Space complexity: O(n), due to the set used to store characters of the current substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: Initialize a set to store unique characters in the current substring.
        char_set = set()
        
        # Step 2: Initialize pointers for the sliding window and the maximum length variable.
        left = 0        # Left pointer of the window
        max_length = 0  # Track the length of the longest substring
        
        # Step 3: Iterate through the string with the right pointer.
        for right in range(len(s)):
            # If the character at the right pointer is already in the set,
            # slide the left pointer to shrink the window until it's not.
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character from the set
                left += 1                 # Move the left pointer to the right
            
            # Add the current character to the set.
            char_set.add(s[right])
            
            # Update the maximum length of the substring found so far.
            max_length = max(max_length, right - left + 1)

        # Step 4: Return the maximum length.
        return max_length
