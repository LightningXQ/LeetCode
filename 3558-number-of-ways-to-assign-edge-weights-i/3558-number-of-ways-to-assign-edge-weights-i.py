class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges)
        graph = list(set() for _ in range(n + 2))
        visited = set()

        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        max_depth = 0
        def dfs(g, node, depth):
            visited.add(node)
            depth += 1
            children = g[node] - visited
            for x in children:
                nonlocal max_depth
                max_depth = max(max_depth, depth)
                dfs(g, x, depth)
            depth -= 1

        dfs(graph, 1, 0)

        return pow(2, max_depth - 1, 10 ** 9 + 7)
