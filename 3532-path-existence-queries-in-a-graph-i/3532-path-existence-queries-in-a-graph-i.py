class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        g = [0] * n

        for i in range(1, n):
            g[i] = g[i - 1] + (nums[i] - nums[i - 1] > maxDiff)
        
        return [g[i] == g[j] for i, j in queries]
        
