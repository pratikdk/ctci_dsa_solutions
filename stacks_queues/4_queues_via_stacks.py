from stack import Stack

class QueueStack:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def size(self):
        return self.push_stack.size + self.pop_stack.size

    def enqueue(self, value):
        self.push_stack.push(value)

    def dequeue(self):
        self.fill_pop_stack()
        return self.pop_stack.pop()

    def peek(self):
        self.fill_pop_stack()
        return self.pop_stack.peek()

    def fill_pop_stack(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())


if __name__ == "__main__":
    qs = QueueStack()
    qs.enqueue(1)
    qs.dequeue()
    qs.enqueue(2)
    qs.dequeue()
    print("Final size:", qs.size())
