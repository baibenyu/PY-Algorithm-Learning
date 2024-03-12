# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/20 17:01'

import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 方法一:递归
    # 遍历所有子树,判断是否有子树与另一棵树相等
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        # 一棵树是另一棵树的子树:1--1,2两颗树相等.2--1树的左子树与2树相等.3--1树的右子树与2树相等
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:  # 当且仅当两棵树同时为空,才为True
            return True
        if not s or not t:
            return False
        # 相同的树要用and,当前值相等,左子树和右子树也相等
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
