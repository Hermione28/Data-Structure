class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def canAchieve(target):
            temp = [0] * (n + 1)
            curr_add = 0
            operations = 0
            
            for i in range(n):
                curr_add += temp[i]
                current_height = arr[i] + curr_add
                
                if current_height < target:
                    need = target - current_height
                    operations += need
                    
                    if operations > k:
                        return False
                    
                    curr_add += need
                    if i + w < n:
                        temp[i + w] -= need
            
            return True
        
        low = min(arr)
        high = min(arr) + k
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            
            if canAchieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

        
