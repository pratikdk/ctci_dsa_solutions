from tree_node import TreeNode
def check_bst(root):
    array = []
    copy_bst(root, array)
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True

def copy_bst(root, array):
    if root == None: return
    copy_bst(root.left, array)
    array.append(root.value)
    copy_bst(root.right, array)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    print("is bst:", check_bst(n1))
    # n2.left = n1
    # n2.right = n3
    # print("is bst:", check_bst(n1))
