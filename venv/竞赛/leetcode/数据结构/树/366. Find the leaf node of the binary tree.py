# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/19 16:03'
import collections
import time
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一: 自底向上递归
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            depth = max(l, r) + 1  # 此处的深度是相对于叶子结点的深度,换言之叶子结点的深度必然为1,而与层数无关
            res[depth].append(root.val)
            return depth

        res = collections.defaultdict(list)
        dfs(root)
        return [v for v in res.values()]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
