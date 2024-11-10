/*
 * Solution for the 'Rotate String' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    public bool RotateString(string s, string goal) =>
        /// Process:
        ///    1. Ensure both strings have the same length.
        ///    2. Check if goal is a substring within a double concatenation of s.
        ///       This removes the need to iterate and exchange chars, reducing time complexity.
        s.Length == goal.Length && (s + s).Contains(goal);
}
