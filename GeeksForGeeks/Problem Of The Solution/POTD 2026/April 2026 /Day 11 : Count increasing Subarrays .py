class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        count = 0
        length = 1  # current increasing streak length

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
                count += (length - 1)
            else:
                length = 1

        return count
