class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        # Step 1: left_min array
        left_min = [0] * n
        left_min[0] = 0

        for i in range(1, n):
            if arr[i] < arr[left_min[i - 1]]:
                left_min[i] = i
            else:
                left_min[i] = left_min[i - 1]

        # Step 2: right_max array
        right_max = [0] * n
        right_max[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[right_max[i + 1]]:
                right_max[i] = i
            else:
                right_max[i] = right_max[i + 1]

        # Step 3: find valid triplet
        for j in range(1, n - 1):
            i = left_min[j]
            k = right_max[j]

            if arr[i] < arr[j] and arr[j] < arr[k]:
                return [arr[i], arr[j], arr[k]]

        return []
