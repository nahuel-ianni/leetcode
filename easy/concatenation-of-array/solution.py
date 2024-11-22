# Solution for the 'Concatenation of Array' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Return the concatenated list by using list repetition.
        return nums * 2

        # Alternative implementation using list addition.
        # return nums + nums

        # Alternative implementation using itertools.chain().
        # Concatenates iterables lazily, avoiding creating intermediate lists during the process.
        # Converting the result back to a list requires materializing all the elements.
        # Useful when dealing with very large inputs or for creating iterables without immediate materialization.
        # return list(chain(nums, nums))
