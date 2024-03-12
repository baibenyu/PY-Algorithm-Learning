# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/23 21:34'
from typing import List


class Solution:
    # 方法一:DFS+回溯,组合问题
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0 # 判断应该删除的左括号数和右括号数
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1);
                # 统计当前字符串中已有的括号数量

        helper(s, 0, lremove, rremove)
        return res

    # 方法二:BFS,按删除括号个数升序,删除不同位置的括号都遍历一遍
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = {s}

        while True:
            for ss in currSet:  # 判断生成的子串是否有效
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:  # 直至ans不为空,说明最少删除数达成
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:  # 若前一个元素与当前元素相同,跳过,因为会生成相同的子串
                        continue
                    if ss[i] == '(' or ss[i] == ')':  # 移除括号,并将结果子串作为下一次循环的输入
                        nextSet.add(ss[:i] + ss[i + 1:])
            currSet = nextSet
