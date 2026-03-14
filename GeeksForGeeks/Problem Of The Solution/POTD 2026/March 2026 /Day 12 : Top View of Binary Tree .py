from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        q = deque()
        q.append((root, 0))
        
        top = {}
        
        while q:
            node, hd = q.popleft()
            
            if hd not in top:
                top[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        for hd in sorted(top):
            result.append(top[hd])
            
        return result
        
        
