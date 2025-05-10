# Solution for the 'Remove Trailing Zeroes From a String' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
    
    # def removeTrailingZeros(self, num: str) -> str:
    #     count = 0

    #     for i in range(len(num) - 1, 0, -1):
    #         if num[i] != '0':
    #             break

    #         count += 1
        
    #     return num[:len(num) - count]