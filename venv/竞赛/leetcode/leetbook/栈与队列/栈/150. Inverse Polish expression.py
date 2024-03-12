# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/16 9:51'

import time
from typing import List


class Solution:
    # 方法一:栈
    # 后序表达式刚好切合先入后出的特性
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for each in tokens:
            if each.isdigit():
                stack.append(each)
            elif each[0] == "-":
                if each[1:].isdigit():
                    stack.append(each)
                else:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if each == "+":
                    stack.append(a + b)
                elif each == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
        return int(stack[0])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
