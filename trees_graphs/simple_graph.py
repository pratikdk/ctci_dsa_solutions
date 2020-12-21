class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        src_node = Node(src)
        dest_node = Node(dest)
        # assign src_node's next to whatever is first at dest, vice versa
        src_node.next = self.graph[dest]
        dest_node.next = self.graph[src]

        # Place dest_node at source and src_node at dest
        self.graph[src] = dest_node
        self.graph[dest] = src_node

    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i} \nhead", end="")
            temp = self.graph[i]
            while temp != None:
                print(f" -> {temp.value}", end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    # Print Adjacency list
    graph.print_graph()
