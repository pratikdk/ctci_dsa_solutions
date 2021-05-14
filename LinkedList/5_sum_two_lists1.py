# (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295

from linked_list import Node, nodelist_builder, printNodes

def sum_two_list(node1, node2, carry):
    if (node1==None) and (node2==None) and (carry==0):
        return None
    result = Node()
    value = carry
    if node1 != None:
        value += node1.data
    if node2 != None:
        value += node2.data
    result.data = value%10
    carry = value//10
    if (node1 != None) or (node2 != None):
        node = sum_two_list(None if node1==None else node1.next,
                            None if node2==None else node2.next,
                            carry)
        result.next = node
    return result


if __name__ == "__main__":
    data = [
        #([7, 1, 6], [5, 9, 2])
        ([6, 1, 7], [2, 9, 5]),
        ([9, 9], [9, 9])
    ]
    for d in data:
        head1 = nodelist_builder(d[0])
        head2 = nodelist_builder(d[1])
        rhead = sum_two_list(head1, head2, 0)
        #delete_middle_node(head.next.next)
        printNodes(rhead)
        print()
