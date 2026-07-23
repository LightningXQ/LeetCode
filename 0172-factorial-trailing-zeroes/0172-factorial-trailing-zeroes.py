class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        num = 5

        while True:
            if num > n: break
            zeros += n // num
            
            num *= 5

        return zeros
