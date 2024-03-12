# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 10:09'

import time


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root is None:
            return "#"
        data = ""
        data += str(root.val) + '-' + str(len(root.children))
        for child in root.children:
            data += '-' + self.serialize(child)
        return data

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == "#":
            return None
        data = data.split('-')
        return self.dfs(data)

    def dfs(self, data: List[str]) -> 'Node':
        # 建root结点
        val = int(data.pop(0))
        root = Node(val)
        root.children = []
        # 递归儿子们
        size = int(data.pop(0))
        for _ in range(size):
            root.children.append(self.dfs(data))
        return root


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
