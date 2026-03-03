
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Base case
        if n == 1:
            return "0"
        
        mid = 2 ** (n - 1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # position in reversed part
            new_k = 2 ** n - k
            bit = self.findKthBit(n - 1, new_k)
            
            # invert the bit
            return "1" if bit == "0" else "0"
