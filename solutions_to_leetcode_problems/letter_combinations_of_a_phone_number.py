# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.

# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Example:
# Input: "234
# Output: ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
# "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
from itertools import combinations


class Solution(object):

    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        a = []
        count = len(digits)
        combo = []

        def check_validity_of_digits(digits):
            telephone_pad = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                             "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                             "9": ["w", "x", "y", "z"]}
            for digit in digits:
                if digit in telephone_pad:
                    a.append(telephone_pad[digit])
                else:
                    return "invalid mapping"

        if count == 1:
            check_validity_of_digits(digits)
            if not a:
                return []
            else:
                return a[0]
        else:
            check_validity_of_digits(digits)
            a = a[::-1]
            print a
            for i in range(len(a)-1):
                print i
                print a[i]


            #     for elem in a[i]:
            #         # print elem
            #         for j in range(len(a[i+1])):
            #             # print a[i+1][j]
            #             combo.append(elem + a[i+1][j])

            # print combo


def main():
    result = Solution()
    print result.letter_combinations("234")


main()
