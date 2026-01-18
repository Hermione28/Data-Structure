class Solution(object):
    def largestMagicSquare(self, grid):
        r, c = len(grid), len(grid[0])
        
        # Prefix sums
        row = [[0] * (c + 1) for _ in range(r)]
        col = [[0] * c for _ in range(r + 1)]
        diag = [[0] * (c + 1) for _ in range(r + 1)]
        anti = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(r):
            for j in range(c):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag[i + 1][j + 1] = diag[i][j] + grid[i][j]
                anti[i + 1][j] = anti[i][j + 1] + grid[i][j]
        
        # Try largest size first
        for size in range(min(r, c), 1, -1):
            for i in range(r - size + 1):
                for j in range(c - size + 1):
                    target = row[i][j + size] - row[i][j]
                    ok = True
                    
                    # Check rows
                    for x in range(i, i + size):
                        if row[x][j + size] - row[x][j] != target:
                            ok = False
                            break
                    
                    # Check columns
                    for y in range(j, j + size):
                        if col[i + size][y] - col[i][y] != target:
                            ok = False
                            break
                    
                    # Check diagonals
                    d1 = diag[i + size][j + size] - diag[i][j]
                    d2 = anti[i + size][j] - anti[i][j + size]
                    
                    if d1 != target or d2 != target:
                        ok = False
                    
                    if ok:
                        return size
        
        return 1
