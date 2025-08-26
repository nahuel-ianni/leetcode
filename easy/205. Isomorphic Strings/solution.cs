/*
 * Solution for the 'Isomorphic Strings' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    public bool IsIsomorphic(string s, string t)
    {
        // Process:
        //   1. Check if the lengths of the strings are different.
        //      If so, return false immediately.
        //   2. Use two dictionaries to map characters:
        //      - One to map characters from 's' to 't'.
        //      - Another to map characters from 't' to 's'.
        //   3. Iterate through both strings simultaneously.
        //      - Check if the mapping for a character in 's' is consistent with its corresponding character in 't'.
        //      - Similarly, check the reverse mapping from 't' to 's'.
        //      - If any inconsistency is found, return false.
        //   4. If all character mappings are consistent, return true.

        if (s.Length != t.Length)
            return false;

        // Create dictionaries to map characters from 's' to 't' and vice versa.
        var mapS = new Dictionary<char, char>();
        var mapT = new Dictionary<char, char>();

        // Iterate through the characters of both strings.
        for (var i = 0; i < s.Length; i++)
        {
            // Check for inconsistent mappings in both dictionaries.
            if ((mapS.ContainsKey(s[i]) && mapS[s[i]] != t[i]) ||
                (mapT.ContainsKey(t[i]) && mapT[t[i]] != s[i]))
                return false;

            // Add or update the mappings in both dictionaries.
            mapS[s[i]] = t[i];
            mapT[t[i]] = s[i];
        }

        // If no inconsistencies are found, the strings are isomorphic.
        return true;
    }
}
