class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

    def set_order(self, value):
        self.order = value
    def get_order(self):
        return self.order

    def is_older_than(self, a):
        return self.order < a.get_order()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class AnimalQueue:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.order = 0

    def enqueue(self, a):
        a.set_order(self.order) # Set
        self.order += 1 # Increment
        if isinstance(a, Dog):
            self.dogs.add_last(a)
        elif isinstance(a, Cat):
            self.cats.add_last(a)

    def dequeue_any(self):
        if self.dogs.is_empty():
            return self.dequeue_cat()
        elif self.cats.is_empty():
            return self.dequeue_dog()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.is_older_than(cat):
            return dequeue_dog()
        else:
            return dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.poll()

    def dequeue_cat(self):
        return self.cats.poll()

class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_last(self, value):
        new_node = Node(value)
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def poll(self):
        if self.head == None:
            raise Exception("Linked list is empty")
        value = self.head
        self.head = self.head.next
        return value

    def peek(self):
        if self.head == None:
            raise Exception("Linked list is empty")
        return self.head

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

    def is_empty(self):
        return self.head == None


if __name__ == "__main__":
    pass
    # ll = LinkedList()
    # ll.add_last(1)
    # ll.add_last(2)
    # ll.add_last(3)
    # ll.add_last(4)
    # ll.add_last(5)
    # ll.printList()
    # print()
    # ll.poll()
    # ll.poll()
    # ll.poll()
    # ll.poll()
    # ll.poll()
    # ll.printList()
