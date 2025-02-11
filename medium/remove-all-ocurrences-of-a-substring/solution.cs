/*
 * Solution for the 'Remove All Occurrences of a Substring' problem.
 * Time complexity: O(n * m)
 * Space complexity: O(n)
 */

public class Solution
{
    public string RemoveOccurrences(string s, string part)
    {
        if (s.Equals(part))
            return string.Empty;
        else if (s.Length <= part.Length)
            return s;

        var sb = new StringBuilder(s.Length);

        for (int i = 0; i < s.Length; i++) {
            sb.Append(s[i]);
            if (s[i] == part[part.Length - 1] 
                && sb.Length >= part.Length
                && sb.ToString().EndsWith(part))
                    sb.Remove(sb.Length - part.Length, part.Length);
        }

        return sb.ToString();
    }
}