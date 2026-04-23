class Solution(object):
    def twoEditWords(self, queries, dictionary):
        result = []
        
        for q in queries:
            for d in dictionary:
                diff = 0
                
                # count differences
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                    if diff > 2:
                        break
                
                if diff <= 2:
                    result.append(q)
                    break   # no need to check other dictionary words
        
        return result
