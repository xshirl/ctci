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

    def delete(self, key):

        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def delete_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def remove_duplicates(self):
        current = second = self.head
        while current:
            while second.next:   # check second.next here rather than second
                if second.next.data == current.data:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('C')
llist.append('B')
llist.append('D')
llist.reverse_iterative()
llist.remove_duplicates()
llist.print_list()
