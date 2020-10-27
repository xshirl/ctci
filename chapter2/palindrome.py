class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += "," + str(self.next)


def copy(node):
    if node:
        return Node(node.data, node.next)
    else:
        return None


def copy_reverse(head):
    prev = None
    node = copy(head)
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = copy(next)

    return prev


def is_palindrome(head):
    forward, backward = head, copy_reverse(head)
    while forward:
        if forward.data != backward.data:
            return False
        forward, backward = forward.next, backward.next
    return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Node) -> bool:
        fast = slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True
