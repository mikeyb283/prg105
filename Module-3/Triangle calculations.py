def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print('no')
    else:
        print('yes')
a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))
c = int(input('Enter length of side c: '))
is_triangle(a, b, c)
