class Solution:
    def maxChocolate(self, grid):
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

        def solve(i, j1, j2):
            # out of boundary
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return -10**9

            # last row
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]

            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            maxi = 0

            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]

                    value += solve(i + 1, j1 + dj1, j2 + dj2)
                    maxi = max(maxi, value)

            dp[i][j1][j2] = maxi
            return maxi

        return solve(0, 0, m - 1)
