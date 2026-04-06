import heapq

class Node:
    def __init__(self, val=None, sum_=0, idx=-1):
        self.val = val
        self.sum = sum_
        self.idx = idx
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.sum != other.sum:
            return self.sum < other.sum
        return self.idx < other.idx


class Solution:
    def huffmanCodes(self, s, f):
        pq = []
        
        for i in range(len(s)):
            heapq.heappush(pq, Node(s[i], f[i], i))
        
        while len(pq) > 1:
            t1 = heapq.heappop(pq)
            t2 = heapq.heappop(pq)
            
            temp = Node(None, t1.sum + t2.sum, min(t1.idx, t2.idx))
            temp.left = t1
            temp.right = t2
            
            heapq.heappush(pq, temp)
        
        res = []
        
        def preorder(root, path):
            if not root:
                return
            
            if root.val is not None:
                res.append(path if path != "" else "0")
                return
            
            preorder(root.left, path + '0')
            preorder(root.right, path + '1')
        
        preorder(pq[0], "")
        
        return res
