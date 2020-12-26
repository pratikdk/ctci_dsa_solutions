from tree_node import TreeNode

def count_paths_with_sum(root, target_sum):
    return count(root, target_sum, 0, {})

def count(root, target_sum, running_sum, path_map):
    if root == None: return 0
    running_sum += root.value

    paths = path_map.get(running_sum-target_sum, 0)

    if running_sum == target_sum: paths += 1

    increment_map_val(path_map, running_sum, 1)
    paths += count(root.left, target_sum, running_sum, path_map)
    paths += count(root.right, target_sum, running_sum, path_map)
    increment_map_val(path_map, running_sum, -1)

    return paths


def increment_map_val(map, key, value):
    new_value = map.get(key, 0) + value
    if new_value == 0: # when decrementing
        del map[key]
    else:
        map[key] = new_value


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
    #inorder_print(t_root, cons_array)
    print(cons_array)
    print(count_paths_with_sum(t_root, 8))
