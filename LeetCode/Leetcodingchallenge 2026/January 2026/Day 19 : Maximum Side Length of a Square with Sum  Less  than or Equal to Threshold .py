class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
       
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )
        
      
        def is_valid(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        pref[i][j]
                        - pref[i - k][j]
                        - pref[i][j - k]
                        + pref[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False
        
     
        left, right = 0, min(m, n)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
