'''Approach
Algorithm
In each iteration, select an element from the unsorted part of the array using an outer loop.
Place this selected element in its correct position within the sorted part of the array.
Use an inner loop to shift the remaining elements, if necessary, to accommodate the selected element. This involves shifting elements by one position until the selected element can be placed in the correct position.
Continue this process until the entire array is sorted.'''

class solution:
  def selectionsort(self,nums):
    n = len(nums)
    for i in range(1,n):
      key=nums[i]
      j= i-1
      while j>=0 and nums[j] > key:
        nums[j+1]=nums[j]
        j=j-1
     nums[j+1] = key
   return nums
      
