# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 10:00'

import time
from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.ans = []

    # 方法一:递归
    def postorder(self, root: 'Node') -> List[int]:
        if root is not None:
            for node in root.children:
                self.postorder(node)
            self.ans.append(root.val)
            return self.ans
        else:
            return self.ans

    # 方法二:迭代
    def postorder2(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = []
        nextIndex = defaultdict(int)
        node = root
        while st or node:
            while node:  # 一直向左下前进
                st.append(node)
                if not node.children:
                    break
                nextIndex[node] = 1  # 标记当前层的结点遍历到的位置
                node = node.children[0]
            node = st[-1]
            i = nextIndex[node]
            if i < len(node.children):  # 更换为子结点
                nextIndex[node] = i + 1
                node = node.children[i]
            else:  # 已遍历结束,添加为结果
                ans.append(node.val)
                st.pop()
                del nextIndex[node]
                node = None
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
