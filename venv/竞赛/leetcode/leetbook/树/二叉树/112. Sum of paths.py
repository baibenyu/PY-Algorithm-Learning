# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/1 9:10'
import collections
import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 方法一:DFS--自顶向下
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:  # 只有遍历到的结点是叶子结点才执行判断
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 方法二:BFS
    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que = collections.deque()
        que.append((root, root.val))
        while que:
            node, path = que.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                que.append((node.left, path + node.left.val))
            if node.right:
                que.append((node.right, path + node.right.val))
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
