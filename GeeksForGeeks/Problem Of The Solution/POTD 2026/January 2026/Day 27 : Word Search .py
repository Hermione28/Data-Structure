class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        def dfs(i, j, idx):
            # If full word is matched
            if idx == len(word):
                return True
            
            # Boundary and mismatch checks
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[idx]:
                return False
            
            # Mark cell as visited
            temp = mat[i][j]
            mat[i][j] = '#'
            
            # Explore all 4 directions
            found = (dfs(i+1, j, idx+1) or
                     dfs(i-1, j, idx+1) or
                     dfs(i, j+1, idx+1) or
                     dfs(i, j-1, idx+1))
            
            # Backtrack
            mat[i][j] = temp
            return found
        
        # Try starting DFS from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

