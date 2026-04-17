class Solution:
    def canFormPalindrome(self, s):
        freq = {}
        
        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Count odd frequencies
        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1
        
        # Check condition
        return odd_count <= 1
