class Solution:    
    def findUnion(self, a, b):
        # Use a set to store distinct elements
        union_set = set()
        
        for num in a:
            union_set.add(num)
        
        for num in b:
            union_set.add(num)
        
        # Return as a list (driver will sort)
        return list(union_set)
