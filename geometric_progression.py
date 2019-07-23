# Geometric progression using recursion
# starting term = a = 1
# factor = r = a2/a1
# Find the nth term - 8th term
#  1, 3, 9, 27, ...


def geo_sequence(a, r, n):

    if r == 0 or r == 1:
        raise Exception("Sequence is not geometric")
    if n < 1:
        raise Exception("n should be >= 1")

    if a == 0:
        return 0

    if n == 1:
        return a
    else:
        return r * geo_sequence(a, r, n-1)


print geo_sequence(6, 2, 9)
print geo_sequence(1, 3, 8)
print geo_sequence(10, 3, 4)


print geo_sequence(2, 4, -1)
