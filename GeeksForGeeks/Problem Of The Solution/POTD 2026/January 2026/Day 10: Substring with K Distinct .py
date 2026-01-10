class Solution:
    def countSubstr(self, s, k):
        
        def atMostK(s, k):
            if k == 0:
                return 0
            
            freq = {}
            left = 0
            count = 0
            
            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1
                
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                
                count += (right - left + 1)
            
            return count
        
        return atMostK(s, k) - atMostK(s, k - 1)
