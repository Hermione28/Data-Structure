class Solution:
    def maxSum(self, arr):
        n = len(arr)
        
        # Sum of array elements
        arrSum = sum(arr)
        
        # Initial value of i*arr[i]
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]
        
        maxVal = currVal
        
        # Compute subsequent values using rotation formula
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)
        
        return maxVal

