from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def travel(pos: int , sign: int) -> int:
            if pos + 2 < n:
                one = sum(stoneValue[pos:pos + 1]) * sign + travel(pos + 1, sign * -1)
                two = sum(stoneValue[pos:pos + 2]) * sign + travel(pos + 2, sign * -1)
                three = sum(stoneValue[pos:pos + 3]) * sign + travel(pos + 3, sign * -1)
                if sign == 1: return max(one, two, three)
                else: return min(one, two, three)
            elif pos + 1 < n:
                one = sum(stoneValue[pos:pos + 1]) * sign + travel(pos + 1, sign * -1)
                two = sum(stoneValue[pos:pos + 2]) * sign + travel(pos + 2, sign * -1)
                if sign == 1: return max(one, two)
                else: return min(one, two)
            elif pos < n:
                return sum(stoneValue[pos:pos + 1]) * sign
            else: return 0

        result = travel(0, 1)

        if result > 0: return "Alice"
        elif result == 0: return "Tie"
        elif result < 1: return "Bob"
