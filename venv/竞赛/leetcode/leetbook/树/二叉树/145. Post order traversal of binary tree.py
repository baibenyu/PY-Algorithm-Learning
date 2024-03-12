# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 7:54'

import time
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:迭代-后序--与前序不同在于先向右下遍历--得到的排序是根右左,所以在返回时要逆向返回得到左右根
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]

    # 方法二:递归
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal2(root.left) + self.postorderTraversal2(root.right) + [root.val]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
