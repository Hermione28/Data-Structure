import heapq
from collections import defaultdict

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        INF = 10**18
        
        # Graph
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))
        
        # Trie for original strings
        class Trie:
            def __init__(self):
                self.children = {}
                self.word = None
        
        root = Trie()
        max_len = 0
        for o in original:
            node = root
            for ch in o:
                node = node.children.setdefault(ch, Trie())
            node.word = o
            max_len = max(max_len, len(o))
        
        # Cache for substring conversion cost
        cache = {}
        
        def min_cost(s, t):
            if s == t:
                return 0
            if (s, t) in cache:
                return cache[(s, t)]
            
            pq = [(0, s)]
            seen = {}
            
            while pq:
                cost_so_far, cur = heapq.heappop(pq)
                if cur == t:
                    cache[(s, t)] = cost_so_far
                    return cost_so_far
                if cur in seen and seen[cur] <= cost_so_far:
                    continue
                seen[cur] = cost_so_far
                for nxt, w in graph[cur]:
                    heapq.heappush(pq, (cost_so_far + w, nxt))
            
            cache[(s, t)] = INF
            return INF
        
        # DP
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            
            # single character match
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            node = root
            for j in range(i, min(n, i + max_len)):
                if source[j] not in node.children:
                    break
                node = node.children[source[j]]
                if node.word:
                    src_sub = node.word
                    tgt_sub = target[i:j+1]
                    c = min_cost(src_sub, tgt_sub)
                    if c < INF:
                        dp[j + 1] = min(dp[j + 1], dp[i] + c)
        
        return dp[n] if dp[n] < INF else -1
