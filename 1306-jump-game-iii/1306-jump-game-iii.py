class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        # just stupid annotation
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
