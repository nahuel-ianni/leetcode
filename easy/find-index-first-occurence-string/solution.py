# Solution for the 'Find the Index of the First Occurrence in a String' problem.
# Time complexity: O(n * m), where n = len(haystack) and m = len(needle).
# Space complexity: O(m) due to slicing.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Handle edge case when needle is empty
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        # Iterate through haystack up to the point where needle can fit
        for i in range(n - m + 1):
            # Check if the substring of haystack matches needle
            if haystack[i:i + m] == needle:
                return i
        
        # If no match is found, return -1
        return -1
