class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # If only one student is chosen, difference is always 0
        if k == 1:
            return 0
        
        # Sort the scores
        nums.sort()
        
        min_diff = float('inf')
        
        # Sliding window of size k
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
