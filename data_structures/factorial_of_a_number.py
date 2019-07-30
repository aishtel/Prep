# Return the factorial of a given number.

# Example:
# n = 6
# fact = 6*5*4*3*2*1 = 720


def factorial(n):
    fact = 1
    try:
        if n == 0:
            return 1
        elif n < 0:
            raise Exception("Factorial not defined for negative numbers")
        else:
            for i in range(1, n+1):
                fact = fact * i
        return fact
    except TypeError:
        raise Exception("Factorial not defined for non integers")


print "The factorial is", factorial(6)
print "The factorial is", factorial(25)
print "The factorial is", factorial(1)
# print "The factorial is", factorial(-5)
# print "The factorial is", factorial(0.1)

