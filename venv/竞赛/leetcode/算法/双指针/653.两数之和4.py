# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 15:28'

import time
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS+集合
    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:  # 检查集合中已经是否有能与当前值加起来为k的值
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

    # 方法二:BFS+集合
    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        q = deque([root])
        while q:
            node = q.popleft()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

    # 方法三:递归+midorder+双指针
    # 此方法基于二叉搜索树的中序遍历是递增序列的特性
    def findTarget3(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def inorderTraversal(node: Optional[TreeNode]) -> None:
            if node:
                inorderTraversal(node.left)
                arr.append(node.val)
                inorderTraversal(node.right)

        inorderTraversal(root)

        left, right = 0, len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum == k:
                return True
            if sum < k:
                left += 1
            else:
                right -= 1
        return False

    # 方法四:迭代+midorder+双指针
    def findTarget4(self, root: Optional[TreeNode], k: int) -> bool:
        left, right = root, root
        leftStk, rightStk = [left], [right]
        while left.left:
            left = left.left
            leftStk.append(left)
        while right.right:
            right = right.right
            rightStk.append(right)
        while left != right:
            sum = left.val + right.val
            if sum == k:
                return True
            if sum < k:
                left = leftStk.pop()
                node = left.right
                while node:
                    leftStk.append(node)
                    node = node.left
            else:
                right = rightStk.pop()
                node = right.left
                while node:
                    rightStk.append(node)
                    node = node.right
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
