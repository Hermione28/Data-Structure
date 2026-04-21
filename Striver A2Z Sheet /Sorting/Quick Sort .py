'''Quick Sort
Algorithm :-
The core idea behind Quicksort lies in partitioning the array around a pivot element such that all elements smaller than the pivot lie to its left and all greater elements lie to its right. This positioning ensures that the pivot is in its correct sorted place. By doing this for each recursive call, the problem is broken down into smaller subproblems where each side of the pivot can be independently sorted. This divide-and-conquer strategy allows Quicksort to sort parts of the array separately.
Select a pivot element from the array (commonly the last element, but can be first, middle, or random).
Rearrange the elements in the array such that all elements smaller than the pivot are placed before it and all greater elements are placed after it (this step is called partitioning).
After partitioning, the pivot is in its correct sorted position.
Recursively apply the same process to the subarrays on the left and right of the pivot.
Base condition for recursion is when the subarray has zero or one element, as it's already sorted.
Combine the results of the recursive calls to obtain the fully sorted array.'''



class Solution:
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickSortHelper(self, nums, low, high):
        if low < high:
            pivotIndex = self.partition(nums, low, high)

            self.quickSortHelper(nums, low, pivotIndex - 1)
            self.quickSortHelper(nums, pivotIndex + 1, high)

    def quickSort(self, nums):
        self.quickSortHelper(nums, 0, len(nums) - 1)
        return nums
