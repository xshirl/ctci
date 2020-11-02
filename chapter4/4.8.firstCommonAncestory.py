class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def first_common_ancestor(node1, node2):
    search1 = node1
    search2 = node2
    ancestors1, ancestors2 = {}, {}
    while search1 or search2:
        if search1:
            if search1 in ancestors2:
                return search1
            ancestors1[search1] = True
            search1 = search1.parent
        if search2:
            if search2 in ancestors1:
                return search2
            ancestors2[search2] = True
            search2 = search2.parent
    return None
