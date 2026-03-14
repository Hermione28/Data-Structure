class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)

        def backtrack(start, parts, path):
            # If 4 parts formed and string fully used
            if parts == 4 and start == n:
                res.append(".".join(path))
                return

            # If parts exceed or string finished early
            if parts == 4 or start == n:
                return

            # Try segments of length 1 to 3
            for l in range(1, 4):
                if start + l > n:
                    break

                segment = s[start:start+l]

                # Leading zero case
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # Value should be <=255
                if int(segment) <= 255:
                    backtrack(start+l, parts+1, path+[segment])

        backtrack(0, 0, [])
        return res
        
