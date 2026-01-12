from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        result = []
        
        for i in range(len(arr)):
            # Remove elements outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements from the back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add maximum for current window
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result

