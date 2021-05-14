from tree_node import TreeNode
# Think about your are generating ordered permutations
# using a bottom up approach and then weaving(permute) them
def all_sequences(node):
    result = []
    if node == None:
        result.append([])
        return result
    # Seq construction starts from root as first node
    prefix = []
    prefix.append(node.value)
    # Compute left and right perumutations
    left_list = all_sequences(node.left)
    right_list = all_sequences(node.right)
    # Below runs when hit rock bottom
    for left_seq in left_list:
        for right_seq in right_list:
            weaved = []
            weave_left_right_lists(left_seq, right_seq, weaved, prefix)
            result.extend(weaved)
    return result

# Just packs weaved list with weaved left and right sequences
def weave_left_right_lists(left_seq, right_seq, weaved, prefix):
    # if one sequence is empty offload the other to prefix and Return
    if len(left_seq) == 0 or len(right_seq) == 0:
        prefix_copy = prefix.copy()
        prefix_copy.extend(left_seq)
        prefix_copy.extend(right_seq)
        weaved.append(prefix_copy)
        return
    # recurse to pop and push off of a sequence at a time until any of the sequence is empty
    left = left_seq.pop(0)
    prefix.append(left)
    weave_left_right_lists(left_seq, right_seq, weaved, prefix)
    prefix.pop()
    left_seq.insert(0, left)

    right = right_seq.pop(0)
    prefix.append(right)
    weave_left_right_lists(left_seq, right_seq, weaved, prefix)
    prefix.pop()
    right_seq.insert(0, right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    # n4 = TreeNode(0)
    # n5 = TreeNode(-1)
    n2.left = n1
    n2.right = n3
    # n1.left = n4
    # n4.left = n5
    print(all_sequences(n2))
