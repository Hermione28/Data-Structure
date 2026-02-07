class Solution(object):
    def minimumDeletions(self, s):
        a_right = s.count('a')   # total 'a's
        b_left = 0
        
        # IMPORTANT: consider split before index 0
        ans = a_right
        
        for ch in s:
            if ch == 'a':
                a_right -= 1
            else:  # ch == 'b'
                b_left += 1
            
            ans = min(ans, b_left + a_right)
        
        return ans

