class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):

                # area 0 rhombus
                sums.add(grid[r][c])

                d = 1
                while (r-d >= 0 and r+d < m and c-d >= 0 and c+d < n):
                    total = 0

                    # top -> right
                    i, j = r-d, c
                    for k in range(d):
                        total += grid[i+k][j+k]

                    # right -> bottom
                    i, j = r, c+d
                    for k in range(d):
                        total += grid[i+k][j-k]

                    # bottom -> left
                    i, j = r+d, c
                    for k in range(d):
                        total += grid[i-k][j-k]

                    # left -> top
                    i, j = r, c-d
                    for k in range(d):
                        total += grid[i-k][j+k]

                    sums.add(total)
                    d += 1

        return sorted(sums, reverse=True)[:3]
