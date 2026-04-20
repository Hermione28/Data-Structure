class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n > 0 :
            #extract last digit from number 
            lastdigit = n % 10
            revNum = revNum * 10 + lastdigit
            # remove the last digit from number
            n = n // 10
        return revNum
