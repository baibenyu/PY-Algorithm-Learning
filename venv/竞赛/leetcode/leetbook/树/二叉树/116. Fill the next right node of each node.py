# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 16:34'

import time

"""
# Definition for a Node."""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 方法一:迭代,层序遍历
    def connect(self, root: 'Node') -> 'Node':
        import collections
        if not root:
            return root
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])
        # 外层的 while 循环迭代的是层数
        while Q:
            # 记录当前队列大小
            size = len(Q)
            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node = Q.popleft()
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        # 返回根节点
        return root

    # 方法二:迭代,利用已经建立的next指针
    def connect2(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # 从根节点开始
        leftmost = root
        while leftmost.left:
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                # 指针向后移动
                head = head.next
            # 去下一层的最左的节点
            leftmost = leftmost.left
        return root


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
