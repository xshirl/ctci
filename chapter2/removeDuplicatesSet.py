class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def removeDuplicatesWithSet(self, head: Node) -> Node:
        hashSet = set()
        node = head
        prev = None
        while node:
            if node.data not in hashSet:
                hashSet.add(node.data)
                prev = node
            else:
                prev.next = node.next
            node = node.next
        return head
