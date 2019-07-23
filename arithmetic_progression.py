# Arithmetic progression using recursion
# starting term = a = 1
# factor = d = a2 - a1
# Find the nth term - 8th term
#  1, 4, 7, 10...


def arithmetic_sequence(a, d, n):

    if d == 0 or d == 1:
        raise Exception("Sequence is not geometric")
    if n < 1:
        raise Exception("n should be >= 1")

    if a == 0:
        return 0

    if n == 1:
        return a
    else:
        return d + arithmetic_sequence(a, d, n-1)


print arithmetic_sequence(6, 2, 9)
print arithmetic_sequence(1, 3, 8)
print arithmetic_sequence(10, 3, 4)


# print arithmetic_sequence(2, 4, -1)

