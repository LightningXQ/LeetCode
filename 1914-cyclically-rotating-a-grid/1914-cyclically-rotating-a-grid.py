class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        n_layers = min(m, n) // 2

        layers = [list() for _ in range(n_layers)]

        # linearize grid
        for j in range(n_layers):
            for i in range(j, n - 1 - j):
                layers[j].append(grid[j][i])
            for i in range(j, m - 1 - j):
                layers[j].append(grid[i][n - 1 - j])
            for i in range(n - 1 - j, j, -1):
                layers[j].append(grid[m - 1 - j][i])
            for i in range(m - 1 - j, j, -1):
                layers[j].append(grid[i][j])
        
        # rotate
        for l in layers:
            for _ in range(k % len(l)):
                l.append(l.pop(0))

        # restore grid
        for j in range(n_layers):
            l = iter(layers[j])
            for i in range(j, n - 1 - j):
                grid[j][i] = next(l)
            for i in range(j, m - 1 - j):
                grid[i][n - 1 - j] = next(l)
            for i in range(n - 1 - j, j, -1):
                grid[m - 1 - j][i] = next(l)
            for i in range(m - 1 - j, j, -1):
                grid[i][j] = next(l)

        return grid
            
