class Solution:
    def minCost(self, heights, cost):
        # Pair heights with cost
        towers = list(zip(heights, cost))
        
        # Sort by heights
        towers.sort()
        
        # Total weight
        total_cost = sum(cost)
        
        # Find weighted median
        cumulative = 0
        median_height = 0
        
        for h, c in towers:
            cumulative += c
            if cumulative >= total_cost / 2:
                median_height = h
                break
        
        # Calculate minimum cost
        min_cost = 0
        for h, c in towers:
            min_cost += abs(h - median_height) * c
        
        return min_cost

        
