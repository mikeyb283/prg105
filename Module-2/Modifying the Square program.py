import turtle
bob = turtle.Turtle()
print (bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 150)

turtle.mainloop()
