from simple_graph import Graph
# Solving using breadth first search
# -1: Unvisited, 0: Visited, 1: Visiting
def search(graph, start, end):
    if start == end:
        return True
    for node in graph.get_nodes():
        node.value = -1
    queue = []
    start.value = 1
    queue.append(start)
    current_node = None
    while len(queue) > 0: # if queue is not empty
        current_node = queue.pop(0)
        for adjacent_node in graph.get_adjacents(current_node):
            if adjacent_node.value == -1:
                if adjacent_node == end:
                    return true
                else: # push it to queue
                    adjacent_node.value = 1
                    queue.append(adjacent_node)
        current_node.value = 0 # Demark current node
    return False
