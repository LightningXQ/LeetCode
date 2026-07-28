class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        a = ord('a')
        d = [0] * 26

        for c in s[0:n // 2]:
            d[ord(c) - a] += 1

        parts = []
        for i in range(26):
            parts.append(chr(i + a) * d[i])

        half = "".join(parts)

        if n % 2:   return half + s[n // 2] + half[::-1]
        else:       return half + half[::-1]
