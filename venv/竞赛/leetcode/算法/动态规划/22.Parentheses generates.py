# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/24 15:14'
from functools import lru_cache
from typing import List


class Solution:
    # 方法一:回溯+DFS,组合问题--将括号作为字符串来排列
    def generateParenthesis(self, n: int) -> List[str]:
        def check(string: list):
            l, r = 0, 0
            for each in string:
                if each == "(":
                    l += 1
                else:
                    r += 1
                if r > l:
                    return False
            if l == r:
                return True
            else:
                return False

        def backing(index: int, llimit: int, rlimit: int):
            if index == n - 1:
                if check(strcombination):
                    ans.append("".join(strcombination.copy()))
                return
            else:
                for i in range(llimit, rlimit):
                    strcombination[i] = "("
                    backing(index + 1, i + 1, n + index + 2)  # 左边界=当前索引+1(即保证下一次不重复更改同一索引),右边界=长度-(应改变的次数-已经或正在改变的次数)
                    strcombination[i] = ")"

        strcombination = ["("] + [")"] * (2 * n - 1)  # 必须以左括号开头
        ans = []
        backing(0, 1, n + 1)
        return ans

    # 方法二:动态规划
    # 将有效的整对括号作为单位来排列组合,因为有效组合有一对括号的左括号必然在最开头,剩下的n-1对括号只有两种情况,在该对括号的右括号的左边或右边
    # 问题就变成了左边放几个括号和右边放几个括号,而这两个子问题又可以套用上述解释继续分解,直至到已知的0对括号及1对括号的排列
    def generateParenthesis2(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = [[None], ["()"]]  # 分别对应只有0组括号,和只有1组括号的所有可能
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):  # 左边放j个,右边放剩下的括号
                now_list1 = total_l[j]  # j个括号的组合情况
                now_list2 = total_l[i - 1 - j]  # 剩下个数的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 is None:
                            k1 = ""
                        if k2 is None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)  # 把所有可能的情况添加到 l 中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中
        return total_l[n]

    @lru_cache(None)
    # 方法三:记忆化搜索
    def generateParenthesis3(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis3(c):
                for right in self.generateParenthesis3(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans
