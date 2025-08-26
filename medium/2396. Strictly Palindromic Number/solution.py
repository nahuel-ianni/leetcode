# Solution for the 'Strictly Palindromic Number' problem.
# Time complexity: O(1).
# Space complexity: O(1).

class Solution:
    # Consider the representation of n in base n - 2:
    #     n = 1 * (n - 2) ^ 1 + 2 * (n - 2) ^ 0
    # The number n in base (n - 2) is always 12, which is not palindromic.
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False