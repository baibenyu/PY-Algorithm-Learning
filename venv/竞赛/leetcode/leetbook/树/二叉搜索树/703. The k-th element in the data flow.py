# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 16:04'

import time
from typing import List


class Heap:
    def __init__(self, desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):
        """
        添加元素
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0, self.size - 1)
        self.heap.pop()
        self._sift_down(0)
        return item

    def _smaller(self, lhs, rhs):
        return lhs > rhs if self.desc else lhs < rhs

    def _sift_up(self, index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系
        （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
        则持续将当前节点向上调整
        """
        while index:
            parent = (index - 1) // 2

            if self._smaller(self.heap[parent], self.heap[index]):
                break

            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系
        （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
        则持续将当前节点向下调整
        """
        # 若存在子节点
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.push(num)
            if self.heap.size > k:
                self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.size > self.k:
            self.heap.pop()
        return self.heap.top()


# 节点数据结构如下：
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1


class KthLargest:
    def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
        if not cur:  # 首次插入元素
            cur = TreeNode(val)
            return cur
        if cur.val < val:  # 插入元素比当前元素大，插入至右子树
            cur.right = self.insertIntoBST(cur.right, val)
        else:  # 插入元素比当前元素小或等于，插入至左子树
            cur.left = self.insertIntoBST(cur.left, val)
        cur.count += 1  # 若插入至子树，当前节点的count需要+1
        return cur

    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        self.kLarge = None  # 记录第k大
        for i in nums:  # 逐个插入
            self.root = self.insertIntoBST(self.root, i)

    def findKHelper(self, cur: TreeNode, k) -> TreeNode:
        curCnt = 1  # 如果无右节点，当前是第1大的数
        if cur.right:  # 如果有右节点，则当前是cur.right.count+1大的数
            curCnt += cur.right.count
        if k == curCnt:  # 当前值即为第k大
            return cur
        elif k < curCnt:  # 第k大在右子树
            return self.findKHelper(cur.right, k)
        else:  # 第k大在左子树，为左子树的第k-curCnt大
            return self.findKHelper(cur.left, k - curCnt)

    def add(self, val: int) -> int:
        # self.kLarge没有值，或者当前值大于self.kLarge才插入
        if self.kLarge and val > self.kLarge or not self.kLarge:
            self.root = self.insertIntoBST(self.root, val)
        self.kLarge = self.findKHelper(self.root, self.k).val
        return self.kLarge


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
