class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        n = len(nums)
        res = [0] * n
        groups = defaultdict(list)
        
        for i in range(n):
            groups[nums[i]].append(i)
        
        for indices in groups.values():
            prefix = 0
            total = sum(indices)
            size = len(indices)
            
            for i in range(size):
                idx = indices[i]
                
                left = idx * i - prefix
                right = (total - prefix - idx) - idx * (size - i - 1)
                
                res[idx] = left + right
                
                prefix += idx
        
        return res

        
