class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for p in nums:
            found = -1
            for x in range(p + 1):
                if (x | (x + 1)) == p:
                    found = x
                    break
            ans.append(found)

        return ans
