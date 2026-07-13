class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        states = [0] * 26

        for elm in range(26):
            small, large = chr(elm + 97), chr(elm + 65)

            for c in word:
                if c == small:
                    if states[elm] == 0: states[elm] = 1
                    if states[elm] == 2: states[elm] = 3
                if c == large:
                    if states[elm] == 0: states[elm] = 3
                    if states[elm] == 1: states[elm] = 2
        
        return states.count(2)
