/*
 * Solution for the 'Letter Combinations of a Phone Number' problem.
 * Time complexity: O(n * 4^n), where n is the length of the digits string.
 *     This is due to generating all combinations (which grows exponentially as 4^n in the worst case) 
 *     and appending each letter combination (which takes O(n) time).
 * Space complexity: O(4^n), due to the space required to store the resulting list of strings,
 *     where there are 4^n combinations, and each string has a length of n.
 */

public class Solution
{
    Dictionary<char, List<string>> digit_table = 
        new Dictionary<char, List<string>> 
        {
            ['2'] = new List<string> { "a", "b", "c" },
            ['3'] = new List<string> { "d", "e", "f" },
            ['4'] = new List<string> { "g", "h", "i" },
            ['5'] = new List<string> { "j", "k", "l" },
            ['6'] = new List<string> { "m", "n", "o" },
            ['7'] = new List<string> { "p", "q", "r", "s" },
            ['8'] = new List<string> { "t", "u", "v" },
            ['9'] = new List<string> { "w", "x", "y", "z" }
        };

    public IList<string> LetterCombinations(string digits)
    {
        var result = new List<string>();

        if (string.IsNullOrEmpty(digits))
            return result;

        result.Add("");

        foreach (var digit in digits)
        {
            var letters = digit_table[digit];
            var temp = new List<string>();

            foreach (var combination in result)
                foreach (var letter in letters)
                    temp.Add(combination + letter);

            result = temp;
        }

        return result;
    }
}