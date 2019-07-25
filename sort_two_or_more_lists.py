# Given k unsorted lists, build a single sorted list containing all the elements

# Input :
# list1 = [25, 18, 9, 41, 26, 31]
# list2 = [25, 45, 3, 32, 15, 20]
# Output :
# [3, 9, 15, 18, 20, 25, 25, 26, 31, 32, 41, 45]
#
# Input :
# list1 = ["suraj", "anand", "gaurav", "aman", "kishore"]
# list2 = ["rohan", "ram", "mohan", "priya", "komal"]
# Output :
# ['aman', 'anand', 'gaurav', 'kishore', 'komal', 'mohan', 'priya', 'ram', 'rohan', 'suraj']


def sort_list(k):
    merge_list = []
    for i in range(len(k)):
        merge_list = merge_list + k[i]
    merge_list.sort()
    return merge_list


print sort_list([[25, 18, 9, 41, 26, 31], [25, 45, 3, 32, 15, 20], [1, 4, 3]])
print "******************************************************************************************"
print sort_list([["suraj", "anand", "gaurav", "aman", "kishore"], ["rohan", "ram", "mohan", "priya", "komal"]])
