# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 16:48'
import collections
import time

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法一:BFS
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 当成图，构建邻接表中尚未构建的部分
        node_parent = dict()

        def dfs_find_parent(node: TreeNode) -> None:  # 通过哈希表建图,找到父节点
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        dfs_find_parent(root)

        # bfs波纹法， 先visit&先判适应于距离大于1

        # k == 0
        if k == 0:
            return [target.val]

        res = []

        Q = collections.deque()
        visited = set()
        Q.append(target)
        visited.add(target)  # 先visit
        level = 0
        while Q and level < k:
            level += 1
            for _ in range(len(Q)):
                x = Q.popleft()
                for y in [node_parent[x] if x in node_parent else None, x.left, x.right]:  # 遍历父结点,左孩子,右孩子
                    if y and y not in visited:
                        if level == k:
                            res.append(y.val)  # 先判
                        Q.append(y)
                        visited.add(y)

        return res

    # 方法二:DFS
    def distanceK2(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        maps = {}  # 构建哈希表，记录每个节点的父亲节点

        def findP(root):
            if root.left:
                maps[root.left.val] = root
                findP(root.left)
            if root.right:
                maps[root.right.val] = root
                findP(root.right)

        res = []

        def dfs(root, node, k):
            '''
            需要记录上一个遍历的节点是啥，防止5-->3 然后 3又去左子树5  这样走了两步
            '''
            if k == 0:
                res.append(root.val)
                return
            if root.left and root.left != node:  # 左
                dfs(root.left, root, k - 1)
            if root.right and root.right != node:  # 右
                dfs(root.right, root, k - 1)
            if root.val in maps and maps[root.val] != node:  # 父亲
                dfs(maps[root.val], root, k - 1)

        findP(root)
        dfs(target, None, k)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
