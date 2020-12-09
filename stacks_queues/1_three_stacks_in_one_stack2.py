class FlexibleMultiStack():
    class StackInfo:
        def __init__(self, start, capacity):
            self.start = start
            self.capacity = capacity
            self.size = 0

        def is_full(self):
            return self.size == self.capacity

        def is_empty(self):
            return self.size == 0

        def is_within_stack_capacity(self, parent, index):
            if index < 0 or index >= len(parent.values):
                return False
            unwrapped_index = (len(parent.values) + index) if index < start else index
            end = start + self.capacity
            return start <= unwrapped_index && unwrapped_index < end

        def last_capacity_index(self, parent): # Wrap if necessary
            return parent.adjust_index(self.start + self.capacity -1)

        def last_element_index(self, parent): # Wrap if necessary
            return parent.adjust_index(self.start + self.capacity -1)

    def __init__(self, no_of_stacks, default_size):
        self.info = []
        for i in range(no_of_stacks):
            info.append(StackInfo(start=(i*default_size), default_size))
        self.values = [None]*(no_of_stacks*default_size)

    def push(self, stack_num, value):
        if self.all_stacks_are_full():
            raise Exception("All stacks are full")
        # if current stack is full
        stack = self.info[stack_num]
        if stack.is_full():
            self.expand(stack_num)
        # Finally push the element
        stack.size += 1
        self.values[stack.last_element_index()] = value

    def pop(self, stack_num):
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception(f"Stack {stack_num} is empty, Nothing to pop()")
        value = self.values[stack.last_element_index()]
        self.values[stack.last_element_index()] = None
        stack.size -= 1
        return value

    def peek(self, stack_num):
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception(f"Stack {stack_num} is empty, Nothing to peek()")
        return self.values[stack.last_element_index()]

    # Utility methods
    def expand(self, stack_num):
        self.shift((stack_num+1) % len(self.info)) #if 3 stacks -> 1 2 0
        self.info[stack_num].capacity += 1

    def shift(self, stack_num):
        stack = self.info[stack_num]
        if stack.size >= stack.capacity:
            next_stack = (stack_num+1) % len(self.info)
            shift(next_stack)
            stack.capacity += 1
        # Shift all elements in stack over by one
        index = stack.last_capacity_index()
        while stack.is_within_stack_capacity(index):
            previous_index = self.previous_index(index)
            self.values[index] = self.values[previous_index]
            index = previous_index
        # fix start and capacity of new shifted and shrunked stack
        self.values[stack.start] = None
        stack.start = self.next_index(stack.start)
        stack.capacity -= 1

    def no_of_elements(self):
        count = 0
        for stack_info in self.info:
            count += stack_info.size
        return count

    def all_stacks_are_full(self):
        return self.no_of_elements() == len(self.values)

    def adjust_index(self, index):
        max = len(self.values)
        return ((index%max)+max)%max # get a wrapper(wrt max) nummber

    def next_index(self, index):
        return self.adjust_index(index+1)

    def previous_index(self, index):
        return self.adjust_index(index-1)
