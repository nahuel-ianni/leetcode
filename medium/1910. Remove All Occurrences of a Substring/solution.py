# Solution for the "Remove All Occurrences of a Substring" problem.
# Time complexity: O(n * 4^n)
# Space complexity: O(n * 4^n)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if s == part:
            return ""
        elif len(s) <= len(part):
            return s

        res = []
        chs = list(part)
        len_p = len(chs)

        for c in s:
            res.append(c)
            if res[-len_p:] == chs:
                del res[-len_p:]
        
        return "".join(res)