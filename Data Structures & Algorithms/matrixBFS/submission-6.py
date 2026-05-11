class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0)])

        directions = [(1,0), (0,1), (-1, 0), (0,-1)]

        visited = set()

        path = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)

                if node == (len(grid)-1, len(grid[0])-1):
                    return path

                for dx, dy in directions:
                    i = node[0] + dx
                    j = node[1] + dy

                    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] or (i,j) in visited:
                        continue

                    q.append((i,j)) 
            path += 1


        return -1