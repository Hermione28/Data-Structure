class Solution:
    def longestCycle(self, V, edges):
        # Create outgoing edge mapping
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v
        
        visited = [False] * V
        max_cycle = -1
        
        for i in range(V):
            if visited[i]:
                continue
            
            curr = i
            time = {}
            step = 0
            
            while curr != -1 and not visited[curr]:
                visited[curr] = True
                time[curr] = step
                step += 1
                
                next_node = graph[curr]
                
                if next_node in time:
                    cycle_length = step - time[next_node]
                    max_cycle = max(max_cycle, cycle_length)
                    break
                
                curr = next_node
        
        return max_cycle
        

