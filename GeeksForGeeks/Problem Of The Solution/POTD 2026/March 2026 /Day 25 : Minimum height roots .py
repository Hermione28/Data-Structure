from collections import defaultdict, deque

class Solution:
    def minHeightRoot(self, V, edges):
        # Edge case
        if V == 1:
            return [0]

        # Step 1: Build graph
        adj = defaultdict(list)
        degree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Step 2: Find initial leaves
        q = deque()
        for i in range(V):
            if degree[i] == 1:
                q.append(i)

        # Step 3: Remove leaves layer by layer
        remaining_nodes = V

        while remaining_nodes > 2:
            size = len(q)
            remaining_nodes -= size

            for _ in range(size):
                node = q.popleft()
                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        # Remaining nodes are MHT roots
        return list(q)
        

