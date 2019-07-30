# Given a 32-bit signed integer, reverse digits of an integer.
# Example:1
# Input: 123
# Output: 321

# Example:2
# Input: -123
# Output: -321

# Example:3
# Input: 120
# Output: 21


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            temp = str(x)[::-1]
            rtype = int(temp)
            if rtype <= 2147483647:
                return rtype
            else:
                return 0
        except ValueError:
            temp = list(str(x))
            temp.pop(0)
            rtype = int("".join(temp)[::-1])
            if rtype >= -2147483648:
                return rtype
            else:
                return 0


solution = Solution()
print "-----------------------"
print "Given a 32-bit signed integer, reverse digits of an integer."
print "Reverse 123:", solution.reverse(123)
print "Reverse -123:", solution.reverse(-123)
print "Reverse 120:", solution.reverse(120)
print "Reverse -120:", solution.reverse(-120)
print "Reverse 0:", solution.reverse(0)
print "The data type of reverse of 123:", type(solution.reverse(123))
print "-----------------------"
