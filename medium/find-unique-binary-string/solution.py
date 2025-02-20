# Solution for the "Find Unique Binary String" problem.
# Solution implements "Cantor's Diagonalization" method.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(
            "0" if nums[i][i] == "1" else "1" 
            for i in range(len(nums))
        )
