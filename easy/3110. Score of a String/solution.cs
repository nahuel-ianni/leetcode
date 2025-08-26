/*
 * Solution for the 'Score of a String' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */

public class Solution
{
    public int ScoreOfString(string s)
    {
        /// Process:
        ///     1. Iterate through each character in 's' (up to the second-last).
        ///     2. Subtract ASCII values of adjacent characters, take the absolute difference.
        ///     3. Sum these absolute differences and return the result.
        var output = 0;

        for (var i = 0; i < s.Length - 1; i++)
            output += Math.Abs(s[i] - s[i + 1]);

        return output;    
    }

    // Alternative implementation using LINQ:
    // More concise but introduces some overhead due to LINQ's iterator and lambda expression, 
    // which may impact performance for large inputs.
    // public int ScoreOfString(string s) =>
    //     Enumerable.Range(0, s.Length - 1)
    //               .Sum(i => Math.Abs(s[i] - s[i + 1]));
}
