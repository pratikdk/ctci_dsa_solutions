from tree_node import TreeNode

def isBST(root):
    return checkBST(root, None, None)

def checkBST(root, min, max):
    if root == None:
        return True
    if (max and max < root.value) or (min and min <= root.value):
        return False
    if not checkBST(root.left, min, root.value) or not checkBST(root.right, root.value, max):
        return False
    return True

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n3
    n1.right = n2
    print("is bst:", isBST(n1))
