from linked_list import nodelist_builder, printNodes

def partition(node, x):
    head = node
    tail = node
    while node != None:
        next = node.next
        if node.data < x:
            # Insert at head
            node.next = head
            head = node
        else:
            # Insert at tail
            tail.next = node
            tail = node
        node = next
    # Dereference tail
    tail.next = None
    return head


if __name__ == "__main__":
    data = [
        ([10, 1, 2, 3, 4, 4, 5], 3),
        ([3, 5, 8, 5, 10, 2, 1], 5)
    ]
    for test_tuple in data:
        head = nodelist_builder(test_tuple[0])
        new_head = partition(head, test_tuple[1])
        printNodes(new_head)
        print()
