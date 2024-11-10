/*
 * Solution for the 'Palindrome Number' problem.
 * Time complexity: O(log(n)).
 * Space complexity: O(1).
 */

public class Solution
{
    public bool IsPalindrome(int number)
    {
        // Process:
        //     1. Handle negatives immediately (return false).
        //     2. Reverse digits and compare with the original number.
        if (number < 0)
            return false;

        var mod = 10;
        var reversedNumber = 0;
        var manipulatedNumber = number;
        
        while (manipulatedNumber != 0)
        {
            reversedNumber = (reversedNumber * mod) + (manipulatedNumber % mod);
            manipulatedNumber /= mod;
        }

        return number == reversedNumber;
    }
}
