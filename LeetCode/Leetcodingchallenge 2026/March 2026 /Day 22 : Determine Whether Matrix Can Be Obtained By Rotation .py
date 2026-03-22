class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)
        
        # Function to rotate matrix 90° clockwise
        def rotate(matrix):
            # Transpose
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Reverse each row
            for i in range(n):
                matrix[i].reverse()
        
        # Try all 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False
