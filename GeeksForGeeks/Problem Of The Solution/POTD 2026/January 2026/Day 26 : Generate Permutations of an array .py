class Solution:
    def permuteDist(self, arr):
        result = []
        used = [False] * len(arr)
        
        def backtrack(path):
            if len(path) == len(arr):
                result.append(path[:])
                return
            
            for i in range(len(arr)):
                if used[i]:
                    continue
                used[i] = True
                path.append(arr[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return result


        
        
        
