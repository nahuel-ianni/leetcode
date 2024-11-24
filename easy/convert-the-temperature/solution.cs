/*
 * Solution for the 'Convert the Temperature' problem.
 * Time complexity: O(1).
 * Space complexity: O(1).
 */
 
public class Solution
{
    public double[] ConvertTemperature(double celsius) =>
        [
            celsius + 273.15,
            celsius * 1.8 + 32
        ];   
}
