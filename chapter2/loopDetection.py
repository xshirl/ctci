class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def loopDetection(head):
    nodes = {}
    node = head
    while node:
        if node in nodes:
            return node
        nodes[node] = True
        node = node.next
    return None
