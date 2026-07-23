class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0

        for i in range(1, 6):
            zeros += n // (5 ** i)

        return zeros
