class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n  # Initialize with n (end of array)
        
        # Find next smaller element for each index
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        
        # Count valid subarrays
        count = 0
        for i in range(n):
            count += (next_smaller[i] - i)
        
        return count
        
