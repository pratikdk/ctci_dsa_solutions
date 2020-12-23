from tree_node import TreeNode

def is_balanced(root):
    return check_height(root) != float('-inf')
    if root == None: return True


def check_height(root):
    if root == None: return -1

    left_height = check_height(root.left)
    if left_height == float('-inf'): return float('-inf')

    right_height = check_height(root.right)
    if right_height == float('-inf'): return float('-inf')

    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n2.left = n3
    n3.left = n4
    n1.right = n5
    print("is balanced:", is_balanced(n1))
