class BSTNode:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def minimal_height_bst(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    left = minimal_height_bst(arr[:mid])
    right = minimal_height_bst(arr[(mid+1):])
    return BSTNode(arr[mid], left, right)
