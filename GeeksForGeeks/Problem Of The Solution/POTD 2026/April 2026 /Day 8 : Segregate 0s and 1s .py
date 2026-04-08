class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            if arr[left] == 0:
                left += 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
