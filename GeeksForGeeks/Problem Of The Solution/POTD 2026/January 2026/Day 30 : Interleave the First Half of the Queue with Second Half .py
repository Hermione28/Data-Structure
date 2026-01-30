from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        
        first_half = deque()
        
        for _ in range(half):
            first_half.append(q.popleft())
        
        while first_half:
            q.append(first_half.popleft())
            q.append(q.popleft())


