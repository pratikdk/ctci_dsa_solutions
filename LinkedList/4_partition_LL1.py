from linked_list import nodelist_builder, printNodes

def partition(node, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while node != None:
        next = node.next
        node.next = None # Dereference next pointer
        if node.data < x:
            if before_start == None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = before_end.next
        else:
            if after_start == None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = after_end.next
        node = next
    if before_start == None:
        return after_start
    # Merge before and after linked list
    before_end.next = after_start
    return before_start


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
