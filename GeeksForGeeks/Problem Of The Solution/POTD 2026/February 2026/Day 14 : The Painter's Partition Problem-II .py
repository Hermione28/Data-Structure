class Solution:
    def minTime(self, arr, k):
        # Helper function to check if possible within max_time
        def can_paint(max_time):
            painters = 1
            curr_time = 0

            for length in arr:
                if curr_time + length <= max_time:
                    curr_time += length
                else:
                    painters += 1
                    curr_time = length
                    if painters > k:
                        return False
            return True

        # Binary search range
        left = max(arr)      # minimum possible time
        right = sum(arr)     # maximum possible time
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if can_paint(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

        
