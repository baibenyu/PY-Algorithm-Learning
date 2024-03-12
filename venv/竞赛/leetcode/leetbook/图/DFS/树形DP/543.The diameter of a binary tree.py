# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/11 20:40'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:最大直径--两结点所经过最短路径的最大值->路径=经过的结点数-1->两结点之间所经过的最大结点数-1
    # 任意一条路径都可以表示为以某结点为根结点的子树,那么子树的深度=max(子树的左子树深度,右子树深度)+1
    # 又因为深度=从叶子结点到根结点所经过的结点数->路径总结点数=左子树深度+右子树深度+1
    # 求的是最大值,所以在递归中记录和比较当前经过的最大结点数
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return self.ans - 1
