class Node():
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list or []
        self.shortest_path = None

    def add_edge_to(self, node):
        self.adjacency_list += [node]

    def __str__(self):
        return self.data


class Queue():
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item


def find_route(node1, node2):
    path = None
    queue = Queue()
    node = node1
    node.shortest_path = [node]
    all_visited_nodes = [node]
    while node:
        for adjacent in node.adjacency_list:
            if not adjacent.shortest_path:
                adjacent.shortest_path = node.shortest_path + [adjacent]
                if adjacent == node2:
                    path = node.shortest_path + [adjacent]
                    break
                queue.add(adjacent)
                all_visited_nodes.append(adjacent)
            node = queue.remove()
    for visited in all_visited_nodes:
        visited.shortest_path = None
    return path
