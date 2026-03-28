class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)

        # Step 1: Validate diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        res = [''] * n
        ch = ord('a')

        # Step 2: Assign characters
        for i in range(n):
            if res[i] == '':
                if ch > ord('z'):
                    return ""
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = chr(ch)
                ch += 1

        word = "".join(res)

        # Step 3: Build LCP matrix from constructed word
        calc = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        calc[i][j] = 1 + calc[i+1][j+1]
                    else:
                        calc[i][j] = 1
                else:
                    calc[i][j] = 0

        # Step 4: Compare matrices
        if calc == lcp:
            return word
        return ""
