# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/10 19:58'

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS,每遍历一次深度加1,返回左右子树中的最大值,自底向上(后序)
    def maxDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth_1(root.left), self.maxDepth_1(root.right)) + 1

    # 方法二:BFS
    def maxDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = collections.deque([root])

        while q:
            for i in range(len(q)):  # 遍历当前队列所有结点--即层序遍历二叉树
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
