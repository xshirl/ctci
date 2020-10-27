class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def is_balanced(binary_tree):

    if not binary_tree:
        return (True, 0)

    (left_balanced, left_depth) = is_balanced(binary_tree.left)

    if not left_balanced:
        return (False, None)

    (right_balanced, right_depth) = is_balanced(binary_tree.right)
    if (not right_balanced) or (abs(left_depth - right_depth) > 1):
        return (False, None)

    depth = max(left_depth, right_depth) + 1

    return (True, depth)
