# Breadth first approach
from tree_node import TreeNode

def createLevelLinkedList(root):
    res = []
    current = []
    if root != None:
        current.append(root)
    while current:
        res.append(current)
        parents = current
        current = []
        for parent in parents:
            if parent.left != None:
                current.append(parent.left)
            if parent.right != None:
                current.append(parent.right)
    return res

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    level_list = createLevelLinkedList(n1)
    print(len(level_list))
