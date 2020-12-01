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
