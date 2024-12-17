# Solution for the "Letter Combinations of a Phone Number" problem.
# Time complexity: O(n * 4^n)
# Space complexity: O(n * 4^n)

from itertools import product

class Solution:
    digit_map = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        chars = [self.digit_map[digit] for digit in digits]
        return [''.join(combination) for combination in product(*chars)]