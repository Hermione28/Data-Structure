class Solution(object):
    def minimumDistance(self, nums):
        n = len(nums)
        ans = float('inf')

        # Try all triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        ans = min(ans, dist)

        return ans if ans != float('inf') else -1
