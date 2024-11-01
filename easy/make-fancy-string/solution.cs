/// This is my solution for the 'Delete characters to make fancy string' problem.
/// Time complexity: O(n).
/// Space complexity: O(n).

public class Solution
{
    public string MakeFancyString(string s)
    {
        // Guard against empty or null strings.
        if (string.IsNullOrEmpty(s))
            return s;

        var count = 1;
        var lastChar = default(char);

        // StringBuilder more performant when concatenating over 10 strings, 
        // and can be noticeable already between 5 and 10. With a string's length
        // of 10^5, performance is lowered to O(n) from O(n^2) with concatenation.
        var builder = new StringBuilder();
        
        foreach (char c in s)
        {
            if (c == lastChar)
            {
                count++;

                if (count > 2)
                    continue;
            }
            else
                count = 1;

            lastChar = c;
            builder.Append(c);
        }

        return builder.ToString();
    }
}
