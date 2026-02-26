class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        map_s1_to_s2 = {}
        map_s2_to_s1 = {}
        
        for c1, c2 in zip(s1, s2):
            # Check mapping from s1 to s2
            if c1 in map_s1_to_s2:
                if map_s1_to_s2[c1] != c2:
                    return False
            else:
                map_s1_to_s2[c1] = c2
            
            # Check reverse mapping from s2 to s1
            if c2 in map_s2_to_s1:
                if map_s2_to_s1[c2] != c1:
                    return False
            else:
                map_s2_to_s1[c2] = c1
        
        return True
