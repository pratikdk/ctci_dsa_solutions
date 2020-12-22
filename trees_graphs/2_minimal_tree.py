from tree_node import TreeNode

def create_minimal_bst(array):
    return create_tree(array, 0, len(array)-1)

def create_tree(array, start, end):
    if end < start:
        return None
    mid = int((start+end)/2)
    mid_node = TreeNode(array[mid])
    mid_node.left = create_tree(array, start, mid-1)
    mid_node.right = create_tree(array, mid+1, end)
    return mid_node

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    tree_mid = create_minimal_bst(arr)
    print(tree_mid)
