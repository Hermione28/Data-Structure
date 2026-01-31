class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # left may go out of range → wrap around
        return letters[left % len(letters)]
