/*
 * Solution for the 'First Unique Character in a String' problem.
 * Time complexity: O(n).
 * Space complexity: O(n).
 */
 
 public class Solution
{
    public int FirstUniqChar(string s)
    {
        var uniqueChar = s.GroupBy(c => c)
                          .Where(g => g.Count() == 1)
                          .Select(g => g.Key)
                          .FirstOrDefault();

        return uniqueChar != default(char) ? s.IndexOf(uniqueChar) : -1;
    }

    // Alternative implementation without LINQ.
    // public int FirstUniqChar(string s)
    // {
    //     var dictionary = new Dictionary<char, int>();
    //     foreach (var ch in s)
    //     {
    //         if (dictionary.ContainsKey(ch))
    //             dictionary[ch]++;

    //         else
    //             dictionary[ch] = 1;
    //     }

    //     for (var i = 0; i < s.Length; i++)
    //         if (dictionary[s[i]] == 1)
    //             return i;

    //     return -1;
    // }
}