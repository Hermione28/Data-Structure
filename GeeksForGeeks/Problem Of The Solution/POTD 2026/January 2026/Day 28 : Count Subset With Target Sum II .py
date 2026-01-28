from collections import defaultdict

class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        def subset_sums(nums):
            sums = [0]
            for num in nums:
                sums += [num + s for s in sums]
            return sums
        
        left_sums = subset_sums(left)
        right_sums = subset_sums(right)
        
        freq = defaultdict(int)
        for s in right_sums:
            freq[s] += 1
        
        count = 0
        for s in left_sums:
            count += freq[k - s]
        
        return count
