from stack import Stack

class NodeWithMin:
    def __init__(self, value, min):
        self.value = value
        self.min = min

class StackWithMin(Stack):
    def __init__(self):
        super(StackWithMin, self).__init__()

    def min(self):
        if self.is_empty():
            return float('inf')
        else:
            return self.peek().min

    def push(self, value):
        new_min = min(value, self.min())
        node = NodeWithMin(value, new_min)
        super().push(node)


if __name__ == "__main__":
    s1 = StackWithMin()
    for i in range(20, 200):
        s1.push(i)
    print("Min:", s1.min())
    print("size:", s1.size)
