from linked_list import Node, nodelist_builder, printNodes

def is_palindrome(node):
    slow = node
    fast = node # Traverses 2x the speed of slow
    stack = []
    while fast != None and fast.next != None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    # Move slow head ahead by one position if odd number of elements
    if fast != None:
        slow = slow.next
    # Return False if elements don't match
    while slow != None:
        if stack.pop() != slow.data:
            return False
        slow = slow.next
    return True


if __name__ == "__main__":
    #data = [1, 2, 3, 4, 4, 5]
    data = [1, 1, 2, 3, 3, 2, 1, 1]
    head = nodelist_builder(data)
    print(is_palindrome(head))
