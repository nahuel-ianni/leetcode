/*
 * Solution for the 'Length of Last Word' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 * 
 * Alternative (space complexity: O(n)):
 *     public int LengthOfLastWord(string s) => s.Trim().Split(' ').Last().Length;
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
