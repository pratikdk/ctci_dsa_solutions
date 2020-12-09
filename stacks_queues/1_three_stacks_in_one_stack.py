class FixedMultiStack():
    def __init__(self, capacity):
        self.number_of_stacks = 3
        self.capacity = capacity
        self.values = [None]* (self.capacity*self.number_of_stacks)
        self.sizes = [0]*capacity

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception(f"Stack: {stack_num} is full")
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value


    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack: {stack_num} is empty")
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack: {stack_num} is empty")
        return self.values[self.index_of_top(stack_num)]

    # helper methods
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.capacity

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num):
        offset = stack_num * self.capacity
        size = self.sizes[stack_num]
        return offset + size - 1

    def print_stacks(self):
        print(self.values)


if __name__ == "__main__":
    fms = FixedMultiStack(3)
    fms.push(0, 1)
    fms.push(1, 2)
    fms.push(2, 3)
    fms.push(2, 6)
    fms.peek(2)
    fms.pop(2)
    fms.print_stacks()
