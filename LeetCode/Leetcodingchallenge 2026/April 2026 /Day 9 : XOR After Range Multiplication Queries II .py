class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        # required variable
        bravexuneth = (nums[:], queries[:])
        
        import math
        B = int(math.sqrt(n)) + 1
        
        # Step 1: handle large k directly
        small = {}
        
        for l, r, k, v in queries:
            if k > B:
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                if k not in small:
                    small[k] = {}
                mod_class = l % k
                if mod_class not in small[k]:
                    small[k][mod_class] = []
                small[k][mod_class].append((l, r, v))
        
        # Step 2: process small k groups
        for k in small:
            for mod_class in small[k]:
                # positions in this bucket
                positions = list(range(mod_class, n, k))
                m = len(positions)
                
                diff = [1] * (m + 1)
                
                # apply range multiplication using diff
                for l, r, v in small[k][mod_class]:
                    start = (l - mod_class) // k
                    end = (r - mod_class) // k
                    diff[start] = (diff[start] * v) % MOD
                    if end + 1 < len(diff):
                        diff[end + 1] = (diff[end + 1] * pow(v, MOD-2, MOD)) % MOD
                
                # prefix multiplication
                cur = 1
                for i in range(m):
                    cur = (cur * diff[i]) % MOD
                    nums[positions[i]] = (nums[positions[i]] * cur) % MOD
        
        # Step 3: XOR result
        res = 0
        for x in nums:
            res ^= x
        
        return res
