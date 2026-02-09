class Solution:
    def maxProduct(self, arr):
        # Initialize variables
        max_ending = arr[0]
        min_ending = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            # If current element is negative, swap
            if arr[i] < 0:
                max_ending, min_ending = min_ending, max_ending

            # Update max and min ending here
            max_ending = max(arr[i], max_ending * arr[i])
            min_ending = min(arr[i], min_ending * arr[i])

            # Update result
            result = max(result, max_ending)

        return result

