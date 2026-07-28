class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        a = ord('a')
        d = [0] * 26
        for c in s:
            d[ord(c) - a] += 1
        
        string = ""
        odd = -1
        for e in range(26):
            i = d[e]
            if i % 2: odd = e
            string += (chr(e + a) * (i // 2))
        
        if odd == -1: return string + string[::-1]
        else: return string + chr(odd + a) + string[::-1]

        

        