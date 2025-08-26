# Solution for the 'Score of a String' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Process:
        #   1. Iterate through each character in 's' up to the second-last.
        #   2. Calculate the absolute difference in ASCII values between each character and its adjacent.
        #   3. Accumulate these differences and return the total score.
        output = 0
        
        for i in range(0, len(s) - 1):
            output += abs(ord(s[i]) - ord(s[i + 1]))

        return output

    # Alternative implementation using sum with a generator expression:
    # Slightly less efficient for large inputs but more concise.
    # def scoreOfString(self, s: str) -> int:
    #     return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
