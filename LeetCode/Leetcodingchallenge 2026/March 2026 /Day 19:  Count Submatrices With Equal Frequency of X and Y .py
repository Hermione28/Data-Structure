class Solution(object):
    def numberOfSubmatrices(self, grid):
        n, m = len(grid), len(grid[0])
        
        # prefix sum and count of X
        prefix = [[0]*m for _ in range(n)]
        countX = [[0]*m for _ in range(n)]
        
        def val(c):
            if c == 'X': return 1
            if c == 'Y': return -1
            return 0
        
        res = 0
        
        for i in range(n):
            for j in range(m):
                v = val(grid[i][j])
                
                prefix[i][j] = v
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                    countX[i][j] += countX[i-1][j]
                
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                    countX[i][j] += countX[i][j-1]
                
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
                
                # check conditions
                if prefix[i][j] == 0 and countX[i][j] > 0:
                    res += 1
        
        return res
