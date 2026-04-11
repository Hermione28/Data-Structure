class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        index_map = defaultdict(list)
        
        
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        ans = float('inf')
        
       
        for indices in index_map.values():
            if len(indices) < 3:
                continue
            
            
            for i in range(len(indices) - 2):
                p = indices[i]
                r = indices[i + 2]
                
                distance = 2 * (r - p)
                ans = min(ans, distance)
        
        return ans if ans != float('inf') else -1
