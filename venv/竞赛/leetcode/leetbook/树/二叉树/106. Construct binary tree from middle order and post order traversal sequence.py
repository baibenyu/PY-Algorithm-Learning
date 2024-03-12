# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 9:13'

import time
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:递归--根据后序遍历确定根结点,建立根结点,再根据根结点在中序遍历中的位置确定左右子树的范围
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def myBuildTree(postorder_left: int, postorder_right: int, inorder_left: int, inorder_right: int):
            if inorder_left > inorder_right:
                return None

            # 后序遍历中的最后一个节点就是根节点
            postorder_root = postorder_right
            # 在中序遍历中定位根节点
            inorder_root = index[postorder[postorder_root]]

            # 先把根节点建立出来
            root = TreeNode(postorder[postorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            root.left = myBuildTree(postorder_left, postorder_left + size_left_subtree - 1, inorder_left,
                                    inorder_root - 1)
            # 得到右子树中的节点数目
            size_right_subtree = inorder_right - inorder_root
            # 递归地构造右子树，并连接到根节点
            root.right = myBuildTree(postorder_right - 1 - (size_right_subtree - 1), postorder_right - 1,
                                     inorder_root + 1,
                                     inorder_right)
            return root

        n = len(postorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
