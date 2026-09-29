class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        cols, rows = len(grid[0]), len(grid)
        visit = set()
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            visit.add((i, j))
            q.append((i, j))

            while q:
                row, col = q.popleft()
                # right, down, up, left
                directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

                for di, dj in directions:
                    i, j = row + di, col + dj
                    if i in range(rows) and j in range(cols) and grid[i][j] == "1" and (i, j) not in visit:
                        q.append((i, j))
                        visit.add((i, j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    islands += 1
        return islands
