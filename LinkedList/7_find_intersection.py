from linked_list import Node, nodelist_builder, printNodes

class Result():
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def get_tail_and_size(node):
    counter = 0
    while node != None:
        counter += 1
        node = node.next
    return Result(node, counter)

def get_kth_node(node, k):
    while k>0 and node != None:
        node = node.next
        k -= 1
    return node


def find_intersection(node1, node2):
    result1 = get_tail_and_size(node1)
    result2 = get_tail_and_size(node2)
    if result1.tail != result2.tail:
        return None
    shorter = node1 if result1.size < result2.size else node2
    longer = node2 if result1.size < result2.size else node1
    # Shift head of longer list
    longer = get_kth_node(longer, abs(result1.size - result2.size))
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return longer


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    # list 1
    n1.next = n2
    n2.next = n3
    n3.next = n5
    # List 2
    n4.next = n3
    n3.next = n5

    printNodes(n1)
    print()
    printNodes(n4)
    print("Intersection:", find_intersection(n1, n4).data)
