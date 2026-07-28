class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        a = ord('a')
        d = [0] * 26

        for c in s[0:n // 2]:
            d[ord(c) - a] += 1
        
        string = ""
        for i in range(26):
            string += (chr(i + a) * d[i])
        
        if n % 2: return string + s[n // 2] + string[::-1]
        else: return string + string[::-1]
        