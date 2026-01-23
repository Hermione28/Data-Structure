class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        prevGE = [-1] * n
        nextGE = [n] * n
        stack = []

        # Previous Greater or Equal
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            prevGE[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Greater or Equal
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            nextGE[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            left = i - prevGE[i] - 1
            right = nextGE[i] - i - 1
            ans = max(ans, left + right + 1)

        return ans

        
