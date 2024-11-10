/*
 * Solution for the 'Circular sentence' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */
 
 public class Solution
{
    public bool IsCircularSentence(string sentence)
    {
        // Process:
        //     1. Check if the first and last characters match.
        //     2. Verify circular condition at each space, ensuring continuity.
        if (sentence[0] != sentence[sentence.Length - 1])
            return false;

        for (var x = 1; x < sentence.Length; x++)
        {
            if (sentence[x] == ' ' &&
                sentence[x - 1] != sentence[x + 1])
                    return false;
        }

        return true;
    }
}
