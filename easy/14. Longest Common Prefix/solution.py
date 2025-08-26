# Solution for the 'Longest Common Prefix' problem.
# Time complexity: O(m * n).
# Space complexity: O(1).

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        # Iterate over each character of the first string
        for index in range(len(strs[0])):
            ch = strs[0][index]
            
            # Compare this character with corresponding characters in all other strings
            for s in strs[1:]:
                if index >= len(s) or s[index] != ch:
                    return strs[0][:index]
        
        # If all characters matched, return the whole first string
        return strs[0]
