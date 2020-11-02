def isBalanced(root):

    def findDepth(root):
        if not root:
            return 0
        left = findDepth(root.left)
        right = findDepth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return findDepth(root) != -1
