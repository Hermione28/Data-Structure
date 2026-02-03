class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # p: end index of first increasing segment (0..p)
        for p in range(1, n-2):  # need at least one element after decreasing segment
            for q in range(p+1, n-1):  # need at least one element for third segment
                # check first segment strictly increasing
                if not all(nums[i] < nums[i+1] for i in range(p)):
                    continue
                # check second segment strictly decreasing
                if not all(nums[i] > nums[i+1] for i in range(p, q)):
                    continue
                # check third segment strictly increasing
                if not all(nums[i] < nums[i+1] for i in range(q, n-1)):
                    continue
                return True
        return False
