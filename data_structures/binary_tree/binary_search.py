# Find the lowest common ancestor of two nodes in a binary search tree.
# Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA).
# You may assume that both the values exist in the tree.

# Example:
# Assume n1 < n2

#                20
#         8               22
#     4       12
#         10      14

# LA of 10 and 14 is 12
# LCA of 14 and 8 is 8
# LCA of 10 and 22 is 20


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def lca(root, n1, n2):
    if root is None:
        return None

    elif root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    elif root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" % (n1, n2, t.data)
print "*******************"
n1 = 14
n2 = 8
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" % (n1, n2, t.data)
print "*******************"
n1 = 10
n2 = 22
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" % (n1, n2, t.data)
print "*******************"
