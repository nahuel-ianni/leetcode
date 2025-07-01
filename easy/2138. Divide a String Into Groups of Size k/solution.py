# Solution for the 'Divide a String Into Groups of Size k' problem.
# Time complexity: O(n).
# Space complexity: O(m + n).

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []

        for i in range(0, len(s), k):
            groups.append(s[i:i+k].ljust(k, fill))

        return groups

    # def divideString(self, s: str, k: int, fill: str) -> List[str]:
    #     return [s[i:i+k].ljust(k, fill) for i in range(0, len(s), k)]
