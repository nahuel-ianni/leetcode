# Solution for the 'Reverse Vowels of a String' problem.
# Time complexity: O(n).
# Space complexity: O(n).

class Solution:
    vowels = set('aeiouAEIOU')

    def is_vowel(self, ch: str) -> bool:
        return ch in self.vowels

    def reverseVowels(self, s: str) -> str:
        result = list(s)
        i, x = 0, len(s) - 1
        
        while i < x:
            while i < x and not self.is_vowel(result[i]):
                i += 1
            while i < x and not self.is_vowel(result[x]):
                x -= 1
                
            result[i], result[x] = result[x], result[i]
            i += 1
            x -= 1
        
        return ''.join(result)
