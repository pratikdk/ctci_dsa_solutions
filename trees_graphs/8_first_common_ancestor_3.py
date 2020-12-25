from tree_node import TreeNode

def common_ancestor(root, a, b):
    if not covers(root, a) or not covers(root, b):
        return None
    return ancestor_helper(root, a, b)

def ancestor_helper(root, a, b):
    if root == None or root == a or root == b:
        return root
    a_onleft = covers(root.left, a)
    b_onleft = covers(root.left, b)
    if a_onleft != b_onleft:
        return root
    childside = root.left if a_onleft else root.right
    return ancestor_helper(childside, a, b)


def covers(root, b):
    if root == None: return False
    if root == b: return True
    return covers(root.left, b) or covers(root.right, b)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    ##
    n2.left = n1
    n2.right = n3
    n1.parent = n2
    n3.parent = n2
    ##
    n5.left = n4
    n5.right = n6
    n4.parent = n5
    n6.parent = n5
    ##
    print(common_ancestor(n2, n1, n4))
    print(common_ancestor(n2, n1, n3).value)
