class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeDupsHashSet(head: Node) -> Node:
    hashSet = set()
    curr = head
    prev = None
    while curr:
        if curr.val not in hashSet:
            hashSet.add(curr.val)
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next


class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
