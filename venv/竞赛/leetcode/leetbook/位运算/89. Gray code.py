# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/5 11:18'
from typing import List


class Solution:
    # 方法一:模拟--在前一个序列上,分别在二进制上与1和与0,与0相当于不变,与1,并且要中心对称
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        if n == 1:
            return ans

        for i in range(1, n):
            temp = []
            for each in ans:
                temp.append(each ^ (1 << i))
            ans.extend(temp[::-1])
        return ans

    def grayCode2(self, n: int) -> List[int]:
        # 假设上一个格雷编码为G(N-1)，则G(n)为，首先将G(N-1)进行倒序，再在首部加上1就行
        head = 1
        ret = [0]
        # 遍历得到n位的格雷编码
        for i in range(n):
            # 每位格雷编码生成
            for j in range(len(ret) - 1, -1, -1):
                ret.append(head + ret[j])
            head <<= 1
        return ret
