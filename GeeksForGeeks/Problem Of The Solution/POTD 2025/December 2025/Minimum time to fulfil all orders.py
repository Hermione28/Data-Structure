class Solution:
    def minTime(self, ranks, n):
        # Helper function to check if we can make n donuts in 'time'
        def canMake(time):
            total = 0
            for r in ranks:
                t = 0
                k = 1
                while True:
                    t += r * k
                    if t > time:
                        break
                    total += 1
                    if total >= n:
                        return True
                    k += 1
            return False

        # Binary search on time
        low = 0
        high = min(ranks) * n * (n + 1) // 2
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        
