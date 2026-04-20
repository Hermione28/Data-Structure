# A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..
'''We can iterate through numbers from 1 to n, counting how many of these numbers divide n without a remainder. If exactly two numbers do, so n is prime otherwise it is not prime.'''
class Solution:
    def isPrime(self, n):
        #your code goes here
        cnt = 0
        for i in range ( 1, n+1):
            if n % i == 0:
                cnt += 1
        return cnt == 2

  '''Optimal Approch : We can optimise the algorithm by only iterating up to the square root of n when checking for factors. This is because if n has a factor greater than its square root, it must also have a factor smaller than its square root.'''
import math

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
          
