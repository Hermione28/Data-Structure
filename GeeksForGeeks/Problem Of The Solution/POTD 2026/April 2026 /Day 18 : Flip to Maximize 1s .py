class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)
        
        max_gain = 0
        current_gain = 0
        
        for num in arr:
            value = 1 if num == 0 else -1
            
            current_gain = max(value, current_gain + value)
            max_gain = max(max_gain, current_gain)
        
        return total_ones + max_gain
        
