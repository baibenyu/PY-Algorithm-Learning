# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/16 8:48'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS--后序遍历,层层返回
    def longestConsecutive(self, root: TreeNode) -> int:

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            ans = 1
            # 判断左右子树的根节点值是否为当前节点值+1
            if root.left and root.left.val == root.val + 1:
                ans = max(ans, l + 1)
            if root.right and root.right.val == root.val + 1:
                ans = max(ans, r + 1)
            # 记录最长链
            res = max(res, ans)
            return ans

        res = 0
        dfs(root)
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
