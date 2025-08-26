# Solution for the 'Unique Morse Code Words' problem.
# Time complexity: O(n*k).
# Space complexity: O(n*k).

from typing import List

class Solution:
    MORSE_CODE = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
        "e": ".",  "f": "..-.", "g": "--.",  "h": "....",
        "i": "..", "j": ".---", "k": "-.-",  "l": ".-..",
        "m": "--", "n": "-.",   "o": "---",  "p": ".--.",
        "q": "--.-","r": ".-.", "s": "...",  "t": "-",
        "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--","z": "--.."
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniques = set()

        for word in words:
            code_parts = [Solution.MORSE_CODE[ch] for ch in word]
            uniques.add(''.join(code_parts))

        return len(uniques)
