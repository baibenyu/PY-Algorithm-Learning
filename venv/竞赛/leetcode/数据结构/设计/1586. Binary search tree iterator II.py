# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/25 15:16'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # 方法一:迭代+双栈
    def __init__(self, root: TreeNode):
        self.stk = []
        p = root
        while p:
            self.stk.append(p)
            p = p.left

        self.nums = []  # 存储中序遍历所谓左边的值,即遍历过的值
        self.i = 0  # 指针

    def hasNext(self) -> bool:
        if self.i == len(self.nums) and self.stk == []:
            return False
        return True

    def next(self) -> int:
        if self.i <= len(self.nums) - 1:  # 如果指针左移过,且数值已经算出,直接返回
            self.i += 1
            return self.nums[self.i - 1]

        cur = self.stk.pop()
        self.nums.append(cur.val)

        p = cur.right
        while p:
            self.stk.append(p)
            p = p.left

        self.i += 1
        return cur.val

    def hasPrev(self) -> bool:
        return 2 <= self.i  # 至少是第2个（从1开始数）

    def prev(self) -> int:
        self.i -= 1
        return self.nums[self.i - 1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
