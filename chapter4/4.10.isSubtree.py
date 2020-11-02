class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSubtree(s, t) -> bool:
    def match(s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val) and match(s.left, t.left) and match(s.right, t.right)

    if match(s, t):
        return True
    if not s:
        return False
    return isSubtree(s.left, t) or isSubtree(s.right, t)
