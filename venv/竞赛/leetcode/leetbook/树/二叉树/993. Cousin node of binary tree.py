# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/3 8:41'
import collections
import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:BFS
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False

        # 用来判断是否遍历到 x 或 y 的辅助函数
        def update(node: TreeNode, parent: TreeNode, depth: int):
            if node.val == x:
                nonlocal x_parent, x_depth, x_found
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                nonlocal y_parent, y_depth, y_found
                y_parent, y_depth, y_found = parent, depth, True

        q = collections.deque([(root, 0)])
        update(root, None, 0)

        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, node, depth + 1)
            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, node, depth + 1)

            if x_found and y_found:
                break

        return x_depth == y_depth and x_parent != y_parent


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
