# Solution for the 'Single Number' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Process:
        #   1. Initialize 'unique' to 0.
        #   2. Iterate through each number in 'nums'.
        #   3. XOR each number with 'unique'. 
        #      - Paired numbers cancel each other to 0.
        #      - Only the unique, unpaired number remains.
        #   4. Return 'unique', the number that appears only once.
        unique = 0
        
        for num in nums:
            unique ^= num
        
        return unique
