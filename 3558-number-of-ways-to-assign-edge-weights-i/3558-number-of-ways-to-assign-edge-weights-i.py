class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges)

        edges.sort(key=lambda x: min(x[0], x[1]))

        depths = [0] * (n + 2)
        max_depth = 0

        for i, j in edges:
            if i > j: i, j = j, i
            depths[j] = depths[i] + 1
            if depths[j] > max_depth: max_depth = depths[j]

        return pow(2, max_depth - 1, 10 ** 9 + 7)