# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/30 9:43'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def successor(self, root):  # 寻找当前结点的后继结点--有右子树情况下,先向右一步,然后一直向左直至直至无左结点
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):  # 寻找当前结点的前驱结点--有左子树的情况下,先向左一步,然后一直向右直至无右结点
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)  # 先将后继结点值赋给当前值,然后递归找到后继结点并删除
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)  # 同上,前驱
                root.left = self.deleteNode(root.left, root.val)

        return root


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
