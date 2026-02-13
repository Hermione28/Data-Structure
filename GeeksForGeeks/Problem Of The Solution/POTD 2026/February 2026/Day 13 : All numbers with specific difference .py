class Solution:
    def getCount(self, n, d):
        # Function to compute sum of digits
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # Binary search to find smallest number satisfying condition
        left, right = 1, n
        ans = n + 1  # default (no valid number)

        while left <= right:
            mid = (left + right) // 2
            if mid - digit_sum(mid) >= d:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        # If no number satisfies condition
        if ans == n + 1:
            return 0

        return n - ans + 1

        
        
