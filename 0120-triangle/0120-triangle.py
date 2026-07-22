class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            tmp = list()
            for j in range(len(triangle[i])):
                tmp.append(triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1]))
            triangle[i] = tmp
        
        return triangle[0][0]