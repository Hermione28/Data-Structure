
from collections import defaultdict

class Solution:
    def countFrequencies(self, nums):
        # Create a defaultdict to store frequencies
        freq_map = defaultdict(int)

        # Count frequencies
        for num in nums:
            freq_map[num] += 1

        # Convert to list of tuples (optional, depending on requirement)
        result = []
        for key, value in freq_map.items():
            result.append((key, value))

        return result
