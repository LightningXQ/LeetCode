class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp1 = dp2 = dp3 = 0

        for i in range(n - 1, -1, -1):
            current_sum = 0
            best = float('-inf')
            for k in range(1, 4):
                if i + k > n: break
                current_sum += stoneValue[i + k - 1]
                best = max(best, current_sum - [dp1, dp2, dp3][k - 1])
            dp1, dp2, dp3 = best, dp1, dp2

        if dp1 > 0: return "Alice"
        elif dp1 == 0: return "Tie"
        else: return "Bob"


