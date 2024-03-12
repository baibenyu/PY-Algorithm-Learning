# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/3 7:22'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:迭代DFS
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        path, pos = list(), 0
        while pos < len(traversal):
            level = 0
            while traversal[pos] == '-':  # 求层数
                level += 1
                pos += 1
            value = 0

            while pos < len(traversal) and traversal[pos].isdigit():  # 求当前结点的值
                value = value * 10 + (ord(traversal[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)

            if level == len(path):  # 建树,一条直线
                if path:
                    path[-1].left = node
            else:  # 回溯到父结点
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
