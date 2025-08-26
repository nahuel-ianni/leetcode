# Solution for the "Reverse Integer" problem.
# Time complexity: O(log(n))
# Space complexity: O(1)

class Solution:
    MAX = 2**31 - 1
    MIN = -2**31

    def reverse(self, x: int) -> int:
        revx = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            x, mod = divmod(x, 10)
            if revx > (self.MAX - mod) // 10:
                return 0

            revx = revx * 10 + mod
        
        return revx * sign

    # def reverse(self, x: int) -> int:
        # r = reversed(str(abs(x)))
        # r = int(''.join(r) if x > 0 else '-' + ''.join(r))
        # return r if self.MIN <= r <= self.MAX else 0
