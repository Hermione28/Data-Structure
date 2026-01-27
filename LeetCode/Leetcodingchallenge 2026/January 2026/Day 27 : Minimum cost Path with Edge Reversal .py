import heapq

class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        
        # Build graph
        for u, v, w in edges:
            adj[u].append((v, w))        # normal edge
            adj[v].append((u, 2 * w))    # reversed edge
        
        # Dijkstra
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            if u == n - 1:
                return cost
            
            for v, w in adj[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        
        return -1
