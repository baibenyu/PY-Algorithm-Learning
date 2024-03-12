# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/22 10:54'

import time


def build_tree(arr, tree, node, left, right):  # 构建一颗线段树,父节点值等于左右孩子节点值之和
    if left == right:
        tree[node] = arr[left]
        return
    else:
        mid = left + ((right - left) >> 1)
        left_node = 2 * node + 1  # 左右孩子在树的数组中的下标
        right_node = 2 * node + 2
        build_tree(arr, tree, left_node, left, mid)
        build_tree(arr, tree, right_node, mid + 1, right)

        tree[node] = tree[left_node] + tree[right_node]


def update_tree(arr, tree, node, left, right, index, val):  # 更改某个值
    if left == right:
        arr[index] = val
        tree[node] = val
        return
    else:
        mid = left + ((right - left) >> 1)
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        if index <= mid:
            update_tree(arr, tree, left_node, left, mid, index, val)
        else:
            update_tree(arr, tree, right_node, mid + 1, right, index, val)
        tree[node] = tree[left_node] + tree[right_node]


def query_tree(arr, tree, node, left, right, L, R):  # 查询一段区间的和
    if R < left or L > right:
        return 0
    elif L <= left and right <= R:
        return tree[node]
    elif left == right:
        return tree[node]
    else:
        mid = left + ((right - left) >> 1)
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        left_sum = query_tree(arr, tree, left_node, left, mid, L, R)
        right_sum = query_tree(arr, tree, right_node, mid + 1, right, L, R)
        return left_sum + right_sum


if __name__ == '__main__':
    start = time.clock()
    arr = [i for i in range(1, 12, 2)]
    length = len(arr)
    tree = [0 for i in range(1000)]
    build_tree(arr, tree, 0, 0, length - 1)
    for i in range(16):
        print(tree[i])
    print("我是更新的分割线-------------------------------")
    update_tree(arr, tree, 0, 0, length - 1, 4, 5)
    for i in range(16):
        print(tree[i])
    print(query_tree(arr, tree, 0, 0, length - 1, 2, 5))
    end = time.clock()
    print(end - start)
