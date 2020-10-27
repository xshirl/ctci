class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def intersection(head1, head2):

    nodes = {}
    node = head1
    while node:
        nodes[node] = True
        node = node.next
    node = head2
    while node:
        if node in nodes:
            return node
        node = node.next
    return None


def intersection2(head1, head2):
    nodes = {}
    node = head1
    while node:
        nodes[node] = True
        node = node.next
    node = head2
    while node:
        if node in nodes:
            return node
        node = node.next
    return None
