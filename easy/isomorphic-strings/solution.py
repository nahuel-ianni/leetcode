# Solution for the 'Isomorphic Strings' problem.
# Time complexity: O(n), where n is the length of the strings.
# Space complexity: O(n), due to the dictionaries and result lists.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Process:
        #   1. Check if the lengths of the strings are different.
        #   2. Define a helper function `encode` to transform each string.
        #      - Assign a unique identifier to each character based on its first occurrence.
        #      - Build a list of identifiers representing the string's structure.
        #   3. Compare the encoded forms of both strings.
        
        if len(s) != len(t):
            return False
        
        def encode(string):
            mapping = {}
            result = []
            
            # Iterate over the string.
            for i, char in enumerate(string):
                # If the character is not already in the mapping,
                # assign it a unique identifier (the current index).
                if char not in mapping:
                    mapping[char] = i
                
                # Append the identifier for the character to the result list.
                result.append(mapping[char])
            
            # Return the encoded list of identifiers.
            return result

        # Compare the encoded representations of both strings.
        return encode(s) == encode(t)
