class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)


def preOrderTraversal(root):
    if root:
        print(root.val)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val)
