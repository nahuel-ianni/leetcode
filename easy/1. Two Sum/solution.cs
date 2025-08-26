/*
 * Solution for the 'Two Sum' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        /// Process:
        ///    1. Use dictionary to store each number's index.
        ///    2. Check if complement (target - nums[x]) is already in dictionary.
        var indexes = new int[2];
        var dictionary = new Dictionary<int, int>();

        for (var x = 0; x < nums.Length; x++)
        {
            var value = target - nums[x];

            if (dictionary.ContainsKey(value))
            {
                indexes = [dictionary[value], x];
                break;
            }

            dictionary.TryAdd(nums[x], x);
        }

        return indexes;
    }
}
