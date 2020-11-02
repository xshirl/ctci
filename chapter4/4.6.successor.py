class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def successor(root):
    if not root:
        return None
    child = root.right
    if child:
        while child.left:
            child = child.left
    if child:
        return child
    if root.parent and root.parent.val > root.val:
        return root.parent

    return None
