'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        prefix = {0:1}   # prefix sum frequency
        self.count = 0
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.data
            
            if curr_sum - k in prefix:
                self.count += prefix[curr_sum - k]
            
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1   # backtrack
        
        dfs(root, 0)
        return self.count
