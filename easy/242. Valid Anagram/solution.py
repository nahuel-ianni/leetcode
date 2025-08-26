# Solution for the 'Valid Anagram' problem.
# Time complexity: O(n).
# Space complexity: O(n).

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return the result of comparing the two Counters directly.
        return Counter(s) == Counter(t)


# Alternative implementation using dictionaries.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Step 1: Guard against strings with different lenghts.
#         if len(s) != len(t):
#             return False
        
#         char_count = {}
        
#         # Step 2: Iterate through both strings simultaneously using zip().
#         #         Increment counts for characters in 's', decrement for characters in 't'.
#         for ch1, ch2 in zip(s, t):
#             char_count[ch1] = char_count.get(ch1, 0) + 1  # Increment count for 's'
#             char_count[ch2] = char_count.get(ch2, 0) - 1  # Decrement count for 't'
        
#         # Step 3: Check if all counts are zero.
#         #         If any count is non-zero, the strings are not anagrams.
#         return all(count == 0 for count in char_count.values())
