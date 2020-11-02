from Node import Node


def loopDetection(head):
    nodes = {}
    node = head
    while node:
        if node in nodes:
            return node
        nodes[node] = True
        node = node.next

    return None


def loopDetection2(head):
    node = head
    nodes = {}
    while node:
        if node in nodes:
            return node
        nodes[node] = True
    return None
