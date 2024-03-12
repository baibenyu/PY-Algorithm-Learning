# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/14 15:38'
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:双重递归--题目要求的路径只能由父节点指向子结点
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum) -> int:  # 遍历以根结点为起始结点所有可能路径和
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)  # 实际上每经过一次子结点,下一次判断的目标值都会减去当前节点值
            ret += rootSum(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0
        # 遍历所有结点为起始结点的所有路径
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

    # 方法二:存储递归过程中求出的前缀和+回溯路径条数

    def pathSum_2(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val  # 当前前缀和
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1  # 将路径条数的状态回溯到相应的递归层

            return ret

        return dfs(root, 0)
