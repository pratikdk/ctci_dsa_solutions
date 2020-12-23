from tree_node import TreeNode

def is_balanced(root):
    if root == None: return True
    # Check if height is violated
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1: # 1 diff is allowed
        return False
    else: # recurse further and back to root, publish violation status
        return is_balanced(root.left) and is_balanced(root.right)


def get_height(root):
    if root == None: return -1
    return max(get_height(root.left), get_height(root.right)) + 1


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
