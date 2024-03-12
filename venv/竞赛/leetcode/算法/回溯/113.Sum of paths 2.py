# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/29 15:59'

import time
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:回溯+DFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def preorder(root, target, temp):
            nonlocal ans
            if not root:
                return
            temp.append(root.val)
            if not root.left and not root.right:
                if root.val == target:
                    ans.append(temp.copy())
                temp.pop()
                return
            preorder(root.left, target - root.val, temp)
            preorder(root.right, target - root.val, temp)
            temp.pop()

        preorder(root, targetSum, [])
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
