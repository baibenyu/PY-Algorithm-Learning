# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 7:50'

import time
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            nonlocal ans
            if not root:
                return
            else:
                ans.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return ans

    # 方法二:迭代
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        import collections
        if not root:
            return []
        q = collections.deque([root])
        cur = root
        ans = []
        while q:
            while cur:
                ans.append(cur.val)
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            cur = cur.right
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
