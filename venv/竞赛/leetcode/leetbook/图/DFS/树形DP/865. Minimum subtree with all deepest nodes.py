# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/17 9:38'

import time


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        depth = {None: -1}  # 标记各结点的深度

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        max_depth = max(depth.values())

        def answer(node):  # 回溯找最大深度对应的结点,返回时只返回已有结果的或有两个孩子的
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
