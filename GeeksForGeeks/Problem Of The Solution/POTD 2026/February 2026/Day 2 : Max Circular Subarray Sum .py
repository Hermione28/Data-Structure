class Solution:
    def maxCircularSum(self, arr):
        total_sum = 0
        
        max_ending = min_ending = 0
        max_sum = -10**18
        min_sum = 10**18
        
        for x in arr:
            
            max_ending = max(x, max_ending + x)
            max_sum = max(max_sum, max_ending)
            
            
            min_ending = min(x, min_ending + x)
            min_sum = min(min_sum, min_ending)
            
            total_sum += x
        
       
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)

