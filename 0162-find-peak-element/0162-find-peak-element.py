class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n - 2):
            prv, cur, nxt = nums[i:i + 3]
            if prv < cur > nxt: return i + 1
        
        return nums.index(max(nums))
