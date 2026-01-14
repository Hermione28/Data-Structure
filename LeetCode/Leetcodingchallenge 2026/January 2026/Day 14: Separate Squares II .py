class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))       
            events.append((y + l, -1, x, x + l))  

        events.sort()
        active = []
        prev_y = events[0][0]
        slabs = []   

        def union_width(intervals):
            intervals.sort()
            width = 0
            cur_start, cur_end = intervals[0]
            for s, e in intervals[1:]:
                if s > cur_end:
                    width += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            width += cur_end - cur_start
            return width

        for y, typ, x1, x2 in events:
            if y > prev_y and active:
                w = union_width(active)
                slabs.append((prev_y, y, w))
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y

        total_area = sum((y2 - y1) * w for y1, y2, w in slabs)
        target = total_area / 2.0

        acc = 0.0
        for y1, y2, w in slabs:
            slab_area = (y2 - y1) * w
            if acc + slab_area >= target:
                return y1 + (target - acc) / w
            acc += slab_area

        return 0.0

