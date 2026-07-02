from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        dq = deque()
        dq.append((0, 0))

        while dq:
            x, y = dq.popleft()
            # up, down, left, right node from current node
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_dist = dist[x][y] + grid[nx][ny]
                    if dist[nx][ny] > new_dist:
                        dist[nx][ny] = new_dist
                        if dist[nx][ny] == 1:
                            dq.append((nx, ny))
                        else:
                            dq.appendleft((nx, ny))

        return bool(dist[-1][-1] < health)
