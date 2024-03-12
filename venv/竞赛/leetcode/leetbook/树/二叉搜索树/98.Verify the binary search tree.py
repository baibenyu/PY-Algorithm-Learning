# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/13 15:54'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 注意事项：二叉搜索树要保证左子树中所有的结点都小于根结点，右子树中所有的结点都大于根结点，而不是仅仅保证左孩子和右孩子
    # 方法一：递归--设置结点值的上限和下限，对于左子树，应该小于上限，对于右子树，应该大于下限
    def isValidBST_1(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    # 方法二:迭代,中序遍历时结点按左根右排列,又因为二叉搜索树左子树<根结点<右子树,所以二叉搜索树中序遍历得到的序列是递增序列
    def isValidBST_2(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

