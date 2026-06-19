class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxx = 0
        tmp = 0
        for a in gain:
            tmp += a
            if tmp > maxx: maxx = tmp
        return maxx
