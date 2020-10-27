class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("Previous node not in list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def kthfromLast(self, k):
        temp = self.head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if k > length:
            print("Location is greater than length")
            return

        temp = self.head
        for i in range(0, length - k):
            temp = temp.next
        print(temp.data)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('C')
llist.append('B')
llist.append('D')
llist.kthfromLast(2)
llist.kthfromLast(3)
