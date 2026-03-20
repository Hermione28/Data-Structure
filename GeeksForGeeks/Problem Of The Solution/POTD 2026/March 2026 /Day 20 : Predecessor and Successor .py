class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None
        
        curr = root
        
        while curr:
            if curr.data < key:
                pre = curr
                curr = curr.right
            elif curr.data > key:
                suc = curr
                curr = curr.left
            else:
                # Find predecessor (max in left subtree)
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    pre = temp
                
                # Find successor (min in right subtree)
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                
                break
        
        return [pre, suc]
