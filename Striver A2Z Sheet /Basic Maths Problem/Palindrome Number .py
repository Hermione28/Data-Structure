#Palindrome number is the number whose reverse is exactly same as the original number .
#Algorithm
'''Initialise an integer revNum to 0. This variable will store the reverse of the number.
Make a duplicate of the original number and store it in an integer dup for later comparison.
Run a while loop with the condition n>0 to reverse the number and at each iteration
Get the last digit of n by using the modulus operator % with 10 and store it in a temporary variable ld.
Update the revNum by multiplying it by 10 and adding the last digit ld.
Update n by integer division with 10 effectively removing the last digit.
After the loop, check if the original number dup is equal to the reversed number revNum.
If they are equal, return true indicating the number is a palindrome.
If they are not equal, return false indicating that the number is not a palindrome.'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        revNum = 0
        dup = x
        
        while x > 0:
            ld = x % 10
            revNum = (revNum * 10) + ld
            x //= 10
        
        return dup == revNum

