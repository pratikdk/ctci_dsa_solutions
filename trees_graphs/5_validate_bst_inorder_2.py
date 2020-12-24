from tree_node import TreeNode

def check_bst(root, last_printed):
    if root == None: return True

    if not check_bst(root.left, last_printed): return False

    if last_printed != None and root.value <=  last_printed: return False
    last_printed = root.value

    if not check_bst(root.right, last_printed): return False

    return True

if __name__ == "__main__":
    last_printed = None
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n3
    n1.right = n2
    print("is bst:", check_bst(n1, last_printed))
