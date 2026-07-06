class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        pivot = 0
        for i in range(1, n):
            prv, cur = nums[pivot], nums[i]
            if prv == cur: continue
            else:
                pivot += 1
                nums[pivot] = cur
            
        return pivot + 1
