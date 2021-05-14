from tree_node import TreeNode

def common_ancestor(a, b):
    delta = depth(a) - depth(b)
    shallow_node = b if delta > 0 else a
    deeper_node = a if delta > 0 else b
    deeper_node = go_upby(deeper_node, abs(delta))
    while shallow_node != deeper_node and shallow_node != None and deeper_node != None:
        # move up for both
        shallow_node = shallow_node.parent
        deeper_node = deeper_node.parent
    # Falsify if any node touched None(exited the root)
    #return shallow_node if shallow_node and deeper_node else None
    return None if shallow_node == None or deeper_node == None else shallow_node

def go_upby(node, delta):
    while delta > 0 and node != None:
        node = node.parent
        delta -= 1
    return node

def depth(node):
    depth = 0
    while node != None and node.parent != None:
        node = node.parent
        depth += 1
    return depth

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
    print(common_ancestor(n1, n4))
    print(common_ancestor(n1, n3).value)
