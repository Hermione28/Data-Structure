class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        
        # Step 1: Precompute Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = 1
        catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]
        
        # Step 2: Compute result for each root
        result = []
        
        for x in arr:
            left = sum(1 for num in arr if num < x)
            right = sum(1 for num in arr if num > x)
            
            result.append(catalan[left] * catalan[right])
        
        return result
