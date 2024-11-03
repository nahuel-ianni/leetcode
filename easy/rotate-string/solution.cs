/**
 * This is my solution for the 'Rotate String' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    public bool RotateString(string s, string goal)
    {
        // If the lengths are different, then they can't reach the desired goal.
        if (s.Length != goal.Length)
            return false;

        // To reduce time complexity, check if goal is within 2 's' in a row,
        // removing the need to iterate and exchange chars.
        var doubled = s + s;
        return doubled.Contains(goal);
    }
}
