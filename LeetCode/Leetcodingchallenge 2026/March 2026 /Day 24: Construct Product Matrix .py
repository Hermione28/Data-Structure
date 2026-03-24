class Solution(object):
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Step 1: Flatten grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Step 2: Prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # Step 3: Suffix product
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Step 4: Build result
        result = [[0]*m for _ in range(n)]
        
        for i in range(size):
            val = (prefix[i] * suffix[i]) % MOD
            r, c = divmod(i, m)
            result[r][c] = val
        
        return result
