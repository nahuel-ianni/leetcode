# Solution for the 'Move zeroes' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num != 0:
                continue

            idx = i
            while idx < len(nums) - 1 and nums[idx] == 0:
                idx += 1
            
            nums[i] = nums[idx]
            nums[idx] = 0

    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     Time complexity is O(n^2)
    #     """
    #     i = 0
    #     l = len(nums)

    #     while(i < l):
    #         if(nums[i] == 0):
    #             nums.pop(i)
    #             nums.append(0)
    #             l -= 1

    #         else:
    #             i += 1
