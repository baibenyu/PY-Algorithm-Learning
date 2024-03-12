# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/19 15:37'

import time


class Solution:
    # 方法一:经典求树的直径,树的直径是必以某个结点为根的两个叶子结点深度之和+1
    # 因为本题是多叉树所以才要for,否则直接遍历左右子树
    def __init__(self):
        self.maxdist = 0

    def diameter(self, root: 'Node') -> int:

        def DFS(root):
            """对于每个node，记录一下当前每个子树中距离最远的
               返回最深的子树深度"""
            if not root:
                return 0
            if not root.children:
                return 1

            childNum = len(root.children)
            dist = [0] * childNum  # 各子树的深度
            maxD, secmaxD = 0, 0
            for i in range(childNum):
                dist[i] = DFS(root.children[i])  # DFS
                if dist[i] > maxD:  # 找最深的两个子树
                    maxD, secmaxD = dist[i], maxD
                elif dist[i] > secmaxD:
                    secmaxD = dist[i]
            self.maxdist = max(self.maxdist, maxD + secmaxD + 1)  # 更新答案
            return maxD

        DFS(root)
        return self.maxdist


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
