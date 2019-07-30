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
s = "{[]}"
count = 0
temp = []
brackets = {"(": ")", "{": "}", "[": "]"}
if len(s) == 0:
    print True
elif len(s) == 2:
    for i in s:
        if i in brackets and brackets[i] in s:
            print True
            break
        else:
            print False
            break
else:
    if len(s) % 2 == 0:
        s = list(s)
        for i in range(0, len(s), 2):
            if s[i] in brackets and brackets[s[i]] == s[i+1]:
                count = count + 1
        if count == len(s)/2:
            print True
        else:
            print False
    else:
        print False
