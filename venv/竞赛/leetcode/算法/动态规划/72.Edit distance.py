# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 11:18'

class Solution:
    # 方法一:动态规划
    # dp状态表示由word1的前i个字符得到word2的前j个字符所需的最少步数
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):  # 包含m和n
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1 # 对word1前i个字母进行插入得到word2的前j+1个字母
                down = D[i][j - 1] + 1 # 对word1前i+1个字母进行删除得到word2的前j个字母
                left_down = D[i - 1][j - 1] # 替换
                if word1[i - 1] != word2[j - 1]:  # 若最后一个字符不相等,才操作
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]
