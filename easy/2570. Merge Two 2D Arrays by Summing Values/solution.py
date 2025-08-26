# Solution for the 'Merge two 2D arrays by summing values' problem.
# Time complexity: O(n log n).
# Space complexity: O(n).

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        res = dict(nums1)
    
        for k, v in nums2:
            res[k] = res.get(k, 0) + v
    
        return sorted(res.items())
