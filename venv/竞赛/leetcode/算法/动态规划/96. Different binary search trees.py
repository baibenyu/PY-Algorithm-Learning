# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 15:22'

import time


class Solution:
    # 方法一:DP
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):  # G[j - 1](左子树) * G[i - j](右子树)遍历以每个结点j作为根节点的二叉搜索树的个数
                G[i] += G[j - 1] * G[i - j]  # G(n)表示n个数都作为根节点的个数的和

        return G[n]

    # 方法二:数学--卡兰塔数
    # C0 = 1,Cn+1 = 2*(2*n+1)/(n+2)*Cn
    def numTrees2(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
