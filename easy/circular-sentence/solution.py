# This is my solution for the 'Circular Sentence' problem.
# Time complexity: O(n).
# Space complexity: O(1).

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        # Only check characters after each space
        for index in range(1, len(sentence) - 1):
            if sentence[index] == ' ' and sentence[index - 1] != sentence[index + 1]:
                return False

        return True
