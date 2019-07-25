# Greatest common divisor and least common multiple in python using recursion
# This can also be found by importing math function and using math.gcd and math.lcm


def gcd(a, b):
    try:
        if b == 0:
            return a
        elif a == 0:
            return b
        else:
            return gcd(b, a % b)
    except TypeError:
        print "Cannot find greatest common divisor"


def lcm(a, b):
    try:
        if b == 0:
            return b
        elif a == 0:
            return a
        else:
            return (a * b) / gcd(a, b)
    except TypeError:
        print "Cannot find least common multiple"


print gcd(60, 48)
print gcd(48, 60)
print gcd(0, 0)
print gcd(4, 4)
print gcd("a", 7)
print "*****************"
print lcm(1, 56)
print lcm(34, 1)
print lcm(0, 22)
print lcm(13, 0)
print lcm(35, 5)
print lcm(15, 20)
print lcm(60, 48)
print "*****************"


