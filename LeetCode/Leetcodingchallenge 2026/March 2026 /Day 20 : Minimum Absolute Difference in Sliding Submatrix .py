class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = set()
                
                # collect k x k elements (unique)
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                
                # convert to sorted list
                vals = sorted(vals)
                
                # if only one distinct value
                if len(vals) == 1:
                    ans[i][j] = 0
                    continue
                
                # find min absolute difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                ans[i][j] = min_diff
        
        return ans
