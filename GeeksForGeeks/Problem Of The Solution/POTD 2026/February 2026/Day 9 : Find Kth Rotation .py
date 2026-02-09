class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1
        
        while low < high:
            # If subarray is already sorted
            if arr[low] <= arr[high]:
                return low
            
            mid = (low + high) // 2
            
            # Minimum lies in right half
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                # Minimum lies in left half
                high = mid
        
        return low

