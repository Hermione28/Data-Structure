class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        if k > n:
            return False
        
        needed = 1 << k  
        seen = set()
        
        hash_val = 0
        mask = needed - 1
        
        for i in range(n):
            hash_val = ((hash_val << 1) & mask) | int(s[i])
            
            
            if i >= k - 1:
                seen.add(hash_val)
                if len(seen) == needed:
                    return True
        
        return False
