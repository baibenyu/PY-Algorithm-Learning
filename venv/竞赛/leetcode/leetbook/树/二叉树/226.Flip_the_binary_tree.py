# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/9 16:23'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 方法一:递归--自底向上,
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        """
        # 方法二:迭代--用队列存储树结点,进行层序遍历二叉树
        """
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root
        """

        # 方法三:递归--自顶向下,对二叉树进行先序遍历,过程中先实现左右孩子的交换
        def recursion(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            recursion(root.left)
            recursion(root.right)

        recursion(root)
        return root


