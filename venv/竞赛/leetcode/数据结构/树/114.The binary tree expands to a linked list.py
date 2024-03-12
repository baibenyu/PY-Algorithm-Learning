# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/12 14:31'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:先进行先序遍历,并存储访问到的结点,然后再遍历这个存储序列,执行左子树为None,右子树为下一结点
    def flatten_1(self, root: TreeNode) -> None:
        prelist = []

        def pretraverse(root):
            if root:
                prelist.append(root)
                pretraverse(root.left)
                pretraverse(root.right)

        pretraverse(root)
        for i in range(1, len(prelist)):
            pre, after = prelist[i - 1], prelist[i]
            pre.left = None
            pre.right = after

    # 方法二:核心--先序遍历是根左右,将根结点的右子树嫁接到左子树的最后一个经过的结点(最右下的结点--前驱结点)的右下不改变结点的遍历顺序
    def flatten_2(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:  # 如果存在左子树
                predecessor = nxt = curr.left
                while predecessor.right:  # 找到前驱结点
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None  # 左子树按题目设置为空
                curr.right = nxt  # 将原左子树赋值到右子树
            curr = curr.right  # 下一个结点
