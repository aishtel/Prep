# Example Fibonacci series = 0, 1, 1, 2, 3, 5, 8, ....

# Write a function that takes n and returns the nth number in the series using recursion
# n = 3
# series = 0, 1, 1, 2
# n = 4
# series = 0, 1, 1, 2, 3


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 0:
        return "This case is not covered in the program"
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print "The nth number in this series is", fibonacci(6)
print "The nth number in this series is", fibonacci(30)
