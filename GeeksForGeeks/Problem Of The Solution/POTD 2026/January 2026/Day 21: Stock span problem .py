class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = []  # stack to store indices

        for i in range(n):
            # Pop elements from stack while current price is higher or equal
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack is empty, span is i+1
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push current index to stack
            stack.append(i)

        return span

        
        
