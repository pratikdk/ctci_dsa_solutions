from linked_list import nodelist_builder, printNodes
from linked_list import LinkedList, linkedList_builder

def remove_duplicates(node):
    map = {}
    previous = None
    while(node != None):
        if node.data not in map:
            map[node.data] = 1
            if previous:
                previous.next = node
                previous = previous.next
            else:
                previous = node
        node = node.next

if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    head = nodelist_builder(data)
    remove_duplicates(head)
    printNodes(head)


# def remove_duplicates(llist):
#     map = {}
#     previous = None
#     head = llist.head
#     while(head != None):
#         if head.data not in map:
#             map[head.data] = 1
#             if previous:
#                 previous.next = head
#                 previous = previous.next
#             else:
#                 previous = head
#         head = head.next


# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 4, 5]
#     llist = linkedList_builder(data)
#     llist.printList()
#     remove_duplicates(llist)
#     llist.printList()


# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def plug(self, i):
#         new_node = Node(i)
#         head_node = self
#         while(head_node.next != None):
#             head_node = head_node.next
#         head_node.next = new_node
#
# def printLL(head_node, flag=False):
#     while(head_node != None):
#         print(head_node.data)
#         print(hex(id(head_node)))
#         if head_node.data == 2 and flag:
#             head_node.data = 20
#             print(head_node.data)
#             print(hex(id(head_node)))
#         head_node = head_node.next
#
# # def modz(z):
# #     z = 20
# #     print()
#
#
# if __name__ == "__main__":
#     head = Node(0)
#     for i in range(1, 11):
#         n = Node(i)
#         head.plug(i)
#     # printLL(head)
#     # print()
#     head = head.next
#     head = head.next
#     printLL(head, True)
#     #print(head.data)
#     #print(hex(id(head)))
#     printLL(head)
#     print(head.data)
#     #print(head.data)
#     # a = 100
#     # modz(a)
#     # print(a)
