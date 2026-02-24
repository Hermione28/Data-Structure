class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        diff_index = {}   # stores first occurrence of diff
        diff = 0
        max_len = 0
        
        for i in range(n):
            diff += a1[i] - a2[i]
            
            # If diff is 0, span from 0 to i has equal sum
            if diff == 0:
                max_len = i + 1
            
            # If diff seen before, span between previous index+1 to i
            if diff in diff_index:
                max_len = max(max_len, i - diff_index[diff])
            else:
                diff_index[diff] = i
        
        return max_len
        
