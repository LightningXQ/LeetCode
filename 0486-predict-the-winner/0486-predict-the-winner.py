class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0: return True

        @lru_cache
        def solve(l, r):
            if l == r: return nums[l]
            return max(nums[l] - solve(l + 1, r), nums[r] - solve(l, r - 1))
        
        return True if solve(0, n - 1) >= 0 else False