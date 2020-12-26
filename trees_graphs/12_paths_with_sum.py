from tree_node import TreeNode

def count_paths_with_sum(root, target_sum):
    if root == None: return 0

    paths_from_root = count_paths_with_sum_from_node(root, target_sum, 0)

    paths_from_left = count_paths_with_sum(root.left, target_sum)
    paths_from_right = count_paths_with_sum(root.right, target_sum)

    return paths_from_root + paths_from_left + paths_from_right


def count_paths_with_sum_from_node(root, target_sum, running_sum):
    if root == None: return 0

    running_sum += root.value
    path_count = 0
    if running_sum == target_sum:
        path_count += 1

    path_count += count_paths_with_sum_from_node(root.left, target_sum, running_sum)
    path_count += count_paths_with_sum_from_node(root.right, target_sum, running_sum)

    return path_count


def inorder_print(root, collater):
    if root == None: return
    inorder_print(root.left, collater)
    collater.append(root.value)
    inorder_print(root.right, collater)


if __name__ == "__main__":
    vals = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    #vals  = [1, 2, 3]
    buffer = []
    t_root = TreeNode(vals[0])
    buffer.append(t_root)
    val_head = 1
    while buffer:# and val_head < len(vals):
        next_buffer = []
        for n in buffer:
            if val_head < len(vals):
                print(n.value, val_head)
                # Create
                n_l = TreeNode(vals[val_head]) if vals[val_head] else None
                val_head += 1
                n_r = TreeNode(vals[val_head]) if vals[val_head] else None
                val_head += 1
                # Connect
                n.left = n_l
                n.right = n_r
                # pop and push
                if n_l: next_buffer.append(n_l)
                if n_r: next_buffer.append(n_r)
        buffer = next_buffer
    cons_array = []
    inorder_print(t_root, cons_array)
    print(cons_array)
    print(count_paths_with_sum(t_root, 8))
