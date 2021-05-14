# (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295
from linked_list import Node, nodelist_builder, printNodes

class PartialSum():
    sum = None
    carry = 0

def get_length(node):
    counter = 0
    while node:
        counter += 1
        node = node.next
    return counter

def pad(node, padcount):
    for _ in range(padcount):
        node = insert_before(node, 0)
    return node

def insert_before(node, value):
    new_node = Node(value)
    new_node.next = node
    return new_node

def sum_two_list(node1, node2):
    len1 = get_length(node1)
    len2 = get_length(node2)
    if len1 < len2: # pad list 1
        node1 = pad(node1, len2-len1)
    else:
        node2 = pad(node2, len1-len2)
    # print(get_length(node1), get_length(node2))
    # print(node1.data, node2.data)
    sum = sum_list_helper(node1, node2)
    if sum.carry == 0:
        return sum.sum
    else:
        result = insert_before(sum.sum, sum.carry)
        return result

def sum_list_helper(node1, node2):
    if node1 == None and node2 == None:
        sum = PartialSum()
        return sum
    sum = sum_list_helper(node1.next, node2.next)
    value = sum.carry + node1.data + node2.data
    sum.sum = insert_before(sum.sum, value%10)
    sum.carry = value//10
    return sum

if __name__ == "__main__":
    data = [
        ([6, 1, 7, 1], [2, 9, 5]),
        ([9, 9], [9, 9])
    ]
    # head1 = nodelist_builder(data[0][0])
    # head2 = nodelist_builder(data[0][1])
    # rhead = sum_two_list(head1, head2)
    # sum_two_list(head1, head2)
    # printNodes(rhead)

    for d in data:
        head1 = nodelist_builder(d[0])
        head2 = nodelist_builder(d[1])
        rhead = sum_two_list(head1, head2)
        printNodes(rhead)
        print()
