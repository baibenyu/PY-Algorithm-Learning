# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/19 15:24'

import time


# Definition for a binary tree node.
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:层序遍历
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        while q:
            s = len(q)
            tmp = deque()
            for _ in range(s):
                cur = q.popleft()
                if cur == u:
                    if q:
                        return q.popleft()
                    else:
                        return None
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            q = tmp
        return None


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
