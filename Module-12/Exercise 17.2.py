class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point(3,4)
point.print_point()
