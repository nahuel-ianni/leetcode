/*
 * Solution for the 'Longest Substring Without Repeating Characters' problem.
 * Time complexity: O(n), where n is the length of the string.
 * Space complexity: O(n), due to the HashSet used to store unique characters.
 */

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        // Step 1: Use a HashSet to store characters of the current substring.
        var set = new HashSet<char>();
        
        // Step 2: Initialize pointers for the sliding window and the maximum length.
        var left = 0; // Left pointer of the window
        var maxLength = 0; // Track the length of the longest substring

        // Step 3: Iterate through the string with the right pointer.
        for (var right = 0; right < s.Length; right++)
        {
            // If the character at the right pointer is already in the set,
            // slide the left pointer to shrink the window until it's not.
            while (set.Contains(s[right]))
            {
                set.Remove(s[left]); // Remove the leftmost character from the set
                left++; // Move the left pointer to the right
            }

            // Add the current character to the set.
            set.Add(s[right]);
            
            // Update the maximum length of the substring found so far.
            maxLength = Math.Max(maxLength, right - left + 1);
        }

        // Step 4: Return the maximum length.
        return maxLength;
    }
}
