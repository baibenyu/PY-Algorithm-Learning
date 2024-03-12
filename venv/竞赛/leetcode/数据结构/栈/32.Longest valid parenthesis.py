# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 15:36'

class Solution:
    # 方法一:栈的运用
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]  # 初始长度的左边界
        for i in range(len(s)):
            if s[i] == "(":  # 将尚未匹配的左括号下标入栈
                stack.append(i)
            else:
                stack.pop()  # 弹出最近的括号下标--1.向右更新长度计算的左边界(只要连续右括号中最右的那个下标) 或 2.增长现有长度(弹出左括号的下标),向左更新长度计算的左边界
                if not stack:  # 将不会因匹配左括号而出栈的右括号入栈,作为新长度计算的左边界,且保证栈不为空
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])  # 与尚未或不能匹配的括号的下标的距离即连续的距离
        return res
