# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/13 16:35'
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:迭代,逆序中序遍历,总合依次增加
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        total = 0
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            total += cur.val
            cur.val = total
            cur = cur.left
        return root

    # 方法二:递归,逆序中序遍历,每一个结点值等于迄今为止的累加值
    def convertBST_2(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root

    # 方法三;逆序进行morris遍历改中序遍历,顺序morris遍历只需将左右顺序调换
    def convertBST_3(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node: TreeNode) -> TreeNode:  # 找到右子树的最左下结点
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ

        total = 0
        node = root

        while node:
            if not node.right:  # 没有右子树的结点第一次经过就执行操作
                total += node.val
                node.val = total
                node = node.left
            else:  # 有右子树的结点,可以经过两次
                succ = getSuccessor(node)  # 找到右子树的最左下结点
                if not succ.left:  # 如果左子树为空,说明是第一次经过,将左孩子指向当前结点,方便后续返回,当前结点向右移动
                    succ.left = node
                    node = node.right
                else:  # 如果不为空,说明第二次经过,将左孩子复原为空,这时候执行操作->中序
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root
