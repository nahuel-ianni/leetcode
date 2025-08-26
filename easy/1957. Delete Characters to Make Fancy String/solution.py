# Solution for the 'Delete characters to make fancy string' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                
            else:
                # Append one or two occurrences based on the count
                result.append(s[i] * min(count, 2))
                count = 1  # Reset count for the new character

        # Handle the last character(s)
        result.append(s[-1] * min(count, 2))

        return ''.join(result)
