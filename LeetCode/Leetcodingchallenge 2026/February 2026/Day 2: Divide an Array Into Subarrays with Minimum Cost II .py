import bisect

class Container(object):
    def __init__(self, k):
        self.k = k
        self.st1 = []
        self.st2 = []
        self.sm = 0

    def adjust(self):
        while len(self.st1) < self.k and self.st2:
            x = self.st2.pop(0)
            bisect.insort(self.st1, x)
            self.sm += x
        while len(self.st1) > self.k:
            x = self.st1.pop()
            bisect.insort(self.st2, x)
            self.sm -= x

    def add(self, x):
        if self.st2 and x >= self.st2[0]:
            bisect.insort(self.st2, x)
        else:
            bisect.insort(self.st1, x)
            self.sm += x
        self.adjust()

    def erase(self, x):
        i = bisect.bisect_left(self.st1, x)
        if i < len(self.st1) and self.st1[i] == x:
            self.st1.pop(i)
            self.sm -= x
        else:
            j = bisect.bisect_left(self.st2, x)
            self.st2.pop(j)
        self.adjust()

    def sum(self):
        return self.sm


class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)

        cnt = Container(k - 2)

        for i in range(1, k - 1):
            cnt.add(nums[i])

        ans = cnt.sum() + nums[k - 1]

        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cnt.erase(nums[j])
            cnt.add(nums[i - 1])
            ans = min(ans, cnt.sum() + nums[i])

        return ans + nums[0]
