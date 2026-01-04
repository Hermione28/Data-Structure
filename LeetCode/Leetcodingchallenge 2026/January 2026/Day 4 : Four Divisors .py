class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        total = 0
        
        for x in nums:
            div_sum = 1 + x
            count = 2  # 1 and x
            
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    j = x // i
                    if i == j:
                        count += 1
                        div_sum += i
                    else:
                        count += 2
                        div_sum += i + j
                    
                    if count > 4:
                        break
            
            if count == 4:
                total += div_sum
        
        return total

