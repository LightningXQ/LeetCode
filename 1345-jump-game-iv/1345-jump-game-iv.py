class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)

        graph = dict()

        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curr = [0]
        visited = {0}
        step = 0

        while curr:
            nex = list()

            for node in curr:
                if node == n - 1: return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr[node]].clear()

                if node > 0 and node - 1 not in visited:
                    visited.add(node - 1)
                    nex.append(node - 1)

                if node < n - 1 and node + 1 not in visited:
                    visited.add(node + 1)
                    nex.append(node + 1)

            curr = nex
            step += 1

        return step
