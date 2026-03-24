from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        # Step 1: Build graph
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for x, y in prerequisites:
            adj[y].append(x)   # y -> x
            indegree[x] += 1
        
        # Step 2: Queue for nodes with indegree 0
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        # Step 3: Process nodes
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Step 4: Check if all nodes processed
        return count == n
