class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        i, j = 0, len(nums) - 1
        max_sum = 0
        
        while i < j:
            max_sum = max(max_sum, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return max_sum
