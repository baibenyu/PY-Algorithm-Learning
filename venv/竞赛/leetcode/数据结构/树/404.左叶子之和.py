# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 15:18'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
