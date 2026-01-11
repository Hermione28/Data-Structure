class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        min_len = float('inf')
        start_idx = -1
        
        i = 0
        while i < n:
            j = 0
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:
                        break
                i += 1
            
            if j < m:
                break
            
            end = i
            j = m - 1
            while i >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                    if j < 0:
                        break
                i -= 1
            
            start = i
            
            if end - start + 1 < min_len:
                min_len = end - start + 1
                start_idx = start
            
            i = start + 1
        
        return "" if start_idx == -1 else s1[start_idx:start_idx + min_len]

