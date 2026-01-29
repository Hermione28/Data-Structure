from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26
        q = deque()
        result = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            # Remove repeating characters from the front
            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            # Append result
            if q:
                result.append(q[0])
            else:
                result.append('#')

        return "".join(result)

		
