class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        states = [0] * 26

        for c in word:
            c = ord(c)
            if 97 <= c <= 122:
                c -= 97
                if states[c] == 0: states[c] = 1
                if states[c] == 2: states[c] = 3
            if 65 <= c <= 90:
                c -= 65
                if states[c] == 0: states[c] = 3
                if states[c] == 1: states[c] = 2

        return states.count(2)