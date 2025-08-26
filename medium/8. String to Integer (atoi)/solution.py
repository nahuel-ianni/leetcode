# Solution for the 'String to Integer (atoi)' problem.
# Time complexity: O(n)
# Space complexity: O(n) when using split(), O(1) with indexes

class Solution:
    MIN_INT = -2**31
    MAX_INT = 2**31 - 1


    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        mod = -1 if s[i] == '-' else 1
        if s[i] in '+-': 
            i += 1

        val = 0
        while i < len(s) and s[i].isdigit():
            val = val * 10 + int(s[i])
            i += 1

        val *= mod

        if val < Solution.MIN_INT: return Solution.MIN_INT
        if val > Solution.MAX_INT: return Solution.MAX_INT
        return val

    # def myAtoi(self, s: str) -> int:
    #     seq = s.lstrip()

    #     if not seq:
    #         return 0

    #     val = 0
    #     mod = 1 if seq[0] != '-' else -1
    #     seq = seq if seq[0] not in '+-' else seq[1:]

    #     for ch in seq:
    #         if not ch.isdigit():
    #             break
    #         val = val * 10 + int(ch)

    #     val *= mod

    #     if val < Solution.MIN_INT: return Solution.MIN_INT
    #     if val > Solution.MAX_INT: return Solution.MAX_INT
    #     return val
