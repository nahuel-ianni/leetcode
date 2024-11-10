/*
 * Solution for the 'Valid Palindrome' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */

public class Solution
{
    public bool IsPalindrome(string s)
    {
        var left = 0;
        var right = s.Length - 1;

        // Process:
        //   1. Use a two-pointer approach to scan the string from both ends.
        //   2. Skip any non-alphanumeric characters by adjusting 'left' and 'right' pointers.
        //   3. Compare characters from both ends, ensuring case insensitivity.
        while (left < right)
        {
            // Move 'left' pointer to the next alphanumeric character.
            while (left < right && !Char.IsLetterOrDigit(s[left]))
            {
                left += 1;
            }

            // Move 'right' pointer to the previous alphanumeric character.
            while (left < right && !Char.IsLetterOrDigit(s[right]))
            {
                right -= 1;
            }

            if (Char.ToLower(s[left]) != Char.ToLower(s[right]))
                return false;

            left += 1;
            right -= 1;
        }

        return true; 
    }
}
