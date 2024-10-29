public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var indexes = new int[2];
        var dictionary = new Dictionary<int, int>();

        for (var x = 0; x < nums.Length; x++)
        {
            var value = target - nums[x];

            if (dictionary.ContainsKey(value))
            {
                indexes = [dictionary[value], x];
                break;
            }

            dictionary.TryAdd(nums[x], x);
        }

        return indexes;
    }
}
