class GraphNode():
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.dependencies_left = 0


class Queue:
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self):
        return self.array.pop(0)

    def is_not_empty(self):
        return len(self.array) > 0


def build_order(projects, dependencies):
    nodes = {}
    for project in projects:
        nodes[project] = GraphNode(project)
    for dependency in dependencies:
        nodes[dependency[0]].add_edge(nodes[dependency[1]])
    queue = Queue()
    for project in projects:
        node = nodes[project]
        if not node.dependencies_left:
            queue.add(node)
    build_order = []
    while queue.is_not_empty():
        node = queue.remove()
        build_order.append(node.data)
        for dependent in node.edges:
            dependent.dependencies_left -= 1
            if not dependent.dependencies_left:
                queue.add(dependent)
    if len(build_order) < len(projects):
        return Exception("Cycle detected")
    return build_order
