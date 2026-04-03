import bisect

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        n = len(robots)
        if n == 0:
            return 0

        # sort walls
        walls.sort()

        # pair and sort robots with distance
        vp = sorted(zip(robots, distance))

        # intervals[i] = [left_l, left_r, right_l, right_r]
        intervals = [[0]*4 for _ in range(n)]

        for i in range(n):
            pos, d = vp[i]

            left_block = vp[i-1][0] if i > 0 else float('-inf')
            right_block = vp[i+1][0] if i < n-1 else float('inf')

            # LEFT interval
            intervals[i][0] = max(pos - d, left_block)
            intervals[i][1] = pos

            # RIGHT interval
            intervals[i][2] = pos
            intervals[i][3] = min(pos + d, right_block)

        # function to count walls in range [l, r]
        def getCount(l, r):
            if l > r:
                return 0
            left = bisect.bisect_left(walls, l)
            right = bisect.bisect_right(walls, r)
            return right - left

        # memo[i][prev_dir]  (0 = left, 1 = right, 2 = none)
        memo = [[-1]*3 for _ in range(n)]

        def solve(i, prev_dir):
            if i == n:
                return 0

            if memo[i][prev_dir] != -1:
                return memo[i][prev_dir]

            prev_r = float('-inf')

            if prev_dir == 0:
                prev_r = intervals[i-1][1]
            elif prev_dir == 1:
                prev_r = intervals[i-1][3]

            # LEFT option
            l1, r1 = intervals[i][0], intervals[i][1]
            walls_left = getCount(max(l1, prev_r + 1), r1)
            ans_left = walls_left + solve(i + 1, 0)

            # RIGHT option
            l2, r2 = intervals[i][2], intervals[i][3]
            walls_right = getCount(max(l2, prev_r + 1), r2)
            ans_right = walls_right + solve(i + 1, 1)

            memo[i][prev_dir] = max(ans_left, ans_right)
            return memo[i][prev_dir]

        return solve(0, 2)
