class point():
    def __init__(self, x, y, userData):
        self.x = x
        self.y = y
        self.userData = userData

class rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return point.x >= self.x - self.w and point.x <= self.x + self.w and point.y >= self.y - self.h and point.y <= self.y + self.h

    def intersects(self,range):
        return not (range.x - range.w > self.x + self.w or range.x + range.w < self.x - self.w or range.y - range.h > self.y + self.h or range.y + range.h < self.y - self.h)


class cirlce():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.rSquared = self.r * self.r

class quadTree():
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def insert(self, point):

        if not self.boundary.contains(point):
            return False
        if (len(self.points) < self.capacity):
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subDivide()
            
        if self.ne.insert(point):
            return True
        elif self.nw.insert(point):
            return True
        elif self.se.insert(point):
            return True
        elif self.sw.insert(point):
            return True

    def subDivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        ne = rectangle(x + w/2, y - h/2, w/2, h/2)
        self.ne = quadTree(ne, self.capacity)
        nw = rectangle(x - w/2, y - h/2, w/2, h/2)
        self.nw = quadTree(nw, self.capacity)
        se = rectangle(x + w/2, y + h/2, w/2, h/2)
        self.se = quadTree(se, self.capacity)
        sw = rectangle(x - w/2, y + h/2, w/2, h/2)
        self.sw = quadTree(sw, self.capacity)
        self.divided = True


    def query(self, range, found):  
        if not found:
            found = []      
        if not self.boundary.intersects(range):
            return 
        
        for p in self.points:
            if range.contains(p):
                found.append(p)
        
        if self.divided:
            self.nw.query(range, found)
            self.ne.query(range, found)
            self.sw.query(range, found)
            self.se.query(range, found)

        return found
