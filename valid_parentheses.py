# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true


# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
s = "[]"
temp = []
count = 0
brackets = {"(": ")", "{": "}", "[": "]"}
if len(s) == 0:
    print True
elif len(s) == 1:
    print False
elif len(s) == 2:
    for i in s:
        if i in brackets and brackets[i] in s:
            print True
            break
        else:
            print False
            break
else:
    for i in s:
        if i in brackets and brackets[i] in s:
            temp.append()