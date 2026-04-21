class Solution(object):
    def maxFrequency(self, nums, k):
        # Sort the array
        nums.sort()
        
        left = 0
        total = 0
        max_freq = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            # If required operations exceed k, shrink window
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            
            # Update maximum frequency
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
