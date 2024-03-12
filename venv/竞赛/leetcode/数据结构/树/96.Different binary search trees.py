# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/12 20:36'

class Solution:
    # DP问题:1.取i为二叉搜索树的根结点--2.将i-1序列作为左子树,n-i序列作为右子树--3.递归构建左右子树
    # 定义两个函数:1.G(n)表示n个结点的二叉搜索树的个数;2.F(i,n)表示以i为根结点的二叉搜索树个数--所以G(n) = F(i,n)的累加
    # G(0)=1,G(1)=1,F(i,n)=G(n-i)·G(i-1)-->G(n) = G(n-i)·G(i-1)笛卡尔积(即一一排列组合)的累加
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]