/**
 * This is my solution for the 'Circular sentence' problem.
 * Time complexity: O(n).
 * Space complexity: O(1).
 */
 
 public class Solution
{
    public bool IsCircularSentence(string sentence)
    {
        // Check the first and last characters of the sentence.
        if (sentence[0] != sentence[sentence.Length - 1])
            return false;

        for (var x = 1; x < sentence.Length; x++)
        {
            // Check the circular condition between words at every space.
            if (sentence[x] == ' ' &&
                sentence[x - 1] != sentence[x + 1])
                    return false;
        }

        return true;
    }
}
