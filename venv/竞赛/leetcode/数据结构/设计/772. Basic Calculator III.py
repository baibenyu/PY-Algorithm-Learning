# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/17 17:42'

import time


class Solution:
    # 方法一:双栈法
    def calculate(self, s: str) -> int:
        stack_num = []
        stack_opt = []
        i = 0
        priorty = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if '0' <= s[i] <= '9':
                j = i
                while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                    i += 1
                num = int(s[j:i + 1])
                stack_num.append(num)
            elif s[i] == '(':
                stack_opt.append(s[i])
            elif s[i] == ')':
                while stack_opt[-1] != '(':
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A, B, opt)
                    stack_num.append(res)
                stack_opt.pop()
            else:
                while stack_opt and priorty[stack_opt[-1]] >= priorty[s[i]]:
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A, B, opt)
                    stack_num.append(res)
                stack_opt.append(s[i])
            i += 1

        while stack_opt:
            opt = stack_opt.pop()
            A = stack_num.pop()
            B = stack_num.pop()
            res = self.calc(A, B, opt)
            stack_num.append(res)
        return stack_num[-1]

    def calc(self, num1, num2, opt):
        if opt == '+':
            return int(num1) + int(num2)
        elif opt == '-':
            return int(num2) - int(num1)
        elif opt == '*':
            return int(num2) * int(num1)
        elif opt == '/':
            return int(int(num2) / int(num1))


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
