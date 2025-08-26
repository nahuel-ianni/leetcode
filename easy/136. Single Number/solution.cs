/*
 * Solution for the 'Single Number' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */

public class Solution
{
    public int SingleNumber(int[] nums)
    {
        // Process:
        //   1. Initialize 'unique' to 0.
        //   2. Iterate through each number in 'nums'.
        //   3. XOR each number with 'unique'.
        //      - Paired numbers will cancel each other out to 0.
        //      - Only the unpaired number will remain in 'unique'.
        //   4. Return 'unique', the number that appears only once.
        var unique = 0;

        foreach (var number in nums)
            unique ^= number;

        return unique;
    }

    // Alternative implementation using LINQ:
    // More concise but introduces some overhead due to LINQ's iterator and lambda expression, 
    // which may impact performance for large inputs.
    // public int SingleNumber(int[] nums) =>
    //     nums.Aggregate(0, (x, y) => x ^ y);
}
