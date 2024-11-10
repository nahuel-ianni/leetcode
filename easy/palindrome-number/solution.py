# Solution for the 'Palindrome Number' problem.
# While reversing the original number is a straightforward solution, it can be less 
# performant than reversing half for large digit numbers.
#
# Time complexity: O(log(n)).
# Space complexity: O(1).

class Solution:
    mod = 10

    def isPalindrome(self, x: int) -> bool:
        reversed_half = 0
        
        # Early return for negative numbers and multiples of 10 (except zero).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10

        # Check if the number is equal to its reversed half (for even number of digits)
        # or if it's equal after ignoring the middle digit (odd number of digits).
        return x == reversed_half or x == reversed_half // 10
