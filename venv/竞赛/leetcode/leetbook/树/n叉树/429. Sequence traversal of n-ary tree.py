# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/24 14:11'

import time
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 方法一:BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        import collections
        if not root:
            return root
        q = collections.deque([root])
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)
                for each in cur.children:
                    if each:
                        q.append(each)
            ans.append(temp)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
