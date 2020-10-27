from LinkedList import LinkedList


def sum_list(a, b):
    n1, n2 = a.head, b.head
    ll = LinkedList()
    carry = 0

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.append(result % 10)
        carry = result // 10

    if carry != 0:
        ll.append(carry)

    return ll.print_list()


ll_a = LinkedList()
ll_a.append(4)
ll_a.append(0)
ll_a.append(9)
ll_a.print_list()
ll_b = LinkedList()
ll_b.append(3)
ll_b.append(0)
ll_b.append(9)
ll_b.print_list()
print(sum_list(ll_a, ll_b))
