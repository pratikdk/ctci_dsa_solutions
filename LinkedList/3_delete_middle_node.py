from linked_list import nodelist_builder, printNodes

def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    head = nodelist_builder(data)
    delete_middle_node(head.next.next)
    printNodes(head)
