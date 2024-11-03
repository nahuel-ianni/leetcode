/**
 * This is my solution for the 'Rotate String' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 *
 * 1st check: Lengths must be the same if a rotation is to lead to equal strings.
 * 2nd check: By concatenating the string twice, goal should be within. This removes
 *            the need to iterate and exchange chars, reducing time complexity.
 */

public class Solution
{
    public bool RotateString(string s, string goal) =>
        s.Length == goal.Length && (s + s).Contains(goal);
}
