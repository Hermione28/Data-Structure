
class Solution:
    def countDistinct(self, arr, k):
        freq = defaultdict(int)
        result = []
        distinct_count = 0
        
        for i in range(k):
            if freq[arr[i]] == 0:
                distinct_count += 1
            freq[arr[i]] += 1
        
        result.append(distinct_count)
        
        for i in range(k, len(arr)):
            if freq[arr[i - k]] == 1:
                distinct_count -= 1
            freq[arr[i - k]] -= 1
            
            if freq[arr[i]] == 0:
                distinct_count += 1
            freq[arr[i]] += 1
            
            result.append(distinct_count)
        
        return result



        
        
