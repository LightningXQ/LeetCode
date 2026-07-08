class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # l = 0
        # r = n - 1
        # m = (l + r) // 2

        # while True:
        #     lv, mv, rv = nums[l], nums[m], nums[r]

        #     if lv == target: return l
        #     if mv == target: return m
        #     if rv == target: return r

        #     if lv > target or target > rv: return -1

        #     if lv < target < mv or mv < target < lv:
        #         l = l
        #         r = m
        #         m = (l + r) // 2
        #     elif mv < target < rv or rv < target < mv: 
        #         l = m
        #         r = r
        #         m = (l + r) // 2
        #     else:
        #         return -1

        for i, num in enumerate(nums):
            if num == target: return i
        else: return -1