from Node import Node


def isPalindrome(head):
    def copy(node):
        if node:
            return Node(node.val)
        else:
            return None

    def reverse(head):
        prev = None
        node = copy(head)
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
        return prev
    reverse = reverse(head)
    while head:
        if head.val != reverse.val:
            return False
        head = head.next
        reverse = reverse.next
    return True


def palindrome(head):
    def copy(node):
        if node:
            return Node(node.val)
        return None

    def reverse(head):
        prev = None
        node = copy(head)
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
        return prev

    reverse = reverse(head)
    while head:
        if head.val != reverse.val:
            return False
        head = head.next
        reverse = reverse.next
    return True
