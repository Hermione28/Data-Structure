class Solution(object):
    def pyramidTransition(self, bottom, allowed):
         """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict

        # Mapping: (left, right) -> list of top blocks
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)

        memo = {}

        def dfs(curr):
            if curr in memo:
                return memo[curr]

            if len(curr) == 1:
                return True

            def backtrack(i, next_row):
                if i == len(curr) - 1:
                    return dfs(next_row)

                key = (curr[i], curr[i + 1])
                if key not in mp:
                    return False

                for ch in mp[key]:
                    if backtrack(i + 1, next_row + ch):
                        return True

                return False

            memo[curr] = backtrack(0, "")
            return memo[curr]

        return dfs(bottom)
P
