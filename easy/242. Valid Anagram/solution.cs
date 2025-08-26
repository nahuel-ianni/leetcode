/*
 * Solution for the 'Valid Anagram' problem.
 * Time complexity: O(n), where n is the length of the strings.
 *     - Iterating through the strings takes O(n).
 *     - Dictionary operations (insert/update) are O(1) on average.
 * Space complexity: O(n), due to the dictionary used to store character counts.
 */

public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        // Step 1: Guard against strings with different lengths.
        if (s.Length != t.Length)
            return false;

        var dict = new Dictionary<char, int>();

        // Step 2: Iterate through both strings simultaneously.
        for (var i = 0; i < s.Length; i++)
        {
            // Increment the count for the character from string 's'.
            dict[s[i]] = dict.ContainsKey(s[i]) ? dict[s[i]] + 1 : 1;

            // Decrement the count for the character from string 't'.
            dict[t[i]] = dict.ContainsKey(t[i]) ? dict[t[i]] - 1 : -1;
        }

        // Step 3: Check if all character counts in the dictionary are zero.
        //         If any count is non-zero, the strings are not anagrams.
        return dict.Values.All(x => x == 0);
    }
}
