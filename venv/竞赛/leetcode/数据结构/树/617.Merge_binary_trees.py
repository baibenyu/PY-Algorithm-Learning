# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/10 19:45'

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 合并二叉树
    # 方法一:DFS--深度优先遍历,先序
    def mergeTrees_1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees_1(t1.left, t2.left)
        merged.right = self.mergeTrees_1(t1.right, t2.right)
        return merged

    # 方法二:BFS--广度优先遍历,层序
    def mergeTrees_2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        queue = collections.deque([merged])
        queue1 = collections.deque([t1])
        queue2 = collections.deque([t2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2

        return merged
