#Brute Force Approch  :
#To count the number of digits in a number, we can use the algorithm created in Extract Digits as now instead of extracting digits we are simply creating a counter to count the number of digits in the number..
#Algorithm: 1)Initialise a counter to store the number of digits.
#2)While N is greater than 0, execute the following: 
#3)Increment the counter by 1
#4)Update N by removing its last digit by performing a modulo 10 (%10) operation on it.
#5)After exiting the while loop, we return the counter as the number of digits.
def countdigit(self,n):
  cnt = 0
  while n > 0:
    cnt = cnt + 1
    n = n// 10
  return cnt

#Optimal Approch :
#Algorithm :The logarithmic base 10 of a positive integers gives the number of digits in n. We add 1 to the result to ensure that the count is correct even for numbers that are powers of 10.
import math
def countdigit(self,n):
  cnt = int (math.log10(n) + 1)
  return cnt 
  
