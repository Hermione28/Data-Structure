class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        mod = 10**9 + 7
        
        # Create 3D memo array: memo[z][o][lastBit] initialized to -1
        memo = [[[-1 for _ in range(2)] for _ in range(one+1)] for _ in range(zero+1)]
        
        def dp(z, o, lastBit):
            # Base cases
            if z == 0:
                return 0 if lastBit == 0 or o > limit else 1
            if o == 0:
                return 0 if lastBit == 1 or z > limit else 1
            
            # Check memo
            if memo[z][o][lastBit] != -1:
                return memo[z][o][lastBit]
            
            res = 0
            if lastBit == 0:
                # Place a 0 or 1 next
                res = (dp(z-1, o, 0) + dp(z-1, o, 1)) % mod
                if z > limit:
                    res = (res - dp(z - limit - 1, o, 1) + mod) % mod
            else:
                # lastBit == 1
                res = (dp(z, o-1, 0) + dp(z, o-1, 1)) % mod
                if o > limit:
                    res = (res - dp(z, o - limit - 1, 0) + mod) % mod
            
            memo[z][o][lastBit] = res
            return res
        
        return (dp(zero, one, 0) + dp(zero, one, 1)) % mod
