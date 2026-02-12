class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        
        for i in range(n):
            evenSet = set()
            oddSet = set()
            
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evenSet.add(nums[j])
                else:
                    oddSet.add(nums[j])
                
                if len(evenSet) == len(oddSet):
                    ans = max(ans, j - i + 1)
        
        return ans
