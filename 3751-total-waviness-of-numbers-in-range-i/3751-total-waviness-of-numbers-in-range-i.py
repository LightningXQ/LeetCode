class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 < 100: return 0

        num1 = max(num1, 100)
        result = 0
        for num in range(num1, num2 + 1):
            str_num = str(num)
            for n in range(1, len(str_num) - 1):
                prv, cur, nxt = str_num[n - 1:n + 2]
                if (cur > prv and cur > nxt) or (prv > cur and nxt > cur):
                    result += 1

        return result
