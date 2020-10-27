class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def returnKthToLast(self, head: Node, k: int) -> int:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        temp = head
        for _ in range(length - k):
            temp = temp.next

        return temp.val

    def returnKthFromLast2(self, head: Node, k: int) -> int:
        fast = slow = head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
# O(n) time
