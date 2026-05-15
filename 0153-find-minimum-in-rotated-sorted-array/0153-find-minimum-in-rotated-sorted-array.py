class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, m, r = 0, (n - 1) // 2, n - 1

        while True:
            lv = nums[l]
            mv = nums[m]
            rv = nums[r]

            if lv == mv: return min(mv, rv)

            if mv < rv: r = m
            if rv < mv: l = m
            m = (l + r) // 2
