class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        q.append((0, 0))
        path = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row >= rows or col >= cols or min(row, col) < 0 or grid[row][col]:
                    continue
                if row == rows - 1 and col == cols - 1:
                    return path
                grid[row][col] = 1
                q.append((row+1,col))
                q.append((row-1,col))
                q.append((row,col+1))
                q.append((row,col-1))
            path += 1

        return -1 