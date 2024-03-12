# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/19 15:49'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:后序遍历
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:  # 这一步必须放在后序的位置上,因为根结点可能因为子树的删除变为叶子结点,所以要在左右子树处理后
            return None
        return root


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
