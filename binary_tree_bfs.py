# Binary tree search/traverse
# 1. Breadth first search
# 2. Depth first search

# Two ways of printing
# 1. At level order
# 2. At given level

# Example binary tree
#                      1
#               2               3
#           4       5

# Level order traversal or breadth first search is 1 2 3 4 5


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_level_order(root):
    if root is None:
        return None

    queue = []
    queue.append(root)

    while len(queue) > 0:
        print queue[0].data
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Level Order Traversal of binary tree is -"
print_level_order(root)
