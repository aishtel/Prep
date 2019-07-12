# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example:1
# Input: 121
# Output: true

# Example:2
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example:3
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Do it without string conversion


class Solution(object):
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        try:
            rev = int(str(x)[::-1])
            if rev == x:
                return True
            else:
                return False
        except ValueError:
            temp = list(str(x)[::-1])
            rev = "".join(temp)
            if rev == x:
                return True
            else:
                return False

