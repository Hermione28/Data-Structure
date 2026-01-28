
class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])

        # collect all points
        points = []
        for i in range(m):
            for j in range(n):
                points.append((i, j))

        # sort points by grid value
        points.sort(key=lambda p: grid[p[0]][p[1]])

        INF = 10**18
        costs = [[INF] * n for _ in range(m)]

        for _ in range(k + 1):
            # ---- teleport relaxation ----
            minCost = INF
            j = 0
            for i in range(len(points)):
                x, y = points[i]
                minCost = min(minCost, costs[x][y])

                if i + 1 < len(points) and \
                   grid[x][y] == grid[points[i + 1][0]][points[i + 1][1]]:
                    continue

                for r in range(j, i + 1):
                    rx, ry = points[r]
                    costs[rx][ry] = minCost
                j = i + 1

            # ---- normal moves (DP from bottom-right) ----
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i < m - 1:
                        costs[i][j] = min(
                            costs[i][j],
                            costs[i + 1][j] + grid[i + 1][j]
                        )
                    if j < n - 1:
                        costs[i][j] = min(
                            costs[i][j],
                            costs[i][j + 1] + grid[i][j + 1]
                        )

        return costs[0][0]
