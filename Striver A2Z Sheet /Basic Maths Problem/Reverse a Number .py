class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n > 0 :
            lastdigit = n % 10
            revNum = revNum * 10 + lastdigit
            n = n // 10
        return revNum
