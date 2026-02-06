class Solution:
    def smallestDiff(self, a, b, c):
        a.sort()
        b.sort()
        c.sort()
        
        i = j = k = 0
        n = len(a)
        
        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = None
        
        while i < n and j < n and k < n:
            x, y, z = a[i], b[j], c[k]
            
            current_min = min(x, y, z)
            current_max = max(x, y, z)
            diff = current_max - current_min
            total = x + y + z
            
            if diff < best_diff or (diff == best_diff and total < best_sum):
                best_diff = diff
                best_sum = total
                best_triplet = [x, y, z]
            
            # Move pointer of the minimum element
            if current_min == x:
                i += 1
            elif current_min == y:
                j += 1
            else:
                k += 1
        
        # Return in decreasing order
        best_triplet.sort(reverse=True)
        return best_triplet

    

