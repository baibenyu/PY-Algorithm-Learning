# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/3 6:39'
import copy
import time

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS--BST的中序遍历是有序数组,所以排序即可得到中序遍历,根据先序和中序建立树,同105题
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        inorder = copy.copy(preorder)
        inorder.sort()
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    # 方法二:DFS--BST是左子树均小于根结点,右子树均大于根结点,自顶向下分解式建树
    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder.pop(0))
            l, r = [], []
            for i in preorder:
                if i <= root.val:
                    l += [i]
                else:
                    r += [i]
            root.left = self.bstFromPreorder2(l)
            root.right = self.bstFromPreorder2(r)
            return root

    # 方法三:DFS--同二,但更贴合python语言
    def bstFromPreorder3(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            devide = next((i for i, val in enumerate(preorder) if val > root.val), len(preorder))
            root.left = self.bstFromPreorder3(preorder[1: devide])
            root.right = self.bstFromPreorder3(preorder[devide:])
            return root


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
