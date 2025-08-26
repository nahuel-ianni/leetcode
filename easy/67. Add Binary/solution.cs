/*
 * Solution for the 'Circular sentence' problem.
 * Time complexity: O(m + n).
 * Space complexity: O(m + n).
 */
 
 public class Solution
{
    public string AddBinary(string a, string b)
    {
        List<char> result = new List<char>();
        int carry = 0;
        int i = a.Length - 1;
        int j = b.Length - 1;

        while (i >= 0 || j >= 0 || carry > 0)
        {
            int bitA = (i >= 0) ? a[i] - '0' : 0; // Convert char to int
            int bitB = (j >= 0) ? b[j] - '0' : 0; // Convert char to int

            int total = bitA + bitB + carry;

            result.Add((total % 2).ToString()[0]); // Convert int to char

            carry = total / 2;

            i--;
            j--;
        }

        result.Reverse(); // Important: Reverse the list
        return new string(result.ToArray());
    }
}