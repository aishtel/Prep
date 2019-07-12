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
            temp = list(str(x)[::-1])
            temp.insert(0, temp.pop())
            rtype = int(("".join(temp)))
            if rtype >= -2147483648:
                return rtype
            else:
                return 0
