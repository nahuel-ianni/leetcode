# Solution for the 'Convert Date to Binary' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        vals = date.split('-')
        bin_vals = [format(int(d), 'b') for d in vals]
        return '-'.join(bin_vals)