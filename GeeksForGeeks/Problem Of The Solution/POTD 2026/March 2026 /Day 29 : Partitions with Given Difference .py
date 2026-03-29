class Solution:
    def countPartitions(self, arr, diff):
        totalSum = sum(arr)
        
        # Edge case
        if (totalSum + diff) % 2 != 0:
            return 0
        
        target = (totalSum + diff) // 2
        
        # DP array
        dp = [0] * (target + 1)
        dp[0] = 1  # One way to make sum 0
        
        for num in arr:
            # Traverse backwards
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]

