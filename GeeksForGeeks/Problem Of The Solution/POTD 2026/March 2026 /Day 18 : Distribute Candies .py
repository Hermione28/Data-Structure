'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Count moves
            self.moves += abs(left) + abs(right)
            
            # Return balance
            return node.data + left + right - 1
        
        dfs(root)
        return self.moves
