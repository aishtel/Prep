# x power y using recursive
# Example:
# 2 ^ 3 = 2 * 2 * 2 = 8

# Logic:
# 5 ^ 3 = 5 * (5 ^ 2)
# 5 ^ 2 = 5 * (5 * 1)
# 5 ^ 1 = 5 * (5 ^ 0)
# 5 ^ 0 = 1


def x_power_y(x, y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x * x_power_y(x, y-1)


print "-----------------------------------"
print "7 to the power 3 is", x_power_y(7, 3)
print "2 to the power 30 is", x_power_y(2, 30)
print "-1 to the power 3 is", x_power_y(-1, 3)
print "0 to the power 3 is", x_power_y(0, 3)
print "3 to the power 0 is", x_power_y(3, 0)
print "1 to the power 3 is", x_power_y(1, 3)
print "-----------------------------------"
