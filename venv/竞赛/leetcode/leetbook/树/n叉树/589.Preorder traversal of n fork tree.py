# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 19:21'

import time
from typing import List

"""
# Definition for a Node."""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.ans = []

    # 方法一:递归
    def preorder(self, root: 'Node') -> List[int]:
        if root is not None:
            self.ans.append(root.val)
            for node in root.children:
                self.preorder(node)
            return self.ans
        else:
            return self.ans

    # 方法二:迭代,将根结点的子结点逆序入栈
    def preorder2(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(reversed(node.children))  # 因为是入栈,所以需要颠倒顺序
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
