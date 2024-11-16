/*
 * Solution for the 'Find the Index of the First Occurrence in a String' problem.
 * Time complexity: O(n * m), where n = haystack.Length and m = needle.Length.
 * Space complexity: O(m) due to slicing operations.
 */

public class Solution
{
    public int StrStr(string haystack, string needle)
    {
        // Iterate through the haystack up to the point where needle can fit
        for (var i = 0; i <= haystack.Length - needle.Length; i++)
        {
            // Use slicing to compare substring with needle
            if (haystack[i..(i + needle.Length)] == needle)
                return i;
        }

        // If no match is found, return -1
        return -1;
    }
}
