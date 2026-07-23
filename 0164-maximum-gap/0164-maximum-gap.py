class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        nums.sort()
        max_gap = 0

        for i in range(n - 1):
            diff = nums[i + 1] - nums[i]
            if max_gap < diff: max_gap = diff
        
        return max_gap