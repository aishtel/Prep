# Given k unsorted lists, build a single sorted list containing all the elements

# Input :
# list1 = [25, 18, 9, 41, 26, 31]
# list2 = [25, 45, 3, 32, 15, 20]
# Output :
# [3, 9, 15, 18, 20, 25, 25, 26, 31, 32, 41, 45]
#
# Input :
# list1 = ["kim", "dog", "kenny", "aman", "kishore"]
# list2 = ["jan", "strawberry", "mohan", "donkey", "komal"]
# Output :
# ['aman', 'dog', 'donkey', 'jan', 'kenny', 'kim', 'kishore', 'komal', 'mohan', 'strawberry']


class Solution(object):
    def sort_list(self, k):
        """

        :param k: type - list
        :return: list of sorted elements
        """
        merge_list = []
        for i in range(len(k)):
            merge_list = merge_list + k[i]
        merge_list.sort()
        return merge_list


solution = Solution()
print "Sorted Lists"
print "Input:"
print "[25, 18, 9, 41, 26, 31], [25, 45, 3, 32, 15, 20], [1, 4, 3]"
print "Output:"
print solution.sort_list([[25, 18, 9, 41, 26, 31], [25, 45, 3, 32, 15, 20], [1, 4, 3]])
print "------------------------------------------------------------------------------------------"
print "Input:"
print '["kim", "dog", "kenny", "aman", "kishore"], ["jan", "strawberry", "mohan", "donkey", "komal"]'
print "Output:"
print solution.sort_list([["kim", "dog", "kenny", "aman", "kishore"], ["jan", "strawberry", "mohan", "donkey", "komal"]])
print "------------------------------------------------------------------------------------------"
print "Input:"
print "[1, 5, 7, 3], [6, 8, 9, 3], [3, 7, 9, 15]"
print "Output:"
print solution.sort_list([[1, 5, 7, 3], [6, 8, 9, 3], [3, 7, 9, 15]])
print "------------------------------------------------------------------------------------------"
print "Input:"
print '["dog", "cat", "alphabet", "job"], ["umbrella", "thermometer"]'
print "Output:"
print solution.sort_list([["dog", "cat", "alphabet", "job"], ["umbrella", "thermometer"]])
print "------------------------------------------------------------------------------------------"
print "Input:"
print '[1, 7, 9, 3, 7, 5, 67, -6], ["strawberry", "apple", "orange", "banana"]'
print "Output:"
print solution.sort_list([[1, 7, 9, 3, 7, 5, 67, -6], ["strawberry", "apple", "orange", "banana"]])
print "------------------------------------------------------------------------------------------"
