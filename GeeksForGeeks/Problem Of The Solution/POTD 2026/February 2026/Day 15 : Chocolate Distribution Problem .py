class Solution:
    def findMinDiff(self, arr, M):
        # If students are more than packets
        if M > len(arr):
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize minimum difference
        min_diff = float('inf')
        
        # Step 3: Check all windows of size M
        for i in range(len(arr) - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff

