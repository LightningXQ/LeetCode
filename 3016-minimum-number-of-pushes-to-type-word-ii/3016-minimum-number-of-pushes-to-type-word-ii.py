class Solution:
    def minimumPushes(self, word: str) -> int:
        d = [0] * 26

        for c in word:
            i = ord(c) - ord('a')
            d[i] += 1

        d.sort(key=lambda x: -x)

        s1 = sum(d[0:8])
        s2 = sum(d[8:16]) * 2
        s3 = sum(d[16:24]) * 3
        s4 = sum(d[24:]) * 4

        return s1 + s2 + s3 + s4
