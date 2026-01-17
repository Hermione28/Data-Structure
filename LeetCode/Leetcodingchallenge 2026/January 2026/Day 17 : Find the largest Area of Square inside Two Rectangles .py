class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                left   = max(bottomLeft[i][0], bottomLeft[j][0])
                right  = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top    = min(topRight[i][1], topRight[j][1])
                
                width = right - left
                height = top - bottom
                
                if width > 0 and height > 0:
                    max_side = max(max_side, min(width, height))
        
        return max_side * max_side
