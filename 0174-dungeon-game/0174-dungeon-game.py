class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            min_next = min(dp(i + 1, j), dp(i, j + 1))

            return max(1, min_next - dungeon[i][j])

        return dp(0, 0)
