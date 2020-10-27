from Node import Node


def partition(head, x):
    h1 = l1 = Node(0)
    h2 = l2 = Node(0)

    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next


class Solution:
    def partition(self, head, x):
        h1 = l1 = Node(0)
        h2 = l2 = Node(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

    def partition2(self, head, x):
        left_head = Node(None)  # head of the list with nodes values < x
        right_head = Node(None)  # head of the list with nodes values >= x
        left = left_head  # attach here nodes with values < x
        right = right_head  # attach here nodes with values >= x
        # traverse the list and attach current node to left or right nodes
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:  # head.val >= x
                right.next = head
                right = right.next
            head = head.next
        right.next = None  # set tail of the right list to None
        left.next = right_head.next  # attach left list to the right
        return left_head.next  # head of a new partitioned list
