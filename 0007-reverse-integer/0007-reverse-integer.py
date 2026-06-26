class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        sign = 1
        if x < 0: x = -x; sign = -1
        ans = int(''.join(x.__str__()[::-1])) * sign
        return ans if  -(2 ** 31) + 1 < ans < 2 ** 31 - 1 else 0
