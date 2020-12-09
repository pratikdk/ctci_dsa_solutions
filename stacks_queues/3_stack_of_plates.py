from stack import Stack

class Thresholded_stack:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def push(self, value):
        last = self.get_last_stack()
        if last != None and !last.is_full():
            last.push(value)
        else:
            new_stack = Stack(self.capacity)
            new_stack.push(value)
            self.stacks.append(new_stack)

    def pop(self):
        last = self.get_last_stack()
        if last == None:
            raise Exception("Stack is empty, Nothing to pop()")
        value = last.pop()
        if last.is_empty():
            self.stacks.pop()
        return value
