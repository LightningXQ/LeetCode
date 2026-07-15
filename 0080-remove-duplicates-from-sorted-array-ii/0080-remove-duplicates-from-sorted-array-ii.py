class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        curr = prev = pprv = 10 ** 4 + 1
        p = 0

        for i in range(n):
            pprv = prev
            prev = curr
            curr = nums[i]

            if not curr == prev == pprv: 
                nums[p] = curr
                p += 1
        
        return p
