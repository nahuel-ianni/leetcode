# Solution for the 'Isomorphic Strings' problem.
# Time complexity: O(n), where n is the length of the strings.
# Space complexity: O(n), due to the dictionaries used to store character mappings.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Process:
        #   1. Check if the lengths of the strings are different.
        #      If so, return False immediately.
        #   2. Use two dictionaries to map characters from 's' to 't' and vice versa.
        #      - Ensure that each character in 's' maps to a single, consistent character in 't'.
        #      - Similarly, ensure that each character in 't' maps to a single character in 's'.
        #   3. If any mapping is inconsistent, return False.
        #   4. Return True if all character mappings are consistent.

        if len(s) != len(t):
            return False

        # Create dictionaries to map characters from 's' to 't' and vice versa.
        map_s, map_t = {}, {}

        # Iterate through both strings simultaneously using zip.
        for ch_s, ch_t in zip(s, t):
            # Check for inconsistent mappings in either dictionary.
            if ((ch_s in map_s and map_s[ch_s] != ch_t) or
                (ch_t in map_t and map_t[ch_t] != ch_s)):
                return False
            
            # Add or update the mappings in both dictionaries.
            map_s[ch_s] = ch_t
            map_t[ch_t] = ch_s
        
        # If no inconsistencies are found, the strings are isomorphic.
        return True
