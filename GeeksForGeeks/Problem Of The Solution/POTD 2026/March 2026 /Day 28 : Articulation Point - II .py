class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * V
        disc = [0] * V
        low = [0] * V
        parent = [-1] * V
        ap = [False] * V
        
        time = [0]  # mutable time
        
        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            children = 0
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: root node
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    
                    # Case 2: non-root
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        # Run DFS for disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        result = [i for i in range(V) if ap[i]]
        
        if not result:
            return [-1]
        
        return sorted(result)
