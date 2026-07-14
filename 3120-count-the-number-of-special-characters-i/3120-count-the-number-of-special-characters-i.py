class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0

        for i in range(26):
            small, big = chr(i + 97), chr(i + 65)
            
            l = word.find(small)
            m = word.find(big)

            if l != -1 and m != -1: result += 1
        
        return result
