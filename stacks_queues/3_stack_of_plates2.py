class ThresholdedStack2:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def push(self, value):
        last = self.get_last_stack()
        if last != None and not last.is_full():
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

    def is_full(self):
        last = self.get_last_stack()
        return last != None and last.is_full()

    def is_empty(self):
        last = self.get_last_stack()
        return last == none or last.is_empty()

    def pop_at(self, index): # pop from stacks[index]
        return leftshift(index, true)

    def leftshift(self, index, pop_top):
        stack = self.stacks[index]
        popped_item = None
        if pop_top == True:
            popped_item = stack.pop()
        else:
            popped_item = stack.pop_bottom()
        if stack.is_empty():
            stacks.pop()
        elif len(stacks) > index+1:
            left_popped = self.leftshift(index+1, False)
            stack.push(left_popped)
        return remove

class DLLStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.is_full():
            raise Exception("Stack full!!")
        new_node = Node(value)
        self.size += 1
        if self.size == 1:
            self.bottom = new_node
        self.join(new_node, self.top)
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Empty!!")
        popped_node = self.top
        self.top = popped_node.below
        popped_node.below = None
        if self.top != None:
            self.top.above = None
        self.size -= 1
        return popped_node.value

    def pop_bottom(self):
        if self.is_empty():
            raise Exception("Stack Empty!!")
        popped_node = self.bottom
        self.bottom = popped_node.above
        popped_node.above = None
        if self.bottom != None:
            self.bottom.below = None
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty!!")
        return self.top.value

    def join(self, above, below): # old<->new
        if above != None: above.below = below
        if below != None: below.above = above


class Node():
    def __init_(self, value):
        self.value = value
        self.below = None
        self.above = None
