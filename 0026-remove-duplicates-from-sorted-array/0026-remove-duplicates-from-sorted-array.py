class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        pivot = 0
        for i in range(1, n):
            if nums[pivot] != nums[i]:
                pivot += 1
                nums[pivot] = nums[i]
            
        return pivot + 1
