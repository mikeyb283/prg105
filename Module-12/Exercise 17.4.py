class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


point1 = Point(3, 4)
print 'The coordinates of the initial point are: ' + str(point1)

x2 = raw_input('\nBy how much would you like to change the x-coordinate?\n ')
x = int(x2)
y2 = raw_input('\nBy how much would you like to change the y-coordinate?\n ')
y = int(y2)
point2 = Point(x, y)

print '\nThe new coordinates of the point are: ' + str(point1 + point2)
