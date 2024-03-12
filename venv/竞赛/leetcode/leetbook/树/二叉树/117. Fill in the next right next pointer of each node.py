# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/20 16:43'

import time


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 方法一:BFS
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        import collections
        q = collections.deque([root])
        while q:
            length = len(q)
            for j in range(length - 1):
                q[j].next = q[j + 1]
            for i in range(length):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
