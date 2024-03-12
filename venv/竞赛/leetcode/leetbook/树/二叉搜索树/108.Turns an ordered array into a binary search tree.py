# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/29 10:40'

import time
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:贪心
    # 每次分配左右子树的值的区间,尽量平分,二分查找的查找次数即为子树的层数,而从中间开始的二分查找两边的查找次数相差不超过一,即满足平衡二叉树的概念
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 三种策略:1.选择区间中间偏左的结点(当前策略)2.选择区间中间偏右的结点3.随机左右
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
