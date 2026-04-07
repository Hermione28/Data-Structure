class Robot(object):

    def __init__(self, width, height):
        self.path = []
        
        # bottom row (left → right)
        for i in range(width):
            self.path.append((i, 0))
        
        # right column (bottom → top)
        for i in range(1, height):
            self.path.append((width - 1, i))
        
        # top row (right → left)
        for i in range(width - 2, -1, -1):
            self.path.append((i, height - 1))
        
        # left column (top → bottom)
        for i in range(height - 2, 0, -1):
            self.path.append((0, i))
        
        self.perimeter = len(self.path)
        self.idx = 0
        self.moved = False

    def step(self, num):
        self.moved = True
        self.idx = (self.idx + num) % self.perimeter

    def getPos(self):
        return list(self.path[self.idx])

    def getDir(self):
        if not self.moved:
            return "East"
        
        # Special case
        if self.idx == 0:
            return "South"
        
        x1, y1 = self.path[self.idx - 1]
        x2, y2 = self.path[self.idx]
        
        if x2 > x1:
            return "East"
        elif x2 < x1:
            return "West"
        elif y2 > y1:
            return "North"
        else:
            return "South"
