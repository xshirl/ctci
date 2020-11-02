class BSTNode:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if self.head:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
        else:
            self.head = self.tail = ListNode(item)

    def remove(self):
        if not self.head:
            return None
        item = self.head.val
        self.head = self.head.next
        return item


def list_depths(binary_tree):
    if not binary_tree:
        return []
    lists = []
    queue = Queue()
    current_depth = -1
    current_tail = None
    node = binary_tree
    node.depth = 0
    while node:
        if node.depth == current_depth:
            current_tail.next = ListNode(node.val)
            current_tail = current_tail.next
        else:
            current_depth = node.depth
            current_tail = ListNode(node.val)
            lists.append(current_tail)
        for child in [node.left, node.right]:
            if child:
                child.depth = node.depth + 1
                queue.add(child)
        node = queue.remove()
    return lists
