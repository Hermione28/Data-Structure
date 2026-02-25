class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        first_occurrence = {}
        max_len = 0

        for i, num in enumerate(arr):
            # Convert to +1 or -1
            if num > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # Case 1: whole subarray from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Store first occurrence of prefix sum
                if prefix_sum not in first_occurrence:
                    first_occurrence[prefix_sum] = i

                # Check if we can form positive sum subarray
                if (prefix_sum - 1) in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

        return max_len
        
