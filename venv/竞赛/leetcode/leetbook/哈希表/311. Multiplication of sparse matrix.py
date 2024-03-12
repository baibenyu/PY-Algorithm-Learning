# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/13 10:12'

import time
from typing import List


class Solution:
    # 方法一:模拟--普通矩阵乘法
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans

    # 方法二:稀疏矩阵乘法--三元组法
    def multiply2(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(B[0])
        posA = self.getSparseRepresentation(A)
        posB = self.getSparseRepresentation(B)
        res = [[0 for i in range(n)] for j in range(m)]
        for valA, xA, yA in posA:
            for valB, xB, yB in posB:
                if yA == xB:
                    res[xA][yB] += valA * valB
        return res

    def getSparseRepresentation(self, A):
        posList = []
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    posList.append([A[i][j], i, j])
        return posList


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
