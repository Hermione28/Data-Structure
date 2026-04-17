class Solution(object):
    def minMirrorPairDistance(self, nums):
        seen = {}
        ans = float('inf')
        
        for i, num in enumerate(nums):
            # If current number already seen as reverse before
            if num in seen:
                ans = min(ans, i - seen[num])
            
            # Store reverse of current number
            rev = int(str(num)[::-1])
            seen[rev] = i
        
        return ans if ans != float('inf') else -1
