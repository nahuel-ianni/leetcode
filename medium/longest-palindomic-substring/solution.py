# Solution for the 'Longest Palindromic Substring' problem.
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> tuple[int,int]:
            nonlocal start, stop

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left - 1 > stop - start:
                start, stop = left + 1, right

        start, stop = 0, 0
        for idx in range(len(s)):
            expand(idx, idx)
            expand(idx, idx + 1)
        
        return s[start:stop]
