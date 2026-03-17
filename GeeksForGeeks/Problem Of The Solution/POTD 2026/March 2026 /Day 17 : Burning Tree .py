from collections import deque

class Solution:
    def minTime(self, root, target):
        
        # Step 1: Create parent mapping and find target node
        parent = {}
        target_node = None
        
        def dfs(node, par):
            nonlocal target_node
            if not node:
                return
            
            parent[node] = par
            
            if node.data == target:
                target_node = node
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        # Step 2: BFS from target node
        q = deque([target_node])
        visited = set([target_node])
        time = 0
        
        while q:
            size = len(q)
            burned = False
            
            for _ in range(size):
                node = q.popleft()
                
                # Check all 3 directions
                for nei in [node.left, node.right, parent[node]]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                        burned = True
            
            if burned:
                time += 1
        
        return time

