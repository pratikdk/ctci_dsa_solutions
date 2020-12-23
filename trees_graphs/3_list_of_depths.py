from tree_node import TreeNode

def createLevelLinkedList(root):
    res = []
    group_depth_wise(root, res, 0)
    return res

def group_depth_wise(root, res, level):
    if root == None:
        return
    curr_level = None
    if len(res) == level:
        curr_level = []
        res.append(curr_level)
    else:
        curr_level = res[level]
    curr_level.append(root)
    group_depth_wise(root.left, res, level+1)
    group_depth_wise(root.right, res, level+1)

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
