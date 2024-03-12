# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/3 8:14'
import collections
import time
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 方法一:BFS--分奇偶层进行加入
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                else:
                    tmp.append(node.val)  # 奇数层 -> 队列尾部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res

    # 方法二:BFS--一个循环同时处理奇偶层
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            tmp = []
            # 打印奇数层
            for _ in range(len(deque)):
                # 从左向右打印
                node = deque.popleft()
                tmp.append(node.val)
                # 先左后右加入下层节点
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp)
            if not deque: break  # 若为空则提前跳出
            # 打印偶数层
            tmp = []
            for _ in range(len(deque)):
                # 从右向左打印
                node = deque.pop()
                tmp.append(node.val)
                # 先右后左加入下层节点
                if node.right:
                    deque.appendleft(node.right)
                if node.left:
                    deque.appendleft(node.left)
            res.append(tmp)
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
