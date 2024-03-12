# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 19:06'

import time
class Solution:
    # 方法一:利用栈的特性--加减先入栈不计算,乘除运算后入栈
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)

    # 方法二:模拟
    class Solution:
        op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2}

        def calculate(self, s: str) -> int:
            s = "(" + s.replace(" ", "").replace("(-", "(0-") + ")"
            n = len(s)
            # operators & numbers
            op_stack, num_stack = [], []

            i = 0
            while i < n:
                c = s[i]
                i += 1

                if c.isdigit():  # a number
                    num = int(c)
                    while i < n and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    num_stack.append(num)
                elif c == '(':  # (
                    op_stack.append(c)
                elif c == ')':  # calculate until see '('
                    while op_stack and op_stack[-1] != '(':
                        self.calc(num_stack, op_stack)
                    op_stack.pop()
                else:
                    while op_stack and op_stack[-1] != '(':
                        prev_op = op_stack[-1]
                        if self.op_priority[prev_op] < self.op_priority[c]: # 比较计算优先级,若之前的优先级高或相等,直接把之前的计算,若低,则可加入运算符栈
                            break
                        self.calc(num_stack, op_stack)
                    op_stack.append(c)

            return num_stack[0]

        def calc(self, num_stack: list, op_stack: list) -> None:
            op, y, x = op_stack.pop(), num_stack.pop(), num_stack.pop() if num_stack else 0
            ans = 0
            if op == '+':
                ans = x + y
            elif op == '-':
                ans = x - y
            elif op == '*':
                ans = x * y
            elif op == '/':
                ans = x / y
            elif op == '%':
                ans = x % y
            elif op == '^':
                ans = pow(x, y)
            num_stack.append(int(ans))


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
