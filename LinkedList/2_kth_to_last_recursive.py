from linked_list import nodelist_builder, printNodes

# def kth_to_last(node, k):
#     if node == None:
#         return 0
#     count = kth_to_last(node.next, k) + 1
#     if count == k:
#         print("Node value:", node.data)
#     return count

def kth_to_last(node, k):
    if node == None:
        return (0, None, False)
    count, n, stop_count = kth_to_last(node.next, k)
    if not stop_count:
        count = count + 1
        n = node
    if count == k:
        return (count, n, True)
    else:
        return (count, n, stop_count)



if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    head = nodelist_builder(data)
    count, n, _ = kth_to_last(head, 4)
    print(f"k:{count}, val:{n.data}")
    #printNodes(head)
