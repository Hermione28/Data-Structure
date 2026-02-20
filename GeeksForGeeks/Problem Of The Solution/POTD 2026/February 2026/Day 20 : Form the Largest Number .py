class Solution:
    def findLargest(self, arr):
        # Convert integers to strings
        arr = list(map(str, arr))
        
        # Custom comparator using sort key
        arr.sort(key=lambda x: x*10, reverse=True)
        
        # Edge case: if highest is "0", result is "0"
        if arr[0] == "0":
            return "0"
        
        # Join all numbers
        return ''.join(arr)
	    
