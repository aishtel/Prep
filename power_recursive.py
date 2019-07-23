# x power y using recursive
# 2 ^ 3 = 2 * 2 * 2 = 8

# 5 ^ 3 = 5 * (5^2)

# 5 ^ 2 = 5 * (5 * 1)

# 5 ^ 1 = 5 * (5^0)

# 5 ^ 0 = 1


def x_power_y(x, y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x * x_power_y(x, y-1)


print x_power_y(7, 3)
