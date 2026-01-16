class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])
        
        h_dist = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_dist.add(hFences[j] - hFences[i])
        
       
        v_dist = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_dist.add(vFences[j] - vFences[i])
        
        common = h_dist & v_dist
        if not common:
            return -1
        
        side = max(common)
        return (side * side) % MOD
