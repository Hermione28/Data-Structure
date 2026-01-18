class Solution:
    def nextFreqGreater(self, arr):
        from collections import Counter
        
        freq = Counter(arr)
        n = len(arr)
        result = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            
            stack.append(arr[i])
        
        return result

        
