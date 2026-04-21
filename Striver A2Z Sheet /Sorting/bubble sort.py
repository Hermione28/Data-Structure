'''Approach:
Select the range of the unsorted array: Use an outer loop (i) that runs backward from n-1 to 0 (where n is the size of the array). The value i = n-1 means the range is from 0 to n-1, i = n-2 means the range is from 0 to n-2, and so on.
Push the maximum element to the end of the selected range: Use an inner loop (j) that runs from 0 to i-1. Compare adjacent elements and swap them if arr[j] > arr[j+1]. Repeating this process ensures the maximum element in the current range moves to index i.
Progressively sort the array: After each outer loop iteration, the last part of the array becomes sorted. For example:
After the first iteration, the element at the last index is sorted.
After the second iteration, the last two elements are sorted.
This continues until the entire array is sorted.
Complete sorting: After n-1 iterations, the whole array will be sorted.'''

class solution:
  def bubble_sort(self ,nums):
    n = len(nums)
    for i in range(n-1 ,-1,-1):
      for j in range(i):
        if nums[j] > nums[j+1]:
          nums[j] , nums[j+1] = nums[j+1] , nums[j]
    return nums
        
    
''' Optimized approach
The best case occurs if the given array is already sorted. We can reduce the time complexity to O(N) by just adding a small check inside the loops.
We will check in the first iteration if any swap is taking place. If the array is already sorted no swap will occur and we will break out from the loops.
Thus the iteration of the outer loop will be just 1. And our overall time complexity will be O(N).'''

class solution:
  def bubble_sort:
  n = len(nums)
   for i in range(n-1.-1,-1):
     did_swap = false
     for j in range(i):
       if nums[j] > nums[j+1]:
         nums[j],nums[j+1] = nums[j+1],nums[j]
         did_swap = true
     if not did_swap:
       break
