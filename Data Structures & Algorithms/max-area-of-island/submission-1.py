class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            len = 1
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                direction = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in direction:
                    r, c = dr+row, dc+col
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        len += 1
                        q.append((r, c))
                        visit.add((r, c))
            return len
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, bfs(r, c))
        return res