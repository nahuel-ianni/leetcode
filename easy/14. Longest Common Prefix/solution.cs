/*
 * Solution for the 'Longest Common Prefix' problem.
 * Time complexity: O(m * n).
 * Space complexity: O(1).
 */
 
 public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0)
            return "";

        for (var i = 0; i < strs[0].Length; i++)
        {
            var ch = strs[0][i];

            foreach (var word in strs)
                if (i >= word.Length || ch != word[i])
                    return strs[0].Substring(0, i);
        }

        return strs[0];
    }
}