class Solution(object):
    def canPartitionGrid(self, grid):
        total = 0
        
        # compute total sum
        for row in grid:
            for val in row:
                total += val
        
        for _ in range(4):
            exist = set()
            exist.add(0)
            sum_val = 0
            
            m = len(grid)
            n = len(grid[0])
            
            # if not enough rows
            if m < 2:
                grid = self.rotation(grid)
                continue
            
            # single column case
            if n == 1:
                for i in range(m - 1):
                    sum_val += grid[i][0]
                    tag = 2 * sum_val - total
                    
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                
                grid = self.rotation(grid)
                continue
            
            # general case
            for i in range(m - 1):
                for j in range(n):
                    exist.add(grid[i][j])
                    sum_val += grid[i][j]
                
                tag = 2 * sum_val - total
                
                # first row (edge handling)
                if i == 0:
                    if tag == 0 or tag == grid[0][0] or tag == grid[0][n - 1]:
                        return True
                    continue
                
                if tag in exist:
                    return True
            
            grid = self.rotation(grid)
        
        return False
    
    
    def rotation(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        tmp = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                tmp[j][m - 1 - i] = grid[i][j]
        
        return tmp
