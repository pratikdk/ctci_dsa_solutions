import random

class Tree:
    def __init__(self):
        self.root = None

    def size(self):
        return 0 if self.root == None else self.root.get_size()

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

    def get_random(self):
        if self.root == None: # Nothing to return
            return None
        index = random.randint(0, self.size()-1)
        return self.root.get_ith_node(index)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def get_ith_node(self, i):
        leftsize = 0 if self.left == None else self.left.get_size()
        if i < leftsize:
            return self.left.get_ith_node(i)
        elif i == leftsize:
            return self
        else:
            return self.right.get_ith_node(i - (leftsize+1))

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


if __name__ == "__main__":
    t = Tree()
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(4)
    t.insert(0)
    print(t.get_random().value)
