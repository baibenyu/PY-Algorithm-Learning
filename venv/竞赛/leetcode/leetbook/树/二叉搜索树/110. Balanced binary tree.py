# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/16 8:44'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS--求高度的过程中比较左右子树的高度差是否超过1
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        flag = True

        def depth(root: TreeNode) -> int:
            nonlocal flag
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                flag = False
                return -1
            return max(left, right) + 1

        depth(root)
        return flag


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
