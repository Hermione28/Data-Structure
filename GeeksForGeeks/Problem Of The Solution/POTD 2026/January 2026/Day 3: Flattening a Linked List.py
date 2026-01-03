'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def flatten(self, root):
        if root is None or root.next is None:
            return root
        
        root.next = self.flatten(root.next)
        
        root = self.merge(root, root.next)
        
        return root
    
    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        result.next = None   
        return result

