# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/13 9:14'
import collections
import time
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:后序遍历+哈希表--以树的序列值(元组)为键值
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        visited = dict()

        def dfs(root):
            nonlocal ans
            if not root:
                return [None]
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                cur = tuple(left + right + [root.val])
                if cur not in visited:
                    visited[cur] = False
                elif not visited[cur]:
                    ans.append(root)
                    visited[cur] = True
                return left + right + [root.val]

        dfs(root)
        return ans

    # 以字符串作为键值
    def findDuplicateSubtrees2(self, root):
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node:
                return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
