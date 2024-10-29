public class Solution {
    Dictionary<char, char> symbols = new Dictionary<char, char>
    { 
        { ')', '(' },
        { ']', '[' },
        { '}', '{' }
    };

    public bool IsValid(string s) {
        // Guard against strings with uneven number of characters.
        if (s.Length % 2 != 0)
            return false;

        var stack = new Stack<char>();

        foreach (var character in s)
            if (symbols.ContainsKey(character))
            {
                // When the character is a closing symbol, the stack needs to have at least one value -- the opening symbol.
                if (stack.Count == 0 || symbols[character] != stack.Pop())
                    return false;
            }
            else
                stack.Push(character);

        return stack.Count == 0;
    }
}
