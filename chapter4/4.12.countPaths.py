# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        def countPaths(root, target, currentSum):
            if root is None:
                return 0

            currentSum += root.val

            totalPaths = 0
            if currentSum == target:
                totalPaths += 1

            totalPaths += countPaths(root.left, target, currentSum)
            totalPaths += countPaths(root.right, target, currentSum)
            return totalPaths

        paths = countPaths(root, sum, 0)
        leftPaths = self.pathSum(root.left, sum)
        rightPaths = self.pathSum(root.right, sum)
        return paths + leftPaths + rightPaths
