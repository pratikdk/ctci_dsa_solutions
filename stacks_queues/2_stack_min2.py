from stack import Stack

class StackWithMinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, value):
        if value <= self.min():
            self.min_stack.push(value)
        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.min_stack.pop()
        return value

    def min(self):
        if self.min_stack.is_empty():
            return float('inf')
        else:
            return self.min_stack.peek()


if __name__ == "__main__":
    s1 = StackWithMinStack()
    for i in range(20, 200):
        s1.push(i)
    print("Min:", s1.min())
    print("size:", s1.size)
