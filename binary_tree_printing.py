# define the structure of a node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data      # store the value
        self.left = None      # left child (initially empty)
        self.right = None     # right child (initially empty)

# define the binary tree and its traversal methods
class BinaryTree:
    def __init__(self):
        self.root = None      # start with an empty tree

    def in_order(self, node):  # left → root → right
        if node:
            self.in_order(node.left)         # visit left subtree
            print(node.data, end=' ')        # visit root
            self.in_order(node.right)        # visit right subtree

    def pre_order(self, node):  # root → left → right
        if node:
            print(node.data, end=' ')        # visit root
            self.pre_order(node.left)        # visit left subtree
            self.pre_order(node.right)       # visit right subtree

    def post_order(self, node):  # left → right → root
        if node:
            self.post_order(node.left)       # visit left subtree
            self.post_order(node.right)      # visit right subtree
            print(node.data, end=' ')        # visit root

# create a binary tree
t = BinaryTree()
t.root = Node(5)                 # root node
t.root.left = Node(3)           # left child of root
t.root.right = Node(7)          # right child of root

# print nodes in different traversal orders
print("In-order:")
t.in_order(t.root)
print()

print("Post-order:")
t.post_order(t.root)
print()

print("Pre-order:")
t.pre_order(t.root)
print()
