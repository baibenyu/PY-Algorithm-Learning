# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 10:22'

import time

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DP
    # a--在当前结点放置摄像头,覆盖整颗树需要的摄像头数
    # b--无论在当前结点放置与否摄像头,覆盖整颗树需要的摄像头数
    # c--无论当前结点是否被覆盖,覆盖子树所需要的摄像头数
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1  # 当前结点的摄像头数(1个)+左子树所需(除左子树根结点)+右子树(除右子树根结点)所需 # 保证在当前结点放置同时要求全覆盖的一种情况
            b = min(a, la + rb, ra + lb)  # (在当前结点放置所需的摄像头,左子树根结点放置所需+右子树所需,右子树根结点放置所需+左子树所需) # 保证整颗树被覆盖的三种情况
            c = min(a, lb + rb)  # (在当前结点放置所需的摄像头,左子树所需+右子树所需) # 保证子树被覆盖的两种情况
            return [a, b, c]

        a, b, c = dfs(root)
        return b


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
