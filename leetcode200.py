class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, rowL, colL = 0, len(grid), len(grid[0])

        def mark(r, c):
            if r in range(rowL) and c in range(colL) and grid[r][c] == "1":
                grid[r][c] = "-1"
                mark(r, c + 1)
                mark(r, c - 1)
                mark(r + 1, c)
                mark(r - 1, c)

        for i in range(rowL):
            for j in range(colL):
                if grid[i][j] == "1":
                    mark(i, j)
                    res += 1
        return res