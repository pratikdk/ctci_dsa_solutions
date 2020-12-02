from linked_list import Node, nodelist_builder, printNodes

def find_loop_begining(node):
    slow = node
    fast = node # 2x faster than slow
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # Collision
            break
    slow = node # Rest slow back to start of list
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    # list 1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n4
    print()
    print("Loop starts at:", find_loop_begining(n1).data)
