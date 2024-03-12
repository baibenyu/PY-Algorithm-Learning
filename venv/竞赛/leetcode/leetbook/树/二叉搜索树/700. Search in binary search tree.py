# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 15:00'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

    # 方法二:迭代
    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            root = root.left if val < root.val else root.right
        return None


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
