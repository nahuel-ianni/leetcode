# Solution for the 'Check if Binary String Has at Most One Segment of Ones' problem.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not '01' in s
        