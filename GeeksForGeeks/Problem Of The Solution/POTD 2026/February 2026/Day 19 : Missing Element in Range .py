class Solution:
    def missingRange(self, arr, low, high):
        # Convert array to set for fast lookup
        arr_set = set(arr)
        
        missing = []
        
        # Check each number in range
        for num in range(low, high + 1):
            if num not in arr_set:
                missing.append(num)
                
        return missing

