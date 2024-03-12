# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/28 14:53'

import time


class Solution:
    # 方法一:栈
    # 存储左括号
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = 0
        for each in s:
            if each == "(":
                left += 1
                stack.append(each)
            elif each == ")":
                if left > 0:
                    left -= 1
                    stack.append(each)
            else:
                stack.append(each)
        ans = ""
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "(":
                stack.pop(i)
                left -= 1
            if left == 0:
                return ans.join(stack)
        return ""


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
