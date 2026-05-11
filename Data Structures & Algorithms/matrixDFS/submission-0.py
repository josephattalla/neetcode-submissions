class Solution:
    def dfs(self, grid, row, col, visited):
        # GET ROWS & COLS
        rows = len(grid)
        cols = len(grid[0])

        # 0 BASE CASE: OUT OF BOUNDS, ALREADY VISITED, BLOCKED POSITION
        if row == rows or col == cols or min(row, col) < 0 or (row, col) in visited or grid[row][col]:
            return 0
        # 1 BASE CASE: AT BOTTOM-RIGHT CORNER
        if row == rows - 1 and col == cols - 1:
            return 1
        
        # ADD CURRENT VERTEX TO VISITED
        visited[(row, col)] = 1

        # RECURSIVE CASE: COUNT = COUNT FROM NEIGHBORS
        count = 0
        count += self.dfs(grid, row + 1, col, visited)
        count += self.dfs(grid, row - 1, col, visited)
        count += self.dfs(grid, row, col + 1, visited)
        count += self.dfs(grid, row, col - 1, visited)

        # REMOVE CURRENT POSITION FROM VISITED SO OTHER PATHS CAN USE IT
        del visited[(row, col)]

        return count


    def countPaths(self, grid: List[List[int]]) -> int:
        visited = {}
        return self.dfs(grid, 0, 0, visited)