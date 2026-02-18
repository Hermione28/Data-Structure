class Solution:
    def inversionCount(self, arr):
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, inv_left = merge_sort(nums[:mid])
            right, inv_right = merge_sort(nums[mid:])
            
            merged, inv_merge = merge(left, right)
            return merged, inv_left + inv_right + inv_merge
        
        def merge(left, right):
            i = j = inv_count = 0
            merged = []
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i  
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count
        
        _, count = merge_sort(arr)
        return count

