class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        result = 0
        for c in costs:
            if c <= coins:
                result += 1
                coins -= c
            else: break
        return result
