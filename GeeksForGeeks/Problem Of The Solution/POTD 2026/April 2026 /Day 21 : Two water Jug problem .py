import math

class Solution:
    def pour(self, fromJug, toJug, d):
        fromCap = fromJug
        toCap = toJug
        
        fromJug = fromCap
        toJug = 0
        
        step = 1
        
        while fromJug != d and toJug != d:
            temp = min(fromJug, toCap - toJug)
            toJug += temp
            fromJug -= temp
            step += 1
            
            if fromJug == d or toJug == d:
                break
            
            if fromJug == 0:
                fromJug = fromCap
                step += 1
            
            if toJug == toCap:
                toJug = 0
                step += 1
        
        return step

    def minSteps(self, m, n, d):
        if d > max(m, n):
            return -1
        
        if d % math.gcd(m, n) != 0:
            return -1
        
        return min(self.pour(m, n, d), self.pour(n, m, d))
