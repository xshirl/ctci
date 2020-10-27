class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition(node, x):
    beforeStart = beforeEnd = afterStart = afterEnd = None
    while node:
        next = node.next
        node.next = None
        if (node.data < x):
            if beforeStart is None:
                beforeStart = node
                beforeEnd = beforeStart
            else:
                beforeEnd.next = node
                beforeEnd = node
        else:
            if afterStart is None:
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node
        node = next
    if beforeStart is None:
        return afterStart
    beforeStart.next = afterStart
    return beforeStart


def partition2(node, x):
    head = node
    tail = node
    while node:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head
