import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 0

    def insert(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        self.size += 1

    def get_random(self):
        leftsize = 0 if self.left == None else self.left.get_size()
        index = random.randint(0, self.size-1)
        if index < leftsize:
            return self.left.get_random()
        elif index == leftsize:
            return this
        else:
            return self.right.get_random()

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            return None if self.left == None else self.left.find(value)
        elif value > self.value:
            return None if self.right == None else self.right.find(value)

    def get_size(self):
        return self.size

    def get_value(self):
        return self.value
