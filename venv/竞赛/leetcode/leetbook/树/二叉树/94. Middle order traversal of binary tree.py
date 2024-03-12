# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 7:53'

import time
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归实现中序遍历,先序和后序只需稍微调整返回顺序
    def inorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal_1(root.left) + [root.val] + self.inorderTraversal_1(root.right)

    # 方法二:迭代实现中序遍历,同样先序和后序遍历调整顺序,利用栈来模拟递归
    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作--得到的排序是左根右
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
