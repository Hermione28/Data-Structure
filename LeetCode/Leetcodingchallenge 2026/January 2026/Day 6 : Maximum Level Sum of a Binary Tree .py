# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        ans_level = 1
        
        while queue:
            level_sum = 0
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                ans_level = level
            
            level += 1
        
        return ans_level

