from linked_list import nodelist_builder, printNodes


def kth_to_last(node, k):
    p1 = node # Move this pointer k steps ahead
    p2 = node
    for _ in range(k):
        p1 = p1.next
    print(p1.next.data)
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return p2


if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    head = nodelist_builder(data)
    print("value:", kth_to_last(head, 4).data)
