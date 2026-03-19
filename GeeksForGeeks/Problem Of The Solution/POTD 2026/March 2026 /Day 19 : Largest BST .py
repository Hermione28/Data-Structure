class Solution:
    def largestBst(self, root):
        
        self.maxSize = 0
        
        def solve(node):
            # Base case
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            left = solve(node.left)
            right = solve(node.right)
            
            # Check BST condition
            if left[0] and right[0] and left[3] < node.data < right[2]:
                
                size = left[1] + right[1] + 1
                self.maxSize = max(self.maxSize, size)
                
                min_val = min(left[2], node.data)
                max_val = max(right[3], node.data)
                
                return (True, size, min_val, max_val)
            
            # Not a BST
            return (False, 0, 0, 0)
        
        solve(root)
        return self.maxSize
