from linked_list import Node, nodelist_builder, printNodes

def is_palindrome(node):
    rnode = reverse_and_clone(node)
    return is_equal(node, rnode)

def reverse_and_clone(node):
    head = None
    while node != None:
        new_node = Node(node.data)
        new_node.next = head
        head = new_node
        node = node.next
    return head

def is_equal(node1, node2):
    while node1 != None and node2 != None:
        if node1.data != node2.data:
            return False
        node1 = node1.next
        node2 = node2.next
    return node1 == None and node2 == None # Ensures if completely parsed

if __name__ == "__main__":
    #data = [1, 2, 3, 4, 4, 5]
    data = [1, 1, 2, 3, 3, 2, 1, 1]
    head = nodelist_builder(data)
    print(is_palindrome(head))
