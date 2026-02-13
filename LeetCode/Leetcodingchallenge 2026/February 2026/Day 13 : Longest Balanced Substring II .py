class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0


        run = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                run += 1
            else:
                ans = max(ans, run)
                run = 1
        ans = max(ans, run)


        def solve_two(x, y):
            best = 0
            i = 0
            while i < n:
           
                if s[i] != x and s[i] != y:
                    i += 1
                    continue

                diff_index = {0: -1}
                diff = 0
                start = i

                while i < n and (s[i] == x or s[i] == y):
                    diff += 1 if s[i] == x else -1

                    if diff in diff_index:
                        best = max(best, i - start - diff_index[diff])
                    else:
                        diff_index[diff] = i - start

                    i += 1
            return best

        ans = max(ans, solve_two('a', 'b'))
        ans = max(ans, solve_two('a', 'c'))
        ans = max(ans, solve_two('b', 'c'))


        diff_index = {(0, 0): -1}
        ca = cb = cc = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1

            key = (cb - ca, cc - ca)

            if key in diff_index:
                ans = max(ans, i - diff_index[key])
            else:
                diff_index[key] = i

        return ans
