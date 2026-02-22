

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        last_pos = -1
        max_gap = 0
        position = 0
        
        while n > 0:
            if n & 1:  # if current bit is 1
                if last_pos != -1:
                    max_gap = max(max_gap, position - last_pos)
                last_pos = position
            
            n >>= 1
            position += 1
        
        return max_gap
