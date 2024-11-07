# Solution for the 'Score of a String' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Process:
        #   1. Iterate through each character in 's' (up to the second-last).
        #   2. Subtract ASCII values of adjacent characters, take the absolute difference.
        #   3. Sum these absolute differences and return the result.
        return sum(abs(ord(s[x]) - ord(s[x + 1])) for x in range(len(s) - 1))
