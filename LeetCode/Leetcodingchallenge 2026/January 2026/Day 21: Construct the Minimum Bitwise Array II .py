

class Solution(object):
    def minBitwiseArray(self, nums):

        ans = []

        for p in nums:
            # Even prime (only 2)
            if p % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            k = 0
            temp = p
            while temp & 1:
                k += 1
                temp >>= 1

            # Correct formula
            x = p - (1 << (k - 1))
            ans.append(x)

        return ans
