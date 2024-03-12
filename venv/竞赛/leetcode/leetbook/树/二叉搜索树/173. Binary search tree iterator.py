# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/1 17:04'

import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # 方法一:存储中序遍历的值到数组中,O(n)
    def __init__(self, root: TreeNode):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        self.values = inorder(root)
        self.nxt = -1

    def next(self) -> int:
        self.nxt += 1
        return self.values[self.nxt]

    def hasNext(self) -> bool:
        if self.nxt + 1 >= len(self.values):
            return False
        else:
            return True

    # 方法二:迭代+单调栈--可以避免存储全部数值,单个值时间复杂度可以是O(1)
    class BSTIterator(object):

        def __init__(self, root):
            self.stack = []
            while root:
                self.stack.append(root)
                root = root.left

        def next(self):
            cur = self.stack.pop()
            node = cur.right
            while node:
                self.stack.append(node)
                node = node.left
            return cur.val

        def hasNext(self):
            return len(self.stack) > 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
