

### 1) Brute Force Approach


class Solution:
    def GCD(self, n1, n2):
        gcd = 1

        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i

        return gcd


'''Simple Explanation:

* Loop from 1 to minimum of both numbers
* Check if i divides both numbers
* Update gcd whenever a common factor is found
* Final gcd will be the largest common divisor

Time Complexity: O(min(n1, n2))'''

---

### 2) Better Approach


class Solution:
    def GCD(self, n1, n2):
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                return i

        return 1


'''Simple Explanation:

* Start from min(n1, n2) and go backwards
* First number that divides both is the GCD
* Faster because it stops early

Time Complexity: O(min(n1, n2))'''

---

### 3) Optimal Approach (Euclidean Algorithm)


class Solution:
    def GCD(self, n1, n2):
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        if n1 == 0:
            return n2
        else:
            return n1


'''Simple Explanation:

* Use formula: GCD(a, b) = GCD(a % b, b)
* Keep reducing numbers using modulo
* When one becomes 0, the other is the GCD

Example:
GCD(20, 15)
→ 20 % 15 = 5
→ 15 % 5 = 0
→ Answer = 5

Time Complexity: O(log(min(n1, n2))) '''



