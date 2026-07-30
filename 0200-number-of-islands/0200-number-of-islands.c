int numIslands(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = *gridColSize;

    void dfs(int i, int j) {
        if (0 <= i && i < m && 0 <= j && j < n && grid[i][j] == '1') {
            grid[i][j] = '0';
            dfs(i + 1, j);
            dfs(i, j + 1);
            dfs(i - 1, j);
            dfs(i, j - 1);
        }
    }

    int result = 0;
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            if (grid[x][y] == '1') {
                result += 1;
                dfs(x, y);
            }
        }
    }

    return result;
}
