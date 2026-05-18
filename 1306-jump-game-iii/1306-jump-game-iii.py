class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        dump_arr = [[i for i in range(1000)] for j in range(1000)]


        n = len(arr)

        visited = set()
        curr = [start]

        while curr:
            nex = list()

            for node in curr:
                if arr[node] == 0: return True

                for child in [node - arr[node], node + arr[node]]:
                    if 0 <= child <= n - 1 and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curr = nex

        return False
