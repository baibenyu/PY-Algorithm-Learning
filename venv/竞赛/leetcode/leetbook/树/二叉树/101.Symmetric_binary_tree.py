# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/11 16:16'
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:层序遍历,利用队列存储树节点,从两边向中间比较
    def isSymmetric_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append((root.left, root.right))
        while queue:
            left, right = queue.popleft()  # 仅在输出的对象可迭代时才能这么写,一般要有两个对象
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True

    # 方法二:递归判断左子树的左结点和右子树的右结点,左子树的右结点和右子树的左结点是否相同
    def isSymmetric_2(self, root: TreeNode) -> bool:
        def helper(left_root, right_root):
            if not left_root and not right_root:
                return True
            if not left_root or not right_root or abs(left_root.val - right_root.val) > 0:
                return False
            return helper(left_root.left, right_root.right) and helper(left_root.right, right_root.left)

        return helper(root.left, root.right)
