from linked_list import nodelist_builder, printNodes

class Count:
    def __init__(self):
        self.value = 0

def find_kth_to_last(node, k, count):
    if node == None:
        return None
    n = find_kth_to_last(node.next, k, count)
    count.value += 1
    if count.value == k:
        return node
    return n


def kth_to_last(node, k):
    count = Count()
    return find_kth_to_last(node, k, count)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    head = nodelist_builder(data)
    print("value:", kth_to_last(head, 4).data)
