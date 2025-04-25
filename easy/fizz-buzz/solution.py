# Solution for the 'Fizz Buzz' problem.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        vals = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                vals.append('FizzBuzz')
            elif i % 3 == 0:
                vals.append('Fizz')
            elif i % 5 == 0:
                vals.append('Buzz')
            else:
                vals.append(str(i))

        return vals