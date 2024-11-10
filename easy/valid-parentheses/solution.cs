/*
 * Solution for the 'Valid Parentheses' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */

public class Solution
{
    Dictionary<char, char> symbols = new Dictionary<char, char>
    { 
        { ')', '(' },
        { ']', '[' },
        { '}', '{' }
    };

    public bool IsValid(string s)
    {
        /// Process:
        ///    1. Guard against strings with an uneven number of characters.
        ///    2. Use a stack to match closing symbols with their corresponding opening symbols.
        if (s.Length % 2 != 0)
            return false;

        var stack = new Stack<char>();

        foreach (var character in s)
            if (symbols.ContainsKey(character))
            {
                // Check for unmatched closing symbol.
                if (stack.Count == 0 || symbols[character] != stack.Pop())
                    return false;
            }
            else
                stack.Push(character);

        return stack.Count == 0;
    }
}
