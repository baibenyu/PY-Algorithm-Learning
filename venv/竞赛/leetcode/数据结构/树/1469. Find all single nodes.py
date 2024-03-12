# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/12 16:00'

import time


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS
    def getLonelyNodes(self, root):
        def preorder(root):
            if not root:
                return
            if not root.left and root.right:
                res.append(root.right.val)
            elif root.left and not root.right:
                res.append(root.left.val)
            preorder(root.left)
            preorder(root.right)
            return root

        res = []
        preorder(root)
        return res

    # 方法二:BFS
    def getLonelyNodes2(self, root: TreeNode) -> List[int]:
        res = []
        bound = [root]
        while bound:
            bound_next = []
            for node in bound:
                if node.left:
                    bound_next.append(node.left)
                    if node.right:
                        bound_next.append(node.right)
                    else:
                        res.append(node.left.val)
                else:
                    if node.right:
                        res.append(node.right.val)
                        bound_next.append(node.right)

            bound = bound_next
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
