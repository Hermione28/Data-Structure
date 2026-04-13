class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        
        # 🔥 Edge Case: All 9s
        if all(x == 9 for x in num):
            return [1] + [0] * (n - 1) + [1]
        
        result = num[:]
        
        # Step 1: Mirror left → right
        i, j = 0, n - 1
        while i < j:
            result[j] = result[i]
            i += 1
            j -= 1
        
        # Step 2: If already greater
        if result > num:
            return result
        
        # Step 3: Add 1 to middle
        carry = 1
        mid = n // 2
        
        if n % 2 == 1:
            result[mid] += carry
            carry = result[mid] // 10
            result[mid] %= 10
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid
        
        # Step 4: Propagate carry
        while left >= 0:
            result[left] += carry
            carry = result[left] // 10
            result[left] %= 10
            
            result[right] = result[left]
            
            left -= 1
            right += 1
        
        return result
        
