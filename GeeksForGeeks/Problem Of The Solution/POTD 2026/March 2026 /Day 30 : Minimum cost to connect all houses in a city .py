import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        
        visited = [False] * n
        minHeap = [(0, 0)]  # (cost, house_index)
        total_cost = 0
        edges_used = 0
        
        while edges_used < n:
            cost, u = heapq.heappop(minHeap)
            
            if visited[u]:
                continue
            
            visited[u] = True
            total_cost += cost
            edges_used += 1
            
            # Add all unvisited neighbors
            for v in range(n):
                if not visited[v]:
                    x1, y1 = houses[u]
                    x2, y2 = houses[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, v))
        
        return total_cost
