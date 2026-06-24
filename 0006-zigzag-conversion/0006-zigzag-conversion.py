class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        n = len(s)
        pivot = 2 * (numRows - 1)
        result = list()

        for i in range(numRows):
            for p in range(0, n, pivot):
                if i == 0:
                    result.append(s[p])
                elif i == numRows - 1:
                    if p + pivot // 2 < n:
                        result.append(s[p + (pivot // 2)])
                else:
                    if p + i < n:
                        result.append(s[p + i])
                    if p + pivot - i < n:
                        result.append(s[p + pivot - i])


        return "".join(result)
