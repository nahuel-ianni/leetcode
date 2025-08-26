# Solution for the 'Valid Parentheses' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    matching_symbols = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.matching_symbols:
                # Check if the stack has an opening symbol and it matches the current closing symbol.
                if stack and stack[-1] == self.matching_symbols[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        # If the stack is empty, all symbols were matched; otherwise, they're unbalanced.
        return not stack
