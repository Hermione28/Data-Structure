class Solution:
    def kokoEat(self, arr, k):
        import math
        
        low, high = 1, max(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            hours = 0
            for bananas in arr:
                hours += math.ceil(bananas / mid)
            
            if hours <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

        
