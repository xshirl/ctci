class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate(root: TreeNode):

    def check(root, mn, mx):
        if root is None:
            return True
        if root.val <= mn or root.val >= mx:
            return False
        return check(root.left, mn, min(mx, root.val) and check(root.right, max(root.val, mn), mx))
    return check(root, -float('inf'), float('inf'))
