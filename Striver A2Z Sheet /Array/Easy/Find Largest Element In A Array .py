'''Brute Force
Algorithm
Sort the array in ascending order.
Print the element at the (size of the array - 1)th index, which corresponds to the largest element in the array.    TC : O(NlogN)  SC : O(1)'''

class Solution:
    def largestElement(self, nums):
        nums.sort()
        return nums[-1]


'''Optimal Approach
Algorithm
Create a variable called max and initialize it with the value of the first element in the array.
Use a for loop to iterate through the rest of the elements in the array.
In each iteration, compare the current element with the max variable.
If the current element is greater than the max value, update the max value with the current element's value.
After completing the loop, print the max variable, which will hold the largest value in the array.'''

class Solution:
  def largestElement(self, nums):
    max = nums[0]

    for i in range (1,n):
      if nums[i] > max:
        max = nums[i]

    return max


