# Solution for the 'Reverse String' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            aux = s[right]
            s[right] = s[left]
            s[left] = aux

            left += 1
            right -= 1