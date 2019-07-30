# Binary tree search/traverse - Depth first search

# Example binary tree
#                      1
#               2               3
#           4       5

# The Depth First Traversals of this tree can be printed as:
# (a) Inorder   (Left, Root, Right) : 4 2 5 1 3
# (b) Pre-order  (Root, Left, Right) : 1 2 4 5 3
# (c) Post-order (Left, Right, Root) : 4 5 2 3 1


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print root.val
        print_inorder(root.right)


# A function to do pre-order tree traversal
def print_pre_order(root):

    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)


# A function to do post-order tree traversal
def print_post_order(root):

    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "In-order traversal of binary tree is:"
print_inorder(root)
print "*************************************"
print "Pre-order traversal of binary tree is"
print_pre_order(root)
print "**************************************"
print "Post-order traversal of binary tree is"
print_post_order(root)
