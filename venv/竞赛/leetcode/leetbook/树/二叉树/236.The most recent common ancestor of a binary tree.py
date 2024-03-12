# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/14 17:02'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法一:DFS--递归典中典
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        return root  # 2. if left and right:
