# Solution for the 'Move zeroes' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != last_non_zero:
                    nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]

                last_non_zero += 1

    
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     Same complexities but more irrelevant exchanges.
    #     """
    #     for i, num in enumerate(nums):
    #         if num != 0:
    #             continue

    #         idx = i
    #         while idx < len(nums) - 1 and nums[idx] == 0:
    #             idx += 1
    #       
    #         nums[i] = nums[idx]
    #         nums[idx] = 0

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
