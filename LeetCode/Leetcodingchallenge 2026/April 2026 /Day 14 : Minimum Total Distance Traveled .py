class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # dp[i][j] = min distance for first i robots using first j factories
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            
            for i in range(n + 1):
               
                dp[i][j] = dp[i][j - 1]
                
               
                dist = 0
                for k in range(1, min(limit, i) + 1):
                    dist += abs(robot[i - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + dist)
        
        return dp[n][m]
