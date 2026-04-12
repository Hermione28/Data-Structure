class Solution(object):
    def minimumDistance(self, word):
        def dist(a, b):
            if a is None:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        dp = [0] * 26  # dp[j] = max saving when second finger at j
        res = 0
        
        for i in range(1, n):
            cur = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A')
            
            d = dist(prev, cur)
            res += d
            
            new_dp = dp[:]
            for j in range(26):
                
                new_dp[prev] = max(new_dp[prev], dp[j] + d - dist(j, cur))
            
            dp = new_dp
        
        return res - max(dp)
