'''Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Examples
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

Brute Force Approach:
Algorithm :- The brute force approach to find all the divisors of a number is to iterate through every number from 1 to N and check whether it is a divisor or not. We can store all the divisors and return the list of divisors after iteration.
'''
class Solution:
    def divisors(self, n):
        res = []
        for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
        return res


'''Optimal Approach
Algorithm :- We can optimise the previous approach by using the property that for any non-negative integer n, if d is a divisor of n then n/d is also a divisor of n. This property is symmetric about the square root of N. Thus, by traversing just the first half we can avoid redundant iteration and computations improving the efficiency of the algorithm.
Iterate from 1 to sqrt(N) and for every divisor found, if N/divisor is distinct, add that to the list of divisors as well.
'''
import math

class Solution:
    def divisors(self, n):
        res = []
        
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
                
                if i != n // i:
                    res.append(n // i)
        
        return sorted(res)
