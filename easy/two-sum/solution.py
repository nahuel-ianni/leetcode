# This is my solution for the 'Two Sum' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for index, number in enumerate(nums):
            value = target - number

            if value in dictionary:
                return [dictionary[value], index]
            
            dictionary[number] = index

        return []
