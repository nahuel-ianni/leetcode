/**
 * This is my solution for the 'Length of Last Word' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 * 
 * A simpler [to write] solution can be done with the following one-liner, however
 * its space complexity increases to O(n) due to Split creating a new array.
 * Trim can potentially create a new string if the original one contains whitespaces. 
 *
 * public int LengthOfLastWord(string s) => s.Trim().Split(' ').Last().Length;
 */
public class Solution
{
    public int LengthOfLastWord(string s)
    {
        var index = s.Length - 1;

        // Calculate index of the last non-whitespace character.
        while (index >= 0 && s[index] == ' ')
        {
            index--;
        }

        var length = 0;

        // Count all characters starting from the index of the last character 
        // to the first whitespace (or beginning of string).
        while (index >= 0 && s[index] != ' ')
        {
            index--;
            length++;
        }

        return length;
    }
}
