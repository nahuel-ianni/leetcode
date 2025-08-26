/*
 * Solution for the 'Concatenation of Array' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    public int[] GetConcatenation(int[] nums)
    {
        /// Process:
        ///     1. Create a new array, `array`, with double the size of `nums`.
        ///     2. Use a loop to populate the first half of `array` with elements from `nums`.
        ///     3. Populate the second half of `array` by reusing elements from `nums`.
        ///     4. Return the resulting `array`.
        
        var array = new int[nums.Length * 2];

        for (var index = 0; index < nums.Length; index++)
        {
            array[index] = nums[index];
            array[index + nums.Length] = nums[index];
        }

        return array;
    }

    // Alternative implementation using LINQ:
    // More concise but introduces some overhead due to LINQ's abstraction.
    // public int[] GetConcatenation(int[] nums) => 
    //     nums.Concat(nums).ToArray<int>();
}
