# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 15:14'

import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)  # 如果当前节点为空，也就意味着val找到了合适的位置，此时创建节点直接返回。
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)  # 递归创建右子树
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)  # 递归创建左子树
        return root

    # 方法二:迭代
    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left
            else:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right

        return root


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
