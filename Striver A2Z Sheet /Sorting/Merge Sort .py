'''Algorithm
Merge Sort is a classic divide and conquer algorithm. The core idea is based on breaking down a big problem into smaller, manageable sub-problems i.e. sorting smaller arrays and then merging those solutions to get the final sorted result.

It is much easier to merge two sorted arrays than to sort a large unsorted one. Therefore, instead of trying to sort the entire array at once, Merge Sort breaks it into halves repeatedly until we reach arrays of size 1 (which are trivially sorted), and then merges them back in sorted order. This makes the algorithm efficient and predictable, especially for large datasets.
If the array has only one or zero elements, it is already sorted, so we return it as is.
Else, we divide the array into two halves by finding the middle index.
We then apply the merge sort algorithm recursively on each of the two halves to sort them individually.
Once we have two sorted halves, we need to merge them into a single sorted array.
To merge, we compare elements from both halves one by one and place the smaller element into a new array, continuing this until all elements from both halves are used.
This process is repeated at every level of recursion, and finally, we get one fully sorted array after all merges are complete.'''

class solution:
  def merge(self,nums,low,mid,high):
    temp=[]
    left = low
    right = mid+ 1

    while left<= mid and right<= high:
      if nums[left] <= nums[right]:
        temp.append(nums[left])
        left = left +1
      else:
        temp.append(nums[right])
        right = right + 1

   while left <= mid:
     temp.append(nums[left])
     left = left + 1

   while right <= high:
     temp.append(nums[right])
     right = right + 1

   for i in range(low, higt + 1):
     nums[i] = temp[i - low] 

def mergesorthelper(self,nums,low,high):
  if low >= high:
    return

  mid = (low+high) // 2
  self.mergesorthelper(nums,low,mid)
  self.mergesorthelper(nums,mid+1,high)
  self.mergesort(nums,low,mid,high)

def mergesort(self,nums):
  self.mergesorthelper(nums,0,len(nums)-1)
  return nums

'''recursive approch'''

class solution:
  def merge(self,arr,low ,mid,high):
    temp =[]
    left,right = low ,mid+1

    while left <= mid and right <=high:
      if arr[left] <= arr[right]:
        temp.append[left]
        left += 1
      else:
        temp.append[right]
        right += 1

    while left <=mid:
      temp.append[left]
      left += 1

   while right <= high:
     temp.append[right]
     right += 1

  for i in range(low , high + 1):
    arr[i] = temp[i - low]

def mergesort(self,arr,low,high):
  if low >= high:
    return
  mid = ( low + high) //2
  self.mergesort(arr ,low,mid)
  self.mergesort(arr,mid+1,high)
  self.merge(arr,low ,mid,high)


