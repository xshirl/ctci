

class MinStack():
    def __init__(self):
        self.top = None
        self.min = None

    def minStack(self):
        if not self.min:
            return None
        return self.min.data

    def push(self, item):
        if self.min and (self.min.data < item):
            self.min = Node(data=self.min.data, next=self.min)
        else:
            self.min = Node(data=item, next=self.min)
        self.top = Node(data=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.min = self.min.next
        item = self.top.data
        self.top = self.top.next
        return item


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
