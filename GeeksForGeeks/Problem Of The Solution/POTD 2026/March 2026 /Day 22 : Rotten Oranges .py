from collections import deque

class Solution:
    def orangesRot(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Initialize queue and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    queue.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        
        # If no fresh oranges
        if fresh == 0:
            return 0
        
        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS
        while queue:
            size = len(queue)
            infected = False
            
            for _ in range(size):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
                        infected = True
            
            if infected:
                time += 1
        
        # Step 3: Check if all are rotten
        return time if fresh == 0 else -1
