from tree_node import TreeNode

def contains_tree(t1, t2):
    if t2 == None: return True
    return is_subtree(t1, t2)

def is_subtree(r1, r2):
    if r1 == None: return False
    if r1.value == r2.value and matchtree(r1, r2):
        return True
    return is_subtree(r1.left, r2) or is_subtree(r1.right, r2)

def matchtree(r1, r2):
    if r1 == None and r2 == None: return True
    elif r1 == None or r2 == None: return False
    elif r1.value != r2.value: return False
    else:
        return matchtree(r1.left, r2.left) and matchtree(r1.right, r2.right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2.left = n1
    n2.right = n4
    n4.left = n3
    n4.right = n5
    print(matchtree(n3, n3))
