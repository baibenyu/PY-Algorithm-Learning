# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 20:12'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归
    # 任意一条路径都可以表示为以某结点为根结点的子树,那么该路径和就等于左孩子的最大路径和+右孩子的最大路径和+自身结点值
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        # 事实上递归函数返回值是由根结点到叶子结点的最大贡献(根结点到叶子结点的最大路径和),但答案返回的是最大路径和,它是在递归过程中遍历所有根结点(即所有路径)实时更新的,它所代表的是递归过程中求出的最大路径和
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)  # 选择不走路径的值为0
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
