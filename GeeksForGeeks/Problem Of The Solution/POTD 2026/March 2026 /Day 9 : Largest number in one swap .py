class Solution:
    def largestSwap(self, s: str) -> str:
        n = len(s)
        s = list(s)  
        
        
        last_pos = {int(s[i]): i for i in range(n)}
        
       
        for i in range(n):
            current = int(s[i])
            
            for d in range(9, current, -1):  
                if d in last_pos and last_pos[d] > i:
                  
                    j = last_pos[d]
                    s[i], s[j] = s[j], s[i]
                    return "".join(s)
         
        return "".join(s)
        
