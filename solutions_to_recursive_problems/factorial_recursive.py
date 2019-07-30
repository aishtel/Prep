# Return the factorial of a given number using recursive method.

# Example:
# n = 6
# fact = 6*5*4*3*2*1 = 720


def factorial(n):
    if n < 0:
        raise Exception("n should be >= 0")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print "The factorial is", factorial(4)
print "The factorial is", factorial(0)
print "The factorial is", factorial(1)
# print "The factorial is", factorial(-4)
