from swampy.World import World

world = World()


class Point:

    def __init__(self):
        pass


class Circle:

    def __init__(self):
        pass


class Rectangle:

    def __init__(self):
        pass


canvas = world.ca(width=500, height=500, background='gray')


def draw_rectangle(canvas, rect):
    bbox = [[rect.x, rect.y], [rect.x1, rect.y1]]
    canvas.rectangle(bbox, outline='red', width=2, fill='green')


def draw_rectangle_color(canvas, rect1, color):
    bbox = [[rect1.x, rect1.y], [rect1.x1, rect1.y1]]
    canvas.rectangle(bbox, outline='green', width=2, fill=color)


def draw_point(canvas, x, y):
    canvas.circle([x, y], 5, outline='green', fill='red')


def create_circle(x, y, radius):
    c = Circle()
    c.center = Point()
    c.center.x = x
    c.center.y = y
    c.radius = radius
    return c


def draw_circle(window, circ, color):
    window.circle([circ.center.x, circ.center.y], circ.radius, outline='black', fill=color)


rectangle = Rectangle()
rectangle.x = -125
rectangle.y = -125
rectangle.x1 = 125
rectangle.y1 = -100

rectangle1 = Rectangle()
rectangle1.x = 125
rectangle1.y = 125
rectangle1.x1 = -125
rectangle1.y1 = 100

# assign values to coordinates for a point
p1 = 0
p2 = 0

# assign values to create instances of circles
circle1 = create_circle(0, 0, 75)
circle2 = create_circle(0, 0, 50)
circle3 = create_circle(0, 0, 25)


draw_circle(canvas, circle1, 'red')
draw_circle(canvas, circle2, 'green')
draw_circle(canvas, circle3, 'red')

draw_rectangle(canvas, rectangle)
draw_rectangle_color(canvas, rectangle1, 'red')

draw_point(canvas, p1, p2)

world.mainloop()
