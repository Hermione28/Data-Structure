class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)

        # Step 1: count trailing zeros in each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        # Step 2: try to place rows correctly
        for i in range(n):
            needed = n - i - 1
            j = i

            # find row with enough zeros
            while j < n and trailing_zeros[j] < needed:
                j += 1

            if j == n:
                return -1  # impossible

            # bring row j to position i using swaps
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
                j -= 1

        return swaps
