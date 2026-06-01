class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        n = len(cost)
        total_cost = 0

        cost.sort()

        for c in range(n - 1, -1, -3):
            if c > 1: total_cost += (cost[c] + cost[c - 1])
            if c == 1: total_cost += (cost[c] + cost[c - 1]); break
            if c == 0: total_cost += cost[c]; break
            if c == -1: break

        return total_cost
