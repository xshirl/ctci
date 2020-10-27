import Node


class Solution:
    def deleteMiddle(self, node: Node) -> bool:
        if node is None or node.next is None:
            return False
        next = node.next
        node.val = next.val
        node.next = next.next
        return True
