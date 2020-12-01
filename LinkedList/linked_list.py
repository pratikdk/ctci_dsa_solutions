class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = self.tail = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def linkedList_builder(data):
    llist = LinkedList()
    previous = None
    for i in data:
        if llist.head:
            previous.next = Node(i)
            previous = previous.next
        else:
            llist.head = Node(i)
            previous = llist.head
    return llist

def nodelist_builder(data):
    head = None
    tail = None
    for i in data:
        if head:
            tail.next = Node(i)
            tail = tail.next
        else:
            head = tail = Node(i)
    return head

def printNodes(head):
    while(head):
        print(head.data)
        head = head.next

if __name__ == "__main__":
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head = first
    first.next = second
    second.next = third

    llist.printList()
