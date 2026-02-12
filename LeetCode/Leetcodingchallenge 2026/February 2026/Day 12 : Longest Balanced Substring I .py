
class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        max_length = 0
        
        for i in range(n):
            freq = [0] * 26
            maxFreq = 0
            distinct = 0
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                
                if freq[idx] == 0:
                    distinct += 1
                    
                freq[idx] += 1
                maxFreq = max(maxFreq, freq[idx])
                
                length = j - i + 1
                
                # Check balanced condition
                if length == distinct * maxFreq:
                    max_length = max(max_length, length)
        
        return max_length
