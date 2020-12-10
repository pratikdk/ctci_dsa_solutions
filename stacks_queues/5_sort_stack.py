from stack import Stack

class SortStack(Stack):
    def __init__(self):
        super().__init__()

    def sort(self):
        s1 = super()
        s2 = Stack()
        while not s1.is_empty():
            tmp = s1.pop()
            while (not s2.is_empty()) and s2.peek() > tmp:
                s1.push(s2.pop())
            s2.push(tmp)
        while not s2.is_empty():
            s1.push(s2.pop())

if __name__ == "__main__":
    ss = SortStack()
    for i in range(1, 11):
        ss.push(i)
    print(ss)
    ss.sort()
    print(ss)
    print(ss.peek())
