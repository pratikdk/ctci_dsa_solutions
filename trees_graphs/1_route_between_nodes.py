# from simple_graph import Graph
# # Solving using breadth first search
# # -1: Unvisited, 0: Visited, 1: Visiting
# def search(graph, start, end):
#     if start == end:
#         return True
#     for node in graph.get_nodes():
#         node.value = -1
#     queue = []
#     start.value = 1
#     queue.append(start)
#     current_node = None
#     while len(queue) > 0: # if queue is not empty
#         current_node = queue.pop(0)
#         for adjacent_node in graph.get_adjacents(current_node):
#             if adjacent_node.value == -1:
#                 if adjacent_node == end:
#                     return true
#                 else: # push it to queue
#                     adjacent_node.value = 1
#                     queue.append(adjacent_node)
#         current_node.value = 0 # Demark current node
#     return False


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def bfs_util(start_node, end_node, visited):
    queue = []
    queue.append(start_node)
    visited[start_node.value] = True
    while queue:
        u = queue.pop(0)
        if u == end_node:
            return True
        for v in [u.left, u.right]:
            if v and visited[v.value] == False:
                queue.append(v)
                visited[v.value] = True
    return False

def is_path(total_nodes, start, end):
    visited = [False] * total_nodes
    if bfs_util(start, end, visited):
        return True
    return False


if __name__ == "__main__":
    n = 5
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n2.left = n1
    n1.left = n0
    n2.right = n4
    n4.left = n3
    print(is_path(n, n2, n3))
    print(is_path(n, n0, n3))
