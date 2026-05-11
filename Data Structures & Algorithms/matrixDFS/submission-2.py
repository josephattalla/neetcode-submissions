class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        paths = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            nonlocal paths
            if (i, j) in visited or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]:
                return

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                paths += 1
                return

            visited.add((i,j))
            for dx, dy in directions:
                dfs(i+dx, j+dy)
            visited.remove((i,j))

        dfs(0,0)

        return paths