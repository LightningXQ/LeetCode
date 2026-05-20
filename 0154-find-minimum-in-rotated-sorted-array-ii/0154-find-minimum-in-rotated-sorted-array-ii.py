class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        for num in nums:
            if result > num:
                result = num
        return result