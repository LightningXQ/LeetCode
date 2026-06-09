class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        mn, mx = 10 ** 9 + 1, -1
        for num in nums:
            if num < mn: mn = num
            if num > mx: mx = num
        return k * (mx - mn)