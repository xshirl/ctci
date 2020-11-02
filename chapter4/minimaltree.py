import unittest


class BSTNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        string = "(" + str(self.data)
        if self.left:
            string += str(self.left)
        else:
            string += "."
        if self.right:
            string += str(self.right)
        else:
            string += "."
        return string + ")"


def minimal_height_bst(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2
    left = minimal_height_bst(arr[:mid])
    right = minimal_height_bst(arr[(mid+1):])
    return BSTNode(arr[mid], left, right)


def minimalHeightBST(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    left = minimalHeightBST(arr[:mid])
    right = minimalHeightBST(arr[(mid+1):])
    return BSTNode(arr[mid], left, right)


class Test(unittest.TestCase):
    def test_minimal_height_bst(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bst = minimal_height_bst(sorted_array)
        self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")


if __name__ == "__main__":
    unittest.main()
