def get_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_nodes(graph.get_nodes())

def build_graph(vals, dependencies):
    graph = Graph()
    for val in vals:
        graph.get_or_create_node(val)
    # Add edges
    for dependency in dependencies:
        graph.add_edge(dependency[0], dependency[1])
    return graph


def order_nodes(nodes):
    order = []
    shift_nondependent_nodes(order, nodes)
    tobe_processed = 0
    while tobe_processed < len(order):
        curr_node = order[tobe_processed]
        if curr_node == None:
            return None
        children = curr_node.get_children()
        for child in children:
            curr_node.remove_neighbor(child)
        shift_nondependent_nodes(order, children)
        tobe_processed += 1
    return order


def shift_nondependent_nodes(order, nodes):
    for node in nodes:
        if node.get_dependency_count() == 0:
            order.append(node)

class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def get_or_create_node(self, val):
        if val not in self.map:
            node = Node(val)
            self.nodes.add(node)
            self.map[val] = node
        return self.map[val]

    def add_edge(self, val_a, val_b):
        node_a = self.get_or_create_node(val_a)
        node_b = self.get_or_create_node(val_b)
        node_a.add_neighbor(node_b)

    def get_nodes(self):
        return self.nodes

class Node:
    def __init__(self, value):
        self.value = value
        #self.children = []
        self.map = []
        self.n_dependencies = 0

    def add_neighbor(self, node_b):
        if node_b.value not in self.map:
            #self.children.append(node_b)
            self.map[node_b.value] = node_b
            node_b.increment_dep()

    def remove_neighbor(self, node_b):
        if node_b.value in self.map:
            del self.map[node_b.val]
            node_b.decrement_dep()

    def get_children(self):
        return list(self.map.values())

    def get_dependency_count(self):
        return self.n_dependencies

    def increment_dep(self):
        self.n_dependencies += 1

    def decrement_dep(self):
        self.n_dependencies -= 1
