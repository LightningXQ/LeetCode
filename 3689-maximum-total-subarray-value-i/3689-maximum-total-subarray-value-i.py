class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        mn, mx = min(nums), max(nums)
        return k * (mx - mn)