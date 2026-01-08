from collections import defaultdict

class Solution:
    def countSubarrays(self, arr, k):
        freq = defaultdict(int)
        freq[0] = 1
        
        odd_count = 0
        ans = 0
        
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
            
            ans += freq[odd_count - k]
            freq[odd_count] += 1
        
        return ans
