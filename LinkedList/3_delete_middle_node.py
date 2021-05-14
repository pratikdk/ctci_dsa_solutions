from linked_list import nodelist_builder, printNodes

def delete_middle_node(node):
    # node.data = node.next.data
    # node.next = node.next.next
    slow = node
    fast = node
    previous = None
    while fast.next and fast.next.next:
        #if fast.next.next:
        previous = slow
        slow = slow.next
        fast = fast.next.next
    previous.next = slow.next


if __name__ == "__main__":
    #data = [1, 2, 3, 4, 4, 5, 8, 9, 10]
    data = [1, 2, 3, 4, 5, 6]
    head = nodelist_builder(data)
    delete_middle_node(head)
    #delete_middle_node(head.next.next)
    printNodes(head)
