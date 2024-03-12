# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/29 15:29'

import time
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法一:BFS
    # 按正常层序遍历进行,只在偶数层改变插入点
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
