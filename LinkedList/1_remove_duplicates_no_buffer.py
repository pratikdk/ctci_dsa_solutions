from linked_list import nodelist_builder, printNodes

# def remove_duplicates(node):
#     # Using 2 pointers(heads) current and runner
#     current = node
#     while current != None:
#         runner = current
#         while runner.next != None:
#             if current.data == runner.next.data:
#                 runner.next = runner.next.next #skip
#             else:
#                 runner = runner.next # shift ahead
#         current = current.next


def remove_duplicates(node):
    current = node
    runner = node.next
    while runner != None:
        while current.data == runner.data:
            runner = runner.next
            current.next = runner
        current = current.next
        runner = runner.next


if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
    head = nodelist_builder(data)
    remove_duplicates(head)
    printNodes(head)
