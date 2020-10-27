from Node import Node


def intersection(l1, l2):
    a = l1
    b = l2

    def length(n):
        length = 0
        curr = n
        while curr:
            curr = curr.next
            length += 1
        return length
    lenA = length(a)
    lenB = length(b)
    if lenA > lenB:
        for _ in range(lenA - lenB):
            a = a.next
    else:
        for _ in range(lenB - lenA):
            b = b.next
    while a != b:
        a = a.next
        b = b.next
    return a
