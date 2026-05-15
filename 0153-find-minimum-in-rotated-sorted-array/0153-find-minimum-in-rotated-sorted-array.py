class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, m, r = 0, (n - 1) // 2, n - 1
        
        while True:
            lv = nums[l]
            mv = nums[m]
            rv = nums[r]
            
            if lv < mv < rv:
                r = m
                m = (l + r) // 2
            if mv < rv < lv:
                r = m
                m = (l + r) // 2
            if rv < lv < mv:
                l = m
                m = (l + r) // 2

            if lv == mv: return min(mv, rv)