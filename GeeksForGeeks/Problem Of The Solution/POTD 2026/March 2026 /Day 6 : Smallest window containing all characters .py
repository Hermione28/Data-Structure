
from collections import Counter

class Solution:
    def minWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        need = Counter(p)  
        have = {}
        
        required = len(need)  
        formed = 0            
        
        left = 0
        min_len = float("inf")
        start = 0
        
        for right, char in enumerate(s):
            have[char] = have.get(char, 0) + 1
            
            if char in need and have[char] == need[char]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        
        return "" if min_len == float("inf") else s[start:start + min_len]

        # code here
        
