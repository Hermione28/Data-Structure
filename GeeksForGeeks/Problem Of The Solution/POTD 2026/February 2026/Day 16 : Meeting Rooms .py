class Solution:
    def canAttend(self, arr):
        # Sort meetings by start time
        arr.sort(key=lambda x: x[0])
        
        # Check for overlaps
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i-1][1]:
                return False
                
        return True

        
