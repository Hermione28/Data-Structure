class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def get_contribution(is_max):
            left = [0] * n
            right = [0] * n
            stack = []

            # Previous greater/smaller
            for i in range(n):
                while stack and (
                    arr[stack[-1]] < arr[i] if is_max else arr[stack[-1]] > arr[i]
                ):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            # Next greater-or-equal / smaller-or-equal
            for i in range(n - 1, -1, -1):
                while stack and (
                    arr[stack[-1]] <= arr[i] if is_max else arr[stack[-1]] >= arr[i]
                ):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        max_sum = get_contribution(is_max=True)
        min_sum = get_contribution(is_max=False)

        return max_sum - min_sum

