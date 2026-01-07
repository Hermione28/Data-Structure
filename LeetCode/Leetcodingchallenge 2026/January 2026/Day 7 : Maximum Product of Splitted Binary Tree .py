# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        

        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        self.max_prod = 0
        
       
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            subtree_sum = node.val + left_sum + right_sum
            
       
            self.max_prod = max(
                self.max_prod,
                subtree_sum * (total - subtree_sum)
            )
            
            return subtree_sum
        
        dfs(root)
        return self.max_prod % MOD
