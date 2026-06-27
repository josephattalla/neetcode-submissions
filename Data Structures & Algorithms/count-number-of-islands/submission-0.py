class Solution:
    def dfs(self, i, j, grid, rows, cols):

        # base case
        if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] != "1":
            return False

        grid[i][j] = "0"
        self.dfs(i+1, j, grid, rows, cols)
        self.dfs(i, j+1, grid, rows, cols)
        self.dfs(i-1, j, grid, rows, cols)
        self.dfs(i, j-1, grid, rows, cols)

        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num += self.dfs(i, j, grid, rows, cols)

        return num