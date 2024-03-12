# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/10 16:38'

import time

# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 方法一:前序或后序遍历
    # 唯一确定二叉树必须要两个不同的遍历序列,二叉搜索树是特殊的,它的中序遍历是排序好的,所以可以通过对前序或后序的排序来得到
    def serialize(self, root: TreeNode) -> str:
        arr = []

        def postOrder(root: TreeNode) -> None:  # 后序遍历
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)

        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))

        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root

        return construct(-inf, inf)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
