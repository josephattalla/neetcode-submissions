class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # ADD FIRST LAYER TO QUEUE
        q = deque()
        q.append((0, 0))

        # GO THROUGH GRID LAYER BY LAYER, TRACKING # OF LAYERS, RETURNING WHEN @ BOTTOM RIGHT
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