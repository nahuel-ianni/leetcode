/*
 * Solution for the 'Reverse String' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */

public class Solution
{
    public void ReverseString(char[] s)
    {
        var left = 0;
        var right = s.Length - 1;

        while (left < right)
        {
            var aux = s[right];
            s[right] = s[left];
            s[left] = aux;

            left++;
            right--;
        }
    }
}