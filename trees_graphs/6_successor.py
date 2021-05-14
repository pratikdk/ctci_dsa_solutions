from tree_node import TreeNode

def inorder_succ(n):
    if n == None: return None

    if n.right != None: # if has right subtree
        return get_leftmost_child(n.right)
    else:
        q = n
        x = n.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x

def get_leftmost_child(n):
    while n.left != None:
        n = n.left
    return n


if __name__ == "__main__":
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n_1 = TreeNode(-1)
    n2.left = n1
    n1.parent = n2
    n2.right = n3
    n3.parent = n2
    n0.right = n2
    n2.parent = n0
    n0.left = n_1
    n_1.parent = n0
    print(inorder_succ(n2).value)
