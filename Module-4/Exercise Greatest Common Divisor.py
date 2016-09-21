def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
print gcd(192, 270)
print gcd(270, 192)
