# Solution for the 'Word Pattern' problem.
# Time complexity: O(n).
# Space complexity: O(2n) = O(n).

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Gets an array of words
        char_to_word = {}  # Maps pattern characters to words
        word_to_char = {}  # Maps words back to pattern characters
        
        if len(words) != len(pattern):
            return False

        for x, y in zip(pattern, s.split()):
            if ((x in char_to_word and char_to_word[x] != y)
                or (y in word_to_char and word_to_char[y] != x)
            ):
                return False
            
            char_to_word[x] = y
            word_to_char[y] = x

        return True


    # # Alternative function
    # # Time complexity: O(n)
    # # Space complecity: O(n)
    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     chars = {}      # Maps pattern characters to words
    #     words = set()   # Tracks words that have already been mapped
        
    #     for x, y in zip(pattern, s.split()):
    #         if x in chars:
    #             if chars[x] != y:
    #                 return False
    #         else:
    #             if y in words: # Word already mapped to another character
    #                 return False
    #             chars[x] = y
    #             words.add(y)

    #     return True
